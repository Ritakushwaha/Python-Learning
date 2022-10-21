#!/usr/bin/env python
import snowflake.connector
import snowflake_creds_ as sc

# Gets the version
ctx = snowflake.connector.connect(
    user=sc.get_snowflake_creds('username'),
    password=sc.get_snowflake_creds('password'),
    account=sc.get_snowflake_creds('account')
    )
cs = ctx.cursor()

try:
    cs.execute("SELECT current_version()")
    one_row = cs.fetchone()
    print(one_row[0])
finally:
    cs.close()
ctx.close()