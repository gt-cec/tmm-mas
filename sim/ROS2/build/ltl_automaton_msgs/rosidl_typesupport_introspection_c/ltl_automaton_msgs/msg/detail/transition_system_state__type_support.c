// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from ltl_automaton_msgs:msg/TransitionSystemState.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "ltl_automaton_msgs/msg/detail/transition_system_state__rosidl_typesupport_introspection_c.h"
#include "ltl_automaton_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "ltl_automaton_msgs/msg/detail/transition_system_state__functions.h"
#include "ltl_automaton_msgs/msg/detail/transition_system_state__struct.h"


// Include directives for member types
// Member `states`
// Member `state_dimension_names`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void ltl_automaton_msgs__msg__TransitionSystemState__rosidl_typesupport_introspection_c__TransitionSystemState_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  ltl_automaton_msgs__msg__TransitionSystemState__init(message_memory);
}

void ltl_automaton_msgs__msg__TransitionSystemState__rosidl_typesupport_introspection_c__TransitionSystemState_fini_function(void * message_memory)
{
  ltl_automaton_msgs__msg__TransitionSystemState__fini(message_memory);
}

size_t ltl_automaton_msgs__msg__TransitionSystemState__rosidl_typesupport_introspection_c__size_function__TransitionSystemState__states(
  const void * untyped_member)
{
  const rosidl_runtime_c__String__Sequence * member =
    (const rosidl_runtime_c__String__Sequence *)(untyped_member);
  return member->size;
}

const void * ltl_automaton_msgs__msg__TransitionSystemState__rosidl_typesupport_introspection_c__get_const_function__TransitionSystemState__states(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__String__Sequence * member =
    (const rosidl_runtime_c__String__Sequence *)(untyped_member);
  return &member->data[index];
}

void * ltl_automaton_msgs__msg__TransitionSystemState__rosidl_typesupport_introspection_c__get_function__TransitionSystemState__states(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__String__Sequence * member =
    (rosidl_runtime_c__String__Sequence *)(untyped_member);
  return &member->data[index];
}

void ltl_automaton_msgs__msg__TransitionSystemState__rosidl_typesupport_introspection_c__fetch_function__TransitionSystemState__states(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const rosidl_runtime_c__String * item =
    ((const rosidl_runtime_c__String *)
    ltl_automaton_msgs__msg__TransitionSystemState__rosidl_typesupport_introspection_c__get_const_function__TransitionSystemState__states(untyped_member, index));
  rosidl_runtime_c__String * value =
    (rosidl_runtime_c__String *)(untyped_value);
  *value = *item;
}

void ltl_automaton_msgs__msg__TransitionSystemState__rosidl_typesupport_introspection_c__assign_function__TransitionSystemState__states(
  void * untyped_member, size_t index, const void * untyped_value)
{
  rosidl_runtime_c__String * item =
    ((rosidl_runtime_c__String *)
    ltl_automaton_msgs__msg__TransitionSystemState__rosidl_typesupport_introspection_c__get_function__TransitionSystemState__states(untyped_member, index));
  const rosidl_runtime_c__String * value =
    (const rosidl_runtime_c__String *)(untyped_value);
  *item = *value;
}

bool ltl_automaton_msgs__msg__TransitionSystemState__rosidl_typesupport_introspection_c__resize_function__TransitionSystemState__states(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__String__Sequence * member =
    (rosidl_runtime_c__String__Sequence *)(untyped_member);
  rosidl_runtime_c__String__Sequence__fini(member);
  return rosidl_runtime_c__String__Sequence__init(member, size);
}

size_t ltl_automaton_msgs__msg__TransitionSystemState__rosidl_typesupport_introspection_c__size_function__TransitionSystemState__state_dimension_names(
  const void * untyped_member)
{
  const rosidl_runtime_c__String__Sequence * member =
    (const rosidl_runtime_c__String__Sequence *)(untyped_member);
  return member->size;
}

const void * ltl_automaton_msgs__msg__TransitionSystemState__rosidl_typesupport_introspection_c__get_const_function__TransitionSystemState__state_dimension_names(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__String__Sequence * member =
    (const rosidl_runtime_c__String__Sequence *)(untyped_member);
  return &member->data[index];
}

void * ltl_automaton_msgs__msg__TransitionSystemState__rosidl_typesupport_introspection_c__get_function__TransitionSystemState__state_dimension_names(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__String__Sequence * member =
    (rosidl_runtime_c__String__Sequence *)(untyped_member);
  return &member->data[index];
}

void ltl_automaton_msgs__msg__TransitionSystemState__rosidl_typesupport_introspection_c__fetch_function__TransitionSystemState__state_dimension_names(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const rosidl_runtime_c__String * item =
    ((const rosidl_runtime_c__String *)
    ltl_automaton_msgs__msg__TransitionSystemState__rosidl_typesupport_introspection_c__get_const_function__TransitionSystemState__state_dimension_names(untyped_member, index));
  rosidl_runtime_c__String * value =
    (rosidl_runtime_c__String *)(untyped_value);
  *value = *item;
}

