import requests
from flask import current_app as app

class BenchService:
    
    def __init__(self):
        self.TRANSACTION_API = app.config['TRANSACTION_API']
    
    def no_data_err(self):
        return "No transaction data found"
    def invalid_page_err(self):
        return "Not a valid page number"

    def get_all_transactions(self, page_start=1, page_end=None):
        """ Returns list of all transaction and error message if any 
        'transaction list' -> [
            {"Date": String,
            "Ledger": String,
            "Amount": String,
            "Company": String
        }, {.....]
        """
        result_list = []
        count = page_start
        total_transactions = 0
        if not page_end:
            page_end = float('inf')
        while count<=page_end:
                 
            page_data, err = self.get_transaction_by_page(count)
            if err:
                break
            if total_transactions<1:
                total_transactions = page_data.get("count")
            
            result_list.extend(page_data.get("transactions"))
            
            count += 1
        
        if not result_list:
            return None, total_transactions, self.no_data_err()
        
        return result_list, total_transactions, None 

    def get_transaction_by_page(self, page):
        """ Returns transaction list and error message if any 
        based on provided page number
        'transaction list' -> [
            {"Date": String,
            "Ledger": String,
            "Amount": String,
            "Company": String
        }, {.....]
        """
        if not page:
            return {}, self.invalid_page_err()
        try:
            page_num = int(page)
        except:
            return {}, self.invalid_page_err()
        
        result = requests.get(self.TRANSACTION_API.format(page_num))
        
        if not result:
            return {}, self.no_data_err()
        return self.format_transaction_data(result.json()), None
        

    def format_transaction_data(self, page_data):
        return {"count": page_data.get('totalCount', 0), "transactions": page_data.get('transactions', [])}

