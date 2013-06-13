from xml.dom import minidom
xmldoc = minidom.parse('test.xml')
itemlist = xmldoc.getElementsByTagName('item') 
