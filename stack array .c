#include<stdio.h>
#include<stdlib.h>


struct stack 
{
    int size ;
    int top;
    int *arr;
};

int isempty(struct stack * ptr)
{
    if (ptr->top == -1)
    {
        printf("the stack is empty");
    }
    else
    {
        printf("the stack is not empty");
    }
    
    
}

int isfull(struct stack * ptr)
{
    if (ptr->top = ptr->size - 1)
    {
        return 1;
    }
    else
    {
        return 0;
    }
    
    
}

int main()
{
    struct stack * hi;
    hi->size = 80;
    hi->top = -1;
    hi->arr = (int*)malloc(hi->size*sizeof(int));
    hi->arr[1] = 4;
    hi->top++;

    isempty(hi);
    
    return 0;

}
