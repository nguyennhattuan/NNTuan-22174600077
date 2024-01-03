import json

json_data = '{"name": "Tuấn", "age": 20, "city": "Nghệ An"}'

python_obj = json.loads(json_data)

print("Name: ", python_obj["name"])
print("Age: ", python_obj["age"])
print("City: ", python_obj["city"])