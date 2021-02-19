T = int(input())
for tes in range(T) :
    n = int(input())
    arr = list(input().strip().split())

    status = 0
    flag = True

    for code in arr :
        if code in ["start", "restart"] :
            status = 1
        elif code == "stop" :
            if status == 0 :
                print("404")
                flag = False
                break
            else :
                status = 0
    
    if flag :
        print("200")
