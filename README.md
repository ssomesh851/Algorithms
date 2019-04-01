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
