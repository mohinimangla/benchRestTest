from flask import request
from flask_restful import Resource, abort
import requests
from services.bench_service import BenchService
from models import Transaction, as_transaction
import json

class Transactions(Resource):
    
    def get(self):
        
        req_page = request.args.get('page')
        if req_page:
            result, _, err = self.get_transaction_by_page(req_page)
        else: 
            result, _, err = self.get_all_transactions()
        
        if not result:
            abort(404, message=err)
        return result
    
    def get_transaction_by_page(self, page_num):
        # instantiate bench service obj
        bench_service_obj = BenchService()
        
        result, err = bench_service_obj.get_transaction_by_page(page_num)
        if not result:
            return None, None, err
        
        transactions_json = []
        transactions_objlist = []
        for trans_detail in result:
            temp = as_transaction(trans_detail)
            if temp:
                transactions_json.append(temp.serialize())
                transactions_objlist.append(temp)
        return transactions_json, transactions_objlist, None
    
    def get_all_transactions(self):
        # instantiate bench service obj
        bench_service_obj = BenchService()
        
        result, err = bench_service_obj.get_all_transactions()
        if not result:
            return None, None, err
        
        transactions_json = []
        transactions_objlist = []
        for trans_detail in result:
            temp = as_transaction(trans_detail)
            if temp:
                transactions_json.append(temp.serialize())
                transactions_objlist.append(temp)
        return transactions_json, transactions_objlist, None
    
class Report(Transactions):
    def get(self):
        
        _, transactions, err = self.get_all_transactions()
        
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
                
        return daily_balance, None
