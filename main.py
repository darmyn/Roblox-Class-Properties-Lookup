import requests
import json

ok = 200
host = "https://raw.githubusercontent.com/MaximumADHD/Roblox-Client-Tracker/roblox/API-Dump.json"
result = requests.get(host)

if result.status_code == ok:
    restructure = {}
    api = result.json()
    for rbxClass in api["Classes"]:
        properties = []
        for property in rbxClass["Members"]:
            if property["MemberType"] == "Property":
                properties.append(property["Name"])
        restructure[rbxClass["Name"]] = properties
    with open("dump.json", "w") as dump:
        dump.write(json.dumps(restructure))
        dump.close()
else:
    print(result.status_code)
