# -*- coding: utf-8 -*-
"""TA 10 - itertools.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mFSrjPBur6u2mF7FtmuFZ_oYMKAzd3N2
"""

import itertools

"""## 1. ```itertools.chain(*iterables)```


* Combines multiple iterators into a single iterator by chaining them together.
* Useful for iterating over elements from multiple sequences as if they were a single sequence.





"""

data1 = [1, 2, 3]
data2 = [4, 5, 6]
combined_iter = itertools.chain(data1, data2)

for item in combined_iter:
    print(item)


# Output: 1, 2, 3, 4, 5, 6

"""## 2. ```itertools.cycle(iterable)```


* Creates an infinite iterator that cycles through elements of the input iterable.
* Useful for creating a loop that repeats infinitely over a sequence of elements.



"""

count = 0
for item in itertools.cycle(['a', 'b', 'c']):
    print(item)
    count += 1
    if count >= 6:
        break


# Output: a, b, c, a, b, c

"""## 3. ```itertools.permutations(iterable, r=None)```


* Generates all permutations of the elements in the input iterable.
* Optional argument ```r``` specifies the length of permutations, defaulting to the length of the input iterable.


"""

perms = itertools.permutations('abc', 2)
for perm in perms:
    print(perm)


# Output: ('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')

"""## 4. ```itertools.combinations(iterable, r)```

* Generates all combinations of the elements in the input iterable of length ```r```.


"""

combs = itertools.combinations('abcd', 2)
for comb in combs:
    print(comb)


# Output: ('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd'), ('c', 'd')
