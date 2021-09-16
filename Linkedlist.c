#include <stdio.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node *next;

};



void traversing(struct node * ptr)
{
    while (ptr != NULL)
    {
        printf("the element is : %d\n",ptr->data);
        ptr = ptr->next;
    }
    
}

struct node * inserting_first(struct node * head,int data)
{
    struct node * ptr = (struct node*)malloc(sizeof(struct node));  //allocating memeory for new node
    ptr->data = data; //accessing the structure variables 
    ptr->next = head;
    return ptr;
}

struct node * insertAT_index(struct node * head,int data,int index)
{
    struct node * ptr = (struct node*)malloc(sizeof(struct node));
    struct node * p = head;
    int i = 0 ;

    while (i != index-1)
    {
        p= p->next;
        i++;
    }
    ptr->data = data;
    ptr->next = p->next;
    p->next = ptr;
    return ptr;
    
    
}

int main()
{
    struct node *head;
    struct node *second;
    struct node *third;

    head = (struct node *)malloc(sizeof(struct node));
    second = (struct node *)malloc(sizeof(struct node));
    third = (struct node *)malloc(sizeof(struct node));

    head->data = 29;
    head->next = second;

    second->data = 30;
    second->next = third;

    third->data = 31;
    third->next = NULL;

    traversing(head);
    head = insertAT_index(head,25,2);
    traversing(head);

    return 0;


}
