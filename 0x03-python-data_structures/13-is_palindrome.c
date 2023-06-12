#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverseList - reverse all elements of a listint_t list
 * @head: pointer to head of list
 * Return: number of nodes
 */
listint_t *reverseList(listint_t *head)
{
listint_t *prev = NULL;
listint_t *current = head;
listint_t *next = NULL;
while (current != NULL)
{
next = current->next;
current->next = prev;
prev = current;
current = next;
}
return (prev);
}

/**
 * is_palindrome - check if list is palindrome
 * @head: pointer to head of list
 * Return: number of nodes
 */
int is_palindrome(listint_t **head)
{
if (*head == NULL)
{
return (1);
}
listint_t *slowPtr = *head;
listint_t *fastPtr = *head;
while (fastPtr != NULL && fastPtr->next != NULL)
{
slowPtr = slowPtr->next;
fastPtr = fastPtr->next->next;
}
listint_t *secondHalf = reverseList(slowPtr);
listint_t *firstHalf = *head;
while (secondHalf != NULL)
{
if (firstHalf->n != secondHalf->n)
{
return (0);
}
firstHalf = firstHalf->next;
secondHalf = secondHalf->next;
}
return (1);
}
