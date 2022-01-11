#!/usr/bin/env python
# coding: utf-8
## write a formula which returns "Palindrome" or "Not Palindrome" for a given word in (palindrome.xslx)

Solution : 

1. Clean the Given word or Data Using Trim Function.

2. Remove Space between the Word Using the Substitute function

= Substitute(A2, " " ,"")

3. Remove any spaces, commas, exclamation marks & other punctuation symbols.

4. We Wrap this in a lovely SumProduct Formula so that we can check for Palindromeness for  given word.

=IF(SUMPRODUCT(( MID(B2,ROW(OFFSET($A$1,,,LEN(B2))),1) = MID(B2,LEN(B2)-ROW(OFFSET($A$1,,,LEN(B2)))+1,1)) + 0 ) = LEN(B2), "It’s a Palindrome", "It’s not a Palindrome")
# ![Screenshot%20%2817%29.png](attachment:Screenshot%20%2817%29.png)

# In[ ]:




