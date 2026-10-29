def longest_substring(txt: str) -> int:
    if len(txt) == 1 : 
        return 1
    longest_chain = 0
    chain = set()
    count = 0
    for i in range(0, len(txt)):
        for j in range (i, len(txt)): 
            if txt[j] in chain: 
                chain.clear()
                if count > longest_chain:
                    longest_chain = count
                count = 0
                break
            else: 
                count+= 1
                chain.add(txt[j])
    return longest_chain

        

    return longest_chain
                
def test_longest_substring():
    # Cas classiques
    assert longest_substring("abcabcbb") == 3   # "abc"
    assert longest_substring("bbbbb") == 1      # "b"
    assert longest_substring("pwwkew") == 3     # "wke" ou "kew"

    # Cas limite : chaîne vide
    assert longest_substring("") == 0

    # Cas supplémentaires utiles
    assert longest_substring("a") == 1
    assert longest_substring("au") == 2
    assert longest_substring("dvdf") == 3       # "vdf"
    assert longest_substring("abba") == 2       # "ab" ou "ba"
    assert longest_substring("tmmzuxt") == 5    # "mzuxt"
    assert longest_substring("abcdef") == 6
    assert longest_substring("aaaaaa") == 1

    print("Tous les tests sont passés.")


test_longest_substring()