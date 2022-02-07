# benchRestTest
A python-flask app created to consume external APIs and return aggregated results

    Sample Data: http://resttest.bench.co/transactions/1.json ** 1.json increments by 1

Setup:
    install python and pip for running the dev server
    this sets up the server to make request to the apis
    run pip install -r requirements.py
    run python main.py

URL Endpoints:
    /transactions - get request returns list of all transactions
    /transactions?page_num={} - get request returns transsactions on page provided
    /reports - get request returns a report of daily calculated balances
