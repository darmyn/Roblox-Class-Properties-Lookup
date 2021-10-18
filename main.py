from os import read, write
import requests
import json

ok = 200
host = "https://raw.githubusercontent.com/MaximumADHD/Roblox-Client-Tracker/roblox/API-Dump.json"
result = requests.get(host)

temp_repeated_store = {}

if result.status_code == ok:
    restructure = {}
    api = result.json()
    for rbxClass in api["Classes"]:
        properties = []
        methods = []
        for member in rbxClass["Members"]:
            #for key in member.keys():
            #    if not temp_repeated_store.get(key):
            #        temp_repeated_store[str(key)] = True
            #        print(key)
            #tags = member.get("Tags")
            #if tags:
            #    print(tags)

            tags = member.get("Tags")
            ## print(security)

            if tags:
                if "NotScriptable" in tags:
                    print(member["Name"] + ": " + rbxClass["Name"])
                    continue
            if member["MemberType"] == "Property":
                properties.append(member["Name"])
            if member["MemberType"] == "Method":
                methods.append(member["Name"])
            name = rbxClass["Name"]
        restructure[name] = {
            "properties": properties,
            "methods": methods
        }
    with open("dump.json", "w") as dump:
        dump.write(json.dumps(restructure))
        dump.close()
else:
    print(result.status_code)
