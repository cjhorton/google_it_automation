#!/usr/bin/env python3

from os import listdir
from os.path import isfile, join
from PIL import Image

def get_images_in_dir(path):
    """Returns a list of images in the directory indicated by path"""
    #Code borrowed from Stack Overflow - https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
    #Credit to user 'pycruft'

    onlyfiles = [f for f in listdir(path) if isfile(join(path, f)) and not f.startswith(".")]
    #startswith(".") to skip hidden files
    return onlyfiles

def modify_image(name, o_dir, d_dir):
    """modifies an image with name located at orig path and saves to dest path"""
    try:
        print("Generating jpeg for {}".format(name))
        img = Image.open(o_dir + name)
        new_img = img.rotate(90).resize((128, 128))
        new_img = new_img.convert("RGB")
        new_img.save(d_dir + name, "JPEG", quality=100)
    except Exception as  e:
        print(e)

def main():
    """Saves modified images to a new directory"""
    #update the images_path and corrected_path
    images_path = "<absolute path to images>"
    corrected_path = "<absolute path to destination directory>"
    images = get_images_in_dir(images_path)

    #Loop through the images.  For each image, correct, and save in new directory 
    for i in images:
        modify_image(i, images_path, corrected_path)

if __name__ == "__main__":
    main() 
