#!/usr/bin/env python
import sys, string
import re
import nltk
import nltk.data
from nltk.tokenize import word_tokenize

def main():
    
    data_dir = "/Users/Brishti/Documents/Internships/scripts/"
    inputfile = open(data_dir + 'output3.txt', 'r')
<<<<<<< HEAD
    # outputfile = open(data_dir + 'soldby.txt', 'w')
    outputfile = open(data_dir + 'pnsoldby.txt', 'w')
=======
    outputfile = open(data_dir + 'soldby.txt', 'w')
>>>>>>> ea1ce2f3f187e104fd4d3151e44ab93ad7e0d8ed
    
    for line in inputfile:
        if re.match("^\s*$", line):
            continue
        line = line.split('|')
        # print line[2]
        
<<<<<<< HEAD
        # pattern = re.compile("^.*[S|s]old by\s(.*?\s.*?\s)")
        pattern = re.compile("^.*Printed and sold by\s(.*?\s.*)")
=======
        pattern = re.compile("^.*[S|s]old by\s(.*?\s.*?\s)")
>>>>>>> ea1ce2f3f187e104fd4d3151e44ab93ad7e0d8ed
        
        find = pattern.search(line[2])
        if find:
            outputfile.write(line[0] + '|' + find.group(1)+'\n')
            print line[0] + ' ' + find.group(1)
        else:
            continue
            
    inputfile.close()
    outputfile.close()

if __name__ == "__main__":
    main()