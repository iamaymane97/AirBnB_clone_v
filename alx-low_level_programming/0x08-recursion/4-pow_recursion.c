#include "main.h"

/**
 * _pow_recursion - function name
 * @x: parameter 1
 * @y: parameter 2
 * Return: value of a given number passed to the function
 */

int _pow_recursion(int x, int y)
{
	/* Base case 1: If the exponent is negative, return -1 (error). */
	if (y < 0)
		return (-1);

	/* Base case 2: If the exponent is 0, return 1. */
	else if (y == 0)
		return (1);

	/* Recursive case: Calculate x to the power of (y-1) and multiply it by x. */
	else
		return (x * _pow_recursion(x, (y - 1)));
}

