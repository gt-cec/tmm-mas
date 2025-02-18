// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from ltl_automaton_msgs:msg/LTLStateRuns.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "ltl_automaton_msgs/msg/detail/ltl_state_runs__rosidl_typesupport_introspection_c.h"
#include "ltl_automaton_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "ltl_automaton_msgs/msg/detail/ltl_state_runs__functions.h"
#include "ltl_automaton_msgs/msg/detail/ltl_state_runs__struct.h"


// Include directives for member types
// Member `runs`
#include "ltl_automaton_msgs/msg/ltl_state_array.h"
// Member `runs`
#include "ltl_automaton_msgs/msg/detail/ltl_state_array__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void ltl_automaton_msgs__msg__LTLStateRuns__rosidl_typesupport_introspection_c__LTLStateRuns_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  ltl_automaton_msgs__msg__LTLStateRuns__init(message_memory);
}

void ltl_automaton_msgs__msg__LTLStateRuns__rosidl_typesupport_introspection_c__LTLStateRuns_fini_function(void * message_memory)
{
  ltl_automaton_msgs__msg__LTLStateRuns__fini(message_memory);
}

size_t ltl_automaton_msgs__msg__LTLStateRuns__rosidl_typesupport_introspection_c__size_function__LTLStateRuns__runs(
  const void * untyped_member)
{
  const ltl_automaton_msgs__msg__LTLStateArray__Sequence * member =
    (const ltl_automaton_msgs__msg__LTLStateArray__Sequence *)(untyped_member);
  return member->size;
}

const void * ltl_automaton_msgs__msg__LTLStateRuns__rosidl_typesupport_introspection_c__get_const_function__LTLStateRuns__runs(
  const void * untyped_member, size_t index)
{
  const ltl_automaton_msgs__msg__LTLStateArray__Sequence * member =
    (const ltl_automaton_msgs__msg__LTLStateArray__Sequence *)(untyped_member);
  return &member->data[index];
}

void * ltl_automaton_msgs__msg__LTLStateRuns__rosidl_typesupport_introspection_c__get_function__LTLStateRuns__runs(
  void * untyped_member, size_t index)
{
  ltl_automaton_msgs__msg__LTLStateArray__Sequence * member =
    (ltl_automaton_msgs__msg__LTLStateArray__Sequence *)(untyped_member);
  return &member->data[index];
}

void ltl_automaton_msgs__msg__LTLStateRuns__rosidl_typesupport_introspection_c__fetch_function__LTLStateRuns__runs(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const ltl_automaton_msgs__msg__LTLStateArray * item =
    ((const ltl_automaton_msgs__msg__LTLStateArray *)
    ltl_automaton_msgs__msg__LTLStateRuns__rosidl_typesupport_introspection_c__get_const_function__LTLStateRuns__runs(untyped_member, index));
  ltl_automaton_msgs__msg__LTLStateArray * value =
    (ltl_automaton_msgs__msg__LTLStateArray *)(untyped_value);
  *value = *item;
}

void ltl_automaton_msgs__msg__LTLStateRuns__rosidl_typesupport_introspection_c__assign_function__LTLStateRuns__runs(
  void * untyped_member, size_t index, const void * untyped_value)
{
  ltl_automaton_msgs__msg__LTLStateArray * item =
    ((ltl_automaton_msgs__msg__LTLStateArray *)
    ltl_automaton_msgs__msg__LTLStateRuns__rosidl_typesupport_introspection_c__get_function__LTLStateRuns__runs(untyped_member, index));
  const ltl_automaton_msgs__msg__LTLStateArray * value =
    (const ltl_automaton_msgs__msg__LTLStateArray *)(untyped_value);
  *item = *value;
}

bool ltl_automaton_msgs__msg__LTLStateRuns__rosidl_typesupport_introspection_c__resize_function__LTLStateRuns__runs(
  void * untyped_member, size_t size)
{
  ltl_automaton_msgs__msg__LTLStateArray__Sequence * member =
    (ltl_automaton_msgs__msg__LTLStateArray__Sequence *)(untyped_member);
  ltl_automaton_msgs__msg__LTLStateArray__Sequence__fini(member);
  return ltl_automaton_msgs__msg__LTLStateArray__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember ltl_automaton_msgs__msg__LTLStateRuns__rosidl_typesupport_introspection_c__LTLStateRuns_message_member_array[1] = {
  {
    "runs",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ltl_automaton_msgs__msg__LTLStateRuns, runs),  // bytes offset in struct
    NULL,  // default value
    ltl_automaton_msgs__msg__LTLStateRuns__rosidl_typesupport_introspection_c__size_function__LTLStateRuns__runs,  // size() function pointer
    ltl_automaton_msgs__msg__LTLStateRuns__rosidl_typesupport_introspection_c__get_const_function__LTLStateRuns__runs,  // get_const(index) function pointer
    ltl_automaton_msgs__msg__LTLStateRuns__rosidl_typesupport_introspection_c__get_function__LTLStateRuns__runs,  // get(index) function pointer
    ltl_automaton_msgs__msg__LTLStateRuns__rosidl_typesupport_introspection_c__fetch_function__LTLStateRuns__runs,  // fetch(index, &value) function pointer
    ltl_automaton_msgs__msg__LTLStateRuns__rosidl_typesupport_introspection_c__assign_function__LTLStateRuns__runs,  // assign(index, value) function pointer
    ltl_automaton_msgs__msg__LTLStateRuns__rosidl_typesupport_introspection_c__resize_function__LTLStateRuns__runs  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers ltl_automaton_msgs__msg__LTLStateRuns__rosidl_typesupport_introspection_c__LTLStateRuns_message_members = {
  "ltl_automaton_msgs__msg",  // message namespace
  "LTLStateRuns",  // message name
  1,  // number of fields
  sizeof(ltl_automaton_msgs__msg__LTLStateRuns),
  ltl_automaton_msgs__msg__LTLStateRuns__rosidl_typesupport_introspection_c__LTLStateRuns_message_member_array,  // message members
  ltl_automaton_msgs__msg__LTLStateRuns__rosidl_typesupport_introspection_c__LTLStateRuns_init_function,  // function to initialize message memory (memory has to be allocated)
  ltl_automaton_msgs__msg__LTLStateRuns__rosidl_typesupport_introspection_c__LTLStateRuns_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t ltl_automaton_msgs__msg__LTLStateRuns__rosidl_typesupport_introspection_c__LTLStateRuns_message_type_support_handle = {
  0,
  &ltl_automaton_msgs__msg__LTLStateRuns__rosidl_typesupport_introspection_c__LTLStateRuns_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_ltl_automaton_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ltl_automaton_msgs, msg, LTLStateRuns)() {
  ltl_automaton_msgs__msg__LTLStateRuns__rosidl_typesupport_introspection_c__LTLStateRuns_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ltl_automaton_msgs, msg, LTLStateArray)();
  if (!ltl_automaton_msgs__msg__LTLStateRuns__rosidl_typesupport_introspection_c__LTLStateRuns_message_type_support_handle.typesupport_identifier) {
    ltl_automaton_msgs__msg__LTLStateRuns__rosidl_typesupport_introspection_c__LTLStateRuns_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &ltl_automaton_msgs__msg__LTLStateRuns__rosidl_typesupport_introspection_c__LTLStateRuns_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
