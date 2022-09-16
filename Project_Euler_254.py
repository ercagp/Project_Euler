"""
Created on Thu Sep 15 20:49:19 2022
Project Euler problem #254 

@author: ercagpince

"""
import math
import numpy as np  
import time 

  
def f(x):
    all_n = [int(i) for i in str(x)]
    sum_f = sum([math.factorial(j) for j in all_n])
    return sum_f

def sf(x):
    all_n = [int(i) for i in str(x)] 
    sum_sf = sum(all_n)
    return sum_sf
    


m = int(input())
n = np.zeros(m,int)
f_vals = np.zeros(m,int)
s_vals = np.zeros(m,int)
g_index = np.zeros(m,int)
g_vals = np.zeros(m,int)

for i in range(m):
    n[i] = i+1
    f_vals[i] = f(i+1)
    s_vals[i] = sf(f(i+1))

#Define a unique g_vals to avoid greedy selection, 
g_vals = np.array([],int)
g_index = np.array([],int)
    
t_0 =  time.perf_counter()
## Find the sf(n) & g(i) iteratively 
for j in range(m): 
    
    #find n values corresponding to this subset 
    n_sub = n[s_vals == j+1]
    #n_min is the first element 
    if n_sub.size == 0:
        continue
    else:
        n_min = n_sub[0]
    
    g_index = np.append(g_index,s_vals[n == n_min])
    g_vals = np.append(g_vals,n_min)
    
t_f =  time.perf_counter()    


   
sg = np.zeros(g_vals.size,int)
Check = np.arange(1,g_index.size)
#Calculate sum of sg
for k in range(g_vals.size):
    sg[k] = sf(g_vals[k])
    #Check if g_index is a complete set
    if np.array_equal(Check[0:k+1], g_index[0:k+1]):
       sum_sg = sum(sg[0:k+1])
       print('Sum_sg = ', sum_sg)
       print('g_index = ', g_index[k]) 
    
