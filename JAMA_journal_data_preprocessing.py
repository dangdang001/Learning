# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 15:56:17 2018

@author: dyin

Preprocessing the txt file, transpose the list information into new columns

"""
import os
import pandas as pd

os.chdir("//med-cloud01/osa$/Cores/Biostatistics/Donglei/20180118-journal data/data/from PI/")

filenames = ['NEJM 1.1.02-12.31.06.txt', 'NEJM 1.1.07-12.31.11.txt', 'NEJM 1.1.12-12.31.15.txt','NEJM 1.1.16-12.31.17.txt']
with open('combined.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)


with open("combined.txt") as f:
    data0 = f.read().splitlines()

data0 = list(filter(None, data0)) 

data1 = pd.Series(data0)
data1.head(10)

data2 = data1.str.split(' ', 1)


for item in data2:
    if "-" in item[0]:
        item[0]=item[0].translate(None, '-').strip()
    item[1]=item[1].lstrip()
    if item[1][0]=="-":   
        item[1]=item[1][1:]
        
last_name=data2[0][0]
for item in data2:
    if item[0]=="":
        item[0]=last_name
    last_name=item[0]

        
current_ID=data2[0][1]
all_ID=list()
all_var=list()
all_content=list()
for item in data2:
    if 'PMID' in item[0]:
        current_ID=item[1]
    all_ID.append(current_ID)
    all_var.append(item[0])
    all_content.append(item[1])


#create new df 
df=pd.DataFrame(columns=['newpmid','var','content'])
df['newpmid']=all_ID
df['var']=all_var
df['content']=all_content
df=df[df['var']!='PMID']

df=df.sort_values(by=['newpmid', 'var'], ascending=[True, True])

df['order']=df.groupby(['newpmid','var']).cumcount()

df['newvar']=df['var'].str.strip()+df['order'].map(str).str.strip()


print df['newvar'].unique()

test_result=df.pivot(index='newpmid', columns='newvar', values='content')

test_result.to_csv("//med-cloud01/osa$/Cores/Biostatistics/Donglei/20180118-journal data/data/from PI/test.csv", sep=',')
        


