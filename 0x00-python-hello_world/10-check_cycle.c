#include "lists.h"

/**
 * check_cycle - Function checks if a list is cyclic
 * @list: Pointer to first node in the linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *data_head = NULL;

	while (list != NULL)
	{
		if (data_is_here(data_head, list->n))
			return (1);
		add_nodeint(&data_head, list->n);
		list = list->next;
	}
	return (0);
}

/**
 * data_is_here - Function checks local node for value passed
 * @list: Pointer to first node in the local linked list
 * @n: Data to search in the local node
 *
 * Return: 1 if there is, 0 if there is not
 */
size_t data_is_here(listint_t *list, int n)
{
	while (list != NULL)
	{
		if (list->n == n)
			return (1);
		list = list->next;
	}
	return (0);
}
