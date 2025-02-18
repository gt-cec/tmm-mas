// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from ltl_automaton_msgs:msg/LTLStateArray.idl
// generated code does not contain a copyright notice
#include "ltl_automaton_msgs/msg/detail/ltl_state_array__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `ltl_states`
#include "ltl_automaton_msgs/msg/detail/ltl_state__functions.h"

bool
ltl_automaton_msgs__msg__LTLStateArray__init(ltl_automaton_msgs__msg__LTLStateArray * msg)
{
  if (!msg) {
    return false;
  }
  // ltl_states
  if (!ltl_automaton_msgs__msg__LTLState__Sequence__init(&msg->ltl_states, 0)) {
    ltl_automaton_msgs__msg__LTLStateArray__fini(msg);
    return false;
  }
  return true;
}

void
ltl_automaton_msgs__msg__LTLStateArray__fini(ltl_automaton_msgs__msg__LTLStateArray * msg)
{
  if (!msg) {
    return;
  }
  // ltl_states
  ltl_automaton_msgs__msg__LTLState__Sequence__fini(&msg->ltl_states);
}

bool
ltl_automaton_msgs__msg__LTLStateArray__are_equal(const ltl_automaton_msgs__msg__LTLStateArray * lhs, const ltl_automaton_msgs__msg__LTLStateArray * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // ltl_states
  if (!ltl_automaton_msgs__msg__LTLState__Sequence__are_equal(
      &(lhs->ltl_states), &(rhs->ltl_states)))
  {
    return false;
  }
  return true;
}

bool
ltl_automaton_msgs__msg__LTLStateArray__copy(
  const ltl_automaton_msgs__msg__LTLStateArray * input,
  ltl_automaton_msgs__msg__LTLStateArray * output)
{
  if (!input || !output) {
    return false;
  }
  // ltl_states
  if (!ltl_automaton_msgs__msg__LTLState__Sequence__copy(
      &(input->ltl_states), &(output->ltl_states)))
  {
    return false;
  }
  return true;
}

ltl_automaton_msgs__msg__LTLStateArray *
ltl_automaton_msgs__msg__LTLStateArray__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ltl_automaton_msgs__msg__LTLStateArray * msg = (ltl_automaton_msgs__msg__LTLStateArray *)allocator.allocate(sizeof(ltl_automaton_msgs__msg__LTLStateArray), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(ltl_automaton_msgs__msg__LTLStateArray));
  bool success = ltl_automaton_msgs__msg__LTLStateArray__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
ltl_automaton_msgs__msg__LTLStateArray__destroy(ltl_automaton_msgs__msg__LTLStateArray * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    ltl_automaton_msgs__msg__LTLStateArray__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
ltl_automaton_msgs__msg__LTLStateArray__Sequence__init(ltl_automaton_msgs__msg__LTLStateArray__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ltl_automaton_msgs__msg__LTLStateArray * data = NULL;

  if (size) {
    data = (ltl_automaton_msgs__msg__LTLStateArray *)allocator.zero_allocate(size, sizeof(ltl_automaton_msgs__msg__LTLStateArray), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = ltl_automaton_msgs__msg__LTLStateArray__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        ltl_automaton_msgs__msg__LTLStateArray__fini(&data[i - 1]);
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
ltl_automaton_msgs__msg__LTLStateArray__Sequence__fini(ltl_automaton_msgs__msg__LTLStateArray__Sequence * array)
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
      ltl_automaton_msgs__msg__LTLStateArray__fini(&array->data[i]);
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

ltl_automaton_msgs__msg__LTLStateArray__Sequence *
ltl_automaton_msgs__msg__LTLStateArray__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ltl_automaton_msgs__msg__LTLStateArray__Sequence * array = (ltl_automaton_msgs__msg__LTLStateArray__Sequence *)allocator.allocate(sizeof(ltl_automaton_msgs__msg__LTLStateArray__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = ltl_automaton_msgs__msg__LTLStateArray__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
ltl_automaton_msgs__msg__LTLStateArray__Sequence__destroy(ltl_automaton_msgs__msg__LTLStateArray__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    ltl_automaton_msgs__msg__LTLStateArray__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
ltl_automaton_msgs__msg__LTLStateArray__Sequence__are_equal(const ltl_automaton_msgs__msg__LTLStateArray__Sequence * lhs, const ltl_automaton_msgs__msg__LTLStateArray__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!ltl_automaton_msgs__msg__LTLStateArray__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
ltl_automaton_msgs__msg__LTLStateArray__Sequence__copy(
  const ltl_automaton_msgs__msg__LTLStateArray__Sequence * input,
  ltl_automaton_msgs__msg__LTLStateArray__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(ltl_automaton_msgs__msg__LTLStateArray);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    ltl_automaton_msgs__msg__LTLStateArray * data =
      (ltl_automaton_msgs__msg__LTLStateArray *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!ltl_automaton_msgs__msg__LTLStateArray__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          ltl_automaton_msgs__msg__LTLStateArray__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!ltl_automaton_msgs__msg__LTLStateArray__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
