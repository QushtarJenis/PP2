import json as JSON

json = '{"course": "Python", "level": "beginner"}'
data = JSON.loads(json)
print(data["course"])
