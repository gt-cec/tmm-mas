// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from ltl_automaton_msgs:srv/TaskReplanningRelabel.idl
// generated code does not contain a copyright notice
#include "ltl_automaton_msgs/srv/detail/task_replanning_relabel__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

// Include directives for member types
// Member `state`
// Member `label`
#include "rosidl_runtime_c/string_functions.h"
// Member `current_state`
#include "ltl_automaton_msgs/msg/detail/transition_system_state__functions.h"

bool
ltl_automaton_msgs__srv__TaskReplanningRelabel_Request__init(ltl_automaton_msgs__srv__TaskReplanningRelabel_Request * msg)
{
  if (!msg) {
    return false;
  }
  // state
  if (!rosidl_runtime_c__String__Sequence__init(&msg->state, 0)) {
    ltl_automaton_msgs__srv__TaskReplanningRelabel_Request__fini(msg);
    return false;
  }
  // label
  if (!rosidl_runtime_c__String__Sequence__init(&msg->label, 0)) {
    ltl_automaton_msgs__srv__TaskReplanningRelabel_Request__fini(msg);
    return false;
  }
  // current_state
  if (!ltl_automaton_msgs__msg__TransitionSystemState__init(&msg->current_state)) {
    ltl_automaton_msgs__srv__TaskReplanningRelabel_Request__fini(msg);
    return false;
  }
  return true;
}

void
ltl_automaton_msgs__srv__TaskReplanningRelabel_Request__fini(ltl_automaton_msgs__srv__TaskReplanningRelabel_Request * msg)
{
  if (!msg) {
    return;
  }
  // state
  rosidl_runtime_c__String__Sequence__fini(&msg->state);
  // label
  rosidl_runtime_c__String__Sequence__fini(&msg->label);
  // current_state
  ltl_automaton_msgs__msg__TransitionSystemState__fini(&msg->current_state);
}

bool
ltl_automaton_msgs__srv__TaskReplanningRelabel_Request__are_equal(const ltl_automaton_msgs__srv__TaskReplanningRelabel_Request * lhs, const ltl_automaton_msgs__srv__TaskReplanningRelabel_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // state
  if (!rosidl_runtime_c__String__Sequence__are_equal(
      &(lhs->state), &(rhs->state)))
  {
    return false;
  }
  // label
  if (!rosidl_runtime_c__String__Sequence__are_equal(
      &(lhs->label), &(rhs->label)))
  {
    return false;
  }
  // current_state
  if (!ltl_automaton_msgs__msg__TransitionSystemState__are_equal(
      &(lhs->current_state), &(rhs->current_state)))
  {
    return false;
  }
  return true;
}

bool
ltl_automaton_msgs__srv__TaskReplanningRelabel_Request__copy(
  const ltl_automaton_msgs__srv__TaskReplanningRelabel_Request * input,
  ltl_automaton_msgs__srv__TaskReplanningRelabel_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // state
  if (!rosidl_runtime_c__String__Sequence__copy(
      &(input->state), &(output->state)))
  {
    return false;
  }
  // label
  if (!rosidl_runtime_c__String__Sequence__copy(
      &(input->label), &(output->label)))
  {
    return false;
  }
  // current_state
  if (!ltl_automaton_msgs__msg__TransitionSystemState__copy(
      &(input->current_state), &(output->current_state)))
  {
    return false;
  }
  return true;
}

