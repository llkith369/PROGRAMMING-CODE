#include<stdio.h>

int check(int * arr,int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("%d ",arr[i]);
    }
    printf("\n");
    
}

void bubble(int * arr,int n)

{
    int temp;
    for (int i = 0; i < n - 1; i++)
    {
        for ( int j = 0; j < n - 1 - i; j++)
        {
            if (arr[i]>arr[i+1])
            {
                temp = arr[i];
                arr[i] = arr[i+1];
                arr[i+1] = temp;
            }
            
        }
        
    }
    
}

int main ()
{
    int arr[] = {1,5,2,3,4,8,6,7};
    int n = 8;
    check(arr,n);
    bubble(arr,n);
    check(arr,n);
    return 0;
}


