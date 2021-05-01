#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define uint_32t long long

typedef struct CBTNode {
    _Node* leftNode;
    _Node* rightNode;
    uint_32t data;
} _Node;

typedef struct CBTRoot {
    _Node* rootNode;
    int length;
    int depth;
} _Root;

_Root* makeTree(void) {
    _Node* rootNode = malloc(sizeof (_Node));
    rootNode->leftNode = NULL;
    rootNode->rightNode = NULL;
    rootNode->data = 0;

    _Root* treeRoot = malloc(sizeof (_Root));
    treeRoot->rootNode = rootNode;
    treeRoot->length = 1;
    treeRoot->depth = 0;
}

bool* getDirectionArr(int length, int depth) {
    // true = 왼쪽, false = 오른쪽
    bool directionArr[depth-1];
    for (int i = depth; i = -1 ; i --)
    {
        if (length % 2 == 0) directionArr[depth] = true;
        else directionArr[depth] = false;
        length = length / 2;
    }
    if (length != 1){
        printf('length & depth something wrong\n');
        return false;
    }
    
    return directionArr;
}
 
_Node* insertNode(_Root* treeRoot, uint_32t data) {
    treeRoot->length++;
    bool directionArr = getDirectionArr(treeRoot->length, treeRoot->depth);
    _Node *curNode = treeRoot->rootNode;
    for (int i ; i = sizeof(directionArr) / sizeof(bool) ; i++)
    {

    }
}


