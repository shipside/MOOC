#!/usr/bin/env python
'readTextFlie.py --create text file'
import os
import time
#get filename
fname = ('IntegerArray.txt')
global LEVEL
global SOURCE
global INVERT
LEVEL=0
INVERT=0

def split_list(list):
    half = len(list)//2
    return list[:half], list[half:]
	
def cp_list(from_list, to_list, start_index):
	for x in range(0, len(from_list)):
		to_list[start_index+x]=from_list[x]
		
def pr_list(list,name):
	print("DEBUG list name=",name)
	for x in range(0, len(list)):
		print("DEBUG: ",name,"[",x,"]=",list[x])

"""
#test list func
SOURCE = [1,2,3,4,5,6,7,8,9,10]
A, B = split_list(SOURCE)
pr_list(SOURCE,"source1")
cp_list(A,SOURCE,len(SOURCE)//2)
pr_list(SOURCE,"source2")
"""


def mergeSort(A,B):
	global INVERT
	i=0
	j=0
	C=[];
	for k in range(0, len(A)+len(B)):
		#print("DEBUG: k=", k);
		#print("DEBUG:   j=", j);
		#print("DEBUG:   i=", i);
		if (i==len(A)):
			C.append(B[j])
			j=j+1
		elif (j==len(B)):
			C.append(A[i])
			#INVERT+=len(B)
			i+=1
		elif (A[i]<B[j]):
			# C[k]=A[i]
			C.append(A[i])
			i+=1;
		else:
			# C[k]=B[j]
			C.append(B[j])
			INVERT+=len(A)-i
			j+=1;
	return C

#this recursive will split array
def recursive_split_array(source_list):
	global LEVEL
	global INVERT
	LEVEL=LEVEL+1;
	#time.sleep(1)
	#print ("DEBUG: len(source_list)=", len(source_list))
	#print ("DEBUG: LEVEL=", LEVEL)
	
	length=len(source_list)
	half = length//2
	if (length >2):
		A=recursive_split_array(source_list[:half])
		B=recursive_split_array(source_list[half:])
		return mergeSort(A,B)
	else:
		#print("DEBUG LEVEL=", ++LEVEL)
		if (length ==2 and source_list[0]>source_list[1]):
			tmp=source_list[0]
			source_list[0]=source_list[1]
			source_list[1]=tmp
			INVERT+=1
		return source_list;
	LEVEL-=-1;

#this recursive only split index
def recursive_split_index(start_index, length):
	global LEVEL
	global SOURCE
	LEVEL=LEVEL+1;
	#time.sleep(1)
	
	half = length//2
	if (length >2):
		###split and recursion
		#print ("DEBUG: branch len(source_list)=", length)
		#print ("DEBUG: branch LEVEL=", LEVEL)
		recursive_split_index(start_index, half)
		recursive_split_index(start_index+half, length-half)
		###finish sort child, do merge parent here
		
		pr_list(SOURCE, "SOURCE");
		print("DEBUG: start_index=", start_index);
		print("DEBUG: length=", length);
		source_to_split=SOURCE[start_index:start_index+length]
		pr_list(source_to_split, "source_to_split");
		A,B=split_list(source_to_split)
		pr_list(A, "A");
		pr_list(B, "B");
		
		C = mergeSort(A, B)
				
		cp_list(C,SOURCE, start_index)
		pr_list(C, "C");
		pr_list(SOURCE, "SOURCE");
		
	else:
		###can not split any more, do some sort logic here
		print ("DEBUG: leaf len(source_list)=", length)
		print ("DEBUG: leaf LEVEL=", LEVEL)
		if (length ==2 and SOURCE[start_index]>SOURCE[start_index+1]):
			tmp=SOURCE[start_index]
			SOURCE[start_index]=SOURCE[start_index+1]
			SOURCE[start_index+1]=tmp
		#for x in (start_index, start_index+half):
			#if (a[x])
			#print("DEBUG a[",x,"]=",a[x])
		
	LEVEL=LEVEL-1;


ls = os.linesep

#'try:
fobj = open(fname, 'r')
#'except IOError:
#'    print "open file error:\n"
#'else:
SOURCE=[]
for eachline in fobj:
	#print (eachline)
	SOURCE.append(int(eachline));
fobj.close()
print ("DEBUG: fileinfo len(SOURCE)=", len(SOURCE))
print ("DEBUG: fileinfo SOURCE[0]=", SOURCE[0])
print ("DEBUG: fileinfo type(SOURCE[0])=", type(SOURCE[0]))
A, B = split_list(SOURCE)
print ("DEBUG: fileinfo len(B)=", len(B))

#recursive_split_array(a[0:16])
#trim SOURCE limit for easy debug
#limit=6
#SOURCE=SOURCE[0:limit]

#pr_list(SOURCE, "source_before");

#source function 1: user global var sort
#recursive_split_index(0, len(SOURCE))

#source function 2: user retrun var sort
SOURCE=recursive_split_array(SOURCE)

#pr_list(SOURCE, "source_after");
print("INVERT=", INVERT);

#result
#INVERT= 2407905288


