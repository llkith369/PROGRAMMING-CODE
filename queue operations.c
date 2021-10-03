#include <stdio.h>
#include <stdlib.h>

struct queue
{

    int size;
    int f;
    int r;
    int *array;
};

int travel(struct queue *q)
{
    for (int i = 0; i < q->size; i++)
    {
        printf("the element is %d",q->array[i]);
    }
    
    
}

int isfull(struct queue *q)
{
    if (q->r == q->size - 1)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int isempty(struct queue *q)
{
    if (q->f == q->r)
    {
        return 1;
    }
    else
    {
        return 0;
    }
    
    
}

int enqueue(struct queue *q, int value)
{
    if (isfull(q))
    {
        printf("enqueue overflow\n");
    }
    else
    {
        q->r = q->r + 1;
        q->array[q->r] = value;
    }
}

int dequeue(struct queue *q)
{   
    
    int a = -1;
    if (isempty(q))
    {
        printf("dequeue cant be done\n");
    }
    else
    {   
         
        q->f++;
        a = q->array[q->f];
        return a;

    }
    
    
}

int main()
{
    struct queue *hi;
    hi->size = 100;
    hi->f = -1;
    hi->r = -1;
    hi->array =(int *)malloc(hi->size * sizeof(int));
    
    enqueue(hi,1);
    enqueue(hi,2);
    enqueue(hi,3);
    travel(hi);
    dequeue(hi);
    
    
    return 0;



}
