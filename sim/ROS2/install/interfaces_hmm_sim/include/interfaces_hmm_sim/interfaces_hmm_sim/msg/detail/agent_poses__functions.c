// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from interfaces_hmm_sim:msg/AgentPoses.idl
// generated code does not contain a copyright notice
#include "interfaces_hmm_sim/msg/detail/agent_poses__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `agents`
// Member `x`
// Member `y`
// Member `z`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

bool
interfaces_hmm_sim__msg__AgentPoses__init(interfaces_hmm_sim__msg__AgentPoses * msg)
{
  if (!msg) {
    return false;
  }
  // agents
  if (!rosidl_runtime_c__int32__Sequence__init(&msg->agents, 0)) {
    interfaces_hmm_sim__msg__AgentPoses__fini(msg);
    return false;
  }
  // x
  if (!rosidl_runtime_c__float__Sequence__init(&msg->x, 0)) {
    interfaces_hmm_sim__msg__AgentPoses__fini(msg);
    return false;
  }
  // y
  if (!rosidl_runtime_c__float__Sequence__init(&msg->y, 0)) {
    interfaces_hmm_sim__msg__AgentPoses__fini(msg);
    return false;
  }
  // z
  if (!rosidl_runtime_c__float__Sequence__init(&msg->z, 0)) {
    interfaces_hmm_sim__msg__AgentPoses__fini(msg);
    return false;
  }
  return true;
}

void
interfaces_hmm_sim__msg__AgentPoses__fini(interfaces_hmm_sim__msg__AgentPoses * msg)
{
  if (!msg) {
    return;
  }
  // agents
  rosidl_runtime_c__int32__Sequence__fini(&msg->agents);
  // x
  rosidl_runtime_c__float__Sequence__fini(&msg->x);
  // y
  rosidl_runtime_c__float__Sequence__fini(&msg->y);
  // z
  rosidl_runtime_c__float__Sequence__fini(&msg->z);
}

bool
interfaces_hmm_sim__msg__AgentPoses__are_equal(const interfaces_hmm_sim__msg__AgentPoses * lhs, const interfaces_hmm_sim__msg__AgentPoses * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // agents
  if (!rosidl_runtime_c__int32__Sequence__are_equal(
      &(lhs->agents), &(rhs->agents)))
  {
    return false;
  }
  // x
  if (!rosidl_runtime_c__float__Sequence__are_equal(
      &(lhs->x), &(rhs->x)))
  {
    return false;
  }
  // y
  if (!rosidl_runtime_c__float__Sequence__are_equal(
      &(lhs->y), &(rhs->y)))
  {
    return false;
  }
  // z
  if (!rosidl_runtime_c__float__Sequence__are_equal(
      &(lhs->z), &(rhs->z)))
  {
    return false;
  }
  return true;
}

bool
interfaces_hmm_sim__msg__AgentPoses__copy(
  const interfaces_hmm_sim__msg__AgentPoses * input,
  interfaces_hmm_sim__msg__AgentPoses * output)
{
  if (!input || !output) {
    return false;
  }
  // agents
  if (!rosidl_runtime_c__int32__Sequence__copy(
      &(input->agents), &(output->agents)))
  {
    return false;
  }
  // x
  if (!rosidl_runtime_c__float__Sequence__copy(
      &(input->x), &(output->x)))
  {
    return false;
  }
  // y
  if (!rosidl_runtime_c__float__Sequence__copy(
      &(input->y), &(output->y)))
  {
    return false;
  }
  // z
  if (!rosidl_runtime_c__float__Sequence__copy(
      &(input->z), &(output->z)))
  {
    return false;
  }
  return true;
}

interfaces_hmm_sim__msg__AgentPoses *
interfaces_hmm_sim__msg__AgentPoses__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  interfaces_hmm_sim__msg__AgentPoses * msg = (interfaces_hmm_sim__msg__AgentPoses *)allocator.allocate(sizeof(interfaces_hmm_sim__msg__AgentPoses), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(interfaces_hmm_sim__msg__AgentPoses));
  bool success = interfaces_hmm_sim__msg__AgentPoses__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
interfaces_hmm_sim__msg__AgentPoses__destroy(interfaces_hmm_sim__msg__AgentPoses * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    interfaces_hmm_sim__msg__AgentPoses__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
interfaces_hmm_sim__msg__AgentPoses__Sequence__init(interfaces_hmm_sim__msg__AgentPoses__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  interfaces_hmm_sim__msg__AgentPoses * data = NULL;

  if (size) {
    data = (interfaces_hmm_sim__msg__AgentPoses *)allocator.zero_allocate(size, sizeof(interfaces_hmm_sim__msg__AgentPoses), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = interfaces_hmm_sim__msg__AgentPoses__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        interfaces_hmm_sim__msg__AgentPoses__fini(&data[i - 1]);
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
interfaces_hmm_sim__msg__AgentPoses__Sequence__fini(interfaces_hmm_sim__msg__AgentPoses__Sequence * array)
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
      interfaces_hmm_sim__msg__AgentPoses__fini(&array->data[i]);
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

interfaces_hmm_sim__msg__AgentPoses__Sequence *
interfaces_hmm_sim__msg__AgentPoses__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  interfaces_hmm_sim__msg__AgentPoses__Sequence * array = (interfaces_hmm_sim__msg__AgentPoses__Sequence *)allocator.allocate(sizeof(interfaces_hmm_sim__msg__AgentPoses__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = interfaces_hmm_sim__msg__AgentPoses__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
interfaces_hmm_sim__msg__AgentPoses__Sequence__destroy(interfaces_hmm_sim__msg__AgentPoses__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    interfaces_hmm_sim__msg__AgentPoses__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
interfaces_hmm_sim__msg__AgentPoses__Sequence__are_equal(const interfaces_hmm_sim__msg__AgentPoses__Sequence * lhs, const interfaces_hmm_sim__msg__AgentPoses__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!interfaces_hmm_sim__msg__AgentPoses__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
interfaces_hmm_sim__msg__AgentPoses__Sequence__copy(
  const interfaces_hmm_sim__msg__AgentPoses__Sequence * input,
  interfaces_hmm_sim__msg__AgentPoses__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(interfaces_hmm_sim__msg__AgentPoses);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    interfaces_hmm_sim__msg__AgentPoses * data =
      (interfaces_hmm_sim__msg__AgentPoses *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!interfaces_hmm_sim__msg__AgentPoses__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          interfaces_hmm_sim__msg__AgentPoses__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!interfaces_hmm_sim__msg__AgentPoses__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
