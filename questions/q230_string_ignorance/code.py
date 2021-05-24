T = int(input())

for _ in range(T) :
    s = input().strip()
    n = len(s)
    modified = ""
    
    characters = {}

    for ch in s :
        if ch.lower() in characters :
            characters[ch.lower()] += 1
        else :
            characters[ch.lower()] = 1
        
        if characters[ch.lower()] % 2 != 0 :
            modified += ch

    print(modified)
