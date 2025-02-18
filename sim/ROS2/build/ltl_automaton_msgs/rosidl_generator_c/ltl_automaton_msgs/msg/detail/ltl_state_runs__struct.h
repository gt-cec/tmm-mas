// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from ltl_automaton_msgs:msg/LTLStateRuns.idl
// generated code does not contain a copyright notice

#ifndef LTL_AUTOMATON_MSGS__MSG__DETAIL__LTL_STATE_RUNS__STRUCT_H_
#define LTL_AUTOMATON_MSGS__MSG__DETAIL__LTL_STATE_RUNS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'runs'
#include "ltl_automaton_msgs/msg/detail/ltl_state_array__struct.h"

/// Struct defined in msg/LTLStateRuns in the package ltl_automaton_msgs.
/**
  * Define multiple histories of LTL state as an array of LTL state arrays.
 */
typedef struct ltl_automaton_msgs__msg__LTLStateRuns
{
  ltl_automaton_msgs__msg__LTLStateArray__Sequence runs;
} ltl_automaton_msgs__msg__LTLStateRuns;

// Struct for a sequence of ltl_automaton_msgs__msg__LTLStateRuns.
typedef struct ltl_automaton_msgs__msg__LTLStateRuns__Sequence
{
  ltl_automaton_msgs__msg__LTLStateRuns * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ltl_automaton_msgs__msg__LTLStateRuns__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // LTL_AUTOMATON_MSGS__MSG__DETAIL__LTL_STATE_RUNS__STRUCT_H_
