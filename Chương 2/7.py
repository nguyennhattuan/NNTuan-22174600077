import json


python_obj = {"name": "Tuấn", "age": 20, "city": "Nghệ An"}

json_data = json.dumps(python_obj)


print("JSON Data: ", json_data)


json_obj = json.loads(json_data)

for key, value in json_obj.items():
    print("Key: ", key)
    print("Value: ", value)