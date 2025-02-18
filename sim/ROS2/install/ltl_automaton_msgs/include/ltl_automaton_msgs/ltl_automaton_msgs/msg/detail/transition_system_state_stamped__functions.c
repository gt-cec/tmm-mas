// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from ltl_automaton_msgs:msg/TransitionSystemStateStamped.idl
// generated code does not contain a copyright notice
#include "ltl_automaton_msgs/msg/detail/transition_system_state_stamped__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"
// Member `ts_state`
#include "ltl_automaton_msgs/msg/detail/transition_system_state__functions.h"

bool
ltl_automaton_msgs__msg__TransitionSystemStateStamped__init(ltl_automaton_msgs__msg__TransitionSystemStateStamped * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    ltl_automaton_msgs__msg__TransitionSystemStateStamped__fini(msg);
    return false;
  }
  // ts_state
  if (!ltl_automaton_msgs__msg__TransitionSystemState__init(&msg->ts_state)) {
    ltl_automaton_msgs__msg__TransitionSystemStateStamped__fini(msg);
    return false;
  }
  return true;
}

void
ltl_automaton_msgs__msg__TransitionSystemStateStamped__fini(ltl_automaton_msgs__msg__TransitionSystemStateStamped * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // ts_state
  ltl_automaton_msgs__msg__TransitionSystemState__fini(&msg->ts_state);
}

bool
ltl_automaton_msgs__msg__TransitionSystemStateStamped__are_equal(const ltl_automaton_msgs__msg__TransitionSystemStateStamped * lhs, const ltl_automaton_msgs__msg__TransitionSystemStateStamped * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__are_equal(
      &(lhs->header), &(rhs->header)))
  {
    return false;
  }
  // ts_state
  if (!ltl_automaton_msgs__msg__TransitionSystemState__are_equal(
      &(lhs->ts_state), &(rhs->ts_state)))
  {
    return false;
  }
  return true;
}

bool
ltl_automaton_msgs__msg__TransitionSystemStateStamped__copy(
  const ltl_automaton_msgs__msg__TransitionSystemStateStamped * input,
  ltl_automaton_msgs__msg__TransitionSystemStateStamped * output)
{
  if (!input || !output) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__copy(
      &(input->header), &(output->header)))
  {
    return false;
  }
  // ts_state
  if (!ltl_automaton_msgs__msg__TransitionSystemState__copy(
      &(input->ts_state), &(output->ts_state)))
  {
    return false;
  }
  return true;
}

ltl_automaton_msgs__msg__TransitionSystemStateStamped *
ltl_automaton_msgs__msg__TransitionSystemStateStamped__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ltl_automaton_msgs__msg__TransitionSystemStateStamped * msg = (ltl_automaton_msgs__msg__TransitionSystemStateStamped *)allocator.allocate(sizeof(ltl_automaton_msgs__msg__TransitionSystemStateStamped), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(ltl_automaton_msgs__msg__TransitionSystemStateStamped));
  bool success = ltl_automaton_msgs__msg__TransitionSystemStateStamped__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
ltl_automaton_msgs__msg__TransitionSystemStateStamped__destroy(ltl_automaton_msgs__msg__TransitionSystemStateStamped * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    ltl_automaton_msgs__msg__TransitionSystemStateStamped__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
ltl_automaton_msgs__msg__TransitionSystemStateStamped__Sequence__init(ltl_automaton_msgs__msg__TransitionSystemStateStamped__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ltl_automaton_msgs__msg__TransitionSystemStateStamped * data = NULL;

  if (size) {
    data = (ltl_automaton_msgs__msg__TransitionSystemStateStamped *)allocator.zero_allocate(size, sizeof(ltl_automaton_msgs__msg__TransitionSystemStateStamped), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = ltl_automaton_msgs__msg__TransitionSystemStateStamped__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        ltl_automaton_msgs__msg__TransitionSystemStateStamped__fini(&data[i - 1]);
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
ltl_automaton_msgs__msg__TransitionSystemStateStamped__Sequence__fini(ltl_automaton_msgs__msg__TransitionSystemStateStamped__Sequence * array)
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
      ltl_automaton_msgs__msg__TransitionSystemStateStamped__fini(&array->data[i]);
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

ltl_automaton_msgs__msg__TransitionSystemStateStamped__Sequence *
ltl_automaton_msgs__msg__TransitionSystemStateStamped__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ltl_automaton_msgs__msg__TransitionSystemStateStamped__Sequence * array = (ltl_automaton_msgs__msg__TransitionSystemStateStamped__Sequence *)allocator.allocate(sizeof(ltl_automaton_msgs__msg__TransitionSystemStateStamped__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = ltl_automaton_msgs__msg__TransitionSystemStateStamped__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
ltl_automaton_msgs__msg__TransitionSystemStateStamped__Sequence__destroy(ltl_automaton_msgs__msg__TransitionSystemStateStamped__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    ltl_automaton_msgs__msg__TransitionSystemStateStamped__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
ltl_automaton_msgs__msg__TransitionSystemStateStamped__Sequence__are_equal(const ltl_automaton_msgs__msg__TransitionSystemStateStamped__Sequence * lhs, const ltl_automaton_msgs__msg__TransitionSystemStateStamped__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!ltl_automaton_msgs__msg__TransitionSystemStateStamped__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
ltl_automaton_msgs__msg__TransitionSystemStateStamped__Sequence__copy(
  const ltl_automaton_msgs__msg__TransitionSystemStateStamped__Sequence * input,
  ltl_automaton_msgs__msg__TransitionSystemStateStamped__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(ltl_automaton_msgs__msg__TransitionSystemStateStamped);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    ltl_automaton_msgs__msg__TransitionSystemStateStamped * data =
      (ltl_automaton_msgs__msg__TransitionSystemStateStamped *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!ltl_automaton_msgs__msg__TransitionSystemStateStamped__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          ltl_automaton_msgs__msg__TransitionSystemStateStamped__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!ltl_automaton_msgs__msg__TransitionSystemStateStamped__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
