def distinct_window(txt: str, target: int) -> int: 
    chains_num = 0
    count = 0
    car_list = []
    isCounting = False
    if target > len(txt):
        return 0 
    i = 0
    while i < len(txt):
        j = 0
        if(i+target <= len(txt)):
            while j < target:
                if  txt[i + j] in car_list: 
                    j = target
                    car_list = []
                    count = 0
                    i += 1
                elif not (txt[i+j] in list):
                    count+=1
                    car_list.append(txt[i+j])
                    j +=1
                    if count == target: 
                        chains_num += 1
                        car_list = []
                        count = 0
                        j = target
                        i += 1
        else: 
            i = len(txt)
    return chains_num



txt = 'Aa'
target = 2

print(distinct_window(txt, target))