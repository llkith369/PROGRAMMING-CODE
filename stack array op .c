#include <stdio.h>
#include <stdlib.h>

struct stack
{
    int size;
    int top;
    int *arr;
};

int isEmpty(struct stack *ptr)
{
    if (ptr->top == -1)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int isFull(struct stack *ptr)
{
    if (ptr->top == ptr->size - 1)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

void push(struct stack * ptr,int value)
{
    if (isFull(ptr))
    {
        printf("stack overflow");
    }
    else
    {
        ptr->top++;
        ptr->arr[ptr->top] = value;

    }
    
    
}


int pop(struct stack * ptr)
{
    if (isEmpty(ptr))
    {
        printf("stack underflow");
    }
    else
    {
        int n = ptr->top;
        ptr->top--;
        return n; 
    }
    
    
}

int main()
{
    // struct stack s;
    // s.size = 80;
    // s.top = -1;
    // s.arr = (int *) malloc(s.size * sizeof(int));

    struct stack *s;
    s->size = 80;
    s->top = -1;
    s->arr = (int *)malloc(s->size * sizeof(int));
    // Check if stack is empty
    push(s,40);

    return 0;
}
