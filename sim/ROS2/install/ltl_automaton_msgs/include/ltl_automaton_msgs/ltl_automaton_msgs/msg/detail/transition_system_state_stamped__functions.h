// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from ltl_automaton_msgs:msg/TransitionSystemStateStamped.idl
// generated code does not contain a copyright notice

#ifndef LTL_AUTOMATON_MSGS__MSG__DETAIL__TRANSITION_SYSTEM_STATE_STAMPED__FUNCTIONS_H_
#define LTL_AUTOMATON_MSGS__MSG__DETAIL__TRANSITION_SYSTEM_STATE_STAMPED__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "ltl_automaton_msgs/msg/rosidl_generator_c__visibility_control.h"

#include "ltl_automaton_msgs/msg/detail/transition_system_state_stamped__struct.h"

/// Initialize msg/TransitionSystemStateStamped message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * ltl_automaton_msgs__msg__TransitionSystemStateStamped
 * )) before or use
 * ltl_automaton_msgs__msg__TransitionSystemStateStamped__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_ltl_automaton_msgs
bool
ltl_automaton_msgs__msg__TransitionSystemStateStamped__init(ltl_automaton_msgs__msg__TransitionSystemStateStamped * msg);

/// Finalize msg/TransitionSystemStateStamped message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_ltl_automaton_msgs
void
ltl_automaton_msgs__msg__TransitionSystemStateStamped__fini(ltl_automaton_msgs__msg__TransitionSystemStateStamped * msg);

/// Create msg/TransitionSystemStateStamped message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * ltl_automaton_msgs__msg__TransitionSystemStateStamped__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_ltl_automaton_msgs
ltl_automaton_msgs__msg__TransitionSystemStateStamped *
ltl_automaton_msgs__msg__TransitionSystemStateStamped__create();

/// Destroy msg/TransitionSystemStateStamped message.
/**
 * It calls
 * ltl_automaton_msgs__msg__TransitionSystemStateStamped__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_ltl_automaton_msgs
void
ltl_automaton_msgs__msg__TransitionSystemStateStamped__destroy(ltl_automaton_msgs__msg__TransitionSystemStateStamped * msg);

/// Check for msg/TransitionSystemStateStamped message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_ltl_automaton_msgs
bool
ltl_automaton_msgs__msg__TransitionSystemStateStamped__are_equal(const ltl_automaton_msgs__msg__TransitionSystemStateStamped * lhs, const ltl_automaton_msgs__msg__TransitionSystemStateStamped * rhs);

/// Copy a msg/TransitionSystemStateStamped message.
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
ROSIDL_GENERATOR_C_PUBLIC_ltl_automaton_msgs
bool
ltl_automaton_msgs__msg__TransitionSystemStateStamped__copy(
  const ltl_automaton_msgs__msg__TransitionSystemStateStamped * input,
  ltl_automaton_msgs__msg__TransitionSystemStateStamped * output);

/// Initialize array of msg/TransitionSystemStateStamped messages.
/**
 * It allocates the memory for the number of elements and calls
 * ltl_automaton_msgs__msg__TransitionSystemStateStamped__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_ltl_automaton_msgs
bool
ltl_automaton_msgs__msg__TransitionSystemStateStamped__Sequence__init(ltl_automaton_msgs__msg__TransitionSystemStateStamped__Sequence * array, size_t size);

/// Finalize array of msg/TransitionSystemStateStamped messages.
/**
 * It calls
 * ltl_automaton_msgs__msg__TransitionSystemStateStamped__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_ltl_automaton_msgs
void
ltl_automaton_msgs__msg__TransitionSystemStateStamped__Sequence__fini(ltl_automaton_msgs__msg__TransitionSystemStateStamped__Sequence * array);

/// Create array of msg/TransitionSystemStateStamped messages.
/**
 * It allocates the memory for the array and calls
 * ltl_automaton_msgs__msg__TransitionSystemStateStamped__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_ltl_automaton_msgs
ltl_automaton_msgs__msg__TransitionSystemStateStamped__Sequence *
ltl_automaton_msgs__msg__TransitionSystemStateStamped__Sequence__create(size_t size);

/// Destroy array of msg/TransitionSystemStateStamped messages.
/**
 * It calls
 * ltl_automaton_msgs__msg__TransitionSystemStateStamped__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_ltl_automaton_msgs
void
ltl_automaton_msgs__msg__TransitionSystemStateStamped__Sequence__destroy(ltl_automaton_msgs__msg__TransitionSystemStateStamped__Sequence * array);

/// Check for msg/TransitionSystemStateStamped message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_ltl_automaton_msgs
bool
ltl_automaton_msgs__msg__TransitionSystemStateStamped__Sequence__are_equal(const ltl_automaton_msgs__msg__TransitionSystemStateStamped__Sequence * lhs, const ltl_automaton_msgs__msg__TransitionSystemStateStamped__Sequence * rhs);

/// Copy an array of msg/TransitionSystemStateStamped messages.
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
ROSIDL_GENERATOR_C_PUBLIC_ltl_automaton_msgs
bool
ltl_automaton_msgs__msg__TransitionSystemStateStamped__Sequence__copy(
  const ltl_automaton_msgs__msg__TransitionSystemStateStamped__Sequence * input,
  ltl_automaton_msgs__msg__TransitionSystemStateStamped__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // LTL_AUTOMATON_MSGS__MSG__DETAIL__TRANSITION_SYSTEM_STATE_STAMPED__FUNCTIONS_H_
