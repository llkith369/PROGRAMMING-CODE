#include <stdio.h>
#include <Stdlib.h>

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

struct node * deleteATfirst(struct node* head)
{
    struct node * ptr = head;
    head = head->next;
    free(ptr);
    return head;
}

struct node * deleteAT_index(struct node * head,int index)
{
    
    struct node * p = head;
    struct node * q = head->next;

    for (int i = 0; i < index - 1; i++)
    {
        p = p->next;
        q = q->next;

    }
    p->next = q->next;
    free(q);
    return head; 
    
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
    printf("after deletion \n");
    deleteAT_index(head,2);
    traversing(head);

    return 0;

}
