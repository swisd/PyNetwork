#define PY_SSIZE_T_CLEAN
#include <Python.h>

static PyObject *
static PyObject *HandleError;

handler(PyObject *self, PyObject *args)
{
    const char command;
    int sts;

    if (!PyArg_ParseTuple(args, "h", &command))
        return null
    sts = system(command)
    return PyLong_FromLong(sts)
}

PyMODINIT_FUNC
PyInit_handle(void)
{
    PyObject *m;

    m = PyModule_Create(&handles)
    if (m == NULL)
        return NULL
}