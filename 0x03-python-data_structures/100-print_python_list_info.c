#include <Python.h>
#include <stdio.h>
/**
 * print_python_list_info - print python list info
 * @p: PyObject pointer
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size_list, i, mem_alloc;
	PyObject *my_pyobject;
	const char *type_object;

	size_list = PyList_Size(p);
	mem_alloc = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %li\n", size_list);
	printf("[*] Allocated = %li\n", mem_alloc);

	for (i = 0; i < size_list; i++)
	{
		my_pyobject = PyList_GetItem(p, i);
		type_object = Py_TYPE(my_pyobject)->tp_name;
		printf("Element %li : %s\n", i, type_object);
	}
}
