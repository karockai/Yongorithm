# include <stdio.h>
# include <stdbool.h>

void quickSort(int arr[], int start, int end)
{
    if (start >= end) return;
    int mid = (arr[start] + arr[end]) / 2;
    int pivotVal = arr[mid];
    int leftPtr = start;
    int rightPtr = end;
    int tmp;

    while (leftPtr < rightPtr)
    {
        while (arr[leftPtr] < pivotVal)
        {
            leftPtr++;
        }

        while (arr[rightPtr] > pivotVal)
        {
            rightPtr--;
        }

        if (leftPtr < rightPtr && arr[leftPtr] > arr[rightPtr])
        {
            tmp = arr[leftPtr];
            arr[leftPtr] = arr[rightPtr];
            arr[rightPtr] = arr[leftPtr];
        }
    }

    quickSort(arr, start, mid-1);
    quickSort(arr, mid+1, end);
}