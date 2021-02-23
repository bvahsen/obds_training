# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
Created on Wed Jan 27 09:48:13 2021

@author: zafar_et7oqrc

Exercise - Genomic File Format Conversion
1. Write a Python script to convert the SAM file to a BED file
• One BED line per SAM line
• Read SAM file input
• Write BED file output - format your output using fstrings
2. Supply input file names using command line parameters
• Supply the SAM file name on the command line using –i or --input
• Supply the BED file name on the command line using –o or --output
3. Write out a gzip compressed file (.bed.gz)
4. Make the script run on the command line
5. Provide a command line argument to pad the intervals in the bed file
6. Output a file with the coordinates of the sequenced fragments rather
than reads

'chrom' 'chromStart' 'chromEnd' 'score' 'strand'
Sam fields
POS QNAME FLAG RNAME MAPQ CIGAR RNEXT PNEXT TLEN SEQ QUAL
"""
#import required modules
import argparse
import gzip

#define input and output files, so they can be added using the command line
parser = argparse.ArgumentParser("") 
parser.add_argument('--output', dest='bedfile_path', help='This is the output file expecting .gz file name')
parser.add_argument('--input', dest='samfile_path', help='Input file name')
parser.add_argument('--pad', dest='added_pad', help='Add a number of the pad at the start and end of the read', default=0)
args = parser.parse_args()

#this defines the output file, which should be zipped as per instructions 
#Use 'wt' is because the content we would write into the bed file is text based on line 68
with gzip.open (args.bedfile_path, 'wt') as bedfile:
    #this defines input file and what we want to do with it
    with open (args.samfile_path, 'r') as samfile:
        #iterate line by line
        for line in samfile:
            #ignore header line
            if "@" in line:
                continue
            #save a variable to store line values
            #split the line into columns
            list_of_fields = line.split('\t')      
            print(list_of_fields)
            #ignore asterisks where no vales were found
            if "*" in list_of_fields[2]:
                continue
            #defining new variables to then extract this from samfile, as we need name of reed, chromosome name, chromosome start, chromosome end, score, strand
            name = list_of_fields[0]
            chrom = list_of_fields[2]
            #chromosome start is given in file, but we need to calculate padding (whether we want to add or remove any part of the read)
            chromStart = int(list_of_fields[3]) - 1 - int(args.added_pad)
            #file doesn't give chromosome end, so we need to calculate this from the start and the length of the read
            chromEnd = int(len(list_of_fields[9])) + int(list_of_fields[3]) - 1 + int(args.added_pad)
            score = "."
            strand = "+"
            #print(chromStart)
            #print(chromEnd)
            bedfile.write(F"{chrom}\t{chromStart}\t{chromEnd}\t{name}\t{score}\t{strand}\n")
#print(bedfile)
#print(args)


