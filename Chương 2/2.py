import xml.etree.ElementTree as ET

# Tạo cấu trúc node lồng nhau
root = ET.Element('Students')

student1 = ET.SubElement(root, 'Student')
id1 = ET.SubElement(student1, 'Id')
id1.text = '001'
name1 = ET.SubElement(student1, 'Name')
name1.text = 'Nguyễn Văn A'
birth_year1 = ET.SubElement(student1, 'BirthYear')
birth_year1.text = '1999'
class1 = ET.SubElement(student1, 'Class')
class1.text = 'K15'
gender1 = ET.SubElement(student1, 'Gender')
gender1.text = 'Male'

student2 = ET.SubElement(root, 'Student')
id2 = ET.SubElement(student2, 'Id')
id2.text = '002'
name2 = ET.SubElement(student2, 'Name')
name2.text = 'Nguyễn Thị B'
birth_year2 = ET.SubElement(student2, 'BirthYear')
birth_year2.text = '2000'
class2 = ET.SubElement(student2, 'Class')
class2.text = 'K15'
gender2 = ET.SubElement(student2, 'Gender')
gender2.text = 'Female'

# Tạo file XML
tree = ET.ElementTree(root)
tree.write('students.xml')