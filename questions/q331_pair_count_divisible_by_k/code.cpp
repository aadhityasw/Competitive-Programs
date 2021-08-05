#include <bits/stdc++.h>
using namespace std;




class Solution
{
    public:
    int countKdivPairs(int arr[], int n, int K)
    {
        int freq[K] = {0};
        
        for(int i = 0; i < n; i++)
        {
            freq[arr[i] % K]++;
        }
        
        int sum = (freq[0] * (freq[0] - 1)) / 2;
        
        for(int i = 1; i <= K/2 and i != (K - i); i++)
        {
            sum += freq[i] * freq[K - i];
        }
        
        if(K % 2 == 0)
        {
            sum += (freq[K / 2] * (freq[K / 2] - 1)) / 2;
        }
        
        return sum;
    }
};


int main()
{
	int t;
	cin >> t;
	while (t--)
	{
		int n;
		cin >> n;

		int a[n];
		for (int i = 0; i < n; i++)
			cin >> a[i];

		int k;
		cin >> k;

        Solution ob;
		cout << ob. countKdivPairs(a, n , k) << "\n";
	}

	return 0;
}
