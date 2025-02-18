// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from ltl_automaton_msgs:srv/TaskPlanning.idl
// generated code does not contain a copyright notice
#include "ltl_automaton_msgs/srv/detail/task_planning__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

// Include directives for member types
// Member `hard_task`
// Member `soft_task`
#include "rosidl_runtime_c/string_functions.h"

bool
ltl_automaton_msgs__srv__TaskPlanning_Request__init(ltl_automaton_msgs__srv__TaskPlanning_Request * msg)
{
  if (!msg) {
    return false;
  }
  // hard_task
  if (!rosidl_runtime_c__String__init(&msg->hard_task)) {
    ltl_automaton_msgs__srv__TaskPlanning_Request__fini(msg);
    return false;
  }
  // soft_task
  if (!rosidl_runtime_c__String__init(&msg->soft_task)) {
    ltl_automaton_msgs__srv__TaskPlanning_Request__fini(msg);
    return false;
  }
  return true;
}

void
ltl_automaton_msgs__srv__TaskPlanning_Request__fini(ltl_automaton_msgs__srv__TaskPlanning_Request * msg)
{
  if (!msg) {
    return;
  }
  // hard_task
  rosidl_runtime_c__String__fini(&msg->hard_task);
  // soft_task
  rosidl_runtime_c__String__fini(&msg->soft_task);
}

bool
ltl_automaton_msgs__srv__TaskPlanning_Request__are_equal(const ltl_automaton_msgs__srv__TaskPlanning_Request * lhs, const ltl_automaton_msgs__srv__TaskPlanning_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // hard_task
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->hard_task), &(rhs->hard_task)))
  {
    return false;
  }
  // soft_task
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->soft_task), &(rhs->soft_task)))
  {
    return false;
  }
  return true;
}

bool
ltl_automaton_msgs__srv__TaskPlanning_Request__copy(
  const ltl_automaton_msgs__srv__TaskPlanning_Request * input,
  ltl_automaton_msgs__srv__TaskPlanning_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // hard_task
  if (!rosidl_runtime_c__String__copy(
      &(input->hard_task), &(output->hard_task)))
  {
    return false;
  }
  // soft_task
  if (!rosidl_runtime_c__String__copy(
      &(input->soft_task), &(output->soft_task)))
  {
    return false;
  }
  return true;
}

