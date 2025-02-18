// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from ltl_automaton_msgs:srv/TaskReplanningDelete.idl
// generated code does not contain a copyright notice
#include "ltl_automaton_msgs/srv/detail/task_replanning_delete__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "ltl_automaton_msgs/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "ltl_automaton_msgs/srv/detail/task_replanning_delete__struct.h"
#include "ltl_automaton_msgs/srv/detail/task_replanning_delete__functions.h"
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

#include "ltl_automaton_msgs/msg/detail/transition_system_state__functions.h"  // current_state
#include "rosidl_runtime_c/primitives_sequence.h"  // delete_from, delete_to
#include "rosidl_runtime_c/primitives_sequence_functions.h"  // delete_from, delete_to

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


using _TaskReplanningDelete_Request__ros_msg_type = ltl_automaton_msgs__srv__TaskReplanningDelete_Request;

static bool _TaskReplanningDelete_Request__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _TaskReplanningDelete_Request__ros_msg_type * ros_message = static_cast<const _TaskReplanningDelete_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: delete_from
  {
    size_t size = ros_message->delete_from.size;
    auto array_ptr = ros_message->delete_from.data;
    cdr << static_cast<uint32_t>(size);
    cdr.serializeArray(array_ptr, size);
  }

  // Field name: delete_to
  {
    size_t size = ros_message->delete_to.size;
    auto array_ptr = ros_message->delete_to.data;
    cdr << static_cast<uint32_t>(size);
    cdr.serializeArray(array_ptr, size);
  }

  // Field name: current_state
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ltl_automaton_msgs, msg, TransitionSystemState
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->current_state, cdr))
    {
      return false;
    }
  }

  // Field name: exec_index
  {
    cdr << ros_message->exec_index;
  }

  return true;
}

