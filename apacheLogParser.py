#!/usr/bin/env python3

import os, re, argparse
from tabulate import tabulate

# Required arguments are set
parser = argparse.ArgumentParser(description="Apache Log Parser Tool")
parser.add_argument("-l", "--log", type=str, metavar="",  help="Apache Log Parser", required=True)
parser.add_argument("-i", "--ip", type=str, metavar="",  help="enter IP address")
parser.add_argument("-u", "--url", type=str, metavar="",  help="enter the URL")
parser.add_argument("-p", "--path", type=str, metavar="",  help="enter the path or endpoint of the URL")
parser.add_argument("-m", "--method", type=str, metavar="",  help="enter HTTP request method")
parser.add_argument("-s", "--status", type=str, metavar="",  help="enter the resposne status code")
args = parser.parse_args()


# Function that checks if the logs are matched or not.
def isPresent(log, compare_param):
    list = log.split(" ")
    for i in range(0, len(list)): 
        list[i] = list[i].strip("\"")
    
    for i in compare_param:
        if i not in list:
            return
    
    return [list[0], list[3]+list[4], list[5], list[6], list[7], list[8], list[9], list[10]]

# List where returned log will be stored to display
data = []

if os.path.isfile(args.log): 
    compare = []
    if args.ip:
        if re.match(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', args.ip):
            compare.append(args.ip)
        else:
            print("Improper IP Address format: {ip}".format(ip=args.ip))
            exit()
    
    if args.url:
        if re.match(r'[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)', args.url):
            compare.append(args.url)
        else:
            print("Improper path format: {url}".format(url=args.url))
            exit()
    
    if args.path:
        if re.match(r'^(\/.+)\/([^\/]*)$|^(\/.+)', args.path):
            compare.append(args.path)
        else:
            print("Improper path format: {path}".format(path=args.path))
            exit()

    
    if args.method:
        if args.method in ["GET", "POST", "PUT", "DELETE", "POST", "PURGE", "UPDATE"]:
            compare.append(args.method)
        else: 
            print("Improper method name: {method}".format(method=args.method))
            exit()
    
    if args.status:
        try:
            if int(args.status) >= 100 and int(args.status) < 600:
                compare.append(args.status)
            else:
                print("Improper status code:  {status}".format(status=args.status))
                exit()
        except: 
            print("Improper Status Code")
            exit()

    if compare:
        file = open(args.log)
        logs = file.readlines()
        file.close()
        for log in logs:
            log = log.strip()
            tmp = isPresent(log, compare)
            if tmp:
                data.append(tmp)
else: print("There is no file or directory named \"{file}\"" .format(file=args.log))

print(tabulate(data, headers=["IP ADDRESS", "DATE/TIME", "METHOD", "PATH", "PROTOCOL", "STATUS_CODE", "SIZE", "URL"]))
