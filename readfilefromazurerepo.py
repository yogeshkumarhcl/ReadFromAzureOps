# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 23:25:03 2024

@author: v-kumaryo
"""

import requests
import base64


from flask import Flask,request
import json

# Initializing flask app
app = Flask(__name__)



@app.route('/get_content_azuredevops/<pat>/<project_name>/<repository_name>/<file_name>/<branch_name>', methods=['GET','POST'])
def get_content_azuredevops(pat,project_name,repository_name,file_name,branch_name = ''):

    organization_url = 'https://dev.azure.com/microsoft'
    authorization = str(base64.b64encode(bytes(':'+pat, 'ascii')), 'ascii')

    # The REST API URL for retrieving a file from the Git repository
    api_url = f"{organization_url}/{project_name}/_apis/git/repositories/{repository_name}/items?path={file_name}&versionDescriptor.version={branch_name}&includeContent=true&api-version=6.0"
    # Headers for authentication
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Basic '+authorization
    }

    # Make the GET request to fetch the file content
    response = requests.get(api_url, headers=headers)

    # Check for a successful response
    if response.status_code == 200:
        # The file content is in the response's JSON under the 'content' key
        file_content = response.json().get('content', '')

    else:
        file_content = "Unable to fetch data..."
        print("Failed to retrieve file content")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        print(file_content)
    return response.json().get('content', '')


@app.route("/demo", methods=['GET'])
def demo():
    return "This is a demo api"




# Running the api
if __name__ == '__main__':
    app.run()   
