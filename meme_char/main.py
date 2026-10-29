def even_char(a: str, b: str) -> bool:
    equivalent = True
    if(len(a) != len(b)): 
        return False
    comparison = {}
    for i in range(0, len(a)): 
        if comparison.get(a[i]) != None:
            if b[i] == comparison.get(a[i]): 
                equivalent = True
            else: return  False
        else:
            for keys, values in comparison.items():
                if values == b[i] and a[i] != keys: 
                    return False
            comparison[a[i]] = b[i] 
    return equivalent





a = "foo"
b = "bar"

print(even_char(a, b))