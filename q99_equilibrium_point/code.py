def equilibriumPoint(A, N):
    front = 0
    f_sum = 0
    rear = N-1
    r_sum = 0
    
    while True :
        if rear == front :
            if f_sum == r_sum :
                return front+1
            else :
                return -1
        if f_sum < r_sum :
            f_sum += A[front]
            front += 1
        else :
            r_sum += A[rear]
            rear -= 1




import math


def main():

    T = int(input())

    while(T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]

        print(equilibriumPoint(A, N))

        T -= 1


if __name__ == "__main__":
    main()
