// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from ltl_automaton_msgs:srv/TrapCheck.idl
// generated code does not contain a copyright notice

#ifndef LTL_AUTOMATON_MSGS__SRV__DETAIL__TRAP_CHECK__STRUCT_H_
#define LTL_AUTOMATON_MSGS__SRV__DETAIL__TRAP_CHECK__STRUCT_H_

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

/// Struct defined in srv/TrapCheck in the package ltl_automaton_msgs.
typedef struct ltl_automaton_msgs__srv__TrapCheck_Request
{
  /// Transition system state to be tested for trap
  ltl_automaton_msgs__msg__TransitionSystemState ts_state;
} ltl_automaton_msgs__srv__TrapCheck_Request;

// Struct for a sequence of ltl_automaton_msgs__srv__TrapCheck_Request.
typedef struct ltl_automaton_msgs__srv__TrapCheck_Request__Sequence
{
  ltl_automaton_msgs__srv__TrapCheck_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ltl_automaton_msgs__srv__TrapCheck_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/TrapCheck in the package ltl_automaton_msgs.
typedef struct ltl_automaton_msgs__srv__TrapCheck_Response
{
  /// Returns false if state is not connected to agent current
  /// state and therefor cannot be tested for trap
  bool is_connected;
  /// Returns true if check state is a trap, false otherwises
  bool is_trap;
} ltl_automaton_msgs__srv__TrapCheck_Response;

// Struct for a sequence of ltl_automaton_msgs__srv__TrapCheck_Response.
typedef struct ltl_automaton_msgs__srv__TrapCheck_Response__Sequence
{
  ltl_automaton_msgs__srv__TrapCheck_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ltl_automaton_msgs__srv__TrapCheck_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // LTL_AUTOMATON_MSGS__SRV__DETAIL__TRAP_CHECK__STRUCT_H_