static bool _TaskReplanningDelete_Request__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _TaskReplanningDelete_Request__ros_msg_type * ros_message = static_cast<_TaskReplanningDelete_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: delete_from
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->delete_from.data) {
      rosidl_runtime_c__int32__Sequence__fini(&ros_message->delete_from);
    }
    if (!rosidl_runtime_c__int32__Sequence__init(&ros_message->delete_from, size)) {
      fprintf(stderr, "failed to create array for field 'delete_from'");
      return false;
    }
    auto array_ptr = ros_message->delete_from.data;
    cdr.deserializeArray(array_ptr, size);
  }

  // Field name: delete_to
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->delete_to.data) {
      rosidl_runtime_c__int32__Sequence__fini(&ros_message->delete_to);
    }
    if (!rosidl_runtime_c__int32__Sequence__init(&ros_message->delete_to, size)) {
      fprintf(stderr, "failed to create array for field 'delete_to'");
      return false;
    }
    auto array_ptr = ros_message->delete_to.data;
    cdr.deserializeArray(array_ptr, size);
  }

  // Field name: current_state
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ltl_automaton_msgs, msg, TransitionSystemState
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->current_state))
    {
      return false;
    }
  }

  // Field name: exec_index
  {
    cdr >> ros_message->exec_index;
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ltl_automaton_msgs
size_t get_serialized_size_ltl_automaton_msgs__srv__TaskReplanningDelete_Request(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _TaskReplanningDelete_Request__ros_msg_type * ros_message = static_cast<const _TaskReplanningDelete_Request__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name delete_from
  {
    size_t array_size = ros_message->delete_from.size;
    auto array_ptr = ros_message->delete_from.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name delete_to
  {
    size_t array_size = ros_message->delete_to.size;
    auto array_ptr = ros_message->delete_to.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name current_state

  current_alignment += get_serialized_size_ltl_automaton_msgs__msg__TransitionSystemState(
    &(ros_message->current_state), current_alignment);
  // field.name exec_index
  {
    size_t item_size = sizeof(ros_message->exec_index);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _TaskReplanningDelete_Request__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_ltl_automaton_msgs__srv__TaskReplanningDelete_Request(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ltl_automaton_msgs
size_t max_serialized_size_ltl_automaton_msgs__srv__TaskReplanningDelete_Request(
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

  // member: delete_from
  {
    size_t array_size = 0;
    full_bounded = false;
    is_plain = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: delete_to
  {
    size_t array_size = 0;
    full_bounded = false;
    is_plain = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: current_state
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
  // member: exec_index
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = ltl_automaton_msgs__srv__TaskReplanningDelete_Request;
    is_plain =
      (
      offsetof(DataType, exec_index) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _TaskReplanningDelete_Request__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_ltl_automaton_msgs__srv__TaskReplanningDelete_Request(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_TaskReplanningDelete_Request = {
  "ltl_automaton_msgs::srv",
  "TaskReplanningDelete_Request",
  _TaskReplanningDelete_Request__cdr_serialize,
  _TaskReplanningDelete_Request__cdr_deserialize,
  _TaskReplanningDelete_Request__get_serialized_size,
  _TaskReplanningDelete_Request__max_serialized_size
};

static rosidl_message_type_support_t _TaskReplanningDelete_Request__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_TaskReplanningDelete_Request,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ltl_automaton_msgs, srv, TaskReplanningDelete_Request)() {
  return &_TaskReplanningDelete_Request__type_support;
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
// #include "ltl_automaton_msgs/srv/detail/task_replanning_delete__struct.h"
// already included above
// #include "ltl_automaton_msgs/srv/detail/task_replanning_delete__functions.h"
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

#include "ltl_automaton_msgs/msg/detail/ltl_plan__functions.h"  // new_plan_prefix, new_plan_suffix

// forward declare type support functions
size_t get_serialized_size_ltl_automaton_msgs__msg__LTLPlan(
  const void * untyped_ros_message,
  size_t current_alignment);

size_t max_serialized_size_ltl_automaton_msgs__msg__LTLPlan(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ltl_automaton_msgs, msg, LTLPlan)();


using _TaskReplanningDelete_Response__ros_msg_type = ltl_automaton_msgs__srv__TaskReplanningDelete_Response;

static bool _TaskReplanningDelete_Response__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _TaskReplanningDelete_Response__ros_msg_type * ros_message = static_cast<const _TaskReplanningDelete_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: success
  {
    cdr << (ros_message->success ? true : false);
  }

  // Field name: new_plan_prefix
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ltl_automaton_msgs, msg, LTLPlan
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->new_plan_prefix, cdr))
    {
      return false;
    }
  }

  // Field name: new_plan_suffix
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ltl_automaton_msgs, msg, LTLPlan
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->new_plan_suffix, cdr))
    {
      return false;
    }
  }

  return true;
}

static bool _TaskReplanningDelete_Response__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _TaskReplanningDelete_Response__ros_msg_type * ros_message = static_cast<_TaskReplanningDelete_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: success
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->success = tmp ? true : false;
  }

  // Field name: new_plan_prefix
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ltl_automaton_msgs, msg, LTLPlan
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->new_plan_prefix))
    {
      return false;
    }
  }

  // Field name: new_plan_suffix
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, ltl_automaton_msgs, msg, LTLPlan
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->new_plan_suffix))
    {
      return false;
    }
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ltl_automaton_msgs
size_t get_serialized_size_ltl_automaton_msgs__srv__TaskReplanningDelete_Response(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _TaskReplanningDelete_Response__ros_msg_type * ros_message = static_cast<const _TaskReplanningDelete_Response__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name success
  {
    size_t item_size = sizeof(ros_message->success);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name new_plan_prefix

  current_alignment += get_serialized_size_ltl_automaton_msgs__msg__LTLPlan(
    &(ros_message->new_plan_prefix), current_alignment);
  // field.name new_plan_suffix

  current_alignment += get_serialized_size_ltl_automaton_msgs__msg__LTLPlan(
    &(ros_message->new_plan_suffix), current_alignment);

  return current_alignment - initial_alignment;
}

static uint32_t _TaskReplanningDelete_Response__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_ltl_automaton_msgs__srv__TaskReplanningDelete_Response(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ltl_automaton_msgs
size_t max_serialized_size_ltl_automaton_msgs__srv__TaskReplanningDelete_Response(
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

  // member: success
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: new_plan_prefix
  {
    size_t array_size = 1;


    last_member_size = 0;
    for (size_t index = 0; index < array_size; ++index) {
      bool inner_full_bounded;
      bool inner_is_plain;
      size_t inner_size;
      inner_size =
        max_serialized_size_ltl_automaton_msgs__msg__LTLPlan(
        inner_full_bounded, inner_is_plain, current_alignment);
      last_member_size += inner_size;
      current_alignment += inner_size;
      full_bounded &= inner_full_bounded;
      is_plain &= inner_is_plain;
    }
  }
  // member: new_plan_suffix
  {
    size_t array_size = 1;


    last_member_size = 0;
    for (size_t index = 0; index < array_size; ++index) {
      bool inner_full_bounded;
      bool inner_is_plain;
      size_t inner_size;
      inner_size =
        max_serialized_size_ltl_automaton_msgs__msg__LTLPlan(
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
    using DataType = ltl_automaton_msgs__srv__TaskReplanningDelete_Response;
    is_plain =
      (
      offsetof(DataType, new_plan_suffix) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _TaskReplanningDelete_Response__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_ltl_automaton_msgs__srv__TaskReplanningDelete_Response(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_TaskReplanningDelete_Response = {
  "ltl_automaton_msgs::srv",
  "TaskReplanningDelete_Response",
  _TaskReplanningDelete_Response__cdr_serialize,
  _TaskReplanningDelete_Response__cdr_deserialize,
  _TaskReplanningDelete_Response__get_serialized_size,
  _TaskReplanningDelete_Response__max_serialized_size
};

static rosidl_message_type_support_t _TaskReplanningDelete_Response__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_TaskReplanningDelete_Response,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ltl_automaton_msgs, srv, TaskReplanningDelete_Response)() {
  return &_TaskReplanningDelete_Response__type_support;
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
#include "ltl_automaton_msgs/srv/task_replanning_delete.h"

#if defined(__cplusplus)
extern "C"
{
#endif

static service_type_support_callbacks_t TaskReplanningDelete__callbacks = {
  "ltl_automaton_msgs::srv",
  "TaskReplanningDelete",
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ltl_automaton_msgs, srv, TaskReplanningDelete_Request)(),
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ltl_automaton_msgs, srv, TaskReplanningDelete_Response)(),
};

static rosidl_service_type_support_t TaskReplanningDelete__handle = {
  rosidl_typesupport_fastrtps_c__identifier,
  &TaskReplanningDelete__callbacks,
  get_service_typesupport_handle_function,
};

const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ltl_automaton_msgs, srv, TaskReplanningDelete)() {
  return &TaskReplanningDelete__handle;
}

#if defined(__cplusplus)
}
#endif
