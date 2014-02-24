# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: Paul
"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons
import random
from load import load_seq
dna = load_seq("./data/X73525.fa")


def collapse(L):
    """ Converts a list of strings to a string by concatenating all elements of the list """
    output = ""
    for s in L:
        output = output + s
    return output


def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment
    """
    
    # YOUR IMPLEMENTATION HERE
    
    a = len(dna)
    codonNumber = a/3 #figure out the nubmer of codons in the strand to iterate through
    #print codonNumber
    cCount = 0 
    AA = '' #make an empty string that will become the protein strand
    while cCount < codonNumber:
        codon = dna[cCount*3:cCount*3+3]  #slices a codon
        #print codon
        index = 0
        while index < len(codons):    #iterates through possible codons
            A = codons[index]      ##pulls out the list of codons that match an acid from the main list
            Alen = len(A)
            index1 = 0
            while index1 < Alen:  ##checks to see if the codon is in the list that has been pulled out. NOTE: should probably use the in command, but this works as well
                if A[index1] == codon:
                    intAcid = aa[index] ##if the codon does match, assign the amino acid to an intermediate variable and break the loop
                    #print intAcid
                    break
                index1 = index1+1
 
            index = index+1
        AA = AA + intAcid #appends the found acid to the string
        cCount = cCount+1
    return AA

def coding_strand_to_AA_unit_tests():
    """ Unit tests for the coding_strand_to_AA function """
    input1 = 'TTT'
    expectedOut1 = 'F'
    output1 = coding_strand_to_AA(input1)    
    print 'input:', input1,' expected output:', expectedOut1,' actual output: ',output1
    
    input1 = 'TTTTTC'
    expectedOut1 = 'FF'
    output1 = coding_strand_to_AA(input1)    
    print 'input:', input1,' expected output:', expectedOut1,' actual output: ',output1
    
    input1 = 'TTTGGG'
    expectedOut1 = 'FG'
    output1 = coding_strand_to_AA(input1)    
    print 'input:', input1,' expected output:', expectedOut1,' actual output: ',output1
    
    input1 = 'GTTCGAAGC'
    expectedOut1 = 'VRS'
    output1 = coding_strand_to_AA(input1)    
    print 'input:', input1,' expected output:', expectedOut1,' actual output: ',output1
def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    """
    
    a = dna.upper()
    index = 0 
    complement = ''
    while index<len(dna):  #finds what input is and matches it to an ouput
        b = a[index]
        if b == 'A':
            inter =  'T'
        elif b == 'T':
            inter = 'A'
        elif b == 'C':
            inter = 'G'
        elif b == 'G':
            inter  = 'C'
        else:
            print('Error: Input must be in DNA code')    
        complement = complement + inter
        index = index+1
    return complement[::-1] #reverses the string and returns it
        
        
        
def get_reverse_complement_unit_tests():
    """ Unit tests for the get_complement function """

    input1 = 'ACTGGGCGT'
    expectedOut = 'ACGCCCAGT'
    out = get_reverse_complement(input1)
    print 'input:', input1,', expected output:',expectedOut,', actual output:', out
    
    
    input1 = 'TGATTA'
    expectedOut = 'TAATCA'
    out = get_reverse_complement(input1)
    print 'input:', input1,', expected output:',expectedOut,', actual output:', out
def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    """
    
    a = len(dna)
    codonNumber = a/3
    #print codonNumber
    cCount = 0
    while cCount < codonNumber:
        codon = dna[cCount*3:cCount*3+3]
        #print codon
        if codon in ('TGA','TAA','TAG'): #finds end codon and then slices the string
            endIndex = cCount*3
            return dna[0:endIndex]          
        cCount = cCount+1
    return dna
    

def rest_of_ORF_unit_tests():
    """ Unit tests for the rest_of_ORF function """
    
    input1 = 'ACTGTACTATGA'
    expectedOut = 'ACTGTACTA'
    out = rest_of_ORF(input1)
    print 'input:', input1,', expected output:',expectedOut,', actual output:', out
    
    input1 = 'ACTGTACTATGATAGTTT'
    expectedOut = 'ACTGTACTA'
    out = rest_of_ORF(input1)
    print 'input:', input1,', expected output:',expectedOut,', actual output:', out
    
    input1 = 'TGAACT'
    expectedOut = ''
    out = rest_of_ORF(input1)
    print 'input:', input1,', expected output:',expectedOut,', actual output:', out
    
    input1 = 'ACTTACCTAGAT'
    expectedOut = 'ACTTACCTAGAT'
    out = rest_of_ORF(input1)
    print 'input:', input1,', expected output:',expectedOut,', actual output:', out


        
def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    ORF = []
    a = len(dna)
    codonNumber = a/3
    #print codonNumber
    cCount = 0
    while cCount < codonNumber:
        
        codon = dna[cCount*3:cCount*3+3]
        #print codon
        if codon in ('ATG'):  #finds start codons, takes all of the string after the start codon, sends it to rest_of_orf and then returns the string
            startIndex = (cCount+1)*3
            intA =  dna[startIndex-3:len(dna)]
            #print intA
            ORFint = rest_of_ORF(intA)
            ORF.append(ORFint)
            cCount =  cCount+ len(ORFint)/3  ##moves the index to after the end of the reading frame
        cCount = cCount+1
    return ORF        
     
def find_all_ORFs_oneframe_unit_tests():
    """ Unit tests for the find_all_ORFs_oneframe function """
    out = []
    #input1 = 'ATG,CTA,TGC,CAA,TTT,TAA,TGG,TCC,ATG,GGC,CGG,GCC,TAG,CGG,GTA,GTG,AGA'
    input1 = 'ATGCAATTTTAATGGTCCATGGGCCGGGCCTAGCGGGTAGTGAGA'
    expectedOut = ['ATGCAATTT','ATGGGCCGGGCC']
    out = find_all_ORFs_oneframe(input1)
    print 'input:', input1,', expected output:',expectedOut,', actual output:', out
    
    #input1 = 'GTA,AAA,GGG,ATG,AAA,TTT,TAA,TAT,ATG,CGG,TAG,ATG,TGA'
    input1 = 'GTAAAAGGGATGAAATTTTAATATATGCGGTAGATGTGA'
    expectedOut = ['ATGAAATTT','ATGCGG','ATG']
    out = find_all_ORFs_oneframe(input1)
    print 'input:', input1,', expected output:',expectedOut,', actual output:', out

def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
     #makes three strings that are in the three reading frames
    A = dna
    B = dna[1:len(dna)]
    C = dna[2:len(dna)]
    
    AL = find_all_ORFs_oneframe(A)
    BL = find_all_ORFs_oneframe(B)
    CL = find_all_ORFs_oneframe(C)
    
    return AL+BL+CL

def find_all_ORFs_unit_tests():
    """ Unit tests for the find_all_ORFs function """
        
    #input1 = 'GAA,TGA,GCC,CTA,ATG,GTA,TAG,TAT,GGA,ATA,ACG,TGA,AGA,TGA,ACC,ATT,AAG'
    input1 = 'GAATGAGCCCTAATGGTATAGTATGGAATAACGTGAAGATGAACCATTAAG'
    expectedOut = ['ATGGTA','ATGGAA','AGCCCTAATGGTATAGTATGGAATAACGTGAAGATGAACCAT']
    out = find_all_ORFs(input1)
    print 'input:', input1,', expected output:',expectedOut,', actual output:', out
    
    
def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    #print dna
    L1 = find_all_ORFs(dna) #find all on normal strand
    dna_comp = get_reverse_complement(dna)      
    #print dna
    #print dna_comp
    #print dna_comp
    L2 = find_all_ORFs(dna_comp) 
    #print L1
    #print L2
    L3 = L1+L2
    return L3
def find_all_ORFs_both_strands_unit_tests():
    """ Unit tests for the find_all_ORFs_both_strands function """

    input1 = 'ATGCGTTAAAATGAAATTTTGACATTAGATGCCCGGGAAATGATACAAACCCATT'
    expectedOut = ['ATGCGT','ATGAAATTT','ATGATACAAACCCGATT','ATGCCCGGGAAA','ATGTCAAAATTTCATTTTAACGCAT','ATGGGTTTGTATCATTTCCCGGGCATC']
    out = find_all_ORFs_both_strands(input1)
    print 'input:', input1,', expected output:',expectedOut,', actual output:', out

def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string"""


    L = find_all_ORFs_both_strands(dna)
    #print L
    if L == []:
        return 0
    longest = max(L,key=len)
    return longest


def longest_ORF_unit_tests():
    """ Unit tests for the longest_ORF function """
    input1 = 'ATGCGTTAAAATGAAATTTTGACATTAGATGCCCGGGAAATGATACAAACCCATT'
    expectedOut = 'ATGGGTTTGTATCATTTCCCGGGCATC'
    out = longest_ORF(input1)
    print 'input:', input1,', expected output:',expectedOut,', actual output:', out

    input1 = 'GAATGAGCCCTAATGGTATAGTATGGAATAACGTGAAGATGAACCATTAAG'
    expectedOut = 'ATGGTTCATCTTCACGTTATTCCATACTATACCATTAGGGCTCATTC'
    out = longest_ORF(input1)
    print 'input:', input1,', expected output:',expectedOut,', actual output:', out
    # YOUR IMPLEMENTATION HERE

def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles df
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    a = []
    for x in range(num_trials):
        shuffle = ''.join(random.sample(dna,len(dna))) #breaks the string up and shuffles it randomly. 
        longestORF = longest_ORF(shuffle) #determines the longest orf in a specific shuffle
        if longestORF:    #longest ORF will return zero if there is no ORF, so this if statement will only run if there is an ORF detected
            longestInt = len(longestORF)      
            a.append(longestInt)  #appends the llength of the longest ORF to the list
        x = x + 1
    #print a
    longest = max(a) #determines the longest of all of the longets orfs 
    return longest
        
        
            
            

    # YOUR IMPLEMENTATION HERE

def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """
    codingAcids = []
    ORFs = find_all_ORFs_both_strands(dna)  #gets all the dna snippets
    for a in range(len(ORFs)):  #makes sure that it is only using dna snippets that are non-random
        aLen = len(ORFs[a])
        if aLen > threshold:
            acidInt = coding_strand_to_AA(ORFs[a]) #converts dna to amino acids and then appends it to the list of acids
            codingAcids.append(acidInt)
    return codingAcids
        
            
if __name__ == '__main__': 
    b = longest_ORF_noncoding(dna,1500)
    

    a = gene_finder(dna,b)
    print a
            
        
