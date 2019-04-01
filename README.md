# Algorithms
Binary search
Algorithms:


BINARY SEARCH:
> By using it we can search a particular element out of list, but the list must be sorted.
> First we will specify the lower, upper bound [we take these indexes]
> after these we have to find mid index [mid index = (lower+upper)/2]  ==>integer division so result will be integer
>suppose list is [4,7,8,12,45,99]. And u want to search 45 element. u will get 0+5/2 = 2. here 2th position we have 8 value. but the element
we are searching for 45 so it is not matching.
> now next step would be you have to change your lower or upper bound. so which one to change for these you have to check the value you
are searching for is smaller or bigger then the mid value if the value is smaller then u gotta change upper bound that means we will simply
say the mid value is the new upper bound. 
                     if the value is greater then the mid value then u need to change lower bound, so here old lower bound shift to the mid value.
> so again u need to find mid value and repeat the same.

note :  while we are applying loop we need to remember two things one is the moment we found the desired element.
          and lower bound should not greater then upper bound.
          
          
          
 BUUBLE_SORT:
 
 According to Wikipedia "Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly steps through the list to be sorted, compares each pair of adjacent items and swaps them if they are in the wrong order. The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted. The algorithm, which is a comparison sort, is named for the way smaller elements "bubble" to the top of the list. Although the algorithm is simple, it is too slow and impractical for most problems even when compared to insertion sort. It can be practical if the input is usually in sort order but may occasionally have some out-of-order elements nearly in position."




SELECTION SORT ALGORITHM:
-----------------------------
Selection sort algorithm is a simple algorithm it is a in-place comparision based algorithm. In these algorithm we need to compare and need to place into correct position.

let's a take on example:

list = [5,15,3,12,17,0]
        0  1 2  3  4  5
First step:
Search the list and find out the minimum value.
#here we are sorting the number as per the ascending order

So as in the ascending the smallest number will be placed in the first position. We need to find out the minimum value in the list of the numbers. For it we need to write a program.
By the way we can use min method to find out smallest number.
or else we can take the first value in the list as minimum value. After we can compare with all the other value which are presented in the list. If the value is greater then do nothing since it is ascending order if it is small then change the min value. And then check next value in the same way. if get a value which is less then we will take that as our minimal value and again start comparing with next values whether next value smaller then the minimal value no then we do nothing this process will get continuously loop over. Finally we got the Zero is the smallest number in the list by doing these we have been completed the first step.


Second Step:
We need to place this zero value at the 0th index for this we need to swap value 5 and 0.
then index will be like these 0,15,3,12,17,5. So now remaining unsorted we need to find out the minimum value means here '0' has been sorted and remaining numbers we need to check the minimum value. So again take 15 value as a minimal value compare it with next value 3 here 3 is smaller then 15 so now these 3 will be compared with next values in the list if the value are lesser then same process will be repeated. After searching entire list we got the second least number list that is 3, it is in 2nd index now we need to swap it to the 1st index position. 0 3 15 12 17 5. unsorted list take the first element and compare with all and find out small value and place it in respective index postion.

At the end list 0 3  5 12 15 17


Note: Same process will be repeated when we look for maximum value that is Descending order.
At the end list 17 15 12 5 3 0


Third Step:
Take the sublist(ignore sorted part) and repeat step 1 and 2 until all the element are sorted.


























