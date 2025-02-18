// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from ltl_automaton_msgs:msg/RelayRequest.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "ltl_automaton_msgs/msg/detail/relay_request__rosidl_typesupport_introspection_c.h"
#include "ltl_automaton_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "ltl_automaton_msgs/msg/detail/relay_request__functions.h"
#include "ltl_automaton_msgs/msg/detail/relay_request__struct.h"


// Include directives for member types
// Member `from_pose`
// Member `to_pose`
#include "rosidl_runtime_c/primitives_sequence_functions.h"
// Member `current_state`
#include "ltl_automaton_msgs/msg/transition_system_state.h"
// Member `current_state`
#include "ltl_automaton_msgs/msg/detail/transition_system_state__rosidl_typesupport_introspection_c.h"
// Member `type`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void ltl_automaton_msgs__msg__RelayRequest__rosidl_typesupport_introspection_c__RelayRequest_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  ltl_automaton_msgs__msg__RelayRequest__init(message_memory);
}

void ltl_automaton_msgs__msg__RelayRequest__rosidl_typesupport_introspection_c__RelayRequest_fini_function(void * message_memory)
{
  ltl_automaton_msgs__msg__RelayRequest__fini(message_memory);
}

size_t ltl_automaton_msgs__msg__RelayRequest__rosidl_typesupport_introspection_c__size_function__RelayRequest__from_pose(
  const void * untyped_member)
{
  const rosidl_runtime_c__int32__Sequence * member =
    (const rosidl_runtime_c__int32__Sequence *)(untyped_member);
  return member->size;
}

const void * ltl_automaton_msgs__msg__RelayRequest__rosidl_typesupport_introspection_c__get_const_function__RelayRequest__from_pose(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__int32__Sequence * member =
    (const rosidl_runtime_c__int32__Sequence *)(untyped_member);
  return &member->data[index];
}

void * ltl_automaton_msgs__msg__RelayRequest__rosidl_typesupport_introspection_c__get_function__RelayRequest__from_pose(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__int32__Sequence * member =
    (rosidl_runtime_c__int32__Sequence *)(untyped_member);
  return &member->data[index];
}

void ltl_automaton_msgs__msg__RelayRequest__rosidl_typesupport_introspection_c__fetch_function__RelayRequest__from_pose(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const int32_t * item =
    ((const int32_t *)
    ltl_automaton_msgs__msg__RelayRequest__rosidl_typesupport_introspection_c__get_const_function__RelayRequest__from_pose(untyped_member, index));
  int32_t * value =
    (int32_t *)(untyped_value);
  *value = *item;
}

void ltl_automaton_msgs__msg__RelayRequest__rosidl_typesupport_introspection_c__assign_function__RelayRequest__from_pose(
  void * untyped_member, size_t index, const void * untyped_value)
{
  int32_t * item =
    ((int32_t *)
    ltl_automaton_msgs__msg__RelayRequest__rosidl_typesupport_introspection_c__get_function__RelayRequest__from_pose(untyped_member, index));
  const int32_t * value =
    (const int32_t *)(untyped_value);
  *item = *value;
}

bool ltl_automaton_msgs__msg__RelayRequest__rosidl_typesupport_introspection_c__resize_function__RelayRequest__from_pose(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__int32__Sequence * member =
    (rosidl_runtime_c__int32__Sequence *)(untyped_member);
  rosidl_runtime_c__int32__Sequence__fini(member);
  return rosidl_runtime_c__int32__Sequence__init(member, size);
}

size_t ltl_automaton_msgs__msg__RelayRequest__rosidl_typesupport_introspection_c__size_function__RelayRequest__to_pose(
  const void * untyped_member)
{
  const rosidl_runtime_c__int32__Sequence * member =
    (const rosidl_runtime_c__int32__Sequence *)(untyped_member);
  return member->size;
}

const void * ltl_automaton_msgs__msg__RelayRequest__rosidl_typesupport_introspection_c__get_const_function__RelayRequest__to_pose(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__int32__Sequence * member =
    (const rosidl_runtime_c__int32__Sequence *)(untyped_member);
  return &member->data[index];
}

void * ltl_automaton_msgs__msg__RelayRequest__rosidl_typesupport_introspection_c__get_function__RelayRequest__to_pose(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__int32__Sequence * member =
    (rosidl_runtime_c__int32__Sequence *)(untyped_member);
  return &member->data[index];
}

void ltl_automaton_msgs__msg__RelayRequest__rosidl_typesupport_introspection_c__fetch_function__RelayRequest__to_pose(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const int32_t * item =
    ((const int32_t *)
    ltl_automaton_msgs__msg__RelayRequest__rosidl_typesupport_introspection_c__get_const_function__RelayRequest__to_pose(untyped_member, index));
  int32_t * value =
    (int32_t *)(untyped_value);
  *value = *item;
}

void ltl_automaton_msgs__msg__RelayRequest__rosidl_typesupport_introspection_c__assign_function__RelayRequest__to_pose(
  void * untyped_member, size_t index, const void * untyped_value)
{
  int32_t * item =
    ((int32_t *)
    ltl_automaton_msgs__msg__RelayRequest__rosidl_typesupport_introspection_c__get_function__RelayRequest__to_pose(untyped_member, index));
  const int32_t * value =
    (const int32_t *)(untyped_value);
  *item = *value;
}

