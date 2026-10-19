
# set.intersection() method

Look up documentation on the 'intersection()' method
- How is the method described?  
Iterable = object that can provide its elements one at a time, allowing you to loop over it; common examples include lists, tuples, strings, dictionaries, and sets
- What are the inputs?
Takes a set and 0 or more iterable arguments
- What is the output?
It returns a new set of elements common to them; with no arguments,returning a shallow copy of the original set
- Think about the description of the data and also the type

Write a small program to test the method
int_set = setA.intersection( setB )
 a = {"hello", "hi", "goodbye"}
 type(a)
 b = {"goodbye", "so long", "adieu"}
 c = a.intersection(b)
 type(c)