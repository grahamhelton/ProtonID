#!/usr/bin/python3
import dns.resolver
import argparse
import sys
from colorama import Fore,Style
# Define colors and lists
domains = []
reset = Style.RESET_ALL
green = Fore.GREEN
purple = Fore.MAGENTA
red = Fore.RED
sep = Fore.BLUE + "---------------------------" + reset
info = Fore.BLUE + "[" + Fore.GREEN + "+" + Fore.BLUE + "]"+ reset
info_bad = Fore.RED+ "[" + Fore.YELLOW+ "!" + Fore.RED+ "]"+ reset

def parse_args():
    '''Gets arguments from command line'''
    parser = argparse.ArgumentParser(usage="\n python3 protonID.py -e email@example.com \n python3 protonID.py -l emails.txt",
            description="ProtonID: Check if an email address or domain uses protonmail.")
    parser.add_argument('-e', '--email', action='store', help="Check a single email")
    parser.add_argument('-l', '--list', action='store', help="Checks every domain in a list.")
    print(parser.print_help())
    return parser.parse_args()

args = parse_args()

def split_email(email):
    '''If arguments have an @ in them, remove text up to and including the @'''
    if '@' in email:
        email = email.split('@',1)[1]
    domains.append(email)
    return domains 

def dns_query(domains):
    '''Queries MX records to check if protonmail exists in them'''
    for x in dns.resolver.resolve(domains,'MX'):
        if 'protonmail' in x.to_text():
            print(sep)
            print(info,green,domains,"has proton mail MX records.",reset)
            print(info,"    Printing proton MX record...")
            print(info,"  ",purple,x.to_text())
            print(sep)
            break
        else:
            print(info_bad,domains,"does not have proton mx records")

if args.list:
    try:
        with open(args.list) as email_list:
            lines = [line.rstrip() for line in email_list]
        
        for i in range(len(lines)):
            split_email(lines[i])
            dns_query(domains[i])

    except:
        print(info_bad,"Error:",red,args.list,reset,"not found. Did you specify the correct file name?")

if args.email:
    split_email(args.email)
    print(domains)
    dns_query(domains[0])
