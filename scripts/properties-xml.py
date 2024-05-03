#!/usr/bin/env python3

import os, sys, glob
import xml.etree.ElementTree as ET
from io import BytesIO

os.chdir(sys.argv[1])
dirname='/usr/share/backgrounds/gnome-local-custom'
wallpapers = ET.Element('wallpapers')
for wallpaper in glob.glob('*'):
    wallpaper_element = ET.SubElement(wallpapers, 'wallpaper', attrib = {'deleted': 'false'})
    filename = ET.SubElement(wallpaper_element, 'filename')
    filename.text = f"{dirname}/{wallpaper}"
    name = ET.SubElement(wallpaper_element, 'name')
    name.text = wallpaper
    options = ET.SubElement(wallpaper_element, 'options')
    options.text = 'zoom'
    pcolor = ET.SubElement(wallpaper_element, 'pcolor')
    pcolor.text = '#000000'
    scolor = ET.SubElement(wallpaper_element, 'scolor')
    scolor.text = '#ffffff'

out = BytesIO()
xmldoc = ET.ElementTree(wallpapers)
ET.indent(xmldoc)
xmldoc.write(out)
print('<?xml version="1.0" encoding="UTF-8"?>')
print('<!DOCTYPE wallpapers SYSTEM "gnome-wp-list.dtd">')
print(out.getvalue().decode())
