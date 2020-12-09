def maxSubArraySum(a,size):
    summ = a[0]
    max_sum = summ
    for num in range(1, size) :
        summ = max(a[num], summ+a[num])
        max_sum = max(max_sum, summ)
    return max_sum


# At any point we have two options, either to start measuring the sum from the current number or to continue measuring the sum from before.
# We also keep track of the maximum sum which might occur anywhere in the middle of the series.
