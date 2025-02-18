// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from ltl_automaton_msgs:msg/TransitionSystemStateStamped.idl
// generated code does not contain a copyright notice

#ifndef LTL_AUTOMATON_MSGS__MSG__DETAIL__TRANSITION_SYSTEM_STATE_STAMPED__STRUCT_H_
#define LTL_AUTOMATON_MSGS__MSG__DETAIL__TRANSITION_SYSTEM_STATE_STAMPED__STRUCT_H_

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
// Member 'ts_state'
#include "ltl_automaton_msgs/msg/detail/transition_system_state__struct.h"

/// Struct defined in msg/TransitionSystemStateStamped in the package ltl_automaton_msgs.
/**
  * Specify a transition system state with a header and timestamp
  * Used to describe an agent state within a TS (transition system) graph.
 */
typedef struct ltl_automaton_msgs__msg__TransitionSystemStateStamped
{
  std_msgs__msg__Header header;
  ltl_automaton_msgs__msg__TransitionSystemState ts_state;
} ltl_automaton_msgs__msg__TransitionSystemStateStamped;

// Struct for a sequence of ltl_automaton_msgs__msg__TransitionSystemStateStamped.
typedef struct ltl_automaton_msgs__msg__TransitionSystemStateStamped__Sequence
{
  ltl_automaton_msgs__msg__TransitionSystemStateStamped * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ltl_automaton_msgs__msg__TransitionSystemStateStamped__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // LTL_AUTOMATON_MSGS__MSG__DETAIL__TRANSITION_SYSTEM_STATE_STAMPED__STRUCT_H_
