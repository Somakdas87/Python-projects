# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 20:53:37 2021

@author: somak
"""

"""
Hackernoon. com
This is a list of functions for datascience interview problems
listed on Hackernoon.com 
"""
import math as mt
import numpy as np

"======================================================================"

def fizzbuzz(n):
    for i in range(n):
        if i % 3 == 0 and not(i % 15 == 0):
            print('fizz')
        elif i % 5 == 0 and not(i % 15 == 0):
            print('buzz')
        elif i % 15 ==0:
            print('fizzbuzz')
        else:
            print(i)

"======================================================================"

"""
Factorial of a number
"""
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
    
"======================================================================="

"""
Calculate mean
"""

def mean_list(lis):
    sum=0
    for i in lis:
        sum+=i
    return sum/len(lis)

"====================================================================="

"Standard deviation"

def std(lis):
    sum_sqr=0
    for i in lis:
        sum_sqr+=(i-mean_list(lis))**2
    return mt.sqrt(sum_sqr/(len(lis)-1))
'====================================================================='

'''
Root mean square error
'''

def rmse(real_list, predict_list):
    rmse=np.subtract(real_list, predict_list)
    rmse=np.sum(np.multiply(rmse,rmse))
    rmse=np.sqrt(rmse/len(real_list))
    return rmse

'======================================================================'

'''
remove duplicates in a list of numbers
'''

def remove_dupli(lis):
    new_lis=[]
    for i in range(len(lis)):
        if not((lis[i] in new_lis)):
            new_lis.append(lis[i])
    return new_lis

'===================================================================='

'''
count frequency
'''

def frequency(lis):
    freq={}
    for i in lis:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return freq
'====================================================================='

'''
palindrome
'''
def palin(string):
    n=len(string)
    for i in range(n):
        if string[i] != string[n-i-1]:
            return 0
    return 1
'====================================================================='
    
'unique ID count'

def id_count(id_lis):
    count=0
    newlis=[]
    for a in id_lis:
        if not(a in newlis):
            count+=1
            newlis.append(a)
    return count, newlis
'====================================================================='  

'top 3 id selection'

def top3id(lis):
    count=0
    newlis=[]
    for a in lis:
        if not(a in newlis) and count<3:
            count+=1
            newlis.append(a)
    return newlis
'====================================================================='  
'''
RLE
run-length encoding
'''

def rle(string):
    j=None
    count=0
    lis=[]
    for i in range(len(string)):
        if string[i] == j:
            count+=1
            j=string[i]
        else:
            if j!=None:
                lis.append('('+j+','+str(count)+')')
            j=string[i]
            count=1            
    if j!=None:
        lis.append('('+j+','+str(count)+')')
    return lis
'====================================================================='

'''
JACCARD
Calculates the jaccard similarities between two sets,
given by:    
                    |A intersection B|
    jaccard(A,B)= -----------------------
                       |A union B|

'''
def jaccard(lis1,lis2):
    n=[]
    u=[]
    for i in lis1:
        if (i in lis2) and (not i in n):
            n.append(i)
        if not(i in u):
            u.append(i)
    for i in lis2:
        if not(i in u):
            u.append(i)
    print('intersection: ', n)
    print('union: ',u)
    return len(n)/len(u)
    
'====================================================================='

'''
Two sum:
     Given an array and a number N, 
     return True if there are numbers A, B in the array 
     such that A + B = N. 
     Otherwise, return False.
'''

def two_sum(arr, n):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            print(arr[i]+arr[j])
            if arr[i]+arr[j]==n:
                return True
    return False
'====================================================================='

'''
Fibonacci sequence
returns the n-th term of the Fibonacci sequence
'''
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
'===================================================================='
'''
Most frequent outcome:
    We have two dice of different sizes (D1 and D2). 
    We roll them and sum their face values. 
    What are the most probable outcomes?
'''
def freq(d1,d2):
    lis={}
    for i in range(1,d1+1):
        for j in range(1,d2+1):
            if str(i+j) in lis:
                lis[str(i+j)]+=1
            else:
                lis[str(i+j)]=1
    return lis

def most_freq(d1,d2):
    lis=[]
    maxcount=0
    dic=freq(d1,d2)
    for i in dic:
        if dic[i]>maxcount:
            maxcount=dic[i]
    for i in dic:
        if dic[i]==maxcount:
            lis.append(int(i))
    return lis

'==================================================================='

'Reversal of a linked list'
class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None
        
class LinkedList:
    
    def __init__(self):
        self.headval=None
    
    def listprint(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval
    
    def stackInsert(self,data):
        newnode=Node(data)
        newnode.nextval=self.headval
        self.headval=newnode
    
    def queueInsert(self,data):
        if self.headval==None:
            self.stackInsert(data)
        else:
            currentNode=self.headval
            while currentNode.nextval is not None:
                currentNode=currentNode.nextval                
            currentNode.nextval=Node(data)
        
def CreateLinkedList():
    lnklis=LinkedList()
    return lnklis

def ReverseLinkedList(lnklis):
    currentval=lnklis.headval
    newlist=LinkedList()    
    while currentval is not None:
        newnode=Node(currentval.dataval)
        newnode.nextval=newlist.headval
        newlist.headval=newnode
        currentval=currentval.nextval
    return newlist        
           
'=================================================================='
'flipping a Binary Tree' 

class treeNode:
    'tree node'
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.leftval=None
        self.rightval=None

    def printTree(self):
        if self.leftval is not None:
            self.leftval.printTree()
        print(self.dataval)
        if self.rightval is not None:
            self.rightval.printTree()           
        
    def insertTree(self,data):
        if self.dataval is not None:
            if data<self.dataval:
                if self.leftval is not None:
                    self.leftval.insertTree(data)
                else:
                    self.leftval=treeNode(data)
            elif data>=self.dataval:
                if self.rightval is not None:
                    self.rightval.insertTree(data)
                else:
                    self.rightval=treeNode(data)
        else:
            self.dataval=data
            

def flipTree(root):
    'fliping a binary tree'
    if root is None:
        return root
    if root.leftval is None and root.rightval is None:
        return root
    
    flippedTree=treeNode()
    flippedTree.dataval=root.dataval
    flippedTree.leftval=flipTree(root.rightval)
    flippedTree.rightval=flipTree(root.leftval)
    
    return flippedTree

    
def printBranches(root):
    'Output the tree in branch format'
    
'=================================================================='
'Sorting Algorithms'

def linearSort(a):
    n=len(a)
    for i in range(n-2):
        for j in range(i+1,n-1):
            if a[i]>a[j]:
                temp=a[i]
                a[i]=a[j]
                a[j]=temp
    return a

def insertionSort(a):
    n=len(a)    
    for i in range(1,n-1):
        key=a[i]
        j=i-1
        while j>=0 and a[j]>key:
            a[j+1]=a[j]
            j=j-1        
        a[j+1]=key
    return a


'''
Merge Sort:
Input two arrays of numbers and output a new array that is 
the sorted union of the two arrays
'''
def mergeSort(a,b):
    newArray=[]  
    na=len(a)
    nb=len(b)
    i=0
    j=0
    while i<na and j<nb:
        if a[i]<b[j]:
            newArray+=[a[i]]
            i+=1
        else:
            newArray+=[b[j]]
            j+=1
    if i==na:
        newArray+=b[j:]
    if j==nb:
        newArray+=a[i:]
    return newArray
    
'=================================================================='
'Search algorithms'

def binarySearch(arr,num):
    if len(arr)==0:
        return -1
    i=int(len(arr)/2)
    if num==arr[i]:
        return 1
    elif num<arr[i]:
        return binarySearch(arr[:i],num)
    else:
        return binarySearch(arr[i+1:],num)
    
'==================================================================='
'''
Set theoretic manupulation of arrays
'''

'De-duplication of elements in a sorted array'

def deduplicate(array):
    newArray=[]
    for i in array:
        if not(i in newArray):
            newArray+=[i]
    return newArray
          
'Intersection of two arrays'
def intersection(a,b):
    newArray=[]
    for i in a:
        if i in b:
            newArray+=[i]
    return newArray

'Union of two arrays'
def union(a,b):
    newArray=a
    for i in b:
        if not(i in a):
            newArray+=[i]
    return newArray

'====================================================================='

'Implementing addition algorithm with two arrays'

def addition(a,b):
    'a and b are two arrays'
    i=len(a)
    j=len(b)
    newArray=[]
    carry=0
    while i>0 and j>0:
        sum=a[i-1]+b[j-1]+carry
        carry=int(sum/10)
        sum=sum%10
        i-=1
        j-=1
        newArray=[sum]+newArray
    if i>0:
        while i>0:
            sum=a[i-1]+carry
            carry=int(sum/10)
            sum=sum%10
            i-=1            
            newArray=[sum]+newArray
    if j>0:
        while j>0:
            sum=b[j-1]+carry
            carry=int(sum/10)
            sum=sum%10
            j-=1
            newArray=[sum]+newArray
    if carry>0:
        newArray=[carry]+newArray
    return newArray
        
'====================================================================='
