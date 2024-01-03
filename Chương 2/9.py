import json

json_data = """
{
    "company": "Công ty TNHH Đất Việt",
    "address": "abc Giải Phóng – Hà Nội",
    "departments": [
        {"name": "Đơn vị A1", "employees": 10},
        {"name": "Đơn vị A2", "employees": 20},
        {"name": "Đơn vị A3", "employees": 30},
        {"name": "Đơn vị A4", "employees": 15},
        {"name": "Đơn vị A5", "employees": 5}
    ]
}
"""
python_obj = json.loads(json_data)

# Xử lý và hiển thị thông tin của các đơn vị
total_employees = sum(dept["employees"] for dept in python_obj["departments"])

print("Tên công ty:", python_obj["company"])
print("Địa chỉ:", python_obj["address"])
print("-----Thống kê nhân viên theo đơn vị------")

for i, dept in enumerate(python_obj["departments"]):
    percentage = (dept["employees"] / total_employees) * 100
    print(f"{i + 1}./Tên đơn vị: {dept['name']}")
    print(f"- Số nhân viên: {dept['employees']}")
    print(f"- Tỷ lệ: {percentage:.2f}%")