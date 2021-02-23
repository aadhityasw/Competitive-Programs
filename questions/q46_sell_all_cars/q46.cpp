// Codechef  :  CARSELL

// Did not pass

#include<iostream>
using namespace std;

int main()
{
    long long test_cases, tes, n, i, j, k, p, sum, num;
    cin >> test_cases;
    long long *arr;
    for(tes=0;tes<test_cases;tes++)
    {
        cin>>n;
        arr = new long long[n];
        for(i=0;i<n;i++)
        {
            cin>>p;
            if(i==0)
            {
                arr[i] = p;
            }
            else if(p >= arr[i-1])
            {
                arr[i] = p;
            }
            else
            {
                for(j=0;j<i;j++)
                {
                    if(arr[j] > p)
                    {
                        for(k=j;k<i;k++)
                        {
                            arr[k+1] = arr[k];
                        }
                        arr[j] = p;
                    }
                }
            }
        }
        sum = 0;
        p = 0;
        for(i=0;i<n;i++)
        {
            if(arr[i] >= (n-i-1))
            {
                num = arr[i] - (n-i-1);
                sum = (sum+num%1000000007)%1000000007;
            }
            cout<<sum<<" ";
        }
        cout<<sum<<endl;
    }
}