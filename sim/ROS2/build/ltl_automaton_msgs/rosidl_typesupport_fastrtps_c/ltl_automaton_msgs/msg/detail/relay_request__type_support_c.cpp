// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from ltl_automaton_msgs:msg/RelayRequest.idl
// generated code does not contain a copyright notice
#include "ltl_automaton_msgs/msg/detail/relay_request__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "ltl_automaton_msgs/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "ltl_automaton_msgs/msg/detail/relay_request__struct.h"
#include "ltl_automaton_msgs/msg/detail/relay_request__functions.h"
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
#include "rosidl_runtime_c/primitives_sequence.h"  // from_pose, to_pose
#include "rosidl_runtime_c/primitives_sequence_functions.h"  // from_pose, to_pose
#include "rosidl_runtime_c/string.h"  // type
#include "rosidl_runtime_c/string_functions.h"  // type

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


using _RelayRequest__ros_msg_type = ltl_automaton_msgs__msg__RelayRequest;

static bool _RelayRequest__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _RelayRequest__ros_msg_type * ros_message = static_cast<const _RelayRequest__ros_msg_type *>(untyped_ros_message);
  // Field name: from_pose
  {
    size_t size = ros_message->from_pose.size;
    auto array_ptr = ros_message->from_pose.data;
    cdr << static_cast<uint32_t>(size);
    cdr.serializeArray(array_ptr, size);
  }

  // Field name: to_pose
  {
    size_t size = ros_message->to_pose.size;
    auto array_ptr = ros_message->to_pose.data;
    cdr << static_cast<uint32_t>(size);
    cdr.serializeArray(array_ptr, size);
  }

  // Field name: cost
  {
    cdr << ros_message->cost;
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

  // Field name: type
  {
    const rosidl_runtime_c__String * str = &ros_message->type;
    if (str->capacity == 0 || str->capacity <= str->size) {
      fprintf(stderr, "string capacity not greater than size\n");
      return false;
    }
    if (str->data[str->size] != '\0') {
      fprintf(stderr, "string not null-terminated\n");
      return false;
    }
    cdr << str->data;
  }

  return true;
}

static bool _RelayRequest__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _RelayRequest__ros_msg_type * ros_message = static_cast<_RelayRequest__ros_msg_type *>(untyped_ros_message);
  // Field name: from_pose
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->from_pose.data) {
      rosidl_runtime_c__int32__Sequence__fini(&ros_message->from_pose);
    }
    if (!rosidl_runtime_c__int32__Sequence__init(&ros_message->from_pose, size)) {
      fprintf(stderr, "failed to create array for field 'from_pose'");
      return false;
    }
    auto array_ptr = ros_message->from_pose.data;
    cdr.deserializeArray(array_ptr, size);
  }

  // Field name: to_pose
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->to_pose.data) {
      rosidl_runtime_c__int32__Sequence__fini(&ros_message->to_pose);
    }
    if (!rosidl_runtime_c__int32__Sequence__init(&ros_message->to_pose, size)) {
      fprintf(stderr, "failed to create array for field 'to_pose'");
      return false;
    }
    auto array_ptr = ros_message->to_pose.data;
    cdr.deserializeArray(array_ptr, size);
  }

  // Field name: cost
  {
    cdr >> ros_message->cost;
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

  // Field name: type
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->type.data) {
      rosidl_runtime_c__String__init(&ros_message->type);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->type,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'type'\n");
      return false;
    }
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ltl_automaton_msgs
size_t get_serialized_size_ltl_automaton_msgs__msg__RelayRequest(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _RelayRequest__ros_msg_type * ros_message = static_cast<const _RelayRequest__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name from_pose
  {
    size_t array_size = ros_message->from_pose.size;
    auto array_ptr = ros_message->from_pose.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name to_pose
  {
    size_t array_size = ros_message->to_pose.size;
    auto array_ptr = ros_message->to_pose.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name cost
  {
    size_t item_size = sizeof(ros_message->cost);
    current_alignment += item_size +
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
  // field.name type
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->type.size + 1);

  return current_alignment - initial_alignment;
}

static uint32_t _RelayRequest__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_ltl_automaton_msgs__msg__RelayRequest(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_ltl_automaton_msgs
size_t max_serialized_size_ltl_automaton_msgs__msg__RelayRequest(
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

  // member: from_pose
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
  // member: to_pose
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
  // member: cost
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
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
  // member: type
  {
    size_t array_size = 1;

    full_bounded = false;
    is_plain = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = ltl_automaton_msgs__msg__RelayRequest;
    is_plain =
      (
      offsetof(DataType, type) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _RelayRequest__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_ltl_automaton_msgs__msg__RelayRequest(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_RelayRequest = {
  "ltl_automaton_msgs::msg",
  "RelayRequest",
  _RelayRequest__cdr_serialize,
  _RelayRequest__cdr_deserialize,
  _RelayRequest__get_serialized_size,
  _RelayRequest__max_serialized_size
};

static rosidl_message_type_support_t _RelayRequest__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_RelayRequest,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ltl_automaton_msgs, msg, RelayRequest)() {
  return &_RelayRequest__type_support;
}

#if defined(__cplusplus)
}
#endif
