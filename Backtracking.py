def subsets(nums):
    subsets = []
    cur_set = []
    def backtrack(set, start):
        subsets.append(cur_set[:]) #Note when appending lists to lists, make sure to pass in
        for i in range(start, len(nums)):
            cur_set.append(nums[i])
            backtrack(cur_set, i + 1)
            cur_set.pop()
        # if i == len(nums):
        #     subsets.append(cur_set[:])
        #     return
        # else:
        #     new = nums[i]
        #     cur_set.append(new)
        #     backtrack(cur_set, i + 1)
        #     cur_set.pop()
        #     backtrack(cur_set, i + 1)
    backtrack(cur_set, 0)
    return subsets

print(subsets([1,2,3]))

def subsets_two(nums):
    subsets = []
    cur_set = []
    unique = {}
    nums.sort()
    def backtrack(set, start):
        subsets.append(cur_set[:])  # Note when appending lists to lists, make sure to pass in
        for i in range(start, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            cur_set.append(nums[i])
            backtrack(cur_set, i + 1)
            cur_set.pop()
    backtrack(cur_set, 0)
    return subsets

print(subsets_two([1,2,2]))