#!/usr/bin/env python3
# my_list = [1,2,3,4,5,6]
# str_list = ["one", "Two","Three"]
def return_evens(num_list):
    # even = (n%2 == 0) == True
    return([n for n in num_list if (n % 2 == 0) == True])
    # return([n for n in num_list if n == even])

    pass


def make_exclamation(sentence_list):
    return([f"{n}!" for n in sentence_list])
    pass

# print(return_evens(my_list))
# print(make_exclamation(str_list))