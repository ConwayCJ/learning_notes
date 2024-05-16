test_case = [7,2134,564,12,7,87,1,45,578,45,12,34]

def median(nums):
    if len(nums) <= 0:
        return None
        
    sorted_nums = sorted(nums)

    if len(sorted_nums) % 2 == 1:
        mid = len(sorted_nums) // 2
        return sorted_nums[mid]
    else:
        mid_low = len(sorted_nums) // 2
        mid_high = (len(sorted_nums) // 2) + 1

        return (sorted_nums[mid_low] + sorted_nums[mid_high]) / 2 - 1

print(median(test_case))