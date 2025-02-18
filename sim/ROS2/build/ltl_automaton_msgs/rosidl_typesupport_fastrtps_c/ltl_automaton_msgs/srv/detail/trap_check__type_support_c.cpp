// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from ltl_automaton_msgs:srv/TrapCheck.idl
// generated code does not contain a copyright notice
#include "ltl_automaton_msgs/srv/detail/trap_check__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "ltl_automaton_msgs/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "ltl_automaton_msgs/srv/detail/trap_check__struct.h"
#include "ltl_automaton_msgs/srv/detail/trap_check__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif

#include "ltl_automaton_msgs/msg/detail/transition_system_state__functions.h"  // ts_state

// forward declare type support functions
size_t get_serialized_size_ltl_automaton_msgs__msg__TransitionSystemState(
  const void * untyped_ros_message,
  size_t current_alignment);

size_t max_serialized_size_ltl_automaton_msgs__msg__TransitionSystemState(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ltl_automaton_msgs, msg, TransitionSystemState)();


using _TrapCheck_Request__ros_msg_type = ltl_automaton_msgs__srv__TrapCheck_Request;

static bool _TrapCheck_Request__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _TrapCheck_Request__ros_msg_type * ros_message = static_cast<const _TrapCheck_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: ts_state
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ltl_automaton_msgs, msg, TransitionSystemState
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->ts_state, cdr))
    {
      return false;
    }
  }

  return true;
}

static bool _TrapCheck_Request__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _TrapCheck_Request__ros_msg_type * ros_message = static_cast<_TrapCheck_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: ts_state
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ltl_automaton_msgs, msg, TransitionSystemState
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->ts_state))
    {
      return false;
    }
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ltl_automaton_msgs
size_t get_serialized_size_ltl_automaton_msgs__srv__TrapCheck_Request(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _TrapCheck_Request__ros_msg_type * ros_message = static_cast<const _TrapCheck_Request__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name ts_state

  current_alignment += get_serialized_size_ltl_automaton_msgs__msg__TransitionSystemState(
    &(ros_message->ts_state), current_alignment);

  return current_alignment - initial_alignment;
}

static uint32_t _TrapCheck_Request__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_ltl_automaton_msgs__srv__TrapCheck_Request(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ltl_automaton_msgs
size_t max_serialized_size_ltl_automaton_msgs__srv__TrapCheck_Request(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  size_t last_member_size = 0;
  (void)last_member_size;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;

  // member: ts_state
  {
    size_t array_size = 1;


    last_member_size = 0;
    for (size_t index = 0; index < array_size; ++index) {
      bool inner_full_bounded;
      bool inner_is_plain;
      size_t inner_size;
      inner_size =
        max_serialized_size_ltl_automaton_msgs__msg__TransitionSystemState(
        inner_full_bounded, inner_is_plain, current_alignment);
      last_member_size += inner_size;
      current_alignment += inner_size;
      full_bounded &= inner_full_bounded;
      is_plain &= inner_is_plain;
    }
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = ltl_automaton_msgs__srv__TrapCheck_Request;
    is_plain =
      (
      offsetof(DataType, ts_state) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _TrapCheck_Request__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_ltl_automaton_msgs__srv__TrapCheck_Request(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_TrapCheck_Request = {
  "ltl_automaton_msgs::srv",
  "TrapCheck_Request",
  _TrapCheck_Request__cdr_serialize,
  _TrapCheck_Request__cdr_deserialize,
  _TrapCheck_Request__get_serialized_size,
  _TrapCheck_Request__max_serialized_size
};

static rosidl_message_type_support_t _TrapCheck_Request__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_TrapCheck_Request,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ltl_automaton_msgs, srv, TrapCheck_Request)() {
  return &_TrapCheck_Request__type_support;
}

#if defined(__cplusplus)
}
#endif

// already included above
// #include <cassert>
// already included above
// #include <limits>
// already included above
// #include <string>
// already included above
// #include "rosidl_typesupport_fastrtps_c/identifier.h"
// already included above
// #include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
// already included above
// #include "ltl_automaton_msgs/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
// already included above
// #include "ltl_automaton_msgs/srv/detail/trap_check__struct.h"
// already included above
// #include "ltl_automaton_msgs/srv/detail/trap_check__functions.h"
// already included above
// #include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif


// forward declare type support functions


using _TrapCheck_Response__ros_msg_type = ltl_automaton_msgs__srv__TrapCheck_Response;

static bool _TrapCheck_Response__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _TrapCheck_Response__ros_msg_type * ros_message = static_cast<const _TrapCheck_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: is_connected
  {
    cdr << (ros_message->is_connected ? true : false);
  }

  // Field name: is_trap
  {
    cdr << (ros_message->is_trap ? true : false);
  }

  return true;
}

static bool _TrapCheck_Response__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _TrapCheck_Response__ros_msg_type * ros_message = static_cast<_TrapCheck_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: is_connected
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->is_connected = tmp ? true : false;
  }

  // Field name: is_trap
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->is_trap = tmp ? true : false;
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ltl_automaton_msgs
size_t get_serialized_size_ltl_automaton_msgs__srv__TrapCheck_Response(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _TrapCheck_Response__ros_msg_type * ros_message = static_cast<const _TrapCheck_Response__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name is_connected
  {
    size_t item_size = sizeof(ros_message->is_connected);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name is_trap
  {
    size_t item_size = sizeof(ros_message->is_trap);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _TrapCheck_Response__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_ltl_automaton_msgs__srv__TrapCheck_Response(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ltl_automaton_msgs
size_t max_serialized_size_ltl_automaton_msgs__srv__TrapCheck_Response(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  size_t last_member_size = 0;
  (void)last_member_size;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;

  // member: is_connected
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: is_trap
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = ltl_automaton_msgs__srv__TrapCheck_Response;
    is_plain =
      (
      offsetof(DataType, is_trap) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _TrapCheck_Response__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_ltl_automaton_msgs__srv__TrapCheck_Response(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_TrapCheck_Response = {
  "ltl_automaton_msgs::srv",
  "TrapCheck_Response",
  _TrapCheck_Response__cdr_serialize,
  _TrapCheck_Response__cdr_deserialize,
  _TrapCheck_Response__get_serialized_size,
  _TrapCheck_Response__max_serialized_size
};

static rosidl_message_type_support_t _TrapCheck_Response__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_TrapCheck_Response,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ltl_automaton_msgs, srv, TrapCheck_Response)() {
  return &_TrapCheck_Response__type_support;
}

#if defined(__cplusplus)
}
#endif

#include "rosidl_typesupport_fastrtps_cpp/service_type_support.h"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_c/identifier.h"
// already included above
// #include "ltl_automaton_msgs/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "ltl_automaton_msgs/srv/trap_check.h"

#if defined(__cplusplus)
extern "C"
{
#endif

static service_type_support_callbacks_t TrapCheck__callbacks = {
  "ltl_automaton_msgs::srv",
  "TrapCheck",
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ltl_automaton_msgs, srv, TrapCheck_Request)(),
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ltl_automaton_msgs, srv, TrapCheck_Response)(),
};

static rosidl_service_type_support_t TrapCheck__handle = {
  rosidl_typesupport_fastrtps_c__identifier,
  &TrapCheck__callbacks,
  get_service_typesupport_handle_function,
};

const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ltl_automaton_msgs, srv, TrapCheck)() {
  return &TrapCheck__handle;
}

#if defined(__cplusplus)
}
#endif
