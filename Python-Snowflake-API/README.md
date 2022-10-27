### Create a virtual environment
```
python3 -m venv .venv
```



### Install Python Connector :
https://docs.snowflake.com/en/user-guide/python-connector-install.html

1. Run Shell Script 'install_python_connector.sh'
2. Make the shell script executable
```
chmod +x install_python_connector.sh
```
3. Run the script
```
./install_python_connector.sh
```

4. Test the script
```
SELECT count(*) FROM ANALYTICS.DBT_RKUSHWAHA.MY_FIRST_DBT_MODEL --2
```

http://127.0.0.1:5000/aggregator?query=SELECT count(*) FROM ANALYTICS.DBT_RKUSHWAHA.MY_FIRST_DBT_MODEL


http://127.0.0.1:5000/data_fetcher?query=SELECT count(*) FROM ANALYTICS.DBT_RKUSHWAHA.MY_FIRST_DBT_MODEL

### Snowflake pandas
https://docs.snowflake.com/en/user-guide/python-connector-pandas.html

### 

