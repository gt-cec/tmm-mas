// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from ltl_automaton_msgs:msg/RelayResponse.idl
// generated code does not contain a copyright notice

#ifndef LTL_AUTOMATON_MSGS__MSG__DETAIL__RELAY_RESPONSE__STRUCT_H_
#define LTL_AUTOMATON_MSGS__MSG__DETAIL__RELAY_RESPONSE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'new_plan_prefix'
// Member 'new_plan_suffix'
#include "ltl_automaton_msgs/msg/detail/ltl_plan__struct.h"

/// Struct defined in msg/RelayResponse in the package ltl_automaton_msgs.
typedef struct ltl_automaton_msgs__msg__RelayResponse
{
  bool success;
  ltl_automaton_msgs__msg__LTLPlan new_plan_prefix;
  ltl_automaton_msgs__msg__LTLPlan new_plan_suffix;
} ltl_automaton_msgs__msg__RelayResponse;

// Struct for a sequence of ltl_automaton_msgs__msg__RelayResponse.
typedef struct ltl_automaton_msgs__msg__RelayResponse__Sequence
{
  ltl_automaton_msgs__msg__RelayResponse * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ltl_automaton_msgs__msg__RelayResponse__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // LTL_AUTOMATON_MSGS__MSG__DETAIL__RELAY_RESPONSE__STRUCT_H_
