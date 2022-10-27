import pandas as pd
import snowflake.connector as sc
import json
import snowflake_creds_ as s_creds

from flask import Flask, request

app = Flask(__name__)

username = s_creds.get_snowflake_creds('username')
password = s_creds.get_snowflake_creds('password')
account = s_creds.get_snowflake_creds('account')
warehouse = s_creds.get_snowflake_creds('warehouse')
database = s_creds.get_snowflake_creds('database')
schema = s_creds.get_snowflake_creds('schema')
role = s_creds.get_snowflake_creds('role')


def connection():
    try:
        conn = sc.connect(user=username,password=password,account=account)
    except Exception as e:
        print(e)
    return conn

conn = connection()

sql1 = f'use warehouse {warehouse}'
sql2 = f'alter warehouse {warehouse} resume'
sql3 = f'use database {database}'
sql4 = f'use role {role}'
sql5 = f'SELECT count(*) FROM {warehouse}.{database}.MY_FIRST_DBT_MODEL'

def run_query(conn, query):
    print("Executing the {} query".format(query))
    cursor = conn.cursor()
    try:
        cursor.execute(query)
    except Exception as e:
        print(e)
    cursor.close()


def run_query1(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    records=str(cursor.fetchone()[0])
    cursor.close()
    return records


@app.route('/')
def hello_world():
    return "Hello World , Welcome to Snowflake API"

@app.route('/aggregator',methods=['GET','POST'])
def stats_collector():
    query_to_be_executed=request.args.get("query")
    extracted_data=run_query1(conn, query_to_be_executed)
    print(extracted_data)
    return extracted_data

@app.route('/data_fetcher',methods=['GET','POST'])
def data_extractor():
    query_to_be_executed = request.args.get("query")
    data_from_table = pd.read_sql(query_to_be_executed, conn)
    return {"data": json.loads(data_from_table.to_json(orient='records'))}


if __name__=='__main__':
    run_query(conn, sql1)
    run_query(conn, sql2)
    run_query(conn, sql3)
    run_query(conn, sql4)
    run_query(conn, sql5)
    app.run()