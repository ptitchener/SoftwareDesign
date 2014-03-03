# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 18:36:25 2014

@author: paul
"""
import pickle
from pattern.web import *
from urllib import urlopen
import collections
#import numpy

#import matplotlib as mpl

def import_books():
    """ Imports books from project gutenberg using the patter command. This function is run once and then the books are saved to the same folder as the python script"""
    
    oliver_twist_full_text = URL('http://www.gutenberg.org/ebooks/730.txt.utf-8').download()
    hard_times = URL('http://www.gutenberg.org/files/786/786-0.txt').download()
    our_mutual_friend = URL('http://www.gutenberg.org/cache/epub/883/pg883.txt').download()
    paperwick_papers = URL('http://www.gutenberg.org/cache/epub/580/pg580.txt').download()
    a = open('hard_times.txt','w')
    a.write(hard_times)
    a.close()
    b = open('oliver_twist.txt','w')
    b.write(oliver_twist_full_text)
    b.close()
    c = open('our_mutual_friend.txt','w')
    c.write(our_mutual_friend)
    c.close()
    d = open('paperwick_papers.txt','w')
    d.write(paperwick_papers)
    d.close()
    #Note: After demonstrating functionality, we downloaded books directly from project gutenberg beucase it was simpler and quicker.    
def read_book(book):
    """ Opens a book and reads it as a string. Book must be in the form name.txt"""
    a = open(book,'r')
    returns = a.read()
    a.close()
    return returns

def strip_extra(book):
    """Removes the additional text that project gutenberg adds to a book"""
    a = read_book(book)
    #Because project gutenberg ends and finishes a book with many different strings, several posibilities are attempted.
    try:
        end = a.index('End of the Project Gutenberg')
    except ValueError:
        try:
            end = a.index('*** END OF')
        except ValueError:
            end = a.index('***END OF')
    
    ind1 = a.index('***')
    start= a.index('***',ind1)
    return a[start:end] 
        
def delete_extra(book):
    """ Srips additional UTF-8 formating from the downloaded book and returns it as a list of words"""
    b = strip_extra(book)
    b.lower
    a = b.split()
    i = 0
    for i in range(len(a)):
        if '\xe2\x80\x94' in a[i]:
            a[i] = a[i].translate(None,'\xe2\x80\x94')
        elif '\xe2\x80\x99' in a[i]:
            a[i] = a[i].translate(None,'\xe2\x80\x99')
        elif '\xe2\x80\x98' in a[i]:
            a[i] = a[i].translate(None,'\xe2\x80\x98')
        elif '.' in a[i]:
            a[i] = a[i].translate(None,'.')
        elif '\xef\xbb\xbf' in a[i]:
            a[i] = a[i].translate(None,'\xef\xbb\xbf')
    return a
            

def makesdic(book):
    """
    Take a list of strings. Figure out how many times a specific word occurs. 
    And then make that into a dictionary.
    """
    
    #text = "hello there hi there"
    text= delete_extra(book)
    #text = ''.join(str(e) for e in text_list)
    dic = dict()
    dic = {'_all_':0}
    dic_100 = {}
    return collections.Counter(text)


def word_freq(book):
    """ Changes the word count into a frequency count. Input is a dicionary of word counts. Output is a dictionary of word frequencies"""
    count = makesdic(book)
    a = sum(count.values())
    for w in count:
        count[w] = float(count[w])/(a)
    return count
    
    
def compare(book1,book2):
    """ Compares two books based on word frequency and returns the cosine similarity between them. The input is the name of two  books (in the format name.txt). The output is the cosine similarity between them"""
    freq1 = word_freq(book1)
    freq2 = word_freq(book2)
    
    c = dict(freq1.items() + freq2.items()) #findinf the words that appear in both books 
    all_words = map(list,zip(c)) ##mapping the dictionary to a list

    freq1_list = freq1.values() ## getting the frquencies of those lists, to find magnitudes later
    freq2_list = freq2.values()

    flattened = recursive_flatten(all_words) ##map returns a nested list, so this flattens the nested list
    L1 = []
    L2 = []
    for w in flattened: ## This loop determines the frequencies of the words in both books. If a word is not in a book, a frequency of zero is appended
        L1.append(freq1.get(w, 0))
        L2.append(freq2.get(w, 0))
        
    mag1 = magnitude(freq1_list)
    mag2 = magnitude(freq2_list)
    dot = dotprod(L1,L2)
    
    similarity = dot/(mag1*mag2) #finds cosine similarity
    return similarity
    
    
    
    
    
    
def magnitude(L):
    """ Returns the magnitude of a list"""
    if type(L) != list:
        raise Exception("L must be a list")
    a = 0
    
    for w in L:
        a = a + w**2
    return a**.5

def dotprod(L1,L2):
    """Returns the dot product of two lists that are the same length"""
    if len(L1) != len(L2):
        raise Exception('Lenghts of vectors must be equal')
    i = 0
    a = 0
    for i in range(len(L1)):
        a = a + L1[i]*L2[i]
    return a
                 
        
        

def recursive_flatten(L):
    """Flattens a nested list"""
    L1 = []
    for i in range(len(L)):
        if type(L[i])==list:
            L1  = L1 + (recursive_flatten(L[i]))
        else:
           L1.append(L[i])
    return L1
  



def compare_all():
    """Compares 6 different books downloaded from project gutenberg and creates an array with the similarity values"""
    l1 = ['Plato.txt','Dar_voy.txt','PP_Aust.txt','hard_times.txt','Grimm.txt','oliver_twist.txt']
    output1 = []
    compare_once = {}
    for w in l1:
        l_int = []
        for x in l1:
            if w ==x: ## if the two books are the same, similarity is assumed to be perfect
                compare_int =1.0

            else:
                try:
                    compare_int = compare_once[x,w] ## if the two books have already been compared, that value is returned
                except:
                    compare(w,x) ##finding the similarity
                    compare_int = compare(w,x)
                    compare_once[w,x] = compare_int ##adding it to the intermediate list

            l_int.append(compare_int)  #filling in the array of similarities
            print compare_int
            

        output1.append(l_int)
    return output1


if __name__ == '__main__':
    print compare_all()
 