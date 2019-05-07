#include "lists.h"
/**
  *reverse_listint - reverses a list
  *@head: is a pointer to the lists
  *Return: a pointer to the first node of the reverse list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *anterior;
	listint_t *siguiente;

	anterior = NULL;
	siguiente = (*head)->next;
	if (*head == NULL || head == NULL)
	{
		return (NULL);
	}
	if ((*head)->next == NULL)
	{
		return (*head);
	}
	while ((*head)->next != NULL)
	{
		(*head)->next = anterior;
		anterior = *head;
		*head = siguiente;
		siguiente = siguiente->next;
	}
	(*head)->next = anterior;
	return (*head);
}
/**
  *is_palindrome- the same
  *@head: is a pointer to the lists
  *Return: a pointer to the first node of the reverse list
 */
int is_palindrome(listint_t **head)
{
	unsigned int nodes, count;
	listint_t *copy;
	
	copy = reverse_listint(head);
	count = 0;
	for (nodes = 0; *head != NULL; nodes++)
	{
		if ((*head)->n != copy->n)
		{
			return (1);
		}
		else
		{
			count++;
			*head = (*head)->next;
			copy = copy->next;
		}
	}
return (0);
}
