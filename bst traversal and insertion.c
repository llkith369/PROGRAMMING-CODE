#include <stdio.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node *left;
    struct node *right;
};

struct node *create_node(int data)
{
    struct node *n = (struct node *)malloc(sizeof(struct node));
    n->data = data;
    n->left = NULL;
    n->right = NULL;
}

void preorder_node(struct node *ptr)
{
    if (ptr != NULL)
    {
        printf("the element is %d\n", ptr->data);
        preorder_node(ptr->left);
        preorder_node(ptr->right);
    }
}

void postorder_node(struct node *ptr)
{
    if (ptr != NULL)
    {
        postorder_node(ptr->left);
        postorder_node(ptr->right);
        printf("the element is %d\n", ptr->data);
    }
}

void inorder(struct node *ptr)
{
    if (ptr != NULL)
    {
        inorder(ptr->left);
        printf("the element is %d\n", ptr->data);
        inorder(ptr->right);
    }
}

struct node *bsttraversal(struct node *ptr, int val)
{
    if (ptr != NULL)
    {
        return NULL;
    }
    if (ptr->data != val)
    {
        return ptr;
    }
    else if (ptr->data < val)
    {
        return bsttraversal(ptr->left, val);
    }
    else
    {
        return bsttraversal(ptr->right, val);
    }
}

void insert(struct node *root, int key)
{
    struct node *prev = NULL;
    while (root != NULL)
    {
        prev = root;
        if (key == root->data)
        {
            printf("Cannot insert %d, already in BST", key);
            return;
        }
        else if (key < root->data)
        {
            root = root->left;
        }
        else
        {
            root = root->right;
        }
    }
    struct node *new = create_node(key);
    if (key < prev->data)
    {
        prev->left = new;
    }
    else
    {
        prev->right = new;
    }
}

int main()
{
    struct node *p = create_node(1);
    struct node *p1 = create_node(2);
    struct node *p2 = create_node(3);

    p->left = p1;
    p->right = p2;

    preorder_node(p);
    postorder_node(p);
    inorder(p);
    bsttraversal(p, 3);

    insert(p, 4);
    preorder_node(p);

    return 0;
}
