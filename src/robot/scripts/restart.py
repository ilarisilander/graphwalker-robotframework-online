import subprocess
import requests

# This function is called from settings_keywords as Reset Rest Api
def reset_rest_api():
    subprocess.run('curl -X PUT http://localhost:8887/graphwalker/restart')

    # Regular requests put did not work for me, so I had to restart the API with this shell command
