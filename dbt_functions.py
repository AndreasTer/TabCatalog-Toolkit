import requests
import json
import pandas as pd

#get dbt account id
def get_account_id(token):
    
    url = "https://cloud.getdbt.com/api/v2/accounts/"

    payload={}
    headers = {
      'Content-Type': 'appication/json',
      'Authorization': 'Token '+ token
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    #print(response.text)
    response_json = json.loads(response.text)
    account_id = response_json['data'][0]['id']
    return(account_id)

#get jobs by account
def get_jobs(account_id, token):
    url = "https://cloud.getdbt.com/api/v2/accounts/"+account_id+"/jobs"

    payload={}
    headers = {
      'Content-Type': 'appication/json',
      'Authorization': 'Token '+ token
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response_json = json.loads(response.text)
    job_dataframe = pd.json_normalize(response_json['data'])
    name_plus_job_id = job_dataframe[['id','name']]
    return(name_plus_job_id)

#Create table of models/executecompletedat/uniqueId
#Input: job ID, PAT Token
#Output: Table with all models run during the job and their executedCompletedAt, model name (uniqueId), and database written to.

def get_models_information(token, job_id):

    url = "https://metadata.cloud.getdbt.com/graphql"
    job_id = '102781'
    payload="{\"query\":\"{\\n  models(jobId: " + job_id + ") {\\n    uniqueId\\n    executionTime\\n    status\\n    executeCompletedAt\\n    database\\n    schema\\n\\n  }\\n}\",\"variables\":{}}"
    headers = {
      'Authorization': 'Token ' + token,
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    response_json = json.loads(response.text)
    models_table = pd.json_normalize(response_json['data']['models'])
    models_table = models_table[['uniqueId', 'executeCompletedAt', 'database']]
    return(models_table)

def get_all_column_descriptions(token, job_id):
    #for each model, get column descriptions in a table with table name, column name, description
    #union all together
    url = "https://metadata.cloud.getdbt.com/graphql"

    payload="{\"query\":\"{\\n  models(jobId: " + job_id + ") {\\n    uniqueId\\n    executionTime\\n    status\\n    executeCompletedAt\\n    database\\n    columns {\\n        name\\n        description\\n    }\\n\\n  }\\n}\",\"variables\":{}}"
    headers = {
      'Authorization': 'Token '+ token,
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    response_json = json.loads(response.text)
    models_table = pd.json_normalize(response_json['data']['models'])
    model_to_text_description = models_table[['uniqueId', 'executeCompletedAt', 'database']]
    column_info = pd.DataFrame(columns = ['name','description','uniqueId'])
    
    for index,row in models_table.iterrows():
        

        column_descriptions = pd.json_normalize(row['columns'])
        column_descriptions['uniqueId'] = row['uniqueId'].split('.')[-1]
        column_info = pd.concat([column_info, column_descriptions], ignore_index=True)
    
    to_return = [model_to_text_description, column_info]    
    return(to_return)

