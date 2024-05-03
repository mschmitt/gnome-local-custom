#!/usr/bin/env python3

import os, sys, glob
import xml.etree.ElementTree as ET
from io import BytesIO

os.chdir(sys.argv[1])
gresources = ET.Element('gresources')
gresource = ET.SubElement(gresources, 'gresource', attrib = {'prefix': '/org/gnome/shell/theme'})
for resourcefile in glob.glob('*'):
    file = ET.SubElement(gresource, 'file')
    file.text = resourcefile

out = BytesIO()
xmldoc = ET.ElementTree(gresources)
ET.indent(xmldoc)
xmldoc.write(out, encoding='utf-8', xml_declaration=True)
print(out.getvalue().decode())
