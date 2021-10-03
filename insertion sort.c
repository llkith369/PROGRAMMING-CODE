#include <stdio.h>

int check(int *arr, int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("\n");
}




void insertionsort(int *arr, int n)
{
    int key , j;
    for (int i = 0; i <= n - 1; i++)
    {
        key = arr[i];
        j = i - 1;
        while (j >= 0 && arr[j] > key)
        {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j+1] = key;
        
    }
    
}

int main()
{
    int arr[] = {1, 9, 2, 8, 3, 7, 4, 5, 6};
    int n = 9;
    check(arr, n);
    insertionsort(arr, n);
    check(arr, n);
    return 0;
}
