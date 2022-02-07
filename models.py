import json

class Transaction:
    def __init__(self, date, ledger, amount, company):
        self.date = date
        self.ledger = ledger
        self.amount = amount
        self.company = company
        
    def serialize(self):
        return {"Date": self.date,
                "Ledger": self.ledger,
                "Amount": self.amount,
                "Company": self.company}

def as_transaction(dct):
    """deserialize json into Transaction obj"""
    try: 
        amt = float(dct['Amount'])
        return Transaction(dct['Date'], dct['Ledger'], amt, dct['Company'])
    except:
        print("Object: {} does not have a valid amount value: {} skipping...".format(dct, dct['Amount']))
        return None
