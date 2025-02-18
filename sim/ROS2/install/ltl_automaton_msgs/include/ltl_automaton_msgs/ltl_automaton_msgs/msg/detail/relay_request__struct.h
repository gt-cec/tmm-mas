// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from ltl_automaton_msgs:msg/RelayRequest.idl
// generated code does not contain a copyright notice

#ifndef LTL_AUTOMATON_MSGS__MSG__DETAIL__RELAY_REQUEST__STRUCT_H_
#define LTL_AUTOMATON_MSGS__MSG__DETAIL__RELAY_REQUEST__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'from_pose'
// Member 'to_pose'
#include "rosidl_runtime_c/primitives_sequence.h"
// Member 'current_state'
#include "ltl_automaton_msgs/msg/detail/transition_system_state__struct.h"
// Member 'type'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/RelayRequest in the package ltl_automaton_msgs.
typedef struct ltl_automaton_msgs__msg__RelayRequest
{
  rosidl_runtime_c__int32__Sequence from_pose;
  rosidl_runtime_c__int32__Sequence to_pose;
  double cost;
  ltl_automaton_msgs__msg__TransitionSystemState current_state;
  int32_t exec_index;
  rosidl_runtime_c__String type;
} ltl_automaton_msgs__msg__RelayRequest;

// Struct for a sequence of ltl_automaton_msgs__msg__RelayRequest.
typedef struct ltl_automaton_msgs__msg__RelayRequest__Sequence
{
  ltl_automaton_msgs__msg__RelayRequest * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ltl_automaton_msgs__msg__RelayRequest__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // LTL_AUTOMATON_MSGS__MSG__DETAIL__RELAY_REQUEST__STRUCT_H_