bool ltl_automaton_msgs__msg__RelayRequest__rosidl_typesupport_introspection_c__resize_function__RelayRequest__to_pose(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__int32__Sequence * member =
    (rosidl_runtime_c__int32__Sequence *)(untyped_member);
  rosidl_runtime_c__int32__Sequence__fini(member);
  return rosidl_runtime_c__int32__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember ltl_automaton_msgs__msg__RelayRequest__rosidl_typesupport_introspection_c__RelayRequest_message_member_array[6] = {
  {
    "from_pose",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ltl_automaton_msgs__msg__RelayRequest, from_pose),  // bytes offset in struct
    NULL,  // default value
    ltl_automaton_msgs__msg__RelayRequest__rosidl_typesupport_introspection_c__size_function__RelayRequest__from_pose,  // size() function pointer
    ltl_automaton_msgs__msg__RelayRequest__rosidl_typesupport_introspection_c__get_const_function__RelayRequest__from_pose,  // get_const(index) function pointer
    ltl_automaton_msgs__msg__RelayRequest__rosidl_typesupport_introspection_c__get_function__RelayRequest__from_pose,  // get(index) function pointer
    ltl_automaton_msgs__msg__RelayRequest__rosidl_typesupport_introspection_c__fetch_function__RelayRequest__from_pose,  // fetch(index, &value) function pointer
    ltl_automaton_msgs__msg__RelayRequest__rosidl_typesupport_introspection_c__assign_function__RelayRequest__from_pose,  // assign(index, value) function pointer
    ltl_automaton_msgs__msg__RelayRequest__rosidl_typesupport_introspection_c__resize_function__RelayRequest__from_pose  // resize(index) function pointer
  },
  {
    "to_pose",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ltl_automaton_msgs__msg__RelayRequest, to_pose),  // bytes offset in struct
    NULL,  // default value
    ltl_automaton_msgs__msg__RelayRequest__rosidl_typesupport_introspection_c__size_function__RelayRequest__to_pose,  // size() function pointer
    ltl_automaton_msgs__msg__RelayRequest__rosidl_typesupport_introspection_c__get_const_function__RelayRequest__to_pose,  // get_const(index) function pointer
    ltl_automaton_msgs__msg__RelayRequest__rosidl_typesupport_introspection_c__get_function__RelayRequest__to_pose,  // get(index) function pointer
    ltl_automaton_msgs__msg__RelayRequest__rosidl_typesupport_introspection_c__fetch_function__RelayRequest__to_pose,  // fetch(index, &value) function pointer
    ltl_automaton_msgs__msg__RelayRequest__rosidl_typesupport_introspection_c__assign_function__RelayRequest__to_pose,  // assign(index, value) function pointer
    ltl_automaton_msgs__msg__RelayRequest__rosidl_typesupport_introspection_c__resize_function__RelayRequest__to_pose  // resize(index) function pointer
  },
  {
    "cost",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ltl_automaton_msgs__msg__RelayRequest, cost),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "current_state",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ltl_automaton_msgs__msg__RelayRequest, current_state),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "exec_index",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ltl_automaton_msgs__msg__RelayRequest, exec_index),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "type",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ltl_automaton_msgs__msg__RelayRequest, type),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers ltl_automaton_msgs__msg__RelayRequest__rosidl_typesupport_introspection_c__RelayRequest_message_members = {
  "ltl_automaton_msgs__msg",  // message namespace
  "RelayRequest",  // message name
  6,  // number of fields
  sizeof(ltl_automaton_msgs__msg__RelayRequest),
  ltl_automaton_msgs__msg__RelayRequest__rosidl_typesupport_introspection_c__RelayRequest_message_member_array,  // message members
  ltl_automaton_msgs__msg__RelayRequest__rosidl_typesupport_introspection_c__RelayRequest_init_function,  // function to initialize message memory (memory has to be allocated)
  ltl_automaton_msgs__msg__RelayRequest__rosidl_typesupport_introspection_c__RelayRequest_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t ltl_automaton_msgs__msg__RelayRequest__rosidl_typesupport_introspection_c__RelayRequest_message_type_support_handle = {
  0,
  &ltl_automaton_msgs__msg__RelayRequest__rosidl_typesupport_introspection_c__RelayRequest_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_ltl_automaton_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ltl_automaton_msgs, msg, RelayRequest)() {
  ltl_automaton_msgs__msg__RelayRequest__rosidl_typesupport_introspection_c__RelayRequest_message_member_array[3].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ltl_automaton_msgs, msg, TransitionSystemState)();
  if (!ltl_automaton_msgs__msg__RelayRequest__rosidl_typesupport_introspection_c__RelayRequest_message_type_support_handle.typesupport_identifier) {
    ltl_automaton_msgs__msg__RelayRequest__rosidl_typesupport_introspection_c__RelayRequest_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &ltl_automaton_msgs__msg__RelayRequest__rosidl_typesupport_introspection_c__RelayRequest_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
