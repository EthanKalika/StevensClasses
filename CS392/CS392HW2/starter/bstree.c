/*******************************************************************************
 * Name        : bstree.c
 * Author      : Ethan Kalika
 * Pledge      : I pledge my honor that I have abided by the Stevens Honor System
 ******************************************************************************/
#include "bstree.h"

// This is a helper function, it checks if a node is a leaf
int isLeaf(node_t* currNode)
{
    if (currNode -> left == NULL && currNode -> right == NULL)
    {
        return 1;
    }
    return 0;
}

// This is a helper function, it helps add non-root nodes into the tree
void* appendNode(void* dataAddress, size_t numBytes, node_t* ourNode, int (*cmp)(void*,void*))
{
    if (ourNode == NULL)
    {
        struct node* newRootNode = (struct node*)malloc(sizeof(struct node));
        newRootNode -> left = NULL;
        newRootNode -> right = NULL;
        newRootNode -> data = malloc(numBytes);
        unsigned char* src = (unsigned char*) dataAddress;
        for (size_t i = 0; i < numBytes; i++)
        {
            ((unsigned char*)(newRootNode -> data))[i] = src[i];
        }
        ourNode = newRootNode;
    }
    else if (isLeaf(ourNode))
    {
        struct node* newRootNode = (struct node*)malloc(sizeof(struct node));
        newRootNode -> left = NULL;
        newRootNode -> right = NULL;
        newRootNode -> data = malloc(numBytes);
        unsigned char* src = (unsigned char*) dataAddress;
        for (size_t i = 0; i < numBytes; i++)
        {
            ((unsigned char*)(newRootNode -> data))[i] = src[i];
        }
        if(cmp(ourNode -> data, dataAddress) == -1 || cmp(ourNode -> data, dataAddress) == 0)
        {
            ourNode -> right = newRootNode;
        }
        else
        {
            ourNode -> left = newRootNode;
        }
    }
    else
    {
        if(cmp(ourNode -> data, dataAddress) == -1 || cmp(ourNode -> data, dataAddress) == 0)
        {
            ourNode -> right = appendNode(dataAddress, numBytes, ourNode -> right, cmp);
        }
        else
        {
            ourNode -> left = appendNode(dataAddress, numBytes, ourNode -> left, cmp);
        }
    }
    return ourNode;
}

void add_node(void* dataAddress, size_t numBytes, tree_t* ourTree, int (*cmp)(void*,void*))
{
    if (ourTree -> root == NULL)
    {
        struct node* newRootNode = (struct node*)malloc(sizeof(struct node));
        newRootNode -> left = NULL;
        newRootNode -> right = NULL;
        newRootNode -> data = malloc(numBytes);
        unsigned char* src = (unsigned char*) dataAddress;
        for (size_t i = 0; i < numBytes; i++)
        {
            ((unsigned char*)(newRootNode -> data))[i] = src[i];
        }
        ourTree -> root = newRootNode;
    }
    else
    {
        if(cmp(ourTree -> root -> data, dataAddress) == -1 || cmp(ourTree -> root -> data, dataAddress) == 0)
        {
            ourTree -> root -> right = appendNode(dataAddress, numBytes, ourTree -> root -> right, cmp);
        }
        else
        {
            ourTree -> root -> left = appendNode(dataAddress, numBytes, ourTree -> root -> left, cmp);
        }
    }
}

void print_tree(node_t* currNode, void (*print)(void*))
{
    if (!(currNode == NULL))
    {
        if (!((currNode -> left) == NULL))
        {
            print_tree(currNode -> left, print);
        }
        print(currNode -> data);
        if (!((currNode -> right) == NULL))
        {
            print_tree(currNode -> right, print);
        }
    }
}

// Helper function that assists in deleting interior nodes
void destroyNode(node_t* currNode)
{
    if (currNode != NULL)
    {
        if ((currNode -> right) != NULL)
        {
            destroyNode(currNode -> right);
        }
        if ((currNode -> left) != NULL)
        {
            destroyNode(currNode -> left);
        }
        free(currNode -> data);
        currNode -> data = NULL;
        free(currNode);
        currNode = NULL;
    }
}

void destroy(tree_t* ourTree)
{
    if (ourTree != NULL)
    {
        if ((ourTree -> root) != NULL)
        {
            if ((ourTree -> root -> right) != NULL)
            {
                destroyNode(ourTree -> root -> right);
            }
            if ((ourTree -> root -> left) != NULL)
            {
                destroyNode(ourTree -> root -> left);
            }
            free(ourTree -> root -> data);
            ourTree -> root -> data = NULL;
            free(ourTree -> root);
            ourTree -> root = NULL;
        }
    }
}