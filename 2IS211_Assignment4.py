#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 4 Assignment 2 of 2 Sort Algorithm Comparison"""
import time
import random

def insertion_sort(a_list):
    """
    Args:
        start (float) : Time of start.
        end (float) : Time of end.
        current_value : Index of list.
        position (int) : Position of index.

    Returns:
        a_list (list) : Sorted List.
        end-start (float) : Time of process.

    Examples:
        >>> insertion_sort([5,4,2,8,7,6,5,1,0,10])
            ([4, 5, 2, 8, 7, 6, 5, 1, 0, 10], 5.0067901611328125e-06)
    """
    start = time.time()
    for index in range(1, len(a_list)):

        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
            a_list[position] = current_value
        end = time.time()
        return a_list, end-start


def shell_sort(a_list):
    """
    Args:
        start (float) : Time of start.
        end (float) : Time of end.
        sublist_count : Count of middle of list.

    Returns:
        a_list (list): List of number sorted.
        end-start (float): Time of process.

    Examples:
        >>> shell_sort([5,3,6,2,7,8,3,10])
            ([2, 3, 3, 5, 6, 7, 8, 10], 1.9073486328125e-05)
    """
    start = time.time()
    sublist_count = len(a_list) // 2

    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        sublist_count = sublist_count // 2
    end = time.time()
    return a_list, end-start


def gap_insertion_sort(a_list, start, gap):
    """
    Args:
        a_list (list): List of numbers to sort.
        start (int): Index of start.
        gap (int): Index of the gap.

    Returns:
        None

    Examples:
        >>>
    """
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
        a_list[position] = current_value


def python_sort(a_list):
    """
    Args:
        start (float) : Time of start.
        end (float) : Time of end.
        a_list (list) : Sorted list.
    Returns:
        a_list (list) : Sorted list.
        end-start : Time process result
    Examples:
        >>> python_sort([3,2,1])
            ([1, 2, 3, 6, 8], 3.0994415283203125e-06)
        >>>
    """
    start = time.time()
    a_list.sort()
    end = time.time()
    return a_list, end-start

def random_gen(value):
    """
    Args:
        random_list (list) : List of random ints based on values.

    Returns:
        random_list (list) : Creates list of random values fast.

    Examples:
        >>> random_gen(15)
            [5,6,7,3,8,14,3,9,0,6,0,7,11,10,13]
    """
    random_list = random.sample(range(0, value), value)
    return random_list


def main():
    """
    Args:
        test (dict) : Test keys and values.
        random_list (list) : Generated  random lists
        inter_count (int) : Interger of indexed count.
        ouput (dict): Results output

    Returns:
        None

    Examples:
        >>> main()
        >>> List of 500 length the test timed:
            Insertion Sort took  0.0000036 seconds to run on average
            Shell Sort took  0.0010329 seconds to run on average
            Python Sort took  0.0000104 seconds to run on average


            List of 10000 length the test timed:
            Insertion Sort took  0.0000631 seconds to run on average
            Shell Sort took  0.0282072 seconds to run on average
            Python Sort took  0.0001782 seconds to run on average


            List of 1000 length the test timed:
            Insertion Sort took  0.0000056 seconds to run on average
            Shell Sort took  0.0020569 seconds to run on average
            Python Sort took  0.0000179 seconds to run on average
        >>>
    """
    tests = {'test1': 500,
             'test2': 1000,
             'test3': 10000}
    for test in tests.values():
        random_list = random_gen(test)
        iter_count = 100
        output = {'insert':0,
                  'shell':0,
                  'pyth':0}
        while iter_count > 0:
            output['insert'] += insertion_sort(random_list)[1]
            output['shell'] += shell_sort(random_list)[1]
            output['pyth'] += python_sort(random_list)[1]
            iter_count -= 1

        print "List of %s length the test timed:" % test
        print "Insertion Sort took %10.7f seconds to run on average" % \
              (float(output['insert'] / 100))
        print "Shell Sort took %10.7f seconds to run on average" % \
              (float(output['shell'] / 100))
        print "Python Sort took %10.7f seconds to run on average" % \
              (float(output['pyth'] / 100))
        print '\n'

if __name__ == '__main__':
    main()
