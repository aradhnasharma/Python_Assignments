from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, exc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
Base = declarative_base()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///BankDB.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)
BankDB = SQLAlchemy(app)
ma = Marshmallow(app)

# Set up database
engine = create_engine('sqlite:///BankDB.sqlite3',connect_args={'check_same_thread': False},echo=True)
Base.metadata.bind = engine
db = scoped_session(sessionmaker(bind=engine))


class Loan(BankDB.Model):
	customer_id = BankDB.Column(BankDB.Integer, primary_key=True)
	name = BankDB.Column(BankDB.String(10), nullable=False)
	loan_id = BankDB.Column(BankDB.Integer, unique_key=True)
	loan_type = BankDB.Column(BankDB.String(30), nullable=False)
	loan_amount= BankDB.Column(BankDB.Integer, nullable=False)
	loan_date = BankDB.Column(BankDB.String(20), nullable=False)
	rate_of_interest = BankDB.Column(BankDB.Integer, nullable=False)
	duration = BankDB.Column(BankDB.Integer, nullable=False)
	
    def __repr__(self):
        return '<Loan account %r is now created with an loan Type %r >' % (self.loan_id, self.loan_type)

	  
class LoanSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Loan
		
class ViewLoanSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Loan		
    customer_id=auto_field()
    name=auto_field()
    loan_id=auto_field()

	
loan_schema = LoanSchema(many=True)
viewloan_schema = ViewLoanSchema()

class ViewLoan(Resource):
    def get(self,customername):
       loan = Loan.query.filter_by(loan_id=loan_id).first_or_404(description='No loan Exists with this loan Id {}. Kindly Re-check'.format(loan_id))
        return viewloan_schema.dump(loan)
        # return customers_schema.dump(cust)

class ApplyLoan(Resource):
    def get(self):
        loan = Loan.query.all()
        return loan_schema.dump(loan)
    
    def post(self):
        result = db.execute("SELECT * from Loan WHERE username = :c", {"c": request.json['username']}).fetchone()
        if result is None :
                # result = db.query(Customer).count()
                new_loan = Loan(
                    customer_id = request.json['customer_id'],
                    name = request.json['name'],
                    loan_id = request.json['loan_id'],
                    loan_type = request.json['loan_type'],
                    loan_amount = request.json['loan_amount'],
                    loan_date = request.json['loan_date'],
                    rate_of_interest = request.json['rate_of_interest'],
                    duration = request.json['duration']
                )
				
                BankDB.session.add(new_loan)
                BankDB.session.commit()
                return LoanSchema.dump(new_loan), 201
        return f"User {request.json['loan_id']} already exists in the table."
    
api.add_resource(ApplyLoan,'/ApplyLoan')
api.add_resource(ViewLoan,'/GetLoanDetail/<int:loan_id>')
