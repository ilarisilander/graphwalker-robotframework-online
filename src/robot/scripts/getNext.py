import requests
import json
import communicator

'''
This script is imported in the robot test file as a Library.
RobotFramework will call get_next() in runtime.

This script makes a GET request (hasNext) to the graphwalker REST API to see if
the API has any more steps in the model.
Then it makes another GET request (getNext) to get the name of the next step in the model.

The name is then returned to the RobotFramework test and the name is also sent to the communicator.
'''

def get_next():
    has_next_response = requests.get('http://localhost:8887/graphwalker/hasNext')
    response_json = json.loads(has_next_response.text)
    if response_json['hasNext'] == 'true': # Check if there are any more steps in the REST API
        get_next_response = requests.get('http://localhost:8887/graphwalker/getNext')
        json_file = json.loads(get_next_response.text)
        #communicator.get_data(json_file['currentElementName']) # Send step name to communicator
        return json_file['currentElementName'] # Send step name to RobotFramework
    elif response_json['hasNext'] == 'false':
        return 'false'

# print(get_next())
