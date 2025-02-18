// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from ltl_automaton_msgs:msg/LTLStateArray.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "ltl_automaton_msgs/msg/detail/ltl_state_array__rosidl_typesupport_introspection_c.h"
#include "ltl_automaton_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "ltl_automaton_msgs/msg/detail/ltl_state_array__functions.h"
#include "ltl_automaton_msgs/msg/detail/ltl_state_array__struct.h"


// Include directives for member types
// Member `ltl_states`
#include "ltl_automaton_msgs/msg/ltl_state.h"
// Member `ltl_states`
#include "ltl_automaton_msgs/msg/detail/ltl_state__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void ltl_automaton_msgs__msg__LTLStateArray__rosidl_typesupport_introspection_c__LTLStateArray_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  ltl_automaton_msgs__msg__LTLStateArray__init(message_memory);
}

void ltl_automaton_msgs__msg__LTLStateArray__rosidl_typesupport_introspection_c__LTLStateArray_fini_function(void * message_memory)
{
  ltl_automaton_msgs__msg__LTLStateArray__fini(message_memory);
}

size_t ltl_automaton_msgs__msg__LTLStateArray__rosidl_typesupport_introspection_c__size_function__LTLStateArray__ltl_states(
  const void * untyped_member)
{
  const ltl_automaton_msgs__msg__LTLState__Sequence * member =
    (const ltl_automaton_msgs__msg__LTLState__Sequence *)(untyped_member);
  return member->size;
}

const void * ltl_automaton_msgs__msg__LTLStateArray__rosidl_typesupport_introspection_c__get_const_function__LTLStateArray__ltl_states(
  const void * untyped_member, size_t index)
{
  const ltl_automaton_msgs__msg__LTLState__Sequence * member =
    (const ltl_automaton_msgs__msg__LTLState__Sequence *)(untyped_member);
  return &member->data[index];
}

void * ltl_automaton_msgs__msg__LTLStateArray__rosidl_typesupport_introspection_c__get_function__LTLStateArray__ltl_states(
  void * untyped_member, size_t index)
{
  ltl_automaton_msgs__msg__LTLState__Sequence * member =
    (ltl_automaton_msgs__msg__LTLState__Sequence *)(untyped_member);
  return &member->data[index];
}

void ltl_automaton_msgs__msg__LTLStateArray__rosidl_typesupport_introspection_c__fetch_function__LTLStateArray__ltl_states(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const ltl_automaton_msgs__msg__LTLState * item =
    ((const ltl_automaton_msgs__msg__LTLState *)
    ltl_automaton_msgs__msg__LTLStateArray__rosidl_typesupport_introspection_c__get_const_function__LTLStateArray__ltl_states(untyped_member, index));
  ltl_automaton_msgs__msg__LTLState * value =
    (ltl_automaton_msgs__msg__LTLState *)(untyped_value);
  *value = *item;
}

void ltl_automaton_msgs__msg__LTLStateArray__rosidl_typesupport_introspection_c__assign_function__LTLStateArray__ltl_states(
  void * untyped_member, size_t index, const void * untyped_value)
{
  ltl_automaton_msgs__msg__LTLState * item =
    ((ltl_automaton_msgs__msg__LTLState *)
    ltl_automaton_msgs__msg__LTLStateArray__rosidl_typesupport_introspection_c__get_function__LTLStateArray__ltl_states(untyped_member, index));
  const ltl_automaton_msgs__msg__LTLState * value =
    (const ltl_automaton_msgs__msg__LTLState *)(untyped_value);
  *item = *value;
}

bool ltl_automaton_msgs__msg__LTLStateArray__rosidl_typesupport_introspection_c__resize_function__LTLStateArray__ltl_states(
  void * untyped_member, size_t size)
{
  ltl_automaton_msgs__msg__LTLState__Sequence * member =
    (ltl_automaton_msgs__msg__LTLState__Sequence *)(untyped_member);
  ltl_automaton_msgs__msg__LTLState__Sequence__fini(member);
  return ltl_automaton_msgs__msg__LTLState__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember ltl_automaton_msgs__msg__LTLStateArray__rosidl_typesupport_introspection_c__LTLStateArray_message_member_array[1] = {
  {
    "ltl_states",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ltl_automaton_msgs__msg__LTLStateArray, ltl_states),  // bytes offset in struct
    NULL,  // default value
    ltl_automaton_msgs__msg__LTLStateArray__rosidl_typesupport_introspection_c__size_function__LTLStateArray__ltl_states,  // size() function pointer
    ltl_automaton_msgs__msg__LTLStateArray__rosidl_typesupport_introspection_c__get_const_function__LTLStateArray__ltl_states,  // get_const(index) function pointer
    ltl_automaton_msgs__msg__LTLStateArray__rosidl_typesupport_introspection_c__get_function__LTLStateArray__ltl_states,  // get(index) function pointer
    ltl_automaton_msgs__msg__LTLStateArray__rosidl_typesupport_introspection_c__fetch_function__LTLStateArray__ltl_states,  // fetch(index, &value) function pointer
    ltl_automaton_msgs__msg__LTLStateArray__rosidl_typesupport_introspection_c__assign_function__LTLStateArray__ltl_states,  // assign(index, value) function pointer
    ltl_automaton_msgs__msg__LTLStateArray__rosidl_typesupport_introspection_c__resize_function__LTLStateArray__ltl_states  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers ltl_automaton_msgs__msg__LTLStateArray__rosidl_typesupport_introspection_c__LTLStateArray_message_members = {
  "ltl_automaton_msgs__msg",  // message namespace
  "LTLStateArray",  // message name
  1,  // number of fields
  sizeof(ltl_automaton_msgs__msg__LTLStateArray),
  ltl_automaton_msgs__msg__LTLStateArray__rosidl_typesupport_introspection_c__LTLStateArray_message_member_array,  // message members
  ltl_automaton_msgs__msg__LTLStateArray__rosidl_typesupport_introspection_c__LTLStateArray_init_function,  // function to initialize message memory (memory has to be allocated)
  ltl_automaton_msgs__msg__LTLStateArray__rosidl_typesupport_introspection_c__LTLStateArray_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t ltl_automaton_msgs__msg__LTLStateArray__rosidl_typesupport_introspection_c__LTLStateArray_message_type_support_handle = {
  0,
  &ltl_automaton_msgs__msg__LTLStateArray__rosidl_typesupport_introspection_c__LTLStateArray_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_ltl_automaton_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ltl_automaton_msgs, msg, LTLStateArray)() {
  ltl_automaton_msgs__msg__LTLStateArray__rosidl_typesupport_introspection_c__LTLStateArray_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ltl_automaton_msgs, msg, LTLState)();
  if (!ltl_automaton_msgs__msg__LTLStateArray__rosidl_typesupport_introspection_c__LTLStateArray_message_type_support_handle.typesupport_identifier) {
    ltl_automaton_msgs__msg__LTLStateArray__rosidl_typesupport_introspection_c__LTLStateArray_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &ltl_automaton_msgs__msg__LTLStateArray__rosidl_typesupport_introspection_c__LTLStateArray_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
