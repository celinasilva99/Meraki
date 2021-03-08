import requests
import json
from env import config
import meraki

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
            print("Organisation Name: " +
                  org['name'], "Organisation ID: " + org['id'])
            org_id = org['id']
except HTTPError as http:
    print(http)
except Exception as ex:
    print(ex)

endpoint = f"{endpoint}/{org_id}/networks"

try:
    response = requests.get(
        url=f"{endpoint}", headers=headers)
    if response.status_code == 200:
        nets = response.json()
        for net in nets:
            print(net['productTypes'], "Network Name: " + net['name'])
            net_id = net['id']
except Exception as ex:
    print(ex)

endpoint = f"{config['MERAKI_BASE_URL']}/networks/{net_id}/devices"

try:
    response = requests.get(
        url=f"{endpoint}", headers=headers)
    if response.status_code == 200:
        devices = response.json()
        for device in devices:
            print("Device Mac Address: " +
                  device['mac'], "Device Serial Number: " + device['serial'])
except Exception as ex:
    print(ex)
