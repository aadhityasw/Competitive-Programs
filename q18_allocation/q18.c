// Allocation

//Google Kickstart 2020

#include<stdio.h>

int main()
{
    int testcases, tes, n, i, num, ele, totcost, c;
    long ava;
    scanf("%d", &testcases);
    for(tes=1;tes<=testcases;tes++)
    {
        scanf("%d %ld", &n, &ava);
        int arr[10000];
        ele = 0;
        totcost = 0;
        c = 0;
        for(i=0;i<n;i++)
        {
            scanf("%d", &num);
            if(ele>0 && num > arr[ele-1] && ava >= (totcost + num))
            {
                totcost += num;
                arr[ele] = num;
                ele++;
            }
            else if(ele>0 && num > arr[ele-1] && ava < (totcost + num))
            {

            }
            else if(ele>0 && num < arr[ele-1] && ava < (totcost + num))
            {
                totcost -= arr[ele-1];
                int k= ele-1;
                while(num > arr[k])
                {
                    arr[k+1] = arr[k];
                }
                arr[k] = num;
                arr[ele] = 0;
                totcost += num;
            }
            else if(ele>0 && num < arr[ele-1] && ava >= (totcost + num))
            {
                int k= ele-1;
                while(num > arr[k])
                {
                    arr[k+1] = arr[k];
                }
                arr[k] = num;
                ele ++;
                totcost += num;
            }
            else if(ele == 0 && ava >= (totcost + num))
            {
                totcost += num;
                arr[ele] = num;
                ele++;
            }
            else
            {
                
            }
        }
        printf("Case #%d: %d\n", tes, ele);
    }
}