ltl_automaton_msgs__srv__TaskPlanning_Request *
ltl_automaton_msgs__srv__TaskPlanning_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ltl_automaton_msgs__srv__TaskPlanning_Request * msg = (ltl_automaton_msgs__srv__TaskPlanning_Request *)allocator.allocate(sizeof(ltl_automaton_msgs__srv__TaskPlanning_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(ltl_automaton_msgs__srv__TaskPlanning_Request));
  bool success = ltl_automaton_msgs__srv__TaskPlanning_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
ltl_automaton_msgs__srv__TaskPlanning_Request__destroy(ltl_automaton_msgs__srv__TaskPlanning_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    ltl_automaton_msgs__srv__TaskPlanning_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
ltl_automaton_msgs__srv__TaskPlanning_Request__Sequence__init(ltl_automaton_msgs__srv__TaskPlanning_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ltl_automaton_msgs__srv__TaskPlanning_Request * data = NULL;

  if (size) {
    data = (ltl_automaton_msgs__srv__TaskPlanning_Request *)allocator.zero_allocate(size, sizeof(ltl_automaton_msgs__srv__TaskPlanning_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = ltl_automaton_msgs__srv__TaskPlanning_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        ltl_automaton_msgs__srv__TaskPlanning_Request__fini(&data[i - 1]);
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
ltl_automaton_msgs__srv__TaskPlanning_Request__Sequence__fini(ltl_automaton_msgs__srv__TaskPlanning_Request__Sequence * array)
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
      ltl_automaton_msgs__srv__TaskPlanning_Request__fini(&array->data[i]);
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

ltl_automaton_msgs__srv__TaskPlanning_Request__Sequence *
ltl_automaton_msgs__srv__TaskPlanning_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ltl_automaton_msgs__srv__TaskPlanning_Request__Sequence * array = (ltl_automaton_msgs__srv__TaskPlanning_Request__Sequence *)allocator.allocate(sizeof(ltl_automaton_msgs__srv__TaskPlanning_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = ltl_automaton_msgs__srv__TaskPlanning_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
ltl_automaton_msgs__srv__TaskPlanning_Request__Sequence__destroy(ltl_automaton_msgs__srv__TaskPlanning_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    ltl_automaton_msgs__srv__TaskPlanning_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
ltl_automaton_msgs__srv__TaskPlanning_Request__Sequence__are_equal(const ltl_automaton_msgs__srv__TaskPlanning_Request__Sequence * lhs, const ltl_automaton_msgs__srv__TaskPlanning_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!ltl_automaton_msgs__srv__TaskPlanning_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
ltl_automaton_msgs__srv__TaskPlanning_Request__Sequence__copy(
  const ltl_automaton_msgs__srv__TaskPlanning_Request__Sequence * input,
  ltl_automaton_msgs__srv__TaskPlanning_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(ltl_automaton_msgs__srv__TaskPlanning_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    ltl_automaton_msgs__srv__TaskPlanning_Request * data =
      (ltl_automaton_msgs__srv__TaskPlanning_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!ltl_automaton_msgs__srv__TaskPlanning_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          ltl_automaton_msgs__srv__TaskPlanning_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!ltl_automaton_msgs__srv__TaskPlanning_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


bool
ltl_automaton_msgs__srv__TaskPlanning_Response__init(ltl_automaton_msgs__srv__TaskPlanning_Response * msg)
{
  if (!msg) {
    return false;
  }
  // success
  return true;
}

void
ltl_automaton_msgs__srv__TaskPlanning_Response__fini(ltl_automaton_msgs__srv__TaskPlanning_Response * msg)
{
  if (!msg) {
    return;
  }
  // success
}

bool
ltl_automaton_msgs__srv__TaskPlanning_Response__are_equal(const ltl_automaton_msgs__srv__TaskPlanning_Response * lhs, const ltl_automaton_msgs__srv__TaskPlanning_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // success
  if (lhs->success != rhs->success) {
    return false;
  }
  return true;
}

bool
ltl_automaton_msgs__srv__TaskPlanning_Response__copy(
  const ltl_automaton_msgs__srv__TaskPlanning_Response * input,
  ltl_automaton_msgs__srv__TaskPlanning_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // success
  output->success = input->success;
  return true;
}

ltl_automaton_msgs__srv__TaskPlanning_Response *
ltl_automaton_msgs__srv__TaskPlanning_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ltl_automaton_msgs__srv__TaskPlanning_Response * msg = (ltl_automaton_msgs__srv__TaskPlanning_Response *)allocator.allocate(sizeof(ltl_automaton_msgs__srv__TaskPlanning_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(ltl_automaton_msgs__srv__TaskPlanning_Response));
  bool success = ltl_automaton_msgs__srv__TaskPlanning_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
ltl_automaton_msgs__srv__TaskPlanning_Response__destroy(ltl_automaton_msgs__srv__TaskPlanning_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    ltl_automaton_msgs__srv__TaskPlanning_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
ltl_automaton_msgs__srv__TaskPlanning_Response__Sequence__init(ltl_automaton_msgs__srv__TaskPlanning_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ltl_automaton_msgs__srv__TaskPlanning_Response * data = NULL;

  if (size) {
    data = (ltl_automaton_msgs__srv__TaskPlanning_Response *)allocator.zero_allocate(size, sizeof(ltl_automaton_msgs__srv__TaskPlanning_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = ltl_automaton_msgs__srv__TaskPlanning_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        ltl_automaton_msgs__srv__TaskPlanning_Response__fini(&data[i - 1]);
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
ltl_automaton_msgs__srv__TaskPlanning_Response__Sequence__fini(ltl_automaton_msgs__srv__TaskPlanning_Response__Sequence * array)
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
      ltl_automaton_msgs__srv__TaskPlanning_Response__fini(&array->data[i]);
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

ltl_automaton_msgs__srv__TaskPlanning_Response__Sequence *
ltl_automaton_msgs__srv__TaskPlanning_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ltl_automaton_msgs__srv__TaskPlanning_Response__Sequence * array = (ltl_automaton_msgs__srv__TaskPlanning_Response__Sequence *)allocator.allocate(sizeof(ltl_automaton_msgs__srv__TaskPlanning_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = ltl_automaton_msgs__srv__TaskPlanning_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
ltl_automaton_msgs__srv__TaskPlanning_Response__Sequence__destroy(ltl_automaton_msgs__srv__TaskPlanning_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    ltl_automaton_msgs__srv__TaskPlanning_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
ltl_automaton_msgs__srv__TaskPlanning_Response__Sequence__are_equal(const ltl_automaton_msgs__srv__TaskPlanning_Response__Sequence * lhs, const ltl_automaton_msgs__srv__TaskPlanning_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!ltl_automaton_msgs__srv__TaskPlanning_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
ltl_automaton_msgs__srv__TaskPlanning_Response__Sequence__copy(
  const ltl_automaton_msgs__srv__TaskPlanning_Response__Sequence * input,
  ltl_automaton_msgs__srv__TaskPlanning_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(ltl_automaton_msgs__srv__TaskPlanning_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    ltl_automaton_msgs__srv__TaskPlanning_Response * data =
      (ltl_automaton_msgs__srv__TaskPlanning_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!ltl_automaton_msgs__srv__TaskPlanning_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          ltl_automaton_msgs__srv__TaskPlanning_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!ltl_automaton_msgs__srv__TaskPlanning_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
