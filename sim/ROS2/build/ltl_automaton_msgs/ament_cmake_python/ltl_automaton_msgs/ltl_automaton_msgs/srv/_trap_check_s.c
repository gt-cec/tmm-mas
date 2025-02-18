// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from ltl_automaton_msgs:srv/TrapCheck.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "ltl_automaton_msgs/srv/detail/trap_check__struct.h"
#include "ltl_automaton_msgs/srv/detail/trap_check__functions.h"

bool ltl_automaton_msgs__msg__transition_system_state__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * ltl_automaton_msgs__msg__transition_system_state__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool ltl_automaton_msgs__srv__trap_check__request__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[53];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("ltl_automaton_msgs.srv._trap_check.TrapCheck_Request", full_classname_dest, 52) == 0);
  }
  ltl_automaton_msgs__srv__TrapCheck_Request * ros_message = _ros_message;
  {  // ts_state
    PyObject * field = PyObject_GetAttrString(_pymsg, "ts_state");
    if (!field) {
      return false;
    }
    if (!ltl_automaton_msgs__msg__transition_system_state__convert_from_py(field, &ros_message->ts_state)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * ltl_automaton_msgs__srv__trap_check__request__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of TrapCheck_Request */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("ltl_automaton_msgs.srv._trap_check");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "TrapCheck_Request");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  ltl_automaton_msgs__srv__TrapCheck_Request * ros_message = (ltl_automaton_msgs__srv__TrapCheck_Request *)raw_ros_message;
  {  // ts_state
    PyObject * field = NULL;
    field = ltl_automaton_msgs__msg__transition_system_state__convert_to_py(&ros_message->ts_state);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "ts_state", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}

#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
// already included above
// #include <Python.h>
// already included above
// #include <stdbool.h>
// already included above
// #include "numpy/ndarrayobject.h"
// already included above
// #include "rosidl_runtime_c/visibility_control.h"
// already included above
// #include "ltl_automaton_msgs/srv/detail/trap_check__struct.h"
// already included above
// #include "ltl_automaton_msgs/srv/detail/trap_check__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool ltl_automaton_msgs__srv__trap_check__response__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[54];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("ltl_automaton_msgs.srv._trap_check.TrapCheck_Response", full_classname_dest, 53) == 0);
  }
  ltl_automaton_msgs__srv__TrapCheck_Response * ros_message = _ros_message;
  {  // is_connected
    PyObject * field = PyObject_GetAttrString(_pymsg, "is_connected");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->is_connected = (Py_True == field);
    Py_DECREF(field);
  }
  {  // is_trap
    PyObject * field = PyObject_GetAttrString(_pymsg, "is_trap");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->is_trap = (Py_True == field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * ltl_automaton_msgs__srv__trap_check__response__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of TrapCheck_Response */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("ltl_automaton_msgs.srv._trap_check");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "TrapCheck_Response");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  ltl_automaton_msgs__srv__TrapCheck_Response * ros_message = (ltl_automaton_msgs__srv__TrapCheck_Response *)raw_ros_message;
  {  // is_connected
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->is_connected ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "is_connected", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // is_trap
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->is_trap ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "is_trap", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
