// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from ltl_automaton_msgs:srv/TaskReplanningModify.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "ltl_automaton_msgs/srv/detail/task_replanning_modify__rosidl_typesupport_introspection_c.h"
#include "ltl_automaton_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "ltl_automaton_msgs/srv/detail/task_replanning_modify__functions.h"
#include "ltl_automaton_msgs/srv/detail/task_replanning_modify__struct.h"


// Include directives for member types
// Member `mod_from`
// Member `mod_to`
#include "rosidl_runtime_c/primitives_sequence_functions.h"
// Member `current_state`
#include "ltl_automaton_msgs/msg/transition_system_state.h"
// Member `current_state`
#include "ltl_automaton_msgs/msg/detail/transition_system_state__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void ltl_automaton_msgs__srv__TaskReplanningModify_Request__rosidl_typesupport_introspection_c__TaskReplanningModify_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  ltl_automaton_msgs__srv__TaskReplanningModify_Request__init(message_memory);
}

void ltl_automaton_msgs__srv__TaskReplanningModify_Request__rosidl_typesupport_introspection_c__TaskReplanningModify_Request_fini_function(void * message_memory)
{
  ltl_automaton_msgs__srv__TaskReplanningModify_Request__fini(message_memory);
}

size_t ltl_automaton_msgs__srv__TaskReplanningModify_Request__rosidl_typesupport_introspection_c__size_function__TaskReplanningModify_Request__mod_from(
  const void * untyped_member)
{
  const rosidl_runtime_c__int32__Sequence * member =
    (const rosidl_runtime_c__int32__Sequence *)(untyped_member);
  return member->size;
}

const void * ltl_automaton_msgs__srv__TaskReplanningModify_Request__rosidl_typesupport_introspection_c__get_const_function__TaskReplanningModify_Request__mod_from(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__int32__Sequence * member =
    (const rosidl_runtime_c__int32__Sequence *)(untyped_member);
  return &member->data[index];
}

void * ltl_automaton_msgs__srv__TaskReplanningModify_Request__rosidl_typesupport_introspection_c__get_function__TaskReplanningModify_Request__mod_from(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__int32__Sequence * member =
    (rosidl_runtime_c__int32__Sequence *)(untyped_member);
  return &member->data[index];
}

void ltl_automaton_msgs__srv__TaskReplanningModify_Request__rosidl_typesupport_introspection_c__fetch_function__TaskReplanningModify_Request__mod_from(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const int32_t * item =
    ((const int32_t *)
    ltl_automaton_msgs__srv__TaskReplanningModify_Request__rosidl_typesupport_introspection_c__get_const_function__TaskReplanningModify_Request__mod_from(untyped_member, index));
  int32_t * value =
    (int32_t *)(untyped_value);
  *value = *item;
}

void ltl_automaton_msgs__srv__TaskReplanningModify_Request__rosidl_typesupport_introspection_c__assign_function__TaskReplanningModify_Request__mod_from(
  void * untyped_member, size_t index, const void * untyped_value)
{
  int32_t * item =
    ((int32_t *)
    ltl_automaton_msgs__srv__TaskReplanningModify_Request__rosidl_typesupport_introspection_c__get_function__TaskReplanningModify_Request__mod_from(untyped_member, index));
  const int32_t * value =
    (const int32_t *)(untyped_value);
  *item = *value;
}

bool ltl_automaton_msgs__srv__TaskReplanningModify_Request__rosidl_typesupport_introspection_c__resize_function__TaskReplanningModify_Request__mod_from(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__int32__Sequence * member =
    (rosidl_runtime_c__int32__Sequence *)(untyped_member);
  rosidl_runtime_c__int32__Sequence__fini(member);
  return rosidl_runtime_c__int32__Sequence__init(member, size);
}

size_t ltl_automaton_msgs__srv__TaskReplanningModify_Request__rosidl_typesupport_introspection_c__size_function__TaskReplanningModify_Request__mod_to(
  const void * untyped_member)
{
  const rosidl_runtime_c__int32__Sequence * member =
    (const rosidl_runtime_c__int32__Sequence *)(untyped_member);
  return member->size;
}

const void * ltl_automaton_msgs__srv__TaskReplanningModify_Request__rosidl_typesupport_introspection_c__get_const_function__TaskReplanningModify_Request__mod_to(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__int32__Sequence * member =
    (const rosidl_runtime_c__int32__Sequence *)(untyped_member);
  return &member->data[index];
}

