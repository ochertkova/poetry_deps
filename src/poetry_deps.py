#!/usr/bin/env python3

import re
import os

text_sample = "poetry_sample.txt"
def get_pack_list(text_sample):
    """Get package information from sample.lock file into a list of strings"""
    #package_pattern = re.search(r"\((\w*)\)", text_sample)
    #package_deps_pattern = re.search(r"\((\w*)\)", text_sample)
    #package_extras_pattern = re.search(r"\((\w*)\)", text_sample)
    with open(text_sample, mode='r',encoding='UTF-8') as file:
        return parse_packages(file.readlines())

def get_test_data():
    retval = list(map(parse_package, get_pack_list(text_sample)))
    return retval

def parse_packages(lines):
    pack_list_str = []
    pack_str = ''

    for line in lines:
        if line.strip() == """[metadata]""":
            break
        if line.strip() == """[[package]]""":
            if pack_str == "": #Skip first empty list
                continue
            pack_list_str.append(pack_str)
            pack_str = ""
            continue
        if line.strip() == "": # dont include empty lines in package def lines
           continue
        pack_str = pack_str + line
    pack_list_str.append(pack_str) #Append the last package)
        
    return pack_list_str

def parse_package(pack_str):
    pack_lines = pack_str.splitlines()
    pack_dict = {}
    line_number = 0
    while line_number < len(pack_lines):
        line = pack_lines[line_number]
        try:
            if line == "[package.dependencies]" or pack_str[line_number] == "[package.extras]":
                break
            (key,value) = re.split(r'\s=\s',line.strip(),maxsplit = 1) #Split and unpack on regex expression
            if key == "optional": #  Value is a boolean
                value = value.strip().lower() == "true"
            else: # Value is a string
                re_obj = re.search(r'^\"(.*)\"$', value)
                if re_obj:
                    value = re_obj.group(1)
            pack_dict[key] = value
        except:
            break
        line_number += 1
   
    
    pack_dict["deps"] = []
    if line_number < len(pack_lines) and pack_lines[line_number] == "[package.dependencies]":
        line_number += 1
        while line_number < len(pack_lines):
            line = pack_lines[line_number]
            if line == "[package.extras]":
                break
            (key,value) = re.split(r'\s=\s',line.strip(),maxsplit = 1) #Split and unpack on regex expression
            dep_dict = {'name':key}
            if value.startswith('{'):
                # {version = ">=0.9", optional = true, markers = "extra == \"filecache\""}
                key_values = value[1:-1].split(', ')
                for item in key_values:
                    (k,v) = re.split(r'\s=\s',item.strip(),maxsplit = 1)
                    if k == "optional": #  Value is a boolean
                        v = v.strip().lower() == "true" #returns True
                    dep_dict[k] = v
            else:
                dep_dict["version"] = value
            line_number += 1
            pack_dict["deps"].append(dep_dict)
   
    pack_dict["optional_deps"] = []
    if line_number < len(pack_lines) and pack_lines[line_number] == "[package.extras]":
        line_number += 1
        while line_number < len(pack_lines):
            line = pack_lines[line_number]
            (_,value) = re.split(r'\s=\s',line.strip(),maxsplit = 1) #Split and unpack on regex expression
            profile_deps = value[1:-1].split(', ')
            for pd in profile_deps:
                # "sphinx (>=1.6.5,!=1.8.0,!=3.1.0,!=3.1.1)", "sphinx-rtd-theme"
                dep_ver = pd[1:-1].split(' ')
                op_dep_dict = {'name':dep_ver[0]}
                if len(dep_ver) > 1:
                    op_dep_dict['version'] = dep_ver[1]                
                pack_dict["optional_deps"].append(op_dep_dict)
            line_number += 1
    #print(pack_dict)
    pack_dict["rev_deps"] = []
    return pack_dict

def main():
    pack_list_str = get_pack_list(text_sample)
    for pack in pack_list_str:
        print(parse_package(pack))

    #print(get_pack_list(text_sample))

if __name__ == "__main__":
    main()