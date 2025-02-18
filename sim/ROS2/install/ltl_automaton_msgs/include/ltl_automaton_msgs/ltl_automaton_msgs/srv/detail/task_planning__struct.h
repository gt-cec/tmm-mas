// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from ltl_automaton_msgs:srv/TaskPlanning.idl
// generated code does not contain a copyright notice

#ifndef LTL_AUTOMATON_MSGS__SRV__DETAIL__TASK_PLANNING__STRUCT_H_
#define LTL_AUTOMATON_MSGS__SRV__DETAIL__TASK_PLANNING__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'hard_task'
// Member 'soft_task'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/TaskPlanning in the package ltl_automaton_msgs.
typedef struct ltl_automaton_msgs__srv__TaskPlanning_Request
{
  /// Task is expressed as a hard task LTL formula and soft task LTL formula
  rosidl_runtime_c__String hard_task;
  rosidl_runtime_c__String soft_task;
} ltl_automaton_msgs__srv__TaskPlanning_Request;

// Struct for a sequence of ltl_automaton_msgs__srv__TaskPlanning_Request.
typedef struct ltl_automaton_msgs__srv__TaskPlanning_Request__Sequence
{
  ltl_automaton_msgs__srv__TaskPlanning_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ltl_automaton_msgs__srv__TaskPlanning_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/TaskPlanning in the package ltl_automaton_msgs.
typedef struct ltl_automaton_msgs__srv__TaskPlanning_Response
{
  /// Returns true if planning was successful, false otherwise
  bool success;
} ltl_automaton_msgs__srv__TaskPlanning_Response;

// Struct for a sequence of ltl_automaton_msgs__srv__TaskPlanning_Response.
typedef struct ltl_automaton_msgs__srv__TaskPlanning_Response__Sequence
{
  ltl_automaton_msgs__srv__TaskPlanning_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ltl_automaton_msgs__srv__TaskPlanning_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // LTL_AUTOMATON_MSGS__SRV__DETAIL__TASK_PLANNING__STRUCT_H_
