// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from ltl_automaton_msgs:srv/TaskReplanningRelabel.idl
// generated code does not contain a copyright notice

#ifndef LTL_AUTOMATON_MSGS__SRV__DETAIL__TASK_REPLANNING_RELABEL__STRUCT_H_
#define LTL_AUTOMATON_MSGS__SRV__DETAIL__TASK_REPLANNING_RELABEL__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'state'
// Member 'label'
#include "rosidl_runtime_c/string.h"
// Member 'current_state'
#include "ltl_automaton_msgs/msg/detail/transition_system_state__struct.h"

/// Struct defined in srv/TaskReplanningRelabel in the package ltl_automaton_msgs.
typedef struct ltl_automaton_msgs__srv__TaskReplanningRelabel_Request
{
  rosidl_runtime_c__String__Sequence state;
  rosidl_runtime_c__String__Sequence label;
  ltl_automaton_msgs__msg__TransitionSystemState current_state;
} ltl_automaton_msgs__srv__TaskReplanningRelabel_Request;

// Struct for a sequence of ltl_automaton_msgs__srv__TaskReplanningRelabel_Request.
typedef struct ltl_automaton_msgs__srv__TaskReplanningRelabel_Request__Sequence
{
  ltl_automaton_msgs__srv__TaskReplanningRelabel_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ltl_automaton_msgs__srv__TaskReplanningRelabel_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'new_plan'
#include "ltl_automaton_msgs/msg/detail/ltl_plan__struct.h"

/// Struct defined in srv/TaskReplanningRelabel in the package ltl_automaton_msgs.
typedef struct ltl_automaton_msgs__srv__TaskReplanningRelabel_Response
{
  bool success;
  ltl_automaton_msgs__msg__LTLPlan new_plan;
} ltl_automaton_msgs__srv__TaskReplanningRelabel_Response;

// Struct for a sequence of ltl_automaton_msgs__srv__TaskReplanningRelabel_Response.
typedef struct ltl_automaton_msgs__srv__TaskReplanningRelabel_Response__Sequence
{
  ltl_automaton_msgs__srv__TaskReplanningRelabel_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ltl_automaton_msgs__srv__TaskReplanningRelabel_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // LTL_AUTOMATON_MSGS__SRV__DETAIL__TASK_REPLANNING_RELABEL__STRUCT_H_
