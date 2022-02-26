from xml.etree import cElementTree as ET

document = ET.parse('country_data.xml')
root = document.getroot()

for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print(name, rank)

#print(root.tag)
#print(root[0][2].text)
#print(root.tag, root.attrib)
#print(root[0][2].text)