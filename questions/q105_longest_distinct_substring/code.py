def longest_distinct_substring(s) :
    n = len(s)
    window = ""
    distinctCount = 0
    for i in range(n) :
        if len(window) > 0 and s[i] == window[0] :
            window = window[1:] + s[i]
        elif s[i] not in window :
            window += s[i]
        elif len(window) == 0 :
            window += s[i]
        else :
            while window[0] != s[i] :
                window = window[1:]
            window = window[1:]
            window += s[i]
        distinctCount = max(distinctCount, len(window))
            
    return distinctCount


T = int(input())
for tes in range(T) :
    print(longest_distinct_substring(input().strip()))
