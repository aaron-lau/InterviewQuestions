# Arrays Coding questions

In this directory you will find a file with an answer pertaining to a certain question. These questions are array manipulation question and the problems are explained below. The runtime and space complexity expected to be satisfactory but not guaranteed to be optimal. They are not given and are left to the reader to determine. 


An "Array Integer" is an integer represented by an array, where each digit of the integer is an element in the array. 
For example, the value 123 (one hundred twenty three) would be stored as follows, note the least significant digit is in the zero-th position.

arrayInt[0] = 3;

arrayInt[1] = 2;

arrayInt[2] = 1;

## incrementNumberArray.py

Implement a method that, given an "ArrayInteger", increments the value by one.

Ex. Given the inputs 123, the result would be

arrayInt[0] = 4;

arrayInt[1] = 2;

arrayInt[2] = 1;

## sumNumberArrays.py

Implement a method that, given an "ArrayInteger", adds another "ArrayInteger".

Ex. Given the inputs 123 and 456, the result would be

arrayInt[0] = 9;

arrayInt[1] = 7;

arrayInt[2] = 5;

## multiplyNumberArrays.py

Implement a method that, given an "ArrayInteger", multiplies another "ArrayInteger". 

Ex. Given the inputs 123 and 3, the result would be:

arrayInt[0] = 9;

arrayInt[1] = 6;

arrayInt[2] = 3;

---

Restrictions:

CAN NOT CONVERT AN ARRAY INTO A NUMBER AND THEN BACK INTO AN ARRAY. 

THERE MAY BE NO VALUE STORED IN ANY ARRAY GREATER THAN NINE (9).

## findSmallestIntegerNotInArray

Given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

Ex. Given A = [1, 3, 6, 4, 1, 2], the result would 5.

Ex. Given A = [1, 2, 3], the result would 4.

Ex. Given A = [−1, −3], the result would 1.

---

Restrictions:

N is an integer within the range [1..100,000];

Each element of array A is an integer within the range [−1,000,000..1,000,000].
