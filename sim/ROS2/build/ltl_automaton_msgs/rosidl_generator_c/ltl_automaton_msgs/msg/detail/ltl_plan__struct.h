// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from ltl_automaton_msgs:msg/LTLPlan.idl
// generated code does not contain a copyright notice

#ifndef LTL_AUTOMATON_MSGS__MSG__DETAIL__LTL_PLAN__STRUCT_H_
#define LTL_AUTOMATON_MSGS__MSG__DETAIL__LTL_PLAN__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"
// Member 'action_sequence'
#include "rosidl_runtime_c/string.h"
// Member 'ts_state_sequence'
#include "ltl_automaton_msgs/msg/detail/transition_system_state__struct.h"

/// Struct defined in msg/LTLPlan in the package ltl_automaton_msgs.
/**
  * Specify a plan from an LTL planner as a
  * sequence of actions
 */
typedef struct ltl_automaton_msgs__msg__LTLPlan
{
  std_msgs__msg__Header header;
  /// Sequence of actions in the plan
  rosidl_runtime_c__String__Sequence action_sequence;
  /// Sequence of states in the plan
  ltl_automaton_msgs__msg__TransitionSystemState__Sequence ts_state_sequence;
} ltl_automaton_msgs__msg__LTLPlan;

// Struct for a sequence of ltl_automaton_msgs__msg__LTLPlan.
typedef struct ltl_automaton_msgs__msg__LTLPlan__Sequence
{
  ltl_automaton_msgs__msg__LTLPlan * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ltl_automaton_msgs__msg__LTLPlan__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // LTL_AUTOMATON_MSGS__MSG__DETAIL__LTL_PLAN__STRUCT_H_
