def last_position(nums: list[int], target: int) -> list : 
    positions = []
    last_number = None
    first_position = 0
    last_position = -1
    if len(nums) < 1: 
        return [-1, -1]
    count = 0
    for i in range(0 , len(nums)):
        if last_number == None: 
            last_number = nums[i]
            first_position = i
        if count < target and last_number != nums[i]: 
            first_position = i
            last_position = -1
            count = 1
            last_number = nums[i]
        elif nums[i] == last_number : 
            count+=1
            if count >= target: 
                last_position = i 
                positions = [first_position, last_position]
    if last_position != -1 and count >= target:
        return positions
    else:
        return [-1, -1]
    
    



nums = []


print(last_position(nums, 3))