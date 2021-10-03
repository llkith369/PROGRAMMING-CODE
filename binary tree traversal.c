#include<stdio.h>
#include<stdlib.h>

struct node {
    int data;
    struct node*left;
    struct node*right;
};

struct node * create_node(int data)
{
    struct node * n =  (struct node * )malloc(sizeof(struct node));
    n->data = data;
    n->left = NULL;
    n->right = NULL;

}

void preorder_node(struct node *ptr)
{
    if (ptr != NULL) {
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

int main()
{
    struct node *p  = create_node(1);
    struct node *p1 = create_node(2);
    struct node *p2 = create_node(3);

    p->left = p1;
    p->right = p2;

    preorder_node(p);
    postorder_node(p);
    inorder(p);

    return 0;


    
}
