# TabColumn metadata toolkit

This is an unoffical toolkit for getting column comments from Snowflake or Oracle into Tableau Catalog datasource descriptions. This code is combined from Madelines Lee's awesome [snowflake-tabcatalog](https://github.com/madelinefromtableau) and [dbt_to_tabcatalog](https://github.com/madelinefromtableau/dbt_to_tabcatalog) repositories. I not a developer, so the code is probably quite messy. Please use this toolkit only for demo or testing purposes.
It includes a jupyter notebook, that goes through authentcation, comment-queries and updating the correct columns in Tableau.

# How to use

 1. Install either the [snowflake-connector](https://github.com/snowflakedb/snowflake-connector-python) or [oracledb](https://github.com/oracle/python-oracledb) python client.

```
pip install snowflake-connector-python
pip install oracledb
```

2. Add your connection variables in the [connection_variables.py document](connection_variables.py)

- Create your personal Tableau token [here](https://help.tableau.com/current/pro/desktop/en-us/useracct.htm#create-and-revoke-personal-access-tokens).

3. Comment out parts of the jupyter notebook you don't need for your project (snow/oracle).
4. Let the jupyter blocks run!

# Things to come

dbt metadata ingestion will follow.
