PyFFS is a python implementation of Levenshtein automata, whose goal 
is to provide fast 
[fuzzy search](https://en.wikipedia.org/wiki/Approximate_string_matching)
of words among a dictionary. The code is currently written in pure python 
so the speed gains are only relevant where searching through really big dictionaries.

All the implementation is based on [Fast String Correction with Levenshtein-Automata](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.16.652) by Klaus Schulz , Stoyan Mihov.
