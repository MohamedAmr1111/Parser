# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 01:33:21 2022

@author: Mohamed Amr
"""

import re

file =  open("read.py")

operators = {'=' : 'Assignment op' , '+' :'Addition op' , '-':'Subtraction op', '/' : 'Divisor op', '*' : 'Multiplication op,' , '<' : 'grater than op,' , '>' : 'less than op,'}
operators_Key = operators.keys()

data_type ={'int':'Integer' ,'float':'Floating point','char':'Charchter type'}
data_type_key = data_type.keys()

punctuation_symbol = {':':'colon' , ';':'semi colon' , '.':'dot' ,',':'comma' ,'(':'left bracket' ,')':'righ bracket' ,'}':'curlly right bracket' ,'{':'curlly left bracket' }
punctuation_symbol_key = punctuation_symbol.keys()

keyword={'if':'keyword' , 'while' :'keyword' , 'for' :'keyword'}
keyword_key = keyword.keys()

identifier = {'a' : 'id' , 'b':'id' ,'c':'id','d':'id'  ,'i':'id'}
identifier_key = identifier.keys()


dataflag = False
a=file.read()
count=0
program = a.split("\n")

 

for line in program:
    count = count + 1
    print("line#", count, "\n", line)
    
    tokens=line.split(' ')
    print("Tokens are ", tokens)
    print("Line#", count, "properties \n")
    for token in tokens:
        if token in operators_Key:
            print("operator is ", operators[token])
        if token in data_type_key:
            print("datatype is", data_type[token])
        if token in punctuation_symbol_key:
            print ("Punctuation symbol is", punctuation_symbol[token])
        if token in keyword_key:
            print ("keyword  is", keyword[token])
        if token in identifier_key :
            print ("Identifier is", identifier [token])
        if token.isnumeric():
            print ("it is constant" )
        elif token.__contains__("\""):
            print ("it is constant" )
 
            
           
    dataFlag=False 
    print("___________________________")
