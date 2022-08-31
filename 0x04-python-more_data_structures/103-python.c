#include <Python.h>
#include <stdio.h>


/**
 * print_python_bytes - printf some basic info about python lists
 * @p: PyObject
 *
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	long int length = 0, count, limit;
	char *string;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	length = PyBytes_Size(p);
	string = ((PyBytesObject *)p)->ob_sval;
	printf("  size: %ld\n", length);
	printf("  trying string: %s\n", string);

	if (length >= 10)
		limit = 10;
	else
		limit = length + 1;

	printf("  first %ld bytes:", limit);
	for (count = 0; count < limit; count++)
	{
		if (string[count] >= 0)
			printf(" %02x", string[count]);
		else
			printf(" %02x", 256 + string[count]);
	}

	printf("\n");
}

/**
 * print_python_list - printf some basic info about Python lists
 * @p: PyObject
 *
 *Return: void
 */
void print_python_list(PyObject *p)
{
	long int length, count;
	PyListObject *list;
	PyObject *obj;

	length = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", length);

	list = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", list->allocated);

	for (count = 0; count < length; count++)
	{
		obj = ((PyListObject *)p)->ob_item[count];
		printf("Element %ld: %s\n", count, ((obj)->ob_type)->tp_name);

		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
g
