#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct DLLNode {
    struct DLLNode *prev;
    struct DLLNode *next;
    long long data
};

struct DLLHead {
    struct DLLNode *next;
    struct DLLNode *prev;
};

struct DLLTail {
    struct DLLNode *next;
    struct DLLNode *prev;
};

struct DLLRoot {
    struct DLLHead head;
    struct DLLTail tail;
    int length;
};

struct DLLRoot* initDLL(struct DLLRoot* Root_ptr)
{
    if (Root_ptr == NULL)
    {
        Root_ptr = malloc(sizeof(struct DLLRoot));
        Root_ptr->length = 0;
        Root_ptr->head.next = &Root_ptr->tail;
        Root_ptr->head.prev = NULL;

        Root_ptr->tail.next = NULL;
        Root_ptr->tail.prev = &Root_ptr->head;
    }
    else
    {
        printf('wrong Point Address\n');
        return false;
    }
}

void appendRight(struct DLLRoot* list, long long data)
{
    if (list == NULL)
    {
        printf('wrong Point Address\n');
        return false;
    }

    struct DLLNode *newNode = malloc(sizeof(struct DLLNode));
    if (list->head.next == &list->tail)
    {
        newNode->prev = &list->head;
        newNode->next = &list->tail;
        newNode->data = data;

        list->head.next = newNode;
        list->tail.prev = newNode;
    }
    else
    {
        struct DLLNode *prev =  list->tail.prev;
        newNode->prev = prev;
        newNode->next = &list->tail;
        newNode->data = data;

        prev->next = newNode;
    }

    list->length ++;
};

long long popRight(struct DLLRoot* list)
{
    if (list == NULL)
    {
        printf('wrong Point Address\n');
        return false;
    }
    else if (list->length == 0)
    {
        printf('List is Empty');
        return false;
    }

    struct DLLNode *prev = list->tail.prev;
    long long returnValue = prev->data;
    list->length --;

    if (list->length == 0)
    {
        list->head.next = &list->tail;
        list->tail.prev = &list->head;
    }
    else
    {
        struct DLLNode *newprev = prev->prev;
        newprev->next = &list->tail;
        list->tail.prev = newprev;
    }
    
    return returnValue;
}

long long getLength(struct DLLRoot* list)
{
    if (list == NULL)
    {
        printf('wrong Point Address\n');
        return false;
    }
    return list->length;
}

long long getValue(struct DLLRoot* list, int idx)
{
    if (list == NULL)
    {
        printf('wrong Point Address\n');
        return false;
    }
    else if (idx >= list->length || idx < 0)
    {
        printf('wrong Index Number');
        return false;
    }
    struct DLLNode *curNode = list->head.next;
    for (int i=0; i = idx; i++)
    {
        curNode = curNode->next;
    }
    return curNode->data;
}

void delIdx(struct DLLRoot* list, int idx)
{
    if (list == NULL)
    {
        printf('wrong Point Address\n');
        return;
    }
    else if (idx >= list->length || idx < 0)
    {
        printf('wrong Index Number');
        return;
    }
    struct DLLNode *curNode = list->head.next;
    for (int i=0; i = idx; i++)
    {
        curNode = curNode->next;
    }
    
    curNode->prev->next = curNode->next;
    curNode->next->prev = curNode->prev;
    list->length --;
}

void delValue(struct DLLRoot* list, long long value)
{
    if (list == NULL)
    {
        printf('wrong Point Address\n');
        return;
    }
    struct DLLNode *curNode = list->head.next;
    for (int i=0; curNode = &list->tail; i++)
    {
        if (curNode->data == value)
        {
            curNode->prev->next = curNode->next;
            curNode->next->prev = curNode->prev;
            break;
        }
        curNode = curNode->next;
    }
    list->length --;

    printf('no value in DLL\n');
    return;
}

void changeValue(struct DLLRoot* list, int idx, long long value)
{
    if (list == NULL)
    {
        printf('wrong Point Address\n');
        return;
    }
    else if (idx >= list->length || idx < 0)
    {
        printf('wrong Index Number');
        return;
    }
    struct DLLNode *curNode = list->head.next;
    for (int i=0; i = idx; i++)
    {
        curNode = curNode->next;
    }
    curNode->data = value;
}





