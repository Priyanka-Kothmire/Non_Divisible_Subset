# Algorithm 
 


1.subset whose each pair sum is not divisible by K 

2.Return maximum size of subset with no pair sum divisible by K

3.Initialize an array freq of size K with 0. It will store frequency of all the modulus values as we take modulus of all array elements with K. The size of 'freq' array is 'K' as the possible modulus values when an element is divided by 'K' lie between '0' and 'K-1' (both inclusive)
freq[] = {0, 0, ..., 0} (size K)


4.sum of array elements

5.now let us consider the subset [1,7,2,4]
the possible pairs in this subset are 1+7, 1+2 ,1+4 ,7+2 ,7+4 , 2+4

6.all of these pairs are indivisble by 3, hence this is an acceptable subset.

7.In this, the pair 1 + 2 is divisible by 3. the pair 7 + 2 is divisible by 3 and 2+4 is also divisible by 3.

8.hence this subset is not acceptable,
it is observed that [1, 7, 4] will not ever sum to a multiple of k = 3.

9.And finally the length is the 3.
