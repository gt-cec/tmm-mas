// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from interfaces_hmm_sim:msg/Status.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "interfaces_hmm_sim/msg/detail/status__rosidl_typesupport_introspection_c.h"
#include "interfaces_hmm_sim/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "interfaces_hmm_sim/msg/detail/status__functions.h"
#include "interfaces_hmm_sim/msg/detail/status__struct.h"


// Include directives for member types
// Member `agent`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void interfaces_hmm_sim__msg__Status__rosidl_typesupport_introspection_c__Status_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  interfaces_hmm_sim__msg__Status__init(message_memory);
}

void interfaces_hmm_sim__msg__Status__rosidl_typesupport_introspection_c__Status_fini_function(void * message_memory)
{
  interfaces_hmm_sim__msg__Status__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember interfaces_hmm_sim__msg__Status__rosidl_typesupport_introspection_c__Status_message_member_array[4] = {
  {
    "agent",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces_hmm_sim__msg__Status, agent),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "start",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces_hmm_sim__msg__Status, start),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "arrived",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces_hmm_sim__msg__Status, arrived),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "replan_received",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces_hmm_sim__msg__Status, replan_received),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers interfaces_hmm_sim__msg__Status__rosidl_typesupport_introspection_c__Status_message_members = {
  "interfaces_hmm_sim__msg",  // message namespace
  "Status",  // message name
  4,  // number of fields
  sizeof(interfaces_hmm_sim__msg__Status),
  interfaces_hmm_sim__msg__Status__rosidl_typesupport_introspection_c__Status_message_member_array,  // message members
  interfaces_hmm_sim__msg__Status__rosidl_typesupport_introspection_c__Status_init_function,  // function to initialize message memory (memory has to be allocated)
  interfaces_hmm_sim__msg__Status__rosidl_typesupport_introspection_c__Status_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t interfaces_hmm_sim__msg__Status__rosidl_typesupport_introspection_c__Status_message_type_support_handle = {
  0,
  &interfaces_hmm_sim__msg__Status__rosidl_typesupport_introspection_c__Status_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interfaces_hmm_sim
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces_hmm_sim, msg, Status)() {
  if (!interfaces_hmm_sim__msg__Status__rosidl_typesupport_introspection_c__Status_message_type_support_handle.typesupport_identifier) {
    interfaces_hmm_sim__msg__Status__rosidl_typesupport_introspection_c__Status_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &interfaces_hmm_sim__msg__Status__rosidl_typesupport_introspection_c__Status_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