ltl_automaton_msgs__srv__TaskReplanningRelabel_Request *
ltl_automaton_msgs__srv__TaskReplanningRelabel_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ltl_automaton_msgs__srv__TaskReplanningRelabel_Request * msg = (ltl_automaton_msgs__srv__TaskReplanningRelabel_Request *)allocator.allocate(sizeof(ltl_automaton_msgs__srv__TaskReplanningRelabel_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(ltl_automaton_msgs__srv__TaskReplanningRelabel_Request));
  bool success = ltl_automaton_msgs__srv__TaskReplanningRelabel_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
ltl_automaton_msgs__srv__TaskReplanningRelabel_Request__destroy(ltl_automaton_msgs__srv__TaskReplanningRelabel_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    ltl_automaton_msgs__srv__TaskReplanningRelabel_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
ltl_automaton_msgs__srv__TaskReplanningRelabel_Request__Sequence__init(ltl_automaton_msgs__srv__TaskReplanningRelabel_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ltl_automaton_msgs__srv__TaskReplanningRelabel_Request * data = NULL;

  if (size) {
    data = (ltl_automaton_msgs__srv__TaskReplanningRelabel_Request *)allocator.zero_allocate(size, sizeof(ltl_automaton_msgs__srv__TaskReplanningRelabel_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = ltl_automaton_msgs__srv__TaskReplanningRelabel_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        ltl_automaton_msgs__srv__TaskReplanningRelabel_Request__fini(&data[i - 1]);
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
ltl_automaton_msgs__srv__TaskReplanningRelabel_Request__Sequence__fini(ltl_automaton_msgs__srv__TaskReplanningRelabel_Request__Sequence * array)
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
      ltl_automaton_msgs__srv__TaskReplanningRelabel_Request__fini(&array->data[i]);
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

ltl_automaton_msgs__srv__TaskReplanningRelabel_Request__Sequence *
ltl_automaton_msgs__srv__TaskReplanningRelabel_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ltl_automaton_msgs__srv__TaskReplanningRelabel_Request__Sequence * array = (ltl_automaton_msgs__srv__TaskReplanningRelabel_Request__Sequence *)allocator.allocate(sizeof(ltl_automaton_msgs__srv__TaskReplanningRelabel_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = ltl_automaton_msgs__srv__TaskReplanningRelabel_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
ltl_automaton_msgs__srv__TaskReplanningRelabel_Request__Sequence__destroy(ltl_automaton_msgs__srv__TaskReplanningRelabel_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    ltl_automaton_msgs__srv__TaskReplanningRelabel_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
ltl_automaton_msgs__srv__TaskReplanningRelabel_Request__Sequence__are_equal(const ltl_automaton_msgs__srv__TaskReplanningRelabel_Request__Sequence * lhs, const ltl_automaton_msgs__srv__TaskReplanningRelabel_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!ltl_automaton_msgs__srv__TaskReplanningRelabel_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
ltl_automaton_msgs__srv__TaskReplanningRelabel_Request__Sequence__copy(
  const ltl_automaton_msgs__srv__TaskReplanningRelabel_Request__Sequence * input,
  ltl_automaton_msgs__srv__TaskReplanningRelabel_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(ltl_automaton_msgs__srv__TaskReplanningRelabel_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    ltl_automaton_msgs__srv__TaskReplanningRelabel_Request * data =
      (ltl_automaton_msgs__srv__TaskReplanningRelabel_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!ltl_automaton_msgs__srv__TaskReplanningRelabel_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          ltl_automaton_msgs__srv__TaskReplanningRelabel_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!ltl_automaton_msgs__srv__TaskReplanningRelabel_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `new_plan`
#include "ltl_automaton_msgs/msg/detail/ltl_plan__functions.h"

bool
ltl_automaton_msgs__srv__TaskReplanningRelabel_Response__init(ltl_automaton_msgs__srv__TaskReplanningRelabel_Response * msg)
{
  if (!msg) {
    return false;
  }
  // success
  // new_plan
  if (!ltl_automaton_msgs__msg__LTLPlan__init(&msg->new_plan)) {
    ltl_automaton_msgs__srv__TaskReplanningRelabel_Response__fini(msg);
    return false;
  }
  return true;
}

void
ltl_automaton_msgs__srv__TaskReplanningRelabel_Response__fini(ltl_automaton_msgs__srv__TaskReplanningRelabel_Response * msg)
{
  if (!msg) {
    return;
  }
  // success
  // new_plan
  ltl_automaton_msgs__msg__LTLPlan__fini(&msg->new_plan);
}

bool
ltl_automaton_msgs__srv__TaskReplanningRelabel_Response__are_equal(const ltl_automaton_msgs__srv__TaskReplanningRelabel_Response * lhs, const ltl_automaton_msgs__srv__TaskReplanningRelabel_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // success
  if (lhs->success != rhs->success) {
    return false;
  }
  // new_plan
  if (!ltl_automaton_msgs__msg__LTLPlan__are_equal(
      &(lhs->new_plan), &(rhs->new_plan)))
  {
    return false;
  }
  return true;
}

bool
ltl_automaton_msgs__srv__TaskReplanningRelabel_Response__copy(
  const ltl_automaton_msgs__srv__TaskReplanningRelabel_Response * input,
  ltl_automaton_msgs__srv__TaskReplanningRelabel_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // success
  output->success = input->success;
  // new_plan
  if (!ltl_automaton_msgs__msg__LTLPlan__copy(
      &(input->new_plan), &(output->new_plan)))
  {
    return false;
  }
  return true;
}

ltl_automaton_msgs__srv__TaskReplanningRelabel_Response *
ltl_automaton_msgs__srv__TaskReplanningRelabel_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ltl_automaton_msgs__srv__TaskReplanningRelabel_Response * msg = (ltl_automaton_msgs__srv__TaskReplanningRelabel_Response *)allocator.allocate(sizeof(ltl_automaton_msgs__srv__TaskReplanningRelabel_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(ltl_automaton_msgs__srv__TaskReplanningRelabel_Response));
  bool success = ltl_automaton_msgs__srv__TaskReplanningRelabel_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
ltl_automaton_msgs__srv__TaskReplanningRelabel_Response__destroy(ltl_automaton_msgs__srv__TaskReplanningRelabel_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    ltl_automaton_msgs__srv__TaskReplanningRelabel_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
ltl_automaton_msgs__srv__TaskReplanningRelabel_Response__Sequence__init(ltl_automaton_msgs__srv__TaskReplanningRelabel_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ltl_automaton_msgs__srv__TaskReplanningRelabel_Response * data = NULL;

  if (size) {
    data = (ltl_automaton_msgs__srv__TaskReplanningRelabel_Response *)allocator.zero_allocate(size, sizeof(ltl_automaton_msgs__srv__TaskReplanningRelabel_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = ltl_automaton_msgs__srv__TaskReplanningRelabel_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        ltl_automaton_msgs__srv__TaskReplanningRelabel_Response__fini(&data[i - 1]);
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
ltl_automaton_msgs__srv__TaskReplanningRelabel_Response__Sequence__fini(ltl_automaton_msgs__srv__TaskReplanningRelabel_Response__Sequence * array)
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
      ltl_automaton_msgs__srv__TaskReplanningRelabel_Response__fini(&array->data[i]);
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

ltl_automaton_msgs__srv__TaskReplanningRelabel_Response__Sequence *
ltl_automaton_msgs__srv__TaskReplanningRelabel_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  ltl_automaton_msgs__srv__TaskReplanningRelabel_Response__Sequence * array = (ltl_automaton_msgs__srv__TaskReplanningRelabel_Response__Sequence *)allocator.allocate(sizeof(ltl_automaton_msgs__srv__TaskReplanningRelabel_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = ltl_automaton_msgs__srv__TaskReplanningRelabel_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
ltl_automaton_msgs__srv__TaskReplanningRelabel_Response__Sequence__destroy(ltl_automaton_msgs__srv__TaskReplanningRelabel_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    ltl_automaton_msgs__srv__TaskReplanningRelabel_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
ltl_automaton_msgs__srv__TaskReplanningRelabel_Response__Sequence__are_equal(const ltl_automaton_msgs__srv__TaskReplanningRelabel_Response__Sequence * lhs, const ltl_automaton_msgs__srv__TaskReplanningRelabel_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!ltl_automaton_msgs__srv__TaskReplanningRelabel_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
ltl_automaton_msgs__srv__TaskReplanningRelabel_Response__Sequence__copy(
  const ltl_automaton_msgs__srv__TaskReplanningRelabel_Response__Sequence * input,
  ltl_automaton_msgs__srv__TaskReplanningRelabel_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(ltl_automaton_msgs__srv__TaskReplanningRelabel_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    ltl_automaton_msgs__srv__TaskReplanningRelabel_Response * data =
      (ltl_automaton_msgs__srv__TaskReplanningRelabel_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!ltl_automaton_msgs__srv__TaskReplanningRelabel_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          ltl_automaton_msgs__srv__TaskReplanningRelabel_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!ltl_automaton_msgs__srv__TaskReplanningRelabel_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
