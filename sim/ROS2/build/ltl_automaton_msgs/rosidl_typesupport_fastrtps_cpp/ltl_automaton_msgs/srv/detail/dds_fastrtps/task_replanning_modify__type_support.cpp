// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from ltl_automaton_msgs:srv/TaskReplanningModify.idl
// generated code does not contain a copyright notice
#include "ltl_automaton_msgs/srv/detail/task_replanning_modify__rosidl_typesupport_fastrtps_cpp.hpp"
#include "ltl_automaton_msgs/srv/detail/task_replanning_modify__struct.hpp"

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
namespace ltl_automaton_msgs
{
namespace msg
{
namespace typesupport_fastrtps_cpp
{
bool cdr_serialize(
  const ltl_automaton_msgs::msg::TransitionSystemState &,
  eprosima::fastcdr::Cdr &);
bool cdr_deserialize(
  eprosima::fastcdr::Cdr &,
  ltl_automaton_msgs::msg::TransitionSystemState &);
size_t get_serialized_size(
  const ltl_automaton_msgs::msg::TransitionSystemState &,
  size_t current_alignment);
size_t
max_serialized_size_TransitionSystemState(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);
}  // namespace typesupport_fastrtps_cpp
}  // namespace msg
}  // namespace ltl_automaton_msgs


