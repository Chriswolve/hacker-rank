'''
Problem Statement: Item Counting in a String with Special Constraints

    Description:
    You are given a string 's' containing two types of characters:
    - '*': Represents an item
    - '|': Represents a separator/divider

    The goal is to count the number of items between given start and end indices.

    Specific Constraints:
    1. You need to count items only within sections bounded by '|' characters.
    2. Items outside of '|' sections are not counted.
    3. For each query (defined by startIndices and endIndices):
       - Find the number of items between the first '|' after the start index
         and the last '|' before the end index.

    Parameters:
    - s (str): Input string containing '*' (items) and '|' (separators)
    - startIndices (list): List of start indices for queries
    - endIndices (list): List of corresponding end indices for queries

    Returns:
    - list: Number of items in each specified range

    Example:
    Input: 
    s = "**|**||*|**|"
    startIndices = [1, 1, 3]
    endIndices = [5, 6, 12]
    
    Expected Output:
    [2, 1, 5]

    Explanation:
    - First query (1-5): 2 items between first and last '|'
    - Second query (1-6): 1 item between first and last '|'
    - Third query (3-12): 5 items between first and last '|'
'''

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'numberOfItems' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY startIndices
#  3. INTEGER_ARRAY endIndices
#


def numberOfItems(s, startIndices, endIndices):
    results = [0] * len(startIndices)
    max_len = len(s)
    items = [0] * max_len
    spaces = [(0,0)] * max_len
    # enders = [0] * max_len

    acum = 0
    counter = 0
    pipes = 0
    for i in range(0, max_len):
        if s[i] == '*':
            counter += 1
        elif s[i] == '|':
            # acumulator
            pipes += 1
            if pipes > 1:
                acum += counter

            max_counter = counter
            for index in range(counter+1):
                c = i - counter
                if index < max_counter:
                    spaces[c] = (counter, index + 1)
                else:
                    spaces[c] = (counter, 0)
                counter -= 1

            counter = 0

        items[i] = acum
    
    
    
    '''
    **|**||*|**|
    [0, 0, 0, 0, 0, 2, 2, 2, 3, 3, 3, 5]
    [2, 1, 0, 2, 1, 0, 0, 1, 0, 2, 1, 0]
    [1, 2, 0, 1, 2, 0, 0, 1, 0, 1, 2, 0]
    **|**||*|**|
    [2, 1, 0, 2, 1, 0, 0, 1, 0, 2, 1, 0]
    [1, 2, 0, 1, 2, 0, 0, 1, 0, 1, 2, 0]
    l 2, 0
     11, 2
    5
    [5]
    [5]
    '''

    for i in range(0, len(startIndices)):

        start = startIndices[i]-1
        end = endIndices[i]

        left = spaces[start][0]
        right = spaces[end-1][1]

        result = items[end - 1 - right ] - items[start +left]
        print(result)
        results[i] = result if result > 0 else 0
    # **|*|***|**
    print(results)
    return results


if __name__ == '__main__':

    s = input()

    startIndices_count = int(input().strip())

    startIndices = []

    for _ in range(startIndices_count):
        startIndices_item = int(input().strip())
        startIndices.append(startIndices_item)

    endIndices_count = int(input().strip())

    endIndices = []

    for _ in range(endIndices_count):
        endIndices_item = int(input().strip())
        endIndices.append(endIndices_item)

    result = numberOfItems(s, startIndices, endIndices)

    print(result)
