// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from ltl_automaton_msgs:msg/RelayResponse.idl
// generated code does not contain a copyright notice
#include "ltl_automaton_msgs/msg/detail/relay_response__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `new_plan_prefix`
// Member `new_plan_suffix`
#include "ltl_automaton_msgs/msg/detail/ltl_plan__functions.h"

bool
ltl_automaton_msgs__msg__RelayResponse__init(ltl_automaton_msgs__msg__RelayResponse * msg)
{
  if (!msg) {
    return false;
  }
  // success
  // new_plan_prefix
  if (!ltl_automaton_msgs__msg__LTLPlan__init(&msg->new_plan_prefix)) {
    ltl_automaton_msgs__msg__RelayResponse__fini(msg);
    return false;
  }
  // new_plan_suffix
  if (!ltl_automaton_msgs__msg__LTLPlan__init(&msg->new_plan_suffix)) {
    ltl_automaton_msgs__msg__RelayResponse__fini(msg);
    return false;
  }
  return true;
}

void
ltl_automaton_msgs__msg__RelayResponse__fini(ltl_automaton_msgs__msg__RelayResponse * msg)
{
  if (!msg) {
    return;
  }
  // success
  // new_plan_prefix
  ltl_automaton_msgs__msg__LTLPlan__fini(&msg->new_plan_prefix);
  // new_plan_suffix
  ltl_automaton_msgs__msg__LTLPlan__fini(&msg->new_plan_suffix);
}

bool
ltl_automaton_msgs__msg__RelayResponse__are_equal(const ltl_automaton_msgs__msg__RelayResponse * lhs, const ltl_automaton_msgs__msg__RelayResponse * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // success
  if (lhs->success != rhs->success) {
    return false;
  }
  // new_plan_prefix
  if (!ltl_automaton_msgs__msg__LTLPlan__are_equal(
      &(lhs->new_plan_prefix), &(rhs->new_plan_prefix)))
  {
    return false;
  }
  // new_plan_suffix
  if (!ltl_automaton_msgs__msg__LTLPlan__are_equal(
      &(lhs->new_plan_suffix), &(rhs->new_plan_suffix)))
  {
    return false;
  }
  return true;
}

bool
ltl_automaton_msgs__msg__RelayResponse__copy(
  const ltl_automaton_msgs__msg__RelayResponse * input,
  ltl_automaton_msgs__msg__RelayResponse * output)
{
  if (!input || !output) {
    return false;
  }
  // success
  output->success = input->success;
  // new_plan_prefix
  if (!ltl_automaton_msgs__msg__LTLPlan__copy(
      &(input->new_plan_prefix), &(output->new_plan_prefix)))
  {
    return false;
  }
  // new_plan_suffix
  if (!ltl_automaton_msgs__msg__LTLPlan__copy(
      &(input->new_plan_suffix), &(output->new_plan_suffix)))
  {
    return false;
  }
  return true;
}

ltl_automaton_msgs__msg__RelayResponse *
ltl_automaton_msgs__msg__RelayResponse__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ltl_automaton_msgs__msg__RelayResponse * msg = (ltl_automaton_msgs__msg__RelayResponse *)allocator.allocate(sizeof(ltl_automaton_msgs__msg__RelayResponse), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(ltl_automaton_msgs__msg__RelayResponse));
  bool success = ltl_automaton_msgs__msg__RelayResponse__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
ltl_automaton_msgs__msg__RelayResponse__destroy(ltl_automaton_msgs__msg__RelayResponse * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    ltl_automaton_msgs__msg__RelayResponse__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
ltl_automaton_msgs__msg__RelayResponse__Sequence__init(ltl_automaton_msgs__msg__RelayResponse__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ltl_automaton_msgs__msg__RelayResponse * data = NULL;

  if (size) {
    data = (ltl_automaton_msgs__msg__RelayResponse *)allocator.zero_allocate(size, sizeof(ltl_automaton_msgs__msg__RelayResponse), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = ltl_automaton_msgs__msg__RelayResponse__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        ltl_automaton_msgs__msg__RelayResponse__fini(&data[i - 1]);
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
ltl_automaton_msgs__msg__RelayResponse__Sequence__fini(ltl_automaton_msgs__msg__RelayResponse__Sequence * array)
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
      ltl_automaton_msgs__msg__RelayResponse__fini(&array->data[i]);
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

ltl_automaton_msgs__msg__RelayResponse__Sequence *
ltl_automaton_msgs__msg__RelayResponse__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ltl_automaton_msgs__msg__RelayResponse__Sequence * array = (ltl_automaton_msgs__msg__RelayResponse__Sequence *)allocator.allocate(sizeof(ltl_automaton_msgs__msg__RelayResponse__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = ltl_automaton_msgs__msg__RelayResponse__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
ltl_automaton_msgs__msg__RelayResponse__Sequence__destroy(ltl_automaton_msgs__msg__RelayResponse__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    ltl_automaton_msgs__msg__RelayResponse__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
ltl_automaton_msgs__msg__RelayResponse__Sequence__are_equal(const ltl_automaton_msgs__msg__RelayResponse__Sequence * lhs, const ltl_automaton_msgs__msg__RelayResponse__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!ltl_automaton_msgs__msg__RelayResponse__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
ltl_automaton_msgs__msg__RelayResponse__Sequence__copy(
  const ltl_automaton_msgs__msg__RelayResponse__Sequence * input,
  ltl_automaton_msgs__msg__RelayResponse__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(ltl_automaton_msgs__msg__RelayResponse);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    ltl_automaton_msgs__msg__RelayResponse * data =
      (ltl_automaton_msgs__msg__RelayResponse *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!ltl_automaton_msgs__msg__RelayResponse__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          ltl_automaton_msgs__msg__RelayResponse__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!ltl_automaton_msgs__msg__RelayResponse__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
