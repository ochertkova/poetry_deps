#!/usr/bin/env python3

import re
import os

text_sample = "sample_mini.txt"
def get_pack_info(text_sample):
    """Get package information from sample.lock file into a dictionary"""
    #package_pattern = re.search(r"\((\w*)\)", text_sample)
    #package_deps_pattern = re.search(r"\((\w*)\)", text_sample)
    #package_extras_pattern = re.search(r"\((\w*)\)", text_sample)
    pack_dict = {}
    pack_list_dict = []
    pack_count = 0
    with open(text_sample, mode='r',encoding='UTF-8') as file:
        for line in file.readlines():
            if line.strip() == """[[package]]""":
                print(pack_dict)
                pack_count = pack_count + 1
                pack_list_dict.append(pack_dict)
                pack_dict = {}
                print(pack_list_dict)
                
            if line.strip() == "[package.dependencies]" or line.strip() == "[package.extras]":
                print("Inside dependencies")
                continue
            if line.strip() == "":
                continue
            print(line)
            try:
                (key,value) = re.split(r'\s=\s',line.strip(),maxsplit = 1) #Split and unpack on regex expression
                pack_dict[key] = value
            except:
                continue
            #print(pack_dict)
            #print(pack_count)
        
    return pack_list_dict

def main():
    print(get_pack_info(text_sample))

main()