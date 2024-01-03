import xml.etree.ElementTree as ET

# Tạo cấu trúc node lồng nhau
company = ET.Element('Company')
name = ET.SubElement(company, 'Name')
name.text = 'Tên công ty'
address = ET.SubElement(company, 'Address')
address.text = 'Địa chỉ công ty'
phone = ET.SubElement(company, 'Phone')
phone.text = 'Số điện thoại công ty'
tax_code = ET.SubElement(company, 'TaxCode')
tax_code.text = 'Mã số thuế công ty'

# Tạo file XML
tree = ET.ElementTree(company)
tree.write('company.xml')