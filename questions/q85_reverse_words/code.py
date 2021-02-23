def reverseWords(S):
    # code here
    s = S.split('.')
    s = s[::-1]
    return '.'.join(s)



if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        print(reverseWords(s))
