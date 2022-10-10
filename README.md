# Tableau Catalog toolkit for dbt-cloud and 

This is an unoffical toolkit for getting column comments from dbt-cloud and various databases into the Tableau Catalog. It works for both datasource descriptions and data quality warnings in Tableau Catalog. Currently code for snowflake and oracle is included, but others could easily be added.

This code is combined from Madelines Lee's awesome [snowflake-tabcatalog](https://github.com/madelinefromtableau) and [dbt_to_tabcatalog](https://github.com/madelinefromtableau/dbt_to_tabcatalog) repositories. I not a developer, so the code is probably quite messy. Please use this toolkit only for demo or testing purposes.

The code consists of a jupyter notebook that goes through three steps. Authentcation, metadata queries from databases or dbt and updating the metadata in Tableau catalog.

The Tableau [Data Management Addon](https://www.tableau.com/de-de/products/add-ons/data-management) is required to do metadata ingestion. Dbt-cloud requires a Team license for using the metadata api.

# How to use

 1. Install either the [snowflake-connector](https://github.com/snowflakedb/snowflake-connector-python) or [oracledb](https://github.com/oracle/python-oracledb) python client.

```
pip install snowflake-connector-python
pip install oracledb
```

2. Add your connection variables in the [connection_variables.py document](connection_variables.py)

- Create your personal Tableau token [here](https://help.tableau.com/current/pro/desktop/en-us/useracct.htm#create-and-revoke-personal-access-tokens).
- Get your User token for dbt-cloud [here](https://docs.getdbt.com/docs/dbt-cloud/dbt-cloud-api/user-tokens)

3. Comment out parts of the jupyter notebook you don't need for your project. If you only want to add data-quality warnings from dbt, comment out the snowflake and oracle part.
4. Let the jupyter blocks run!


