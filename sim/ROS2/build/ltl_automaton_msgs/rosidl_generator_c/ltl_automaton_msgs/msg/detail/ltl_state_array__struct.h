// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from ltl_automaton_msgs:msg/LTLStateArray.idl
// generated code does not contain a copyright notice

#ifndef LTL_AUTOMATON_MSGS__MSG__DETAIL__LTL_STATE_ARRAY__STRUCT_H_
#define LTL_AUTOMATON_MSGS__MSG__DETAIL__LTL_STATE_ARRAY__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'ltl_states'
#include "ltl_automaton_msgs/msg/detail/ltl_state__struct.h"

/// Struct defined in msg/LTLStateArray in the package ltl_automaton_msgs.
/**
  * Array of LTL states (also called product states).
 */
typedef struct ltl_automaton_msgs__msg__LTLStateArray
{
  ltl_automaton_msgs__msg__LTLState__Sequence ltl_states;
} ltl_automaton_msgs__msg__LTLStateArray;

// Struct for a sequence of ltl_automaton_msgs__msg__LTLStateArray.
typedef struct ltl_automaton_msgs__msg__LTLStateArray__Sequence
{
  ltl_automaton_msgs__msg__LTLStateArray * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ltl_automaton_msgs__msg__LTLStateArray__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // LTL_AUTOMATON_MSGS__MSG__DETAIL__LTL_STATE_ARRAY__STRUCT_H_
