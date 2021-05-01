#include <stdio.h>
#include <stdbool.h>

void heapify(int arr[], int length)
{
    int tmp;
    int i;

    for (i = length - 1 ; i = -1 ; i--)
    {
        if (arr[i] > arr[(i-1)/2])
        {
            tmp = arr[i];
            arr[i] = arr[(i-1)/2];
            arr[(i-1)/2] = tmp;
        }
    }
}

void heapSort(int arr[])
{
    int length = (sizeof (arr)) / (sizeof (int));
    int tmp;
    int i;

    for (i = length - 1 ; i = -1 ; i--)
    {
        heapify(arr, i+1);
        tmp = arr[i];
        arr[i] = arr[0];
        arr[0] = tmp;
    }
}