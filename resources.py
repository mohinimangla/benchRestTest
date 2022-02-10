from flask import request
from flask_restful import Resource, abort
import requests
from services.bench_service import BenchService
from models import Transaction, as_transaction
import json

DEFAULT_DISPLAY_LIMIT = 10
DEFAULT_DISPLAY_OFFSET = 0

class Transactions(Resource):
    
    def get(self):
        
        req_limit = request.args.get('limit', DEFAULT_DISPLAY_LIMIT)
        req_offset = request.args.get('offset', DEFAULT_DISPLAY_OFFSET)
        
        if not self.validate_limit_offset(req_limit, 1):
            abort(404, message="Not a valid limit value")
        if not self.validate_limit_offset(req_offset):
            abort(404, message="Not a valid offset value")
        
        result, _, err = self.get_all_transactions(int(req_offset), int(req_limit))
        
        if not result:
            abort(404, message=err)
        
        return result
    
    def get_all_transactions(self, offset=DEFAULT_DISPLAY_OFFSET, limit=DEFAULT_DISPLAY_LIMIT):
        # instantiate bench service obj
        bench_service_obj = BenchService()
        
        page_start = (offset)//10 + 1
        if limit:
            page_end = (offset+limit)//10 + 1
        else:
            page_end = limit
        
        transact_list, transact_count, err = bench_service_obj.get_all_transactions(page_start, page_end)
        if err:
            return None, None, err
        
        transactions_json = []
        transactions_objlist = []
        
        if not limit: limit = len(transact_list)
        
        for detail in transact_list[offset%10: min(offset%10+limit, len(transact_list))]:
            temp = as_transaction(detail)
            if temp:
                transactions_json.append(temp.serialize())
                transactions_objlist.append(temp)
        return {"count": transact_count, "transactions": transactions_json}, transactions_objlist, None
    
    def validate_limit_offset(self, val, minval = 0):
        try:
            outval = int(val)
        except:
            return False
        
        return outval>=minval
    
class Report(Transactions):
    def get(self):
        
        _, transactions, err = self.get_all_transactions(limit=None)
        
        if not transactions:
            abort(404, message=err)
        
        result, err = self.get_daily_balance(transactions)
        if not result:
            abort(404, message=err)
        return result
    
    def get_daily_balance(self, transactions_list):
        
        if len(transactions_list) == 0:
            return {}, "No transaction data found to report daily balances"
        
        daily_balance = {}
        for transact in transactions_list:
            if transact.date not in daily_balance:
                daily_balance.update({transact.date: transact.amount})
            else:
                daily_balance[transact.date] += transact.amount
        
        return self.get_running_balance(daily_balance), None
    
    def get_running_balance(self, daily_balance):
        if len(daily_balance) == 0:
            return {}
        out_val = {}
        sorted_date = list(daily_balance.keys())
        print(sorted_date)
        sorted_date = sorted(sorted_date)
        print(sorted_date)
        for i in range(len(sorted_date)):
            if i==0:
                out_val.update({sorted_date[i]: daily_balance[sorted_date[i]]}) 
            else:
                out_val.update({sorted_date[i]: daily_balance[sorted_date[i]]+out_val[sorted_date[i-1]]}) 

        return out_val