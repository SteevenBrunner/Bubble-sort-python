#!/usr/bin/python

###################################################
# Bubble sort algorithm implementation in Python3 #
###################################################

import random
from time import time

max_range = 10001
unsorted_list = random.sample(range(1, max_range), max_range - 1)


def bubble_sort(input_list):
    is_sorted = False
    while is_sorted is False:
        is_sorted = True
        for i in range(len(input_list) - 1):
            if input_list[i] > input_list[i + 1]:
                input_list[i], input_list[i + 1] = input_list[i + 1], input_list[i]
                is_sorted = False
    return input_list


# copy by value
unsorted_list_cpy = unsorted_list[:]

start = time()
bubble_sort(unsorted_list_cpy)
print("bubble sort algorithm ends in " + str(time() - start) + " seconds to sort a list of " + str(max_range - 1)
      + " items.")

unsorted_list_cpy = unsorted_list[:]

start = time()
unsorted_list_cpy.sort()
print("system python sort() Timsort algorithm ends in " + str(time() - start) + " seconds to sort a list of "
      + str(max_range - 1) + " items.")
