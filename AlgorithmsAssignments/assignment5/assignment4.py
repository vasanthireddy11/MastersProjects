import math
import numpy as np
import sys
import collections
import bisect
import os
#from bitarray import bitarray


filename = sys.argv[-1]
outputfilepath = os.path.dirname(filename);
data  = ""
with open(filename) as fp:
	data = fp.read()
    #data = fp.read().replace('\n', '')

def sortSecond(val): 
    return val[1]

def frequency (str) :
    hashmap = {}
    for ch in str :
        hashmap[ch] = hashmap.get(ch,0) + 1
    return hashmap

allCharsFrequencyHashmap = frequency(data)


od = []
od = [(k,v) for k,v in allCharsFrequencyHashmap.items()]


minhashmap = {}
minfreqchars = '';
minfreq = 0

od_backup = od.copy();



#add this to minhash frequency
#loopover all minhash elements and add 0  to them 
#then add new element to minhash and assign '1' to that

#od_backup.pop(0)

while len(od_backup)>1:
	index_to_insert  = 0;
	#different way to find 1st min and 2nd min in od_backup
	min1 = min(od_backup, key=lambda x: x[1])
	min1_index = od_backup.index(min1)
	od_backup.pop(od_backup.index(min1))
	#print(od_backup)
	
	min2 = min(od_backup, key=lambda x: x[1])
	min2_index = od_backup.index(min2)
	od_backup.pop(od_backup.index(min2))
	if(min1_index > min2_index):
		index_to_insert = min1_index
		for elem in min1[0]:
			if elem in minhashmap.keys(): 
				minhashmap[elem] +='1' 
			else:  
				minhashmap[elem] ='1'
		minfreqchars = min1[0]
		
		for elem in min2[0]:
			if elem in minhashmap.keys(): 
				minhashmap[elem] +='0' 
			else:  
				minhashmap[elem] ='0'
		minfreqchars += min2[0]
	else:
		index_to_insert = min2_index
		for elem in min1[0]:
			if elem in minhashmap.keys(): 
				minhashmap[elem] +='0' 
			else:  
				minhashmap[elem] ='0'
		minfreqchars = min1[0]
		
		for elem in min2[0]:
			if elem in minhashmap.keys(): 
				minhashmap[elem] +='1' 
			else:  
				minhashmap[elem] ='1'
		minfreqchars += min2[0]
	
	#print('min1[0]');
	#print(min1[0]);
	
	#minhashmap[od_backup[0][0]] = '1';
	minfreq = min1[1] + min2[1]
	
	#print(minfreq)
	#od_backup.pop(0)
	#od_backup.pop(0)
	od_backup.insert(index_to_insert, (minfreqchars, minfreq))	
	#sort again with new frequency or new tree.
	#But we are sorting list not the hashmap
	#####od_backup.sort(key = sortSecond)  
	#print("after sort                     ")
	#print(od_backup) 
	
	#prepare to strt the next loop
	#minhashmap[od_backup[0][0]] = '';
	
	minfreqchars =''
	minfreq= 0;
print("")
print("Final mapped bits resulted from huffman implementation for all unique characters from the input text:")
print("")
print(minhashmap)
print(" ")





global finalBitsEncodedForm
finalBitsEncodedForm = ''
for ch in data :
    finalBitsEncodedForm += minhashmap[ch]

#print("encoded")
#print(finalBitsEncodedForm)

#WRITE COMPRESSED BITS TO AN OUTPUT FILE 
f = open( outputfilepath + '\output.txt', 'w' )
f.write(finalBitsEncodedForm)
f.close()

print("Length of compressed bits  = " , len(finalBitsEncodedForm))


		



#---------------------------------Below code is for decoding the text -------------------------------------------
#----------------------------------------------------------------------------------------------------------------

#longestBits = 0;
#for key in minhashmap: 
#	if(longestBits < len(minhashmap[key])):
#		longestBits = len(minhashmap[key]);
##print(longestBits)

##reverse hashmap
#minhashmapreverse = {}
#for key in minhashmap: 
#	minhashmapreverse[minhashmap[key]] = key;
#
#print(minhashmapreverse)
#global finaltext
#finaltext = ''
#def huffmanDecode (dictionary, bits, text):
#	
#	print(bits)
#	print(bits)
#	if bits[0:4] in dictionary.keys(): 
#		text += dictionary[bits[0:4]]
#		bits = bits[4:len(bits)]
#	elif bits[0:3] in dictionary.keys(): 
#		
#		text += dictionary[bits[0:3]]
#		print(text)
#		#print(minhashmapreverse[finalBitsEncodedForm[0:3]])
#		bits = bits[3:len(bits)]
#		print(bits)
#	elif bits[0:2] in dictionary.keys(): 
#		text += dictionary[bits[0:2]]
#		bits = bits[2:len(bits)]
#	
#	finalBitsEncodedForm = bits;
#	finaltext = text;
#	
#
#huffmanDecode(minhashmapreverse, finalBitsEncodedForm, finaltext)
#
#huffmanDecode(minhashmapreverse, finalBitsEncodedForm, finaltext)
#
#
##while len(finalBitsEncodedForm) > 1:
##	huffmanDecode(minhashmap, finalBitsEncodedForm, finaltext)
#	#print(finaltext)
#
##print(finaltext)









