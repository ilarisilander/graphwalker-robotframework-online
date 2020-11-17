import requests
import json
import communicator

def get_next():
    has_next_response = requests.get('http://localhost:8887/graphwalker/hasNext')
    response_json = json.loads(has_next_response.text)
    if response_json['hasNext'] == 'true': # Check if there are any more steps in the REST API
        get_next_response = requests.get('http://localhost:8887/graphwalker/getNext')
        json_file = json.loads(get_next_response.text)
        #communicator.get_data(json_file['currentElementName']) # Send data to communicator
        return json_file['currentElementName'] # Send data to RobotFramework
    elif response_json['hasNext'] == 'false':
        return 'false'

# print(get_next())
