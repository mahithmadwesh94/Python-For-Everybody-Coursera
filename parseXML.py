import xml.etree.ElementTree as ET
data = '''<person>
<name>Chuck</name>
<phone type="intl">
12312312312
</phone>
<email hide="yes"/>
</person>
'''
 
tree = ET.fromstring(data);
print('Name:',tree.find('name').text)