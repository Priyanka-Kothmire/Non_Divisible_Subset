def nonDivisibleSubset(A):
    freq = [0 for i in range(K)]
    n=len(A)
    # Compute sum of array elements
    sum = 0
    for i in range(n):
        rem = A[i] % K
        sum += freq[(K - rem) % K]
        freq[rem] += 1
    print( sum )
K=3
nonDivisibleSubset([1, 7, 2, 4])
