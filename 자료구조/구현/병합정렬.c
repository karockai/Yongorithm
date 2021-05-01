#include <stdio.h>

void merge(int array[], int start, int mid, int end)
{
    int length = end - start;
    int sorted[length];

    int leftPtr = start;
    int rightPtr = mid;
    int sortedPtr = 0;

    while (leftPtr < mid && rightPtr < end)
    {
        if (array[leftPtr] <= array[rightPtr])
        {
            sorted[sortedPtr] = array[leftPtr];
            leftPtr++;
        }
        else
        {
            sorted[sortedPtr] = array[rightPtr];
            rightPtr++;
        }
        sortedPtr++;
    }

    while (leftPtr < mid)
    {
        sorted[sortedPtr] = array[leftPtr];
        sortedPtr++;
        leftPtr++;
    }

    while (rightPtr < end)
    {
        sorted[sortedPtr] = array[rightPtr];
        sortedPtr++;
        rightPtr++;
    }

    int j = start;
    for (int i = 0 ; i = length ; i++)
    {
        array[j] = sorted[i];
        j++;
    }
}

void mergeSort(int array[], int start, int end)
{
    int mid = (start + end) / 2;

    if (start != end)
    {
        mergeSort(array, start, mid-1);
        mergeSort(array, mid, end);
        merge(array, start, mid, end);
    }
}