#!/usr/bin/env python3

def return_evens(num_list):
    return_evens = [i for i in num_list if i % 2 == 0]
    return return_evens

def make_exclamation(sentence_list):
    make_exclamation = [string + "!" for string in sentence_list]
    return make_exclamation