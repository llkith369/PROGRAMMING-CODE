#include<stdio.h>
#include<stdlib.h>


struct node {
    int data;
    struct node *next;
};

int linked(struct node * ptr)
{
    while (ptr != NULL)
    {
        printf("the elenment is ",ptr->data);
        ptr = ptr->next;
    }
    
    
}
int isemp(struct node * top)
{
    if (top == NULL)
    {
        return 1;
    }
    else
    {
        return 0;
    }
    
    
}
int isfull(struct node * top)
{   
    struct node *p = (struct node *)malloc(sizeof(struct node));
    if (p == NULL)
    {
        return 1;
    }
    else
    {
        return 0;
    }
    
    
}

int push(struct node * top ,int value)
{
    if (isfull(top))
    {
        printf("the stack over flow");
    }
    else
    {
        struct node *n = (struct node *)malloc(sizeof(struct node));
        top = n;
        n->data = value;
        n->next = top;

    }
    
}

int pop(struct node ** top)
{
    if (isemp(top))
    {
        printf("the stack under flow");
    }
    else
    {
        struct node * n = top;
        top = top->next;;
        int x = n->data;
        free(n);
        return x;

    }
    
}



int main()

{
    struct node *top =NULL;
    top = push(top,22);
    top = push(top,222);
    top = push(top,2222);
    linked(top);
    pop(&top);

    return 0;

}
