#!/usr/bin/env python3

from os import listdir
from os.path import isfile, join
import requests

def get_reviews(path):
    """Returns a list of review file paths in the directory indicated by path"""
    files = [path + f  for f in listdir(path) if isfile(join(path, f)) and not f.startswith(".")]
    #startswith(".") to skip hidden files
    return files

def assemble_list(reviews):
    """Assemble the list of dictionaries that will be passed to the request post command"""
    list = []
    for review in reviews:
        #print(review)
        list.append(parse_review(review))
    return list

def parse_review(review):
    """Parse the review based on the format provided"""
    the_review = {"title": "", "name": "", "date": "", "feedback": ""}
    #print("Parsing review for file: {f}".format(f=review))
    with open(review, 'r') as file:
        lines = file.readlines()
        for num, content in enumerate(lines):
            content = content.strip()
            if num == 0:
                the_review["title"] = content
            elif num == 1:
                the_review["name"] = content
            elif num == 2:
                the_review["date"] = content
            else:
                the_review["feedback"] = content
    return the_review

def main():
    reviews = get_reviews("/data/feedback/")
    list = assemble_list(reviews)
    for l in list:
        #Update the address between the <>
        response = requests.post('http://<Update address>/feedback/', json=l) #Don't forget the final / ;P
        response.raise_for_status()

if __name__ == "__main__":
    main()
