// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from interfaces_hmm_sim:msg/Status.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES_HMM_SIM__MSG__DETAIL__STATUS__STRUCT_H_
#define INTERFACES_HMM_SIM__MSG__DETAIL__STATUS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'agent'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/Status in the package interfaces_hmm_sim.
typedef struct interfaces_hmm_sim__msg__Status
{
  rosidl_runtime_c__String agent;
  bool start;
  bool arrived;
  bool replan_received;
} interfaces_hmm_sim__msg__Status;

// Struct for a sequence of interfaces_hmm_sim__msg__Status.
typedef struct interfaces_hmm_sim__msg__Status__Sequence
{
  interfaces_hmm_sim__msg__Status * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces_hmm_sim__msg__Status__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // INTERFACES_HMM_SIM__MSG__DETAIL__STATUS__STRUCT_H_
