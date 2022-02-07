from flask import Flask
from flask_restful import  Api, abort
from flask_sqlalchemy import SQLAlchemy
from resources import Transactions, Report

app = Flask(__name__)
api = Api(app)
app.config.from_object('config') 
print(app.config)

# register resource
api.add_resource(Transactions, "/transactions") # accessible at /transactions
api.add_resource(Report, "/report") # accessible at /report

if __name__ == "__main__":
    app.run(debug=True)
    