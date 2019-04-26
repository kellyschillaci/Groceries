# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 14:51:26 2019

@author: kdoyl
"""

stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15} 
prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3} 

#a.  Show the expression that gets the value of the stock dictionary at the key ‘orange’. 
print (stock['orange'])

#Show a statement that adds an item to the stock dictionary called ‘cherry’ with some integer value and that adds ‘cherry’ to the prices dictionary with a numeric value.
stock.update({"cherry":15})
prices.update({"cherry":1.25})

#b.  Write the code for a loop that iterates over the stock dictionary and prints each key and value. 
for key in stock:
    print(key, stock[key])
    
#c.  Write the code that will sum the total number in stock of the items in the groceries list. 
groceries = ['apple', 'banana', 'pear'] 
for key in groceries:
    print(key, stock[key])
def compute_stock(groceries):
    total=0
    for item in groceries:
        total += stock[item]
    return total
print(compute_stock(groceries))
#d.  Write the code that can print out the total value in stock of all the items.  
# This program can iterate over the stock dictionary and for each item multiply the number in stock times the price of that item in the prices dictionary.
for key in stock:
    print(key, stock[key] * prices[key])
total=0
for item in prices:
    total += stock[item] * prices[item]
print(total)