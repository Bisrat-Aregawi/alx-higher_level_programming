#include <Python.h>

void print_python_list_info(PyObject *p)
{
        size_t i;
        size_t item_count = PyList_Size(p);
        printf("[*] Size of the Python List = %lu\n", item_count);
        printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

        for (i = 0; i < item_count; i++)
                printf("Element %lu: %s\n", i, PyList_GET_ITEM(p, i)->ob_type->tp_name);
}
