#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int data;
    struct Node *prev;
};

void linkedListTraversal(struct Node *fourth)
{
    struct Node *ptr = fourth;

   while (ptr != NULL)
   {
       printf("the element %d\n",ptr->data);
       ptr = ptr->prev;
   }
    
    
    
}

struct Node *insertAtFirst(struct Node *head, int data)
{
    struct Node *ptr = (struct Node *)malloc(sizeof(struct Node));
    ptr->data = data;

    struct Node *p = head->prev;
    while (p->prev != head)
    {
        p = p->prev;
    }
    // At this point p points to the last node of this circular linked list

    p->prev = ptr;
    ptr->prev = head;
    head = ptr;
    return head;
}

int main()
{

    struct Node *head;
    struct Node *second;
    struct Node *third;
    struct Node *fourth;

    // Allocate memory for nodes in the linked list in Heap
    head = (struct Node *)malloc(sizeof(struct Node));
    second = (struct Node *)malloc(sizeof(struct Node));
    third = (struct Node *)malloc(sizeof(struct Node));
    fourth = (struct Node *)malloc(sizeof(struct Node));

    // Link first and second nodes
    head->data = 4;
    head->prev = NULL;

    // Link second and third nodes
    second->data = 3;
    second->prev = head;

    // Link third and fourth nodes
    third->data = 6;
    third->prev = second;

    // Terminate the list at the third node
    fourth->data = 1;
    fourth->prev = third;

//     printf("Circular Linked list before insertion\n");
        linkedListTraversal(fourth);
//     head = insertAtFirst(head, 54);
//     head = insertAtFirst(head, 58);
//     head = insertAtFirst(head, 59);
//     printf("Circular Linked list after insertion\n");
//     linkedListTraversal(head);
    return 0;
}
