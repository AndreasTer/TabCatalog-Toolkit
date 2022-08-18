import snowflake.connector
import oracledb
import pandas as pd

#------------------------------------------------------------------
#function returns a cursor object that allows you to make snowsql queries
def authenticate_snowflake(snow_u,snow_p,account_name,database_name):
    ctx = snowflake.connector.connect(
        user=snow_u,
        password=snow_p,
        account=account_name,
        database=database_name
        )
    cs = ctx.cursor()
    return(cs)

def authenticate_oracle(ora_u, ora_p, ora_ip, ora_service):
    connection = ora_ip+'/'+ora_service
    ctx = oracledb.connect(user=ora_u, password=ora_p, dsn=connection)
    cs = ctx.cursor()
    return(cs)

#---------------------------------------------------------------------
#function to get all column names and comments from a table
def get_snow_descriptions(cursor_object, table_name, table_schema):
    desc_table_pandas = cursor_object.execute("select column_name, comment, table_schema, table_name from information_schema.columns where table_name = '"+table_name+"' AND table_schema = '"+table_schema+"';").fetch_pandas_all()
    return(desc_table_pandas)

def get_oracle_descriptions(cursor_object, table_name):
    desc_table_pandas = cursor_object.execute("SELECT COLUMN_NAME, COMMENTS, TABLE_NAME FROM SYS.ALL_COL_COMMENTS WHERE TABLE_NAME = '"+table_name+"'")
    test = pd.DataFrame(desc_table_pandas.fetchall(), columns=['COLUMN_NAME','COMMENT', 'TABLE_NAME'])
    return(test)