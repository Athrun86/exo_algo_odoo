

def move_zero(nums : list[int]):
    if(len(nums) < 1):
        return nums
    last_placed = 0
    for i in range (0, len(nums)):
        if nums[i] == 0:
            place_zero = False
            for j in range(i, len(nums)):
                if(place_zero == False): 
                    if(nums[j] != 0): 
                        place_zero= True
                        nums[i] = nums[j]
                        nums[j] = 0
    return nums
            






nums_1 = []


print(move_zero(nums_1))
