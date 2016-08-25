# permutations

*Problem*

There are a large number of 9 digit integers in the range 123456789 to 987654321 where each digit only appears once.
Your mission should you choose to accept is to identify the 100,000th number in this sequence.
The first number is the easiest to find  - 123456789, the second is 123456798, the third is 123456879 and so on.
No digit may repeat so 122345675 is not a valid number in this sequence.

*Solution Approach*

The number of permutations of p unique digits is p! = (p * (p-1) * ... * 2 * 1).
Therefore, the number of 9 digit numbers starting with a '1' is 8! (as there are 8! permutations of the remaining 8 digits).
This is also true for 9 digit numbers starting with '2'.
This pattern can be continued for 9 digits numbers starting with '12'.
There will be 7! numbers, since there are 7! permutations of the remaining 7 digits.

The solution as implemented here utilises this knowledge of permutations, in order to find any kth number in an ordered sequence of numbers which have 'p' unique digits, where 1 <= k <= p!

This makes finding the kth number O(p), where p is the number of digits.

*Setting Up*

Set up a virtual environment
> virtualenv env
> source env\bin\activate

*Run the Project*

cd to the root of the project and run:
> python run.py

Follow the prompts...

Note this solution works for any number of digits (p) to find any number in the sequence (k).

