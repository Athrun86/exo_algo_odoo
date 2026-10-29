def position_insertion(nums : list, target : int) -> int:
    target_found = False
    closest_number = 0 
    closest_index = 0
    if target <= nums[0]: 
        return 0
    for i  in range(0, len(nums)):
        if nums[i] == target : 
            return i
        if  i+1 < len(nums): 
            if nums[i] <= target <= nums[i+1]: 
                closest_index = i
        elif i == len(nums)-1: 
            if nums[i] < target: 
                closest_index = i
                return  closest_index 
    return closest_index


def test_position_insertion():
    # Target déjà présente dans la liste
    assert position_insertion([1, 3, 5, 6], 5) == 2
    assert position_insertion([1, 3, 5, 6], 1) == 0
    assert position_insertion([1, 3, 5, 6], 6) == 3

    # Target absente : insertion au milieu
    assert position_insertion([1, 3, 5, 6], 2) == 0
    assert position_insertion([1, 3, 5, 6], 4) == 1

    # Target absente : insertion au début
    assert position_insertion([1, 3, 5, 6], 0) == 0

    # Target absente : insertion à la fin
    assert position_insertion([1, 3, 5, 6], 7) == 4

    # Listes plus courtes
    assert position_insertion([], 5) == 0
    assert position_insertion([1], 0) == 0
    assert position_insertion([1], 2) == 1

    # Valeurs négatives
    assert position_insertion([-5, -1, 0, 3], -3) == 1
    assert position_insertion([-5, -1, 0, 3], -10) == 0
    assert position_insertion([-5, -1, 0, 3], 10) == 4

    print("Tous les tests sont passés.")


test_position_insertion()