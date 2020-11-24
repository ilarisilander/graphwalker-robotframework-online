import requests
import json

'''
This script is imported in the robot test file as a Library.
RobotFramework will call get_next() in runtime.

This script makes a GET request (hasNext) to the graphwalker REST API to see if
the API has any more steps in the model.
Then it makes another GET request (getNext) to get the name of the next step in the model.

The name is then returned to the RobotFramework test and the name is also sent to the communicator.
'''

def get_next():
    has_next_response = requests.get('http://localhost:8887/graphwalker/hasNext') # GET request to check if model has a step (returns true or false)
    response_json = json.loads(has_next_response.text)
    if response_json['hasNext'] == 'true': # If the response is true (has a step)
        get_next_response = requests.get('http://localhost:8887/graphwalker/getNext') # Get the next step from REST API
        json_file = json.loads(get_next_response.text)
        json_object = {'step': json_file['currentElementName']} # Create an object with the name of the step
        data = json.dumps(json_object, indent=4) # Convert the object to JSON
        new_headers = {'Content-type': 'application/json', 'Accept': 'text/plain'} # Headers for the post request
        requests.post('http://127.0.0.1:5000/', data = data, headers = new_headers) # Send the JSON to the Flask server
        return json_file['currentElementName'] # Send step name to RobotFramework
    elif response_json['hasNext'] == 'false':
        return 'false' # Return false to RobotFramework (no more steps in the model)

#get_next() # For testing purpose. run: python getNext.py to activate the get_next() manually (no need to run RobotFramework)