void * ltl_automaton_msgs__srv__TaskReplanningModify_Request__rosidl_typesupport_introspection_c__get_function__TaskReplanningModify_Request__mod_to(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__int32__Sequence * member =
    (rosidl_runtime_c__int32__Sequence *)(untyped_member);
  return &member->data[index];
}

void ltl_automaton_msgs__srv__TaskReplanningModify_Request__rosidl_typesupport_introspection_c__fetch_function__TaskReplanningModify_Request__mod_to(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const int32_t * item =
    ((const int32_t *)
    ltl_automaton_msgs__srv__TaskReplanningModify_Request__rosidl_typesupport_introspection_c__get_const_function__TaskReplanningModify_Request__mod_to(untyped_member, index));
  int32_t * value =
    (int32_t *)(untyped_value);
  *value = *item;
}

void ltl_automaton_msgs__srv__TaskReplanningModify_Request__rosidl_typesupport_introspection_c__assign_function__TaskReplanningModify_Request__mod_to(
  void * untyped_member, size_t index, const void * untyped_value)
{
  int32_t * item =
    ((int32_t *)
    ltl_automaton_msgs__srv__TaskReplanningModify_Request__rosidl_typesupport_introspection_c__get_function__TaskReplanningModify_Request__mod_to(untyped_member, index));
  const int32_t * value =
    (const int32_t *)(untyped_value);
  *item = *value;
}

bool ltl_automaton_msgs__srv__TaskReplanningModify_Request__rosidl_typesupport_introspection_c__resize_function__TaskReplanningModify_Request__mod_to(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__int32__Sequence * member =
    (rosidl_runtime_c__int32__Sequence *)(untyped_member);
  rosidl_runtime_c__int32__Sequence__fini(member);
  return rosidl_runtime_c__int32__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember ltl_automaton_msgs__srv__TaskReplanningModify_Request__rosidl_typesupport_introspection_c__TaskReplanningModify_Request_message_member_array[5] = {
  {
    "mod_from",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ltl_automaton_msgs__srv__TaskReplanningModify_Request, mod_from),  // bytes offset in struct
    NULL,  // default value
    ltl_automaton_msgs__srv__TaskReplanningModify_Request__rosidl_typesupport_introspection_c__size_function__TaskReplanningModify_Request__mod_from,  // size() function pointer
    ltl_automaton_msgs__srv__TaskReplanningModify_Request__rosidl_typesupport_introspection_c__get_const_function__TaskReplanningModify_Request__mod_from,  // get_const(index) function pointer
    ltl_automaton_msgs__srv__TaskReplanningModify_Request__rosidl_typesupport_introspection_c__get_function__TaskReplanningModify_Request__mod_from,  // get(index) function pointer
    ltl_automaton_msgs__srv__TaskReplanningModify_Request__rosidl_typesupport_introspection_c__fetch_function__TaskReplanningModify_Request__mod_from,  // fetch(index, &value) function pointer
    ltl_automaton_msgs__srv__TaskReplanningModify_Request__rosidl_typesupport_introspection_c__assign_function__TaskReplanningModify_Request__mod_from,  // assign(index, value) function pointer
    ltl_automaton_msgs__srv__TaskReplanningModify_Request__rosidl_typesupport_introspection_c__resize_function__TaskReplanningModify_Request__mod_from  // resize(index) function pointer
  },
  {
    "mod_to",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ltl_automaton_msgs__srv__TaskReplanningModify_Request, mod_to),  // bytes offset in struct
    NULL,  // default value
    ltl_automaton_msgs__srv__TaskReplanningModify_Request__rosidl_typesupport_introspection_c__size_function__TaskReplanningModify_Request__mod_to,  // size() function pointer
    ltl_automaton_msgs__srv__TaskReplanningModify_Request__rosidl_typesupport_introspection_c__get_const_function__TaskReplanningModify_Request__mod_to,  // get_const(index) function pointer
    ltl_automaton_msgs__srv__TaskReplanningModify_Request__rosidl_typesupport_introspection_c__get_function__TaskReplanningModify_Request__mod_to,  // get(index) function pointer
    ltl_automaton_msgs__srv__TaskReplanningModify_Request__rosidl_typesupport_introspection_c__fetch_function__TaskReplanningModify_Request__mod_to,  // fetch(index, &value) function pointer
    ltl_automaton_msgs__srv__TaskReplanningModify_Request__rosidl_typesupport_introspection_c__assign_function__TaskReplanningModify_Request__mod_to,  // assign(index, value) function pointer
    ltl_automaton_msgs__srv__TaskReplanningModify_Request__rosidl_typesupport_introspection_c__resize_function__TaskReplanningModify_Request__mod_to  // resize(index) function pointer
  },
  {
    "cost",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ltl_automaton_msgs__srv__TaskReplanningModify_Request, cost),  // bytes offset in struct
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
    offsetof(ltl_automaton_msgs__srv__TaskReplanningModify_Request, current_state),  // bytes offset in struct
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
    offsetof(ltl_automaton_msgs__srv__TaskReplanningModify_Request, exec_index),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers ltl_automaton_msgs__srv__TaskReplanningModify_Request__rosidl_typesupport_introspection_c__TaskReplanningModify_Request_message_members = {
  "ltl_automaton_msgs__srv",  // message namespace
  "TaskReplanningModify_Request",  // message name
  5,  // number of fields
  sizeof(ltl_automaton_msgs__srv__TaskReplanningModify_Request),
  ltl_automaton_msgs__srv__TaskReplanningModify_Request__rosidl_typesupport_introspection_c__TaskReplanningModify_Request_message_member_array,  // message members
  ltl_automaton_msgs__srv__TaskReplanningModify_Request__rosidl_typesupport_introspection_c__TaskReplanningModify_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  ltl_automaton_msgs__srv__TaskReplanningModify_Request__rosidl_typesupport_introspection_c__TaskReplanningModify_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t ltl_automaton_msgs__srv__TaskReplanningModify_Request__rosidl_typesupport_introspection_c__TaskReplanningModify_Request_message_type_support_handle = {
  0,
  &ltl_automaton_msgs__srv__TaskReplanningModify_Request__rosidl_typesupport_introspection_c__TaskReplanningModify_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_ltl_automaton_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ltl_automaton_msgs, srv, TaskReplanningModify_Request)() {
  ltl_automaton_msgs__srv__TaskReplanningModify_Request__rosidl_typesupport_introspection_c__TaskReplanningModify_Request_message_member_array[3].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ltl_automaton_msgs, msg, TransitionSystemState)();
  if (!ltl_automaton_msgs__srv__TaskReplanningModify_Request__rosidl_typesupport_introspection_c__TaskReplanningModify_Request_message_type_support_handle.typesupport_identifier) {
    ltl_automaton_msgs__srv__TaskReplanningModify_Request__rosidl_typesupport_introspection_c__TaskReplanningModify_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &ltl_automaton_msgs__srv__TaskReplanningModify_Request__rosidl_typesupport_introspection_c__TaskReplanningModify_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "ltl_automaton_msgs/srv/detail/task_replanning_modify__rosidl_typesupport_introspection_c.h"
// already included above
// #include "ltl_automaton_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "ltl_automaton_msgs/srv/detail/task_replanning_modify__functions.h"
// already included above
// #include "ltl_automaton_msgs/srv/detail/task_replanning_modify__struct.h"


// Include directives for member types
// Member `new_plan_prefix`
// Member `new_plan_suffix`
#include "ltl_automaton_msgs/msg/ltl_plan.h"
// Member `new_plan_prefix`
// Member `new_plan_suffix`
#include "ltl_automaton_msgs/msg/detail/ltl_plan__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void ltl_automaton_msgs__srv__TaskReplanningModify_Response__rosidl_typesupport_introspection_c__TaskReplanningModify_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  ltl_automaton_msgs__srv__TaskReplanningModify_Response__init(message_memory);
}

void ltl_automaton_msgs__srv__TaskReplanningModify_Response__rosidl_typesupport_introspection_c__TaskReplanningModify_Response_fini_function(void * message_memory)
{
  ltl_automaton_msgs__srv__TaskReplanningModify_Response__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember ltl_automaton_msgs__srv__TaskReplanningModify_Response__rosidl_typesupport_introspection_c__TaskReplanningModify_Response_message_member_array[3] = {
  {
    "success",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ltl_automaton_msgs__srv__TaskReplanningModify_Response, success),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "new_plan_prefix",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ltl_automaton_msgs__srv__TaskReplanningModify_Response, new_plan_prefix),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "new_plan_suffix",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ltl_automaton_msgs__srv__TaskReplanningModify_Response, new_plan_suffix),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers ltl_automaton_msgs__srv__TaskReplanningModify_Response__rosidl_typesupport_introspection_c__TaskReplanningModify_Response_message_members = {
  "ltl_automaton_msgs__srv",  // message namespace
  "TaskReplanningModify_Response",  // message name
  3,  // number of fields
  sizeof(ltl_automaton_msgs__srv__TaskReplanningModify_Response),
  ltl_automaton_msgs__srv__TaskReplanningModify_Response__rosidl_typesupport_introspection_c__TaskReplanningModify_Response_message_member_array,  // message members
  ltl_automaton_msgs__srv__TaskReplanningModify_Response__rosidl_typesupport_introspection_c__TaskReplanningModify_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  ltl_automaton_msgs__srv__TaskReplanningModify_Response__rosidl_typesupport_introspection_c__TaskReplanningModify_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t ltl_automaton_msgs__srv__TaskReplanningModify_Response__rosidl_typesupport_introspection_c__TaskReplanningModify_Response_message_type_support_handle = {
  0,
  &ltl_automaton_msgs__srv__TaskReplanningModify_Response__rosidl_typesupport_introspection_c__TaskReplanningModify_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_ltl_automaton_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ltl_automaton_msgs, srv, TaskReplanningModify_Response)() {
  ltl_automaton_msgs__srv__TaskReplanningModify_Response__rosidl_typesupport_introspection_c__TaskReplanningModify_Response_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ltl_automaton_msgs, msg, LTLPlan)();
  ltl_automaton_msgs__srv__TaskReplanningModify_Response__rosidl_typesupport_introspection_c__TaskReplanningModify_Response_message_member_array[2].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ltl_automaton_msgs, msg, LTLPlan)();
  if (!ltl_automaton_msgs__srv__TaskReplanningModify_Response__rosidl_typesupport_introspection_c__TaskReplanningModify_Response_message_type_support_handle.typesupport_identifier) {
    ltl_automaton_msgs__srv__TaskReplanningModify_Response__rosidl_typesupport_introspection_c__TaskReplanningModify_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &ltl_automaton_msgs__srv__TaskReplanningModify_Response__rosidl_typesupport_introspection_c__TaskReplanningModify_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "ltl_automaton_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "ltl_automaton_msgs/srv/detail/task_replanning_modify__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers ltl_automaton_msgs__srv__detail__task_replanning_modify__rosidl_typesupport_introspection_c__TaskReplanningModify_service_members = {
  "ltl_automaton_msgs__srv",  // service namespace
  "TaskReplanningModify",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // ltl_automaton_msgs__srv__detail__task_replanning_modify__rosidl_typesupport_introspection_c__TaskReplanningModify_Request_message_type_support_handle,
  NULL  // response message
  // ltl_automaton_msgs__srv__detail__task_replanning_modify__rosidl_typesupport_introspection_c__TaskReplanningModify_Response_message_type_support_handle
};

static rosidl_service_type_support_t ltl_automaton_msgs__srv__detail__task_replanning_modify__rosidl_typesupport_introspection_c__TaskReplanningModify_service_type_support_handle = {
  0,
  &ltl_automaton_msgs__srv__detail__task_replanning_modify__rosidl_typesupport_introspection_c__TaskReplanningModify_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ltl_automaton_msgs, srv, TaskReplanningModify_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ltl_automaton_msgs, srv, TaskReplanningModify_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_ltl_automaton_msgs
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ltl_automaton_msgs, srv, TaskReplanningModify)() {
  if (!ltl_automaton_msgs__srv__detail__task_replanning_modify__rosidl_typesupport_introspection_c__TaskReplanningModify_service_type_support_handle.typesupport_identifier) {
    ltl_automaton_msgs__srv__detail__task_replanning_modify__rosidl_typesupport_introspection_c__TaskReplanningModify_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)ltl_automaton_msgs__srv__detail__task_replanning_modify__rosidl_typesupport_introspection_c__TaskReplanningModify_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ltl_automaton_msgs, srv, TaskReplanningModify_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ltl_automaton_msgs, srv, TaskReplanningModify_Response)()->data;
  }

  return &ltl_automaton_msgs__srv__detail__task_replanning_modify__rosidl_typesupport_introspection_c__TaskReplanningModify_service_type_support_handle;
}