void ltl_automaton_msgs__msg__TransitionSystemState__rosidl_typesupport_introspection_c__assign_function__TransitionSystemState__state_dimension_names(
  void * untyped_member, size_t index, const void * untyped_value)
{
  rosidl_runtime_c__String * item =
    ((rosidl_runtime_c__String *)
    ltl_automaton_msgs__msg__TransitionSystemState__rosidl_typesupport_introspection_c__get_function__TransitionSystemState__state_dimension_names(untyped_member, index));
  const rosidl_runtime_c__String * value =
    (const rosidl_runtime_c__String *)(untyped_value);
  *item = *value;
}

bool ltl_automaton_msgs__msg__TransitionSystemState__rosidl_typesupport_introspection_c__resize_function__TransitionSystemState__state_dimension_names(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__String__Sequence * member =
    (rosidl_runtime_c__String__Sequence *)(untyped_member);
  rosidl_runtime_c__String__Sequence__fini(member);
  return rosidl_runtime_c__String__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember ltl_automaton_msgs__msg__TransitionSystemState__rosidl_typesupport_introspection_c__TransitionSystemState_message_member_array[2] = {
  {
    "states",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ltl_automaton_msgs__msg__TransitionSystemState, states),  // bytes offset in struct
    NULL,  // default value
    ltl_automaton_msgs__msg__TransitionSystemState__rosidl_typesupport_introspection_c__size_function__TransitionSystemState__states,  // size() function pointer
    ltl_automaton_msgs__msg__TransitionSystemState__rosidl_typesupport_introspection_c__get_const_function__TransitionSystemState__states,  // get_const(index) function pointer
    ltl_automaton_msgs__msg__TransitionSystemState__rosidl_typesupport_introspection_c__get_function__TransitionSystemState__states,  // get(index) function pointer
    ltl_automaton_msgs__msg__TransitionSystemState__rosidl_typesupport_introspection_c__fetch_function__TransitionSystemState__states,  // fetch(index, &value) function pointer
    ltl_automaton_msgs__msg__TransitionSystemState__rosidl_typesupport_introspection_c__assign_function__TransitionSystemState__states,  // assign(index, value) function pointer
    ltl_automaton_msgs__msg__TransitionSystemState__rosidl_typesupport_introspection_c__resize_function__TransitionSystemState__states  // resize(index) function pointer
  },
  {
    "state_dimension_names",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ltl_automaton_msgs__msg__TransitionSystemState, state_dimension_names),  // bytes offset in struct
    NULL,  // default value
    ltl_automaton_msgs__msg__TransitionSystemState__rosidl_typesupport_introspection_c__size_function__TransitionSystemState__state_dimension_names,  // size() function pointer
    ltl_automaton_msgs__msg__TransitionSystemState__rosidl_typesupport_introspection_c__get_const_function__TransitionSystemState__state_dimension_names,  // get_const(index) function pointer
    ltl_automaton_msgs__msg__TransitionSystemState__rosidl_typesupport_introspection_c__get_function__TransitionSystemState__state_dimension_names,  // get(index) function pointer
    ltl_automaton_msgs__msg__TransitionSystemState__rosidl_typesupport_introspection_c__fetch_function__TransitionSystemState__state_dimension_names,  // fetch(index, &value) function pointer
    ltl_automaton_msgs__msg__TransitionSystemState__rosidl_typesupport_introspection_c__assign_function__TransitionSystemState__state_dimension_names,  // assign(index, value) function pointer
    ltl_automaton_msgs__msg__TransitionSystemState__rosidl_typesupport_introspection_c__resize_function__TransitionSystemState__state_dimension_names  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers ltl_automaton_msgs__msg__TransitionSystemState__rosidl_typesupport_introspection_c__TransitionSystemState_message_members = {
  "ltl_automaton_msgs__msg",  // message namespace
  "TransitionSystemState",  // message name
  2,  // number of fields
  sizeof(ltl_automaton_msgs__msg__TransitionSystemState),
  ltl_automaton_msgs__msg__TransitionSystemState__rosidl_typesupport_introspection_c__TransitionSystemState_message_member_array,  // message members
  ltl_automaton_msgs__msg__TransitionSystemState__rosidl_typesupport_introspection_c__TransitionSystemState_init_function,  // function to initialize message memory (memory has to be allocated)
  ltl_automaton_msgs__msg__TransitionSystemState__rosidl_typesupport_introspection_c__TransitionSystemState_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t ltl_automaton_msgs__msg__TransitionSystemState__rosidl_typesupport_introspection_c__TransitionSystemState_message_type_support_handle = {
  0,
  &ltl_automaton_msgs__msg__TransitionSystemState__rosidl_typesupport_introspection_c__TransitionSystemState_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_ltl_automaton_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ltl_automaton_msgs, msg, TransitionSystemState)() {
  if (!ltl_automaton_msgs__msg__TransitionSystemState__rosidl_typesupport_introspection_c__TransitionSystemState_message_type_support_handle.typesupport_identifier) {
    ltl_automaton_msgs__msg__TransitionSystemState__rosidl_typesupport_introspection_c__TransitionSystemState_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &ltl_automaton_msgs__msg__TransitionSystemState__rosidl_typesupport_introspection_c__TransitionSystemState_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
