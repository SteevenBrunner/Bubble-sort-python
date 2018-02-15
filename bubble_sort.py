#!/usr/bin/python

###################################################
# Bubble sort algorithm implementation in Python3 #
###################################################

import random

max_range = 10000
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


# To test the algorithm
print(bubble_sort(unsorted_list))
