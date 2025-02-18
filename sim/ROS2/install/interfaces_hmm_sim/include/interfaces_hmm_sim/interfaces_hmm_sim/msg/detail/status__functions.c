// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from interfaces_hmm_sim:msg/Status.idl
// generated code does not contain a copyright notice
#include "interfaces_hmm_sim/msg/detail/status__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `agent`
#include "rosidl_runtime_c/string_functions.h"

bool
interfaces_hmm_sim__msg__Status__init(interfaces_hmm_sim__msg__Status * msg)
{
  if (!msg) {
    return false;
  }
  // agent
  if (!rosidl_runtime_c__String__init(&msg->agent)) {
    interfaces_hmm_sim__msg__Status__fini(msg);
    return false;
  }
  // start
  // arrived
  // replan_received
  return true;
}

void
interfaces_hmm_sim__msg__Status__fini(interfaces_hmm_sim__msg__Status * msg)
{
  if (!msg) {
    return;
  }
  // agent
  rosidl_runtime_c__String__fini(&msg->agent);
  // start
  // arrived
  // replan_received
}

bool
interfaces_hmm_sim__msg__Status__are_equal(const interfaces_hmm_sim__msg__Status * lhs, const interfaces_hmm_sim__msg__Status * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // agent
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->agent), &(rhs->agent)))
  {
    return false;
  }
  // start
  if (lhs->start != rhs->start) {
    return false;
  }
  // arrived
  if (lhs->arrived != rhs->arrived) {
    return false;
  }
  // replan_received
  if (lhs->replan_received != rhs->replan_received) {
    return false;
  }
  return true;
}

bool
interfaces_hmm_sim__msg__Status__copy(
  const interfaces_hmm_sim__msg__Status * input,
  interfaces_hmm_sim__msg__Status * output)
{
  if (!input || !output) {
    return false;
  }
  // agent
  if (!rosidl_runtime_c__String__copy(
      &(input->agent), &(output->agent)))
  {
    return false;
  }
  // start
  output->start = input->start;
  // arrived
  output->arrived = input->arrived;
  // replan_received
  output->replan_received = input->replan_received;
  return true;
}

interfaces_hmm_sim__msg__Status *
interfaces_hmm_sim__msg__Status__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  interfaces_hmm_sim__msg__Status * msg = (interfaces_hmm_sim__msg__Status *)allocator.allocate(sizeof(interfaces_hmm_sim__msg__Status), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(interfaces_hmm_sim__msg__Status));
  bool success = interfaces_hmm_sim__msg__Status__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
interfaces_hmm_sim__msg__Status__destroy(interfaces_hmm_sim__msg__Status * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    interfaces_hmm_sim__msg__Status__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
interfaces_hmm_sim__msg__Status__Sequence__init(interfaces_hmm_sim__msg__Status__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  interfaces_hmm_sim__msg__Status * data = NULL;

  if (size) {
    data = (interfaces_hmm_sim__msg__Status *)allocator.zero_allocate(size, sizeof(interfaces_hmm_sim__msg__Status), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = interfaces_hmm_sim__msg__Status__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        interfaces_hmm_sim__msg__Status__fini(&data[i - 1]);
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
interfaces_hmm_sim__msg__Status__Sequence__fini(interfaces_hmm_sim__msg__Status__Sequence * array)
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
      interfaces_hmm_sim__msg__Status__fini(&array->data[i]);
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

interfaces_hmm_sim__msg__Status__Sequence *
interfaces_hmm_sim__msg__Status__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  interfaces_hmm_sim__msg__Status__Sequence * array = (interfaces_hmm_sim__msg__Status__Sequence *)allocator.allocate(sizeof(interfaces_hmm_sim__msg__Status__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = interfaces_hmm_sim__msg__Status__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
interfaces_hmm_sim__msg__Status__Sequence__destroy(interfaces_hmm_sim__msg__Status__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    interfaces_hmm_sim__msg__Status__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
interfaces_hmm_sim__msg__Status__Sequence__are_equal(const interfaces_hmm_sim__msg__Status__Sequence * lhs, const interfaces_hmm_sim__msg__Status__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!interfaces_hmm_sim__msg__Status__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
interfaces_hmm_sim__msg__Status__Sequence__copy(
  const interfaces_hmm_sim__msg__Status__Sequence * input,
  interfaces_hmm_sim__msg__Status__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(interfaces_hmm_sim__msg__Status);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    interfaces_hmm_sim__msg__Status * data =
      (interfaces_hmm_sim__msg__Status *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!interfaces_hmm_sim__msg__Status__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          interfaces_hmm_sim__msg__Status__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!interfaces_hmm_sim__msg__Status__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
