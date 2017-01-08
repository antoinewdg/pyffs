PyFFS is a python implementation of Levenshtein automata, whose goal 
is to provide fast 
[fuzzy search](https://en.wikipedia.org/wiki/Approximate_string_matching)
of words among a dictionary. The code is currently written in pure python 
so the speed gains are only relevant where searching through really big dictionaries.
Tests on PyPy3.3 show promising results.

All the implementation is based on [Fast String Correction with Levenshtein-Automata](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.16.652) by Klaus Schulz , Stoyan Mihov.

This project is a personal project and not meant to be used as a library, but if you could 
be interested by this please let me know.
