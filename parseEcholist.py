#!/usr/local/bin/python3
# coding: utf8

import re

echolist = "/home/besco/Downloads/240-5832.txt";


def read_file(filename):
    echo = ''
    echolist = list()
    try:
        f = open(filename, "r")
    except:
        print("Can't open file.")
    while True:
        line = f.readline()
        if not line:
            break
        if line[0].strip() != '':
            echo = line.strip("\n").split()[0]
            desc = line.split("\"")[1].strip("\n")
            echolist.append({'name' : echo, 'desc': desc})
        else:
            #desc = "---"+desc.strip("\n") + line.strip()+"---"
            echolist[-1]['desc'] = echolist[-1]['desc'] + " "+line.strip("\"\n ")
            pass
    f.close()
    return echolist

parsed_echos = read_file(echolist)

for i in range(len(parsed_echos)):
    print(parsed_echos[i]['name'] + " - " + parsed_echos[i]['desc'])
