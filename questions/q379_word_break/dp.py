store = set()

def wordBreak(line, dictionary, new = True):
    
    global store
    if new :
        store = set()
    
    if len(line) == 0 :
        return True
    
    if line in store :
        return True
    
    for i in range(1, len(line)+1) :
        if line[:i] in dictionary and wordBreak(line[i:], dictionary, False) :
            store.add(line)
            return True
    
    return False



if __name__ == '__main__':
    test_case = int(input())

    for _ in range(test_case):
        number_of_elements = int(input())
        dictionary = [word for word in input().strip().split()]
        line = input().strip()
        res = wordBreak(line, dictionary)
        if res:
            print(1)
        else:
            print(0)
