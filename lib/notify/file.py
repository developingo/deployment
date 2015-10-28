import json
from datetime import datetime
from lib.settings_loader import settings

"""
Send deploy messages to json files
"""

def deploy_finished(deploy_data):
    with open('%s_'%settings.NAME + datetime.now().strftime('%Y-%m-%dT%H-%M-%S.%f')+'.json', 'w') as message_file:
        json.dump(deploy_data, message_file)

if __name__ == '__main__':
    print()
