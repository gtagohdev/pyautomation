#!/usr/bin/env python3
import os
from PIL import Image, UnidentifiedImageError

image_path = 'supplier-data/images'

def change_image():
    # assume images folder found in current working directory (user home)
    image_source = os.path.join(os.path.expanduser('~'), image_path)
    # get first level of files information
    rootdir, dirs, files = next(os.walk(image_source, topdown=True))
    for f in files:
        image_path_from = os.path.join(rootdir, f)
        # use the same location to save image in jpeg format
        image_path_to = os.path.join(rootdir, os.path.splitext(f)[0])
        print('Transforming image from {} to {}.jpeg'.format(image_path_from, image_path_to))

        try:
            im = Image.open(image_path_from)
            if not im.mode == 'RGB':
                im = im.convert('RGB')
            im.resize((600,400)).save('{}.jpeg'.format(image_path_to))
        except UnidentifiedImageError:
            print('Invalid image file found! {}'.format(image_path_from))
            # ignore it and continue with other files

if __name__ == '__main__':
    change_image()

