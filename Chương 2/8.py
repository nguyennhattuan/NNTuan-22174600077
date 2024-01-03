import json

python_obj = {"name": "Tuấn", "age": 20, "city": "Nghệ An"}

json_data = json.dumps(python_obj, indent=4)

print("JSON Data: ", json_data)