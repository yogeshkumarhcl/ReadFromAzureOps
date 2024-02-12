import requests
import base64
def get_content_azuredevops(pat,project_name,repository_name,file_path,organization_url,branch_name = ''):

    authorization = str(base64.b64encode(bytes(':'+pat, 'ascii')), 'ascii')

    # The REST API URL for retrieving a file from the Git repository
    api_url = f"{organization_url}/{project_name}/_apis/git/repositories/{repository_name}/items?path={file_path}&versionDescriptor.version={branch_name}&includeContent=true&api-version=6.0"
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
