def merge_sort(nums):
    if len(nums) < 2:
        return nums
    
    median = len(nums) // 2
    l_half = nums[:median]
    r_half = nums[median:]
    l_sorted = merge_sort(l_half)
    r_sorted = merge_sort(r_half)
    return merge(l_sorted, r_sorted)


def merge(first, second):
    final = []

    i = 0
    j = 0

    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1
    while i < len(first):
        final.append(first[i])
        i += 1
    
    while j < len(second):
        final.append(second[j])
        j += 1
        
    return final
        
