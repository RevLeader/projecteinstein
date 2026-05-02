# items = list(range(1, 10))

# mid = len(items)/2
# print(round(mid))

# def binary_search():
#     start = 0
#     end = 0
# for i in a:
#     for j in a[i:len(a) - 1]:
#         print(a[i], a[j])

target = 9
nums = [2,9,11,15,7,16]

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            
print(two_sum(nums, target))