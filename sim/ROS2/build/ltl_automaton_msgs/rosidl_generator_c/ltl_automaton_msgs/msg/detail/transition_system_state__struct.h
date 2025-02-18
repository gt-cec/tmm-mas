// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from ltl_automaton_msgs:msg/TransitionSystemState.idl
// generated code does not contain a copyright notice

#ifndef LTL_AUTOMATON_MSGS__MSG__DETAIL__TRANSITION_SYSTEM_STATE__STRUCT_H_
#define LTL_AUTOMATON_MSGS__MSG__DETAIL__TRANSITION_SYSTEM_STATE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'states'
// Member 'state_dimension_names'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/TransitionSystemState in the package ltl_automaton_msgs.
/**
  * Specify a transition system state
  * Used to describe an agent state within a TS (transition system) graph.
  * Number of dimensions within each TS states can vary depending of the
  * defined TS.
 */
typedef struct ltl_automaton_msgs__msg__TransitionSystemState
{
  /// TS (Transition System) state. A TS state is composed of an
  /// array of states from at least 1 transition model or from the
  /// product of more transition models.
  rosidl_runtime_c__String__Sequence states;
  /// Name of each state dimension. State should always be ordered the same
  /// way, but this field can help to disambiguate if needed.
  rosidl_runtime_c__String__Sequence state_dimension_names;
} ltl_automaton_msgs__msg__TransitionSystemState;

// Struct for a sequence of ltl_automaton_msgs__msg__TransitionSystemState.
typedef struct ltl_automaton_msgs__msg__TransitionSystemState__Sequence
{
  ltl_automaton_msgs__msg__TransitionSystemState * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ltl_automaton_msgs__msg__TransitionSystemState__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // LTL_AUTOMATON_MSGS__MSG__DETAIL__TRANSITION_SYSTEM_STATE__STRUCT_H_
