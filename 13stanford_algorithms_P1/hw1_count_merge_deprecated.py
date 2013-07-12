#!/usr/bin/env python
'readTextFlie.py --create text file'
import os
import time
#get filename
fname = ('IntegerArray2.txt')
global level
global source
level=0

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
source = [1,2,3,4,5,6,7,8,9,10]
A, B = split_list(source)
pr_list(source,"source1")
cp_list(A,source,len(source)//2)
pr_list(source,"source2")
"""



#this recursive will split array
def recursive_split_array(source_list):
	global level
	#time.sleep(1)
	print ("DEBUG: len(source_list)=", len(source_list))
	print ("DEBUG: level=", level)
	
	half = len(source_list)//2
	if (half >=2):
		level=level+1;
		recursive_split_array(source_list[:half])
		recursive_split_array(source_list[half:])
	else:
		#print("DEBUG level=", ++level)
		level=level-1;
		return;

#this recursive only split index
def recursive_split_index(start_index, length):
	global level
	global source
	level=level+1;
	#time.sleep(1)
	
	half = length//2
	if (length >2):
		###split and recursion
		#print ("DEBUG: branch len(source_list)=", length)
		#print ("DEBUG: branch level=", level)
		recursive_split_index(start_index, half)
		recursive_split_index(start_index+half, length-half)
		###finish sort child, do merge parent here
		
		pr_list(source, "source");
		print("DEBUG: start_index=", start_index);
		print("DEBUG: length=", length);
		source_to_split=source[start_index:start_index+length]
		pr_list(source_to_split, "source_to_split");
		A,B=split_list(source_to_split)
		pr_list(A, "A");
		pr_list(B, "B");
		i=0
		j=0
		C=[];
		for k in range(0, length):
			print("DEBUG: k=", k);
			print("DEBUG:   j=", j);
			print("DEBUG:   i=", i);
			if (i==len(A)):
				cc=B[j]
				C.append(B[j])
				j=j+1
			elif (j==len(B)):
				C.append(A[i])
				i+=1
			elif (A[i]<B[j]):
				#C[k]=A[i]
				C.append(A[i])
				i+=1;
			else:
				#C[k]=B[j]
				C.append(B[j])
				j+=1;
				
		cp_list(C,source, start_index)
		pr_list(C, "C");
		pr_list(source, "source");
		
	else:
		###can not split any more, do some sort logic here
		print ("DEBUG: leaf len(source_list)=", length)
		print ("DEBUG: leaf level=", level)
		if (length ==2 and source[start_index]>source[start_index+1]):
			tmp=source[start_index]
			source[start_index]=source[start_index+1]
			source[start_index+1]=tmp
		#for x in (start_index, start_index+half):
			#if (a[x])
			#print("DEBUG a[",x,"]=",a[x])
		
	level=level-1;


ls = os.linesep

#'try:
fobj = open(fname, 'r')
#'except IOError:
#'    print "open file error:\n"
#'else:
source=[]
for eachline in fobj:
	#print (eachline)
	source.append(int(eachline));
fobj.close()
print ("DEBUG: len(source)=", len(source))
print ("DEBUG:  source[0]=", source[0])
print ("DEBUG:  type(source[0])=", type(source[0]))
A, B = split_list(source)
print ("DEBUG: len(B)=", len(B))

#recursive_split_array(a[0:16])
#trim source limit for easy debug
#limit=6
#source=source[0:limit]
pr_list(source, "source_before");
recursive_split_index(0, len(source))
pr_list(source, "source_after");



