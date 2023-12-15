import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')
root = tree.getroot()
f = open("demofile2.txt", "w", encoding='UTF-8')

for child in root.findall("./Message"):
    f.write("%s " % child.attrib.get('Date'))
    f.write("%s " % child.attrib.get('Time'))
    f.write("%s -> " % child[0][0].attrib.get('FriendlyName'))
    f.write("%s    " % child[1][0].attrib.get('FriendlyName'))
    f.write("%s\n" % child[2].text)

f.close()