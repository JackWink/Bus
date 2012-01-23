#!/usr/bin/env python
import requests
import argparse
import re
import sys

def get_max_width(table, i):
    return max([len(row[i]) for row in table])

def print_table(out, table):
    col_paddings = []
    for i in range(len(table[0])):
        col_paddings.append(get_max_width(table, i))
   
    print >> out, "\n\n", 
    print >> out, table[0][0].ljust(col_paddings[0] + 1),
    for i in range(1, len(table[0])):
        col = table[0][i].rjust(col_paddings[i] + 2)
        print >> out, col,
    

    print >> out, "\n" 
    print >> out, "-" * (sum(col_paddings) + 3 * len(col_paddings))

    table.pop(0)
    for row in table:
        print >> out, row[0].ljust(col_paddings[0] + 1),
        for i in range(1, len(row)):
            col = row[i].rjust(col_paddings[i] + 2)
            print >> out, col,
        
        print >> out




# Get the route args
parser = argparse.ArgumentParser(description='Display the current bus schedules')
parser.add_argument('route', nargs=1, help='route you\'re trying to view')
args = parser.parse_args()
args.route[0] = args.route[0].upper()

# Get the routes
r = requests.get("http://mobile.aata.org/rideguide_m.asp?route=" + args.route[0])

# parse them
try:
    arr = r.content.split("<hr />")
    routes = [['', '', '', '', ''] for x in range(len(arr) - 1) ]
    routes[0] = ["Direction", "Arriving", "Location", "Next Stop", "Time"]


    # Regex to split the bus direction and time delay
    r = re.compile('(On time|[0-9]+ min ahead|[0-9]+ min behind)')


    for x in xrange(1, len(arr)-1):
        temp = arr[x].split("<br />")

        # strip bus number and space
        temp[0] = temp[0][4:]
        
        # Split the direction and time delay
        loc = r.split(temp[0])
        routes[x][0] = loc[0] 
        routes[x][1] = loc[1]

        # Strip the @ symbol
        routes[x][2] = temp[1][2:]

        # Split the arival time and next stop 
        routes[x][4] = temp[2][-5:].strip()
        routes[x][3] = temp[2][:-5].strip()


    # Print the table
    out = sys.stdout
    print_table(out, routes)
    print "\n"
except:
    print "Info for route " + args.route[0] + " is unavailable.";
