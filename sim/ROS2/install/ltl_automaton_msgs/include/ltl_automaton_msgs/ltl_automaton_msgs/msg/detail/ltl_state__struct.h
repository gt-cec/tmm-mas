// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from ltl_automaton_msgs:msg/LTLState.idl
// generated code does not contain a copyright notice

#ifndef LTL_AUTOMATON_MSGS__MSG__DETAIL__LTL_STATE__STRUCT_H_
#define LTL_AUTOMATON_MSGS__MSG__DETAIL__LTL_STATE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'ts_state'
#include "ltl_automaton_msgs/msg/detail/transition_system_state__struct.h"
// Member 'buchi_state'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/LTLState in the package ltl_automaton_msgs.
/**
  * Specify a LTL state or LTL product state. State is a composition
  * of a transition system state and a Buchi automaton state
 */
typedef struct ltl_automaton_msgs__msg__LTLState
{
  ltl_automaton_msgs__msg__TransitionSystemState ts_state;
  rosidl_runtime_c__String buchi_state;
} ltl_automaton_msgs__msg__LTLState;

// Struct for a sequence of ltl_automaton_msgs__msg__LTLState.
typedef struct ltl_automaton_msgs__msg__LTLState__Sequence
{
  ltl_automaton_msgs__msg__LTLState * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ltl_automaton_msgs__msg__LTLState__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // LTL_AUTOMATON_MSGS__MSG__DETAIL__LTL_STATE__STRUCT_H_
