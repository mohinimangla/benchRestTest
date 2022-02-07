# benchRestTest
A python-flask app created to consume external APIs and return aggregated results

    Sample Data: http://resttest.bench.co/transactions/1.json ** 1.json increments by 1

Setup:

1. install python and pip for running the dev server
2. this sets up the server to make request to the apis
3. run pip install -r requirements.py
4. run python main.py

URL Endpoints:

- /transactions - get request returns list of all transactions
- /transactions?page={} - get request returns transactions on query parameter - page    
- /report - get request returns a report of daily balances

Testing:
    
- Run test.py python module in console
    
- Sample result: 
```	
>>> python test.py 
....
----------------------------------------------------------------------
Ran 4 tests in 4.240s
OK
```
    
	
