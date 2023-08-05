#include <bits/stdc++.h>
#include <Python.h>
#include "levenshtein.h"

using namespace std;

static PyObject* algopyc_WagnerFischer(PyObject *self, PyObject *args)
{
    Py_UNICODE* str1; // char* str1
    Py_UNICODE* str2; // char* str2
    int edit_dist;

    //if (!PyArg_ParseTuple(args, "ss", &str1, &str2))
    if (!PyArg_ParseTuple(args, "uu", &str1, &str2))
        return NULL;
    
    edit_dist = levenshtein(str1, str2);
    return Py_BuildValue("i", edit_dist);
}


static PyMethodDef algoMethods[] = {
    {"Wagner_Fisher", algopyc_WagnerFischer, METH_VARARGS, "returns the Levenshtein distance between strings"},
    {NULL, NULL, 0, NULL}
};


static struct PyModuleDef algoModule = {
    PyModuleDef_HEAD_INIT,
    "algopyc",
    "Implementation of various algorithms",
    -1, algoMethods
};

PyMODINIT_FUNC
PyInit_algopyc(void)
{
    return PyModule_Create(&algoModule);
}