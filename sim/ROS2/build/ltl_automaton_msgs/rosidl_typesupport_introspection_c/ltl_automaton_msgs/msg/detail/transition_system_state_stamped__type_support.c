// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from ltl_automaton_msgs:msg/TransitionSystemStateStamped.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "ltl_automaton_msgs/msg/detail/transition_system_state_stamped__rosidl_typesupport_introspection_c.h"
#include "ltl_automaton_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "ltl_automaton_msgs/msg/detail/transition_system_state_stamped__functions.h"
#include "ltl_automaton_msgs/msg/detail/transition_system_state_stamped__struct.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/header.h"
// Member `header`
#include "std_msgs/msg/detail/header__rosidl_typesupport_introspection_c.h"
// Member `ts_state`
#include "ltl_automaton_msgs/msg/transition_system_state.h"
// Member `ts_state`
#include "ltl_automaton_msgs/msg/detail/transition_system_state__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void ltl_automaton_msgs__msg__TransitionSystemStateStamped__rosidl_typesupport_introspection_c__TransitionSystemStateStamped_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  ltl_automaton_msgs__msg__TransitionSystemStateStamped__init(message_memory);
}

void ltl_automaton_msgs__msg__TransitionSystemStateStamped__rosidl_typesupport_introspection_c__TransitionSystemStateStamped_fini_function(void * message_memory)
{
  ltl_automaton_msgs__msg__TransitionSystemStateStamped__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember ltl_automaton_msgs__msg__TransitionSystemStateStamped__rosidl_typesupport_introspection_c__TransitionSystemStateStamped_message_member_array[2] = {
  {
    "header",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ltl_automaton_msgs__msg__TransitionSystemStateStamped, header),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "ts_state",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ltl_automaton_msgs__msg__TransitionSystemStateStamped, ts_state),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers ltl_automaton_msgs__msg__TransitionSystemStateStamped__rosidl_typesupport_introspection_c__TransitionSystemStateStamped_message_members = {
  "ltl_automaton_msgs__msg",  // message namespace
  "TransitionSystemStateStamped",  // message name
  2,  // number of fields
  sizeof(ltl_automaton_msgs__msg__TransitionSystemStateStamped),
  ltl_automaton_msgs__msg__TransitionSystemStateStamped__rosidl_typesupport_introspection_c__TransitionSystemStateStamped_message_member_array,  // message members
  ltl_automaton_msgs__msg__TransitionSystemStateStamped__rosidl_typesupport_introspection_c__TransitionSystemStateStamped_init_function,  // function to initialize message memory (memory has to be allocated)
  ltl_automaton_msgs__msg__TransitionSystemStateStamped__rosidl_typesupport_introspection_c__TransitionSystemStateStamped_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t ltl_automaton_msgs__msg__TransitionSystemStateStamped__rosidl_typesupport_introspection_c__TransitionSystemStateStamped_message_type_support_handle = {
  0,
  &ltl_automaton_msgs__msg__TransitionSystemStateStamped__rosidl_typesupport_introspection_c__TransitionSystemStateStamped_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_ltl_automaton_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ltl_automaton_msgs, msg, TransitionSystemStateStamped)() {
  ltl_automaton_msgs__msg__TransitionSystemStateStamped__rosidl_typesupport_introspection_c__TransitionSystemStateStamped_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, std_msgs, msg, Header)();
  ltl_automaton_msgs__msg__TransitionSystemStateStamped__rosidl_typesupport_introspection_c__TransitionSystemStateStamped_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ltl_automaton_msgs, msg, TransitionSystemState)();
  if (!ltl_automaton_msgs__msg__TransitionSystemStateStamped__rosidl_typesupport_introspection_c__TransitionSystemStateStamped_message_type_support_handle.typesupport_identifier) {
    ltl_automaton_msgs__msg__TransitionSystemStateStamped__rosidl_typesupport_introspection_c__TransitionSystemStateStamped_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &ltl_automaton_msgs__msg__TransitionSystemStateStamped__rosidl_typesupport_introspection_c__TransitionSystemStateStamped_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
