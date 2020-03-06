// https://medium.com/@holdengrissett/linux-101-how-to-hack-your-process-memory-2514a3d0778d
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>


int get_len(char *str)
{
	int i;

	for (i = 0; str[i]; i++)
		;
	return (i);
}

int main(int ac, char **av)
{
	char *str;
	int i = 1;

	if (ac == 2)
	{
		str = malloc(get_len(av[1]) + 1);
		strcpy(str, av[1]);
	}

	while (i)
	{
		printf("[%d] %s - addr: %p\n", i, str, str);
		sleep(1);
		i++;
	}

	free(str);
	return (0);
}
