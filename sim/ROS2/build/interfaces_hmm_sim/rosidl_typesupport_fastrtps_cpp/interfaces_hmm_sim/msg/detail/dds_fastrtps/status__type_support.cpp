// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from interfaces_hmm_sim:msg/Status.idl
// generated code does not contain a copyright notice
#include "interfaces_hmm_sim/msg/detail/status__rosidl_typesupport_fastrtps_cpp.hpp"
#include "interfaces_hmm_sim/msg/detail/status__struct.hpp"

#include <limits>
#include <stdexcept>
#include <string>
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
#include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions

namespace interfaces_hmm_sim
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_interfaces_hmm_sim
cdr_serialize(
  const interfaces_hmm_sim::msg::Status & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: agent
  cdr << ros_message.agent;
  // Member: start
  cdr << (ros_message.start ? true : false);
  // Member: arrived
  cdr << (ros_message.arrived ? true : false);
  // Member: replan_received
  cdr << (ros_message.replan_received ? true : false);
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_interfaces_hmm_sim
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  interfaces_hmm_sim::msg::Status & ros_message)
{
  // Member: agent
  cdr >> ros_message.agent;

  // Member: start
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.start = tmp ? true : false;
  }

  // Member: arrived
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.arrived = tmp ? true : false;
  }

  // Member: replan_received
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.replan_received = tmp ? true : false;
  }

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_interfaces_hmm_sim
get_serialized_size(
  const interfaces_hmm_sim::msg::Status & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: agent
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message.agent.size() + 1);
  // Member: start
  {
    size_t item_size = sizeof(ros_message.start);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: arrived
  {
    size_t item_size = sizeof(ros_message.arrived);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: replan_received
  {
    size_t item_size = sizeof(ros_message.replan_received);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_interfaces_hmm_sim
max_serialized_size_Status(
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


  // Member: agent
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

  // Member: start
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: arrived
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: replan_received
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
    using DataType = interfaces_hmm_sim::msg::Status;
    is_plain =
      (
      offsetof(DataType, replan_received) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static bool _Status__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const interfaces_hmm_sim::msg::Status *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _Status__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<interfaces_hmm_sim::msg::Status *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _Status__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const interfaces_hmm_sim::msg::Status *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _Status__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_Status(full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}

static message_type_support_callbacks_t _Status__callbacks = {
  "interfaces_hmm_sim::msg",
  "Status",
  _Status__cdr_serialize,
  _Status__cdr_deserialize,
  _Status__get_serialized_size,
  _Status__max_serialized_size
};

static rosidl_message_type_support_t _Status__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_Status__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace interfaces_hmm_sim

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_interfaces_hmm_sim
const rosidl_message_type_support_t *
get_message_type_support_handle<interfaces_hmm_sim::msg::Status>()
{
  return &interfaces_hmm_sim::msg::typesupport_fastrtps_cpp::_Status__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, interfaces_hmm_sim, msg, Status)() {
  return &interfaces_hmm_sim::msg::typesupport_fastrtps_cpp::_Status__handle;
}

#ifdef __cplusplus
}
#endif
