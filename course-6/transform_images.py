#!/usr/bin/env python3
import os
from PIL import Image, UnidentifiedImageError

from_main_path = 'images'
to_main_path = '/opt/icons' # for windows example d:/temp/icons

def runmain():
    # assume images folder found in current working directory (user home)
    image_source = os.path.join(os.path.expanduser('~'), from_main_path)
    # get first level of files information
    rootdir, dirs, files = next(os.walk(image_source, topdown=True))
    for f in files:
        image_path_from = os.path.join(rootdir, f)
        # define new location to save image in jpeg format
        image_path_to = os.path.join(to_main_path, os.path.splitext(f)[0])
        print('Transforming image from {} to {}.jpeg'.format(image_path_from, image_path_to))

        try:
            im = Image.open(image_path_from)
            if not im.mode == 'RGB':
                im = im.convert('RGB')
            im.rotate(-90).resize((128,128)).save('{}.jpeg'.format(image_path_to))
        except UnidentifiedImageError:
            print('Invalid image file found! {}'.format(image_path_from))
            # ignore it and continue with other files

if __name__ == '__main__':
    runmain()


