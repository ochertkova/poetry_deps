#!/usr/bin/env python3

import re
import os

text_sample = "sample_mini.txt"
def get_pack_list(text_sample):
    """Get package information from sample.lock file into a list of strings"""
    #package_pattern = re.search(r"\((\w*)\)", text_sample)
    #package_deps_pattern = re.search(r"\((\w*)\)", text_sample)
    #package_extras_pattern = re.search(r"\((\w*)\)", text_sample)
    with open(text_sample, mode='r',encoding='UTF-8') as file:
        return parse_packages(file.readlines())

def get_test_data():
    return list(map(parse_package, get_pack_list(text_sample)))

def parse_packages(lines):
    pack_list_str = []
    pack_str = ''

    for line in lines:
        if line.strip() == """[[package]]""":
            if pack_str == "": #Skip first empty list
                continue
            pack_list_str.append(pack_str)
            continue
            #if line.strip() == "[package.dependencies]" or line.strip() == "[package.extras]":
                #continue
            #if line.strip() == "":
                #continue
        pack_str = pack_str + line
    pack_list_str.append(pack_str) #Append the last package
        #print(pack_str)
           # try:
            #    (key,value) = re.split(r'\s=\s',line.strip(),maxsplit = 1) #Split and unpack on regex expression
            #    pack_dict[key] = value
           # except:
                #continue
            #print(pack_dict)
            #print(pack_count)
        
    return pack_list_str

def parse_package(pack_str):
    pack_lines = pack_str.splitlines()
    pack_dict = {}
    for line in pack_lines:
        try:
            (key,value) = re.split(r'\s=\s',line.strip(),maxsplit = 1) #Split and unpack on regex expression
            if key == "optional": #  Value is a boolean
                value = value.strip().lower() == "true"
            else: # Value is a string
                re_obj = re.search(r'^\"(.*)\"$', value)
                if re_obj:
                    value = re_obj.group(1)
            pack_dict[key] = value
        except:
            continue 
    return pack_dict

def main():
    pack_list_str = get_pack_list(text_sample)
    for pack in pack_list_str:
        parse_package(pack)
        print(parse_package(pack))

    #print(get_pack_list(text_sample))

main()