// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from interfaces_hmm_sim:msg/AgentPoses.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES_HMM_SIM__MSG__DETAIL__AGENT_POSES__STRUCT_H_
#define INTERFACES_HMM_SIM__MSG__DETAIL__AGENT_POSES__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'agents'
// Member 'x'
// Member 'y'
// Member 'z'
#include "rosidl_runtime_c/primitives_sequence.h"

/// Struct defined in msg/AgentPoses in the package interfaces_hmm_sim.
typedef struct interfaces_hmm_sim__msg__AgentPoses
{
  rosidl_runtime_c__int32__Sequence agents;
  rosidl_runtime_c__float__Sequence x;
  rosidl_runtime_c__float__Sequence y;
  rosidl_runtime_c__float__Sequence z;
} interfaces_hmm_sim__msg__AgentPoses;

// Struct for a sequence of interfaces_hmm_sim__msg__AgentPoses.
typedef struct interfaces_hmm_sim__msg__AgentPoses__Sequence
{
  interfaces_hmm_sim__msg__AgentPoses * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces_hmm_sim__msg__AgentPoses__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // INTERFACES_HMM_SIM__MSG__DETAIL__AGENT_POSES__STRUCT_H_
