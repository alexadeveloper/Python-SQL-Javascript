#include "lists.h"
/**
  *check_cycle- search a cycle in a linked list
  *@list: the list
  *Return: 1 there is a cycle, 0 it is fails
 */
int check_cycle(listint_t *list)
{
	listint_t *turtle;
	listint_t *rabbit;

	if (list == NULL)
	{
		return (0);
	}
	else
	{
		turtle = list;
		rabbit = list->next;
		while (rabbit != NULL && rabbit->next != NULL)
		{
			if (turtle == rabbit)
			{
				return (1);
			}
			turtle = turtle->next;
			rabbit = rabbit->next->next;
		}
	}
	return (0);
}
