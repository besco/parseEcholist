#!/usr/local/bin/python3.5
# coding: utf8

from sys import exit as sys_exit
from sys import argv as sys_argv

if len(sys_argv) == 1:
    echolist = "/home/besco/Downloads/240-5832.txt"
else:
    echolist = sys_argv[1]



def read_file(filename):
    echolist = list()
    try:
        f = open(filename, "r")
    except:
        print("Can't open file: " + filename)
        sys_exit(8)
    while True:
        line = f.readline()
        if not line:
            break
        if line[0].strip() != '':
            echo = line.strip("\n").split()[0]
            desc = line.split("\"")[1].strip("\n ")
            echolist.append({'name': echo, 'desc': desc})
        else:
            echolist[-1]['desc'] = echolist[-1]['desc'].strip("\t") + " "+line.strip("\"\t\n ")
    f.close()
    return echolist

parsed_echos = read_file(echolist)

for i in range(len(parsed_echos)):
    print('{:3d}. {:40} {}'.format(i+1, parsed_echos[i]['name'], parsed_echos[i]['desc']))
