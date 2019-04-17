#!/usr/bin/env python
import sys
import random
import pandas as pd
import math
import copy
import numpy as np


file=open("queries.txt")
df=pd.read_csv('bidder_dataset.csv')
queries=file.read().splitlines()

if len(sys.argv) != 2:
    print('usage : adwords.py <algorithm>')
    sys.exit(1)



def greedy(budget,bidder_list,queries):
    revenue=0.0
    for query in queries:
            max_bid=0.0
            max_bidder=0
            for bidder in bidder_list:
                if query in bidder_list[bidder]:  
                    if (bidder_list[bidder][query]==max_bid ):
                    	if(bidder_list[bidder][query]<=budget[bidder] and bidder<max_bidder):
                        	max_bid=bidder_list[bidder][query]
                        	max_bidder=bidder    
                    if (bidder_list[bidder][query]>max_bid) :
                    	if(bidder_list[bidder][query]<=budget[bidder]):
                        	max_bid=bidder_list[bidder][query]
                        	max_bidder=bidder          
                   						

            if max_bid!=0.0: 
                budget[max_bidder]-=max_bid
                revenue+=max_bid
                
            else:
            	continue

               
    return round(revenue,2)



def calc_init_budget(budget):
    xu={}
    for bidder in budget:
        if bidder not in xu:
            xu[bidder]=1-math.e**(-1)
    return xu

def calculate_xu(x):
    return (1-math.e**(x-1))
    

def msvv(budget,bidder_list,queries,xu):

    budget_main=copy.deepcopy(budget)
    revenue=0.0
    for query in queries:
        max_xu=0.0
        max_bidder=0
        for bidder in bidder_list:
            if query in bidder_list[bidder]:  
                if (bidder_list[bidder][query]*xu[bidder]==max_xu):
                	if( bidder_list[bidder][query]<=budget[bidder]):
                		if(bidder<max_bidder):
                			bid=bidder_list[bidder][query]
                			max_xu=bidder_list[bidder][query]*xu[bidder]
                			max_bidder=bidder
                elif (bidder_list[bidder][query]*xu[bidder]>max_xu):
                	if (bidder_list[bidder][query]<=budget[bidder]):
                		bid=bidder_list[bidder][query]
                		max_xu=bidder_list[bidder][query]*xu[bidder]
                		max_bidder=bidder

					
        if max_xu!=0.0: 
            budget[max_bidder]-=bid
            spent_fraction= (budget_main[max_bidder]-budget[max_bidder])
            spent_fraction/=budget_main[max_bidder]
            xu[max_bidder]=calculate_xu(spent_fraction)
            revenue+=bid
            
        else:
        	continue

    return round(revenue,2)


def balance(budget,bidder_list,queries):
    revenue=0.0

    for query in queries:
        max_bidder=0
        maximum_budget=0.0

        for bidder in bidder_list:
            if query in bidder_list[bidder]:  
                if (budget[bidder]==maximum_budget):
                	if(bidder_list[bidder][query]<=budget[bidder] and bidder<max_bidder):
                		max_bidder=bidder                		
                		max_bidder_bid=bidder_list[bidder][query]
                		maximum_budget=budget[bidder]  
 
                elif (budget[bidder]>maximum_budget):
                	if(bidder_list[bidder][query]<=budget[bidder]):
                		max_bidder=bidder                		
                		max_bidder_bid=bidder_list[bidder][query]
                		maximum_budget=budget[bidder]   

        if maximum_budget!=0.0: 
        	budget[max_bidder]-=max_bidder_bid
        	revenue+=max_bidder_bid
        else:
        	continue
    return round(revenue,2)


budget={}
bidder_list={}

for row in df.values:
    if(np.isnan(row[3])!=True):
        if row[0] not in budget:
            budget[row[0]]=row[3]
    if row[0] not in bidder_list:
        bidder_list[row[0]]={row[1]:row[2]}
    if row[0] in bidder_list:
        bidder_list[row[0]][row[1]]=row[2]



revenues=[]
input_method= sys.argv[1]
optimal=sum(budget.values())
for i in range(100):
    budget_main=copy.deepcopy(budget)
    if(input_method=="balance"):
        revenue=balance(budget_main,bidder_list,queries)
    if(input_method=="msvv"):
        xu=calc_init_budget(budget_main)
        revenue=msvv(budget_main,bidder_list,queries,xu)
    if(input_method=="greedy"):
        revenue=greedy(budget_main,bidder_list,queries)


    if(i==0):
        print(revenue)
    revenues.append(revenue)
    random.shuffle(queries)

avg_revenue = sum(revenues)/len(revenues)
Comp_ratio = avg_revenue /optimal
Comp_ratio=round(Comp_ratio,2)
print(Comp_ratio)    
        

