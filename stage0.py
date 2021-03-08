import requests
import json
from env import config
from requests.exceptions import HTTPError

base_url = 'MERAKI_BASE_URL'
endpoint = f"{config['MERAKI_BASE_URL']}/organizations"


headers = {
    "X-Cisco-Meraki-API-Key": config['MERAKI_KEY']
}

try:
    response = requests.get(
        url=f"{endpoint}", headers=headers)
    if response.status_code == 200:
        orgs = response.json()
        for org in orgs:
            if org['name'] == 'DevNet Sandbox':
                org_id = org['id']
except HTTPError as https:
    print(ex)

except Exception as ex:
    print(ex)

endpoint = f"{endpoint}/{org_id}/networks"

try:
    response = requests.get(
        url=f"{endpoint}", headers=headers)
    if response.status_code == 200:
        nets = response.json()
        for net in nets:
            if net['name'] == 'DevNet Sandbox ALWAYS ON':
                net_id = net['id']
except HTTPError as https:
    print(ex)
except Exception as ex:
    print(ex)


endpoint = f"{config['MERAKI_BASE_URL']}/networks/{net_id}/devices"


try:
    response = requests.get(
        url=f"{endpoint}", headers=headers)
    if response.status_code == 200:
        devices = response.json()
        for device in devices:
            data = (device['name'], device['mac'],
                    device['serial'])
            print(data)

except HTTPError as https:
    print(ex)
except Exception as ex:
    print(ex)

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
