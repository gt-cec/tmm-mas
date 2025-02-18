// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from ltl_automaton_msgs:msg/RelayRequest.idl
// generated code does not contain a copyright notice
#include "ltl_automaton_msgs/msg/detail/relay_request__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `from_pose`
// Member `to_pose`
#include "rosidl_runtime_c/primitives_sequence_functions.h"
// Member `current_state`
#include "ltl_automaton_msgs/msg/detail/transition_system_state__functions.h"
// Member `type`
#include "rosidl_runtime_c/string_functions.h"

bool
ltl_automaton_msgs__msg__RelayRequest__init(ltl_automaton_msgs__msg__RelayRequest * msg)
{
  if (!msg) {
    return false;
  }
  // from_pose
  if (!rosidl_runtime_c__int32__Sequence__init(&msg->from_pose, 0)) {
    ltl_automaton_msgs__msg__RelayRequest__fini(msg);
    return false;
  }
  // to_pose
  if (!rosidl_runtime_c__int32__Sequence__init(&msg->to_pose, 0)) {
    ltl_automaton_msgs__msg__RelayRequest__fini(msg);
    return false;
  }
  // cost
  // current_state
  if (!ltl_automaton_msgs__msg__TransitionSystemState__init(&msg->current_state)) {
    ltl_automaton_msgs__msg__RelayRequest__fini(msg);
    return false;
  }
  // exec_index
  // type
  if (!rosidl_runtime_c__String__init(&msg->type)) {
    ltl_automaton_msgs__msg__RelayRequest__fini(msg);
    return false;
  }
  return true;
}

void
ltl_automaton_msgs__msg__RelayRequest__fini(ltl_automaton_msgs__msg__RelayRequest * msg)
{
  if (!msg) {
    return;
  }
  // from_pose
  rosidl_runtime_c__int32__Sequence__fini(&msg->from_pose);
  // to_pose
  rosidl_runtime_c__int32__Sequence__fini(&msg->to_pose);
  // cost
  // current_state
  ltl_automaton_msgs__msg__TransitionSystemState__fini(&msg->current_state);
  // exec_index
  // type
  rosidl_runtime_c__String__fini(&msg->type);
}

bool
ltl_automaton_msgs__msg__RelayRequest__are_equal(const ltl_automaton_msgs__msg__RelayRequest * lhs, const ltl_automaton_msgs__msg__RelayRequest * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // from_pose
  if (!rosidl_runtime_c__int32__Sequence__are_equal(
      &(lhs->from_pose), &(rhs->from_pose)))
  {
    return false;
  }
  // to_pose
  if (!rosidl_runtime_c__int32__Sequence__are_equal(
      &(lhs->to_pose), &(rhs->to_pose)))
  {
    return false;
  }
  // cost
  if (lhs->cost != rhs->cost) {
    return false;
  }
  // current_state
  if (!ltl_automaton_msgs__msg__TransitionSystemState__are_equal(
      &(lhs->current_state), &(rhs->current_state)))
  {
    return false;
  }
  // exec_index
  if (lhs->exec_index != rhs->exec_index) {
    return false;
  }
  // type
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->type), &(rhs->type)))
  {
    return false;
  }
  return true;
}

bool
ltl_automaton_msgs__msg__RelayRequest__copy(
  const ltl_automaton_msgs__msg__RelayRequest * input,
  ltl_automaton_msgs__msg__RelayRequest * output)
{
  if (!input || !output) {
    return false;
  }
  // from_pose
  if (!rosidl_runtime_c__int32__Sequence__copy(
      &(input->from_pose), &(output->from_pose)))
  {
    return false;
  }
  // to_pose
  if (!rosidl_runtime_c__int32__Sequence__copy(
      &(input->to_pose), &(output->to_pose)))
  {
    return false;
  }
  // cost
  output->cost = input->cost;
  // current_state
  if (!ltl_automaton_msgs__msg__TransitionSystemState__copy(
      &(input->current_state), &(output->current_state)))
  {
    return false;
  }
  // exec_index
  output->exec_index = input->exec_index;
  // type
  if (!rosidl_runtime_c__String__copy(
      &(input->type), &(output->type)))
  {
    return false;
  }
  return true;
}

ltl_automaton_msgs__msg__RelayRequest *
ltl_automaton_msgs__msg__RelayRequest__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ltl_automaton_msgs__msg__RelayRequest * msg = (ltl_automaton_msgs__msg__RelayRequest *)allocator.allocate(sizeof(ltl_automaton_msgs__msg__RelayRequest), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(ltl_automaton_msgs__msg__RelayRequest));
  bool success = ltl_automaton_msgs__msg__RelayRequest__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
ltl_automaton_msgs__msg__RelayRequest__destroy(ltl_automaton_msgs__msg__RelayRequest * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    ltl_automaton_msgs__msg__RelayRequest__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
ltl_automaton_msgs__msg__RelayRequest__Sequence__init(ltl_automaton_msgs__msg__RelayRequest__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ltl_automaton_msgs__msg__RelayRequest * data = NULL;

  if (size) {
    data = (ltl_automaton_msgs__msg__RelayRequest *)allocator.zero_allocate(size, sizeof(ltl_automaton_msgs__msg__RelayRequest), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = ltl_automaton_msgs__msg__RelayRequest__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        ltl_automaton_msgs__msg__RelayRequest__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
ltl_automaton_msgs__msg__RelayRequest__Sequence__fini(ltl_automaton_msgs__msg__RelayRequest__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      ltl_automaton_msgs__msg__RelayRequest__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

ltl_automaton_msgs__msg__RelayRequest__Sequence *
ltl_automaton_msgs__msg__RelayRequest__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ltl_automaton_msgs__msg__RelayRequest__Sequence * array = (ltl_automaton_msgs__msg__RelayRequest__Sequence *)allocator.allocate(sizeof(ltl_automaton_msgs__msg__RelayRequest__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = ltl_automaton_msgs__msg__RelayRequest__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
ltl_automaton_msgs__msg__RelayRequest__Sequence__destroy(ltl_automaton_msgs__msg__RelayRequest__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    ltl_automaton_msgs__msg__RelayRequest__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
ltl_automaton_msgs__msg__RelayRequest__Sequence__are_equal(const ltl_automaton_msgs__msg__RelayRequest__Sequence * lhs, const ltl_automaton_msgs__msg__RelayRequest__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!ltl_automaton_msgs__msg__RelayRequest__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
ltl_automaton_msgs__msg__RelayRequest__Sequence__copy(
  const ltl_automaton_msgs__msg__RelayRequest__Sequence * input,
  ltl_automaton_msgs__msg__RelayRequest__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(ltl_automaton_msgs__msg__RelayRequest);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    ltl_automaton_msgs__msg__RelayRequest * data =
      (ltl_automaton_msgs__msg__RelayRequest *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!ltl_automaton_msgs__msg__RelayRequest__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          ltl_automaton_msgs__msg__RelayRequest__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!ltl_automaton_msgs__msg__RelayRequest__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
