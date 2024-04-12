#Max Circular Subarray Sum
def circularSubarraySum(arr,n):
    ##Your code here
    def kadane(arr):
        max_sum = float('-inf')
        current_sum = 0
        for num in arr:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum
    
    max_subarray_sum = kadane(arr)
    
    # If there's only one element in the array, return that element as the maximum circular subarray sum
    if n == 1:
        return arr[0]
    
    # Check if all elements in the array are negative
    all_negative = all(num < 0 for num in arr)
    if all_negative:
        return max(arr)
    
    # Calculate the total sum of the array
    total_sum = sum(arr)
    
    # Calculate the minimum subarray sum (by changing the sign of each element and applying Kadane's algorithm)
    min_subarray_sum = kadane([-x for x in arr])
    
    # Calculate the circular subarray sum
    circular_subarray_sum = total_sum + min_subarray_sum
    
    # Return the maximum of maximum subarray sum and circular subarray sum
    return max(max_subarray_sum, circular_subarray_sum)