namespace ltl_automaton_msgs
{

namespace srv
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ltl_automaton_msgs
cdr_serialize(
  const ltl_automaton_msgs::srv::TaskReplanningModify_Request & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: mod_from
  {
    cdr << ros_message.mod_from;
  }
  // Member: mod_to
  {
    cdr << ros_message.mod_to;
  }
  // Member: cost
  cdr << ros_message.cost;
  // Member: current_state
  ltl_automaton_msgs::msg::typesupport_fastrtps_cpp::cdr_serialize(
    ros_message.current_state,
    cdr);
  // Member: exec_index
  cdr << ros_message.exec_index;
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ltl_automaton_msgs
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  ltl_automaton_msgs::srv::TaskReplanningModify_Request & ros_message)
{
  // Member: mod_from
  {
    cdr >> ros_message.mod_from;
  }

  // Member: mod_to
  {
    cdr >> ros_message.mod_to;
  }

  // Member: cost
  cdr >> ros_message.cost;

  // Member: current_state
  ltl_automaton_msgs::msg::typesupport_fastrtps_cpp::cdr_deserialize(
    cdr, ros_message.current_state);

  // Member: exec_index
  cdr >> ros_message.exec_index;

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ltl_automaton_msgs
get_serialized_size(
  const ltl_automaton_msgs::srv::TaskReplanningModify_Request & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: mod_from
  {
    size_t array_size = ros_message.mod_from.size();

    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    size_t item_size = sizeof(ros_message.mod_from[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: mod_to
  {
    size_t array_size = ros_message.mod_to.size();

    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    size_t item_size = sizeof(ros_message.mod_to[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: cost
  {
    size_t item_size = sizeof(ros_message.cost);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: current_state

  current_alignment +=
    ltl_automaton_msgs::msg::typesupport_fastrtps_cpp::get_serialized_size(
    ros_message.current_state, current_alignment);
  // Member: exec_index
  {
    size_t item_size = sizeof(ros_message.exec_index);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ltl_automaton_msgs
max_serialized_size_TaskReplanningModify_Request(
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


  // Member: mod_from
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

  // Member: mod_to
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

  // Member: cost
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: current_state
  {
    size_t array_size = 1;


    last_member_size = 0;
    for (size_t index = 0; index < array_size; ++index) {
      bool inner_full_bounded;
      bool inner_is_plain;
      size_t inner_size =
        ltl_automaton_msgs::msg::typesupport_fastrtps_cpp::max_serialized_size_TransitionSystemState(
        inner_full_bounded, inner_is_plain, current_alignment);
      last_member_size += inner_size;
      current_alignment += inner_size;
      full_bounded &= inner_full_bounded;
      is_plain &= inner_is_plain;
    }
  }

  // Member: exec_index
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
    using DataType = ltl_automaton_msgs::srv::TaskReplanningModify_Request;
    is_plain =
      (
      offsetof(DataType, exec_index) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static bool _TaskReplanningModify_Request__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const ltl_automaton_msgs::srv::TaskReplanningModify_Request *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _TaskReplanningModify_Request__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<ltl_automaton_msgs::srv::TaskReplanningModify_Request *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _TaskReplanningModify_Request__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const ltl_automaton_msgs::srv::TaskReplanningModify_Request *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _TaskReplanningModify_Request__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_TaskReplanningModify_Request(full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}

static message_type_support_callbacks_t _TaskReplanningModify_Request__callbacks = {
  "ltl_automaton_msgs::srv",
  "TaskReplanningModify_Request",
  _TaskReplanningModify_Request__cdr_serialize,
  _TaskReplanningModify_Request__cdr_deserialize,
  _TaskReplanningModify_Request__get_serialized_size,
  _TaskReplanningModify_Request__max_serialized_size
};

static rosidl_message_type_support_t _TaskReplanningModify_Request__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_TaskReplanningModify_Request__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace srv

}  // namespace ltl_automaton_msgs

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_ltl_automaton_msgs
const rosidl_message_type_support_t *
get_message_type_support_handle<ltl_automaton_msgs::srv::TaskReplanningModify_Request>()
{
  return &ltl_automaton_msgs::srv::typesupport_fastrtps_cpp::_TaskReplanningModify_Request__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, ltl_automaton_msgs, srv, TaskReplanningModify_Request)() {
  return &ltl_automaton_msgs::srv::typesupport_fastrtps_cpp::_TaskReplanningModify_Request__handle;
}

#ifdef __cplusplus
}
#endif

// already included above
// #include <limits>
// already included above
// #include <stdexcept>
// already included above
// #include <string>
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
// already included above
// #include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions
namespace ltl_automaton_msgs
{
namespace msg
{
namespace typesupport_fastrtps_cpp
{
bool cdr_serialize(
  const ltl_automaton_msgs::msg::LTLPlan &,
  eprosima::fastcdr::Cdr &);
bool cdr_deserialize(
  eprosima::fastcdr::Cdr &,
  ltl_automaton_msgs::msg::LTLPlan &);
size_t get_serialized_size(
  const ltl_automaton_msgs::msg::LTLPlan &,
  size_t current_alignment);
size_t
max_serialized_size_LTLPlan(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);
}  // namespace typesupport_fastrtps_cpp
}  // namespace msg
}  // namespace ltl_automaton_msgs

// functions for ltl_automaton_msgs::msg::LTLPlan already declared above


namespace ltl_automaton_msgs
{

namespace srv
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ltl_automaton_msgs
cdr_serialize(
  const ltl_automaton_msgs::srv::TaskReplanningModify_Response & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: success
  cdr << (ros_message.success ? true : false);
  // Member: new_plan_prefix
  ltl_automaton_msgs::msg::typesupport_fastrtps_cpp::cdr_serialize(
    ros_message.new_plan_prefix,
    cdr);
  // Member: new_plan_suffix
  ltl_automaton_msgs::msg::typesupport_fastrtps_cpp::cdr_serialize(
    ros_message.new_plan_suffix,
    cdr);
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ltl_automaton_msgs
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  ltl_automaton_msgs::srv::TaskReplanningModify_Response & ros_message)
{
  // Member: success
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.success = tmp ? true : false;
  }

  // Member: new_plan_prefix
  ltl_automaton_msgs::msg::typesupport_fastrtps_cpp::cdr_deserialize(
    cdr, ros_message.new_plan_prefix);

  // Member: new_plan_suffix
  ltl_automaton_msgs::msg::typesupport_fastrtps_cpp::cdr_deserialize(
    cdr, ros_message.new_plan_suffix);

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ltl_automaton_msgs
get_serialized_size(
  const ltl_automaton_msgs::srv::TaskReplanningModify_Response & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: success
  {
    size_t item_size = sizeof(ros_message.success);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: new_plan_prefix

  current_alignment +=
    ltl_automaton_msgs::msg::typesupport_fastrtps_cpp::get_serialized_size(
    ros_message.new_plan_prefix, current_alignment);
  // Member: new_plan_suffix

  current_alignment +=
    ltl_automaton_msgs::msg::typesupport_fastrtps_cpp::get_serialized_size(
    ros_message.new_plan_suffix, current_alignment);

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ltl_automaton_msgs
max_serialized_size_TaskReplanningModify_Response(
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


  // Member: success
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: new_plan_prefix
  {
    size_t array_size = 1;


    last_member_size = 0;
    for (size_t index = 0; index < array_size; ++index) {
      bool inner_full_bounded;
      bool inner_is_plain;
      size_t inner_size =
        ltl_automaton_msgs::msg::typesupport_fastrtps_cpp::max_serialized_size_LTLPlan(
        inner_full_bounded, inner_is_plain, current_alignment);
      last_member_size += inner_size;
      current_alignment += inner_size;
      full_bounded &= inner_full_bounded;
      is_plain &= inner_is_plain;
    }
  }

  // Member: new_plan_suffix
  {
    size_t array_size = 1;


    last_member_size = 0;
    for (size_t index = 0; index < array_size; ++index) {
      bool inner_full_bounded;
      bool inner_is_plain;
      size_t inner_size =
        ltl_automaton_msgs::msg::typesupport_fastrtps_cpp::max_serialized_size_LTLPlan(
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
    using DataType = ltl_automaton_msgs::srv::TaskReplanningModify_Response;
    is_plain =
      (
      offsetof(DataType, new_plan_suffix) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static bool _TaskReplanningModify_Response__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const ltl_automaton_msgs::srv::TaskReplanningModify_Response *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _TaskReplanningModify_Response__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<ltl_automaton_msgs::srv::TaskReplanningModify_Response *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _TaskReplanningModify_Response__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const ltl_automaton_msgs::srv::TaskReplanningModify_Response *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _TaskReplanningModify_Response__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_TaskReplanningModify_Response(full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}

static message_type_support_callbacks_t _TaskReplanningModify_Response__callbacks = {
  "ltl_automaton_msgs::srv",
  "TaskReplanningModify_Response",
  _TaskReplanningModify_Response__cdr_serialize,
  _TaskReplanningModify_Response__cdr_deserialize,
  _TaskReplanningModify_Response__get_serialized_size,
  _TaskReplanningModify_Response__max_serialized_size
};

static rosidl_message_type_support_t _TaskReplanningModify_Response__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_TaskReplanningModify_Response__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace srv

}  // namespace ltl_automaton_msgs

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_ltl_automaton_msgs
const rosidl_message_type_support_t *
get_message_type_support_handle<ltl_automaton_msgs::srv::TaskReplanningModify_Response>()
{
  return &ltl_automaton_msgs::srv::typesupport_fastrtps_cpp::_TaskReplanningModify_Response__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, ltl_automaton_msgs, srv, TaskReplanningModify_Response)() {
  return &ltl_automaton_msgs::srv::typesupport_fastrtps_cpp::_TaskReplanningModify_Response__handle;
}

#ifdef __cplusplus
}
#endif

#include "rmw/error_handling.h"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/service_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/service_type_support_decl.hpp"

namespace ltl_automaton_msgs
{

namespace srv
{

namespace typesupport_fastrtps_cpp
{

static service_type_support_callbacks_t _TaskReplanningModify__callbacks = {
  "ltl_automaton_msgs::srv",
  "TaskReplanningModify",
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, ltl_automaton_msgs, srv, TaskReplanningModify_Request)(),
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, ltl_automaton_msgs, srv, TaskReplanningModify_Response)(),
};

static rosidl_service_type_support_t _TaskReplanningModify__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_TaskReplanningModify__callbacks,
  get_service_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace srv

}  // namespace ltl_automaton_msgs

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_ltl_automaton_msgs
const rosidl_service_type_support_t *
get_service_type_support_handle<ltl_automaton_msgs::srv::TaskReplanningModify>()
{
  return &ltl_automaton_msgs::srv::typesupport_fastrtps_cpp::_TaskReplanningModify__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, ltl_automaton_msgs, srv, TaskReplanningModify)() {
  return &ltl_automaton_msgs::srv::typesupport_fastrtps_cpp::_TaskReplanningModify__handle;
}

#ifdef __cplusplus
}
#endif
