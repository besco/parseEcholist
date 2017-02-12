# coding: utf8

from sys import exit as sys_exit
from sys import argv as sys_argv

if len(sys_argv) == 1:
    echolist = '/home/besco/Downloads/echos.txt'
else:
    echolist = sys_argv[1]


def readfile(filename):
    echolist = list()
    try:
        f = open(filename, "r", errors='replace')
    except:
        print("Can't open file:", echolist)
        sys_exit(8)
    while True:
        line = f.readline()
        if not line:
            break
        if '....' in line:
            echo = line.strip("\n").split()[0]
            status = line.strip("\n").split()[2]
            flags = line.strip("\n").split()[3]
            desc = line.split(" \"")[1].strip("\"\n ")
            echolist.append({'name': echo, 'desc': desc, 'status': status, 'flags': flags})
        elif line[0] == ' ' and 'Origin' not in line:
            echolist[-1]['desc'] = echolist[-1]['desc'].strip("\"\t") + " " + line.strip("\"\t\n ")
    return echolist


parsed_echos = readfile(echolist)
for i in range(len(parsed_echos)):
    print('{:3d}. {:40} {}'.format(i+1, parsed_echos[i]['name'], parsed_echos[i]['desc']))
    # print(parsed_echos[i])