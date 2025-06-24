import json

data = {}
with open("sample-data.json", "r") as f:
    data = json.load(f)

arr = data["imdata"]
print("Interface Status")
print(
    "================================================================================"
)
print(
    "DN                                                 Description           Speed    MTU"
)
print(
    "-------------------------------------------------- --------------------  ------  ------"
)

for i in arr:
    print(
        i["l1PhysIf"]["attributes"]["dn"],
        i["l1PhysIf"]["attributes"]["speed"],
        i["l1PhysIf"]["attributes"]["mtu"],
    )
