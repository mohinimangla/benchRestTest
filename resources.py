from flask import request
from flask_restful import Resource, abort
import requests
from services.bench_service import BenchService



class Report(Resource):
    pass
class Transactions(Resource):
    
    def get(self):
        # instantiate bench service obj
        bench_service_obj = BenchService()
        
        # get query parameters if any
        print(request.args)
        
        req_page = request.args.get('page')
        if req_page:
            result, err = bench_service_obj.get_transaction_by_page(req_page)
        else: 
            result, err = bench_service_obj.get_all_transactions()
        
        if not result:
            abort(404, message=err)
        return result
