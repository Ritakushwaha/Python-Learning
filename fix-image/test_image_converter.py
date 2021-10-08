#!/usr/bin/env python3
 
import os
from PIL import Image
size = (128, 128)
for infile in os.listdir():
    outfile = os.path.splitext(infile)[0]
    try:
        with Image.open(infile).convert("RGB") as im:
            if im.format != "JPEG":
                im.thumbnail(size)
                im.rotate(270).save(r"./opt/icons/"+outfile+".jpg")
    except OSError as e:
        print("cannot create thumbnail for", infile, e)