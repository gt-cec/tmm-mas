// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from interfaces_hmm_sim:msg/AgentPoses.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES_HMM_SIM__MSG__DETAIL__AGENT_POSES__FUNCTIONS_H_
#define INTERFACES_HMM_SIM__MSG__DETAIL__AGENT_POSES__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "interfaces_hmm_sim/msg/rosidl_generator_c__visibility_control.h"

#include "interfaces_hmm_sim/msg/detail/agent_poses__struct.h"

/// Initialize msg/AgentPoses message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * interfaces_hmm_sim__msg__AgentPoses
 * )) before or use
 * interfaces_hmm_sim__msg__AgentPoses__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces_hmm_sim
bool
interfaces_hmm_sim__msg__AgentPoses__init(interfaces_hmm_sim__msg__AgentPoses * msg);

/// Finalize msg/AgentPoses message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces_hmm_sim
void
interfaces_hmm_sim__msg__AgentPoses__fini(interfaces_hmm_sim__msg__AgentPoses * msg);

/// Create msg/AgentPoses message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * interfaces_hmm_sim__msg__AgentPoses__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces_hmm_sim
interfaces_hmm_sim__msg__AgentPoses *
interfaces_hmm_sim__msg__AgentPoses__create();

/// Destroy msg/AgentPoses message.
/**
 * It calls
 * interfaces_hmm_sim__msg__AgentPoses__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces_hmm_sim
void
interfaces_hmm_sim__msg__AgentPoses__destroy(interfaces_hmm_sim__msg__AgentPoses * msg);

/// Check for msg/AgentPoses message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces_hmm_sim
bool
interfaces_hmm_sim__msg__AgentPoses__are_equal(const interfaces_hmm_sim__msg__AgentPoses * lhs, const interfaces_hmm_sim__msg__AgentPoses * rhs);

/// Copy a msg/AgentPoses message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces_hmm_sim
bool
interfaces_hmm_sim__msg__AgentPoses__copy(
  const interfaces_hmm_sim__msg__AgentPoses * input,
  interfaces_hmm_sim__msg__AgentPoses * output);

/// Initialize array of msg/AgentPoses messages.
/**
 * It allocates the memory for the number of elements and calls
 * interfaces_hmm_sim__msg__AgentPoses__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces_hmm_sim
bool
interfaces_hmm_sim__msg__AgentPoses__Sequence__init(interfaces_hmm_sim__msg__AgentPoses__Sequence * array, size_t size);

/// Finalize array of msg/AgentPoses messages.
/**
 * It calls
 * interfaces_hmm_sim__msg__AgentPoses__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces_hmm_sim
void
interfaces_hmm_sim__msg__AgentPoses__Sequence__fini(interfaces_hmm_sim__msg__AgentPoses__Sequence * array);

/// Create array of msg/AgentPoses messages.
/**
 * It allocates the memory for the array and calls
 * interfaces_hmm_sim__msg__AgentPoses__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces_hmm_sim
interfaces_hmm_sim__msg__AgentPoses__Sequence *
interfaces_hmm_sim__msg__AgentPoses__Sequence__create(size_t size);

/// Destroy array of msg/AgentPoses messages.
/**
 * It calls
 * interfaces_hmm_sim__msg__AgentPoses__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces_hmm_sim
void
interfaces_hmm_sim__msg__AgentPoses__Sequence__destroy(interfaces_hmm_sim__msg__AgentPoses__Sequence * array);

/// Check for msg/AgentPoses message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces_hmm_sim
bool
interfaces_hmm_sim__msg__AgentPoses__Sequence__are_equal(const interfaces_hmm_sim__msg__AgentPoses__Sequence * lhs, const interfaces_hmm_sim__msg__AgentPoses__Sequence * rhs);

/// Copy an array of msg/AgentPoses messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces_hmm_sim
bool
interfaces_hmm_sim__msg__AgentPoses__Sequence__copy(
  const interfaces_hmm_sim__msg__AgentPoses__Sequence * input,
  interfaces_hmm_sim__msg__AgentPoses__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // INTERFACES_HMM_SIM__MSG__DETAIL__AGENT_POSES__FUNCTIONS_H_
