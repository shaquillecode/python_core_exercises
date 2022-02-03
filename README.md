1.This is a git repo called 'python_core' 
2.Added the following solutions below to the repo
3.Included 'tests' directory for unit testing

Exercise 1
Count all letters, digits, and special symbols from a given string

input: str1 = "P@#yn26at^&i5ve"

output: Total counts of Chars = 8, Digits = 3 , and Symbols = 4 

Exercise 2
Given two strings str1 and str2 and below operations that can performed on str1.

Find minimum number of edits (operations) required to convert ‘str1’ into ‘str2’.

Operations:

1.Insert
2.Remove
3.Replace

Input:   str1 = "geek", str2 = "gesek"
Output:  1
We can convert str1 into str2 by inserting a 's'.

Input:   str1 = "cat", str2 = "cut"
Output:  1
We can convert str1 into str2 by replacing 'a' with 'u'.

Input:   str1 = "sunday", str2 = "saturday"
Output:  3
Last three and first characters are same.  We basically
need to convert "un" to "atur".  This can be done using
below three operations. 
Replace 'n' with 'r', insert t, insert a