#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 15:24:16 2021

@author: Bjorn1

Write an algorithm to calculate GC Content
"""

sequence = """GGAGGAGGTGGGAGTTTACGGGAGGAAGGGCCACGGAGATGGGTCGCTTCTCCTGGAGCT
AGAGCTGCGGGCTGGGGTCTCCAGGGTTCGGCCCGGGGAGCCGACCCTGGTCGGCCGTCG
GGGCTCTGCTCGGCCCTCCTGAAACCTCCGCCTCCTCCAGCAGGGGGCGGGCCGGGGCCG
CGTCTCGGGGGGAAGGCGATCAGGTCGCCCCCTCCTCCGATTCCCCCGCCTTCCAGGACA
GCCTCCAGCCCAGAGGGGCGGTCCGGGGGCGGGGTCGCACCGCCCCCTCTCGCTCCCAAT
CCCGGGGCGGCCGGGCGGGGGTGGGCAGGGGGCGTGAGGCCGCCCCTGCGTCCCGGGGGC
CCCCCGAAAACGCGCTCCGGGTGCCCGGTCCCTCCGCTGCGCCCTGCCGCCGTCCTCCCG
GGGGTCTCGGGCGGCCGCGGCCGTGTCCTTCGCGTCCCGGCGGCGCGGCGGGAGGGGCCG
GCGTGACGCAGCGGTTGCTACGGGCCGCCCTTATAAATAACCGGGCTCAGGAGAAACTTT
AGCGAGTCAGAGCCGCGCACGGGACTGGGAAGGGGACCCACCCGAGGGTCCAGCCACCAG
CCCCCTCACTAATAGCGGCCACCCCGGCAGCGGCGGCAGCAGCAGCAGCGACGCAGCGGC
GACAGCTCAGAGCAGGGAGGCCGCGCCACCTGCGGGCCGGCCGGAGCGGGCAGCCCCAGG
CCCCCTCCCCGGGCACCCGCGTTCATGCAACGCCTGGTGGCCTGGGACCCAGCATGTCTC
CCCCTGCCGCCGCCGCCGCCTGCCTTTAAATCCATGGAAGTGGCCAACTTCTACTACGAG
GCGGACTGCTTGGCTGCTGCGTACGGCGGCAAGGCGGCCCCCGCGGCGCCCCCCGCGGCC
AGACCCGGGCCGCGCCCCCCCGCCGGCGAGCTGGGCAGCATCGGCGACCACGAGCGCGCC
ATCGACTTCAGCCCGTACCTGGAGCCGCTGGGCGCGCCGCAGGCCCCGGCGCCCGCCACG
GCCACGGACACCTTCGAGGCGGCTCCGCCCGCGCCCGCCCCCGCGCCCGCCTCCTCCGGG
CAGCACCACGACTTCCTCTCCGACCTCTTCTCCGACGACTACGGGGGCAAGAACTGCAAG
AAGCCGGCCGAGTACGGCTACGTGAGCCTGGGGCGCCTGGGGGCCGCCAAGGGCGCGCTG
CACCCCGGCTGCTTCGCGCCCCTGCACCCACCGCCCCCGCCGCCGCCGCCGCCCGCCGAG
CTCAAGGCGGAGCCGGGCTTCGAGCCCGCGGACTGCAAGCGGAAGGAGGAGGCCGGGGCG
CCGGGCGGCGGCGCAGGCATGGCGGCGGGCTTCCCGTACGCGCTGCGCGCTTACCTCGGC
TACCAGGCGGTGCCGAGCGGCAGCAGCGGGAGCCTCTCCACGTCCTCCTCGTCCAGCCCG
CCCGGCACGCCGAGCCCCGCTGACGCCAAGGCGCCCCCGACCGCCTGCTACGCGGGGGCC
GCGCCGGCGCCCTCGCAGGTCAAGAGCAAGGCCAAGAAGACCGTGGACAAGCACAGCGAC
GAGTACAAGATCCGGCGCGAGCGCAACAACATCGCCGTGCGCAAGAGCCGCGACAAGGCC
AAGATGCGCAACCTGGAGACGCAGCACAAGGTCCTGGAGCTCACGGCCGAGAACGAGCGG
CTGCAGAAGAAGGTGGAGCAGCTGTCGCGCGAGCTCAGCACCCTGCGGAACTTGTTCAAG
CAGCTGCCCGAGCCCCTGCTCGCCTCCTCCGGCCACTGCTAGCGCGGCCCCCGCGCGCGT
CCCCCTGCCGGCCGGGGCTGAGACTCCGGGGAGCGCCCGCGCCCGCGCCCTCGCCCCCGC
CCCCGGCGGCGCCGGCAAAACTTTGGCACTGGGGCACTTGGCAGCGCGGGGAGCCCGTCG
GTAATTTTAATATTTTATTATATATATATATCTATATTTTTGTCCAAACCAACCGCACAT
GCAGATGGGGCTCCCGCCCGTGGTGTTATTTAAAGAAGAAACGTCTATGTGTACAGATGA
ATGATAAACTCTCTGCTTCTCCCTCTGCCCCTCTCCAGGCGCCGGCGGGCGGGCCGGTTT
CGAAGTTGATGCAATCGGTTTAAACATGGCTGAACGCGTGTGTACACGGGACTGACGCAA
CCCACGTGTAACTGTCAGCCGGGCCCTGAGTAATCGCTTAAAGATGTTCCTACGGGCTTG
TTGCTGTTGATGTTTTGTTTTGTTTTGTTTTTTGGTCTTTTTTTGTATTATAAAAAATAA
TCTATTTCTATGAGAAAAGAGGCGTCTGTATATTTTGGGAATCTTTTCCGTTTCAAGCAT
TAAGAACACTTTTAATAAACTTTTTTTTGAGAATGGTTACAAAGCCTTTTGGGGGCAGTA
ATTGGCTTTTGTTTTTTATTTTTTTACTTTATTTTGGATTTGTAGGATTTTGTTTTTGCG
TTTCTGGTGTGTAGGGGGTTGTGTGTGGGGGGCTGCTGTTATTTTTGGAGGTTTTGGTGG
TTGGGTGGGGGTGTTGCAGCTGGTTTTTCTGCCTCCTCTGCTACTCCCCCTCCCACACAC
ACAGGGTCTGCTTGAGATGGGGTTCCAGCCCCGGGGGAAAGGGGAGAAGAGTAATGGGTC
AGGCATTCAGGCTGACTCAGAGCCCCTAGGCGCCGGGACGGGTGGCTGGGAACCCTGCTT
GAGAAGAGATTCCGGAGCCTCTGGCTGGTCCCGAGTGTCAGGCTTGGGTTTGGAAGGGCT
GGGAGGTCTGTGACCCCTGCCCTGTGTTTGGGGACTAGGTAGGCAGGCCTGTGACTGTAG
GAGGAGGGGGTTCAGGTCTTGGTCCTGCTGAGCCCGAGTCAGGGCAGATGCTTTTGGTCA
GTGTAGTGGGGTGGGTTGTTTAAAACACAGTTTGTGTATACATGTGTATTTTAAAGAGGG
GAGCCTGGGTGTGTGGGCGAGTCTGTGTTTGTGTGTCCC"""

#lets count the number of Gs and Cs and the number of total bases in above sequence


#for each character 
#if its G or C, add 1 to something

def count(sequence):
    GC_content = 0
    for character in sequence:
        if character == 'G':
            GC_content = GC_content + 1
        if character == 'C':
            GC_content = GC_content + 1
    return GC_content

def length_count(sequence):
    length_seq = 0
    for character in sequence:
        if character == 'G':
            length_seq = length_seq + 1
        if character == 'C':
            length_seq = length_seq + 1
        if character == 'A':
            length_seq = length_seq + 1
        if character == 'T':    
            length_seq = length_seq + 1
    return length_seq

def proportion(GC_number, length_sequence):
    proportion = (GC_number / length_sequence) * 100
    return proportion

def get_GC_content(sequence):
    length_sequence = length_count(sequence)
    GC_content = count(sequence)
    GC_proportion = proportion(GC_content, length_sequence)
    return GC_proportion

print(get_GC_content(sequence))