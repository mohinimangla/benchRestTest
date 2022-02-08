# benchRestTest
A python-flask app created to consume external APIs and return aggregated results

    Sample Data: http://resttest.bench.co/transactions/1.json ** 1.json increments by 1

### Setup

1. install python and pip for running the dev server
2. this sets up the server to make request to the apis
3. run pip install -r requirements.py
4. run python main.py

### URL Endpoints

- /transactions - get request returns list of all transactions
This API will return count of all transactions and details of first 10 transactions received from the external API
Additional query parameters for this API are
    - limit: resets the number of transactions to be displayed
    - offset: resets the starting point for the the results to be displayed
- /report - get request returns a report of daily balances across all pages

### Testing
    
- Run test.py python module in console
    
- Sample result: 
```	
>>> python test.py 
....
----------------------------------------------------------------------
Ran 4 tests in 4.240s
OK
```
    
### Assumptions
- Number of results returned from the transactions-bench API call will always be less than or equal to 10
- If there are a maximum of `n` pages that can be returned from transactions-bench API, then for all pages < `n` the number of results returned will be 10

## Application Structure
- Endpoints `/transaction` and `/report` are defined by registering resources in main.py
- `Resources` are defined in resource.py. Here the query parameters are fetched from the request and logic is defined for parsing data models and formatting results for output
- Resources are dependent on `data models` which are defined in models.py along with their respective serializers
- Resources are also responsible for getting data from the `external service API` which is handled in services/bench_service
- `Unit tests` have been defined in test.py