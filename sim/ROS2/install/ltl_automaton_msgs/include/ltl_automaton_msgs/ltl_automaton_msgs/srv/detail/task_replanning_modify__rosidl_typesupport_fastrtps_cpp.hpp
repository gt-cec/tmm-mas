// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__rosidl_typesupport_fastrtps_cpp.hpp.em
// with input from ltl_automaton_msgs:srv/TaskReplanningModify.idl
// generated code does not contain a copyright notice

#ifndef LTL_AUTOMATON_MSGS__SRV__DETAIL__TASK_REPLANNING_MODIFY__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
#define LTL_AUTOMATON_MSGS__SRV__DETAIL__TASK_REPLANNING_MODIFY__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_

#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "ltl_automaton_msgs/msg/rosidl_typesupport_fastrtps_cpp__visibility_control.h"
#include "ltl_automaton_msgs/srv/detail/task_replanning_modify__struct.hpp"

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

#include "fastcdr/Cdr.h"

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
  eprosima::fastcdr::Cdr & cdr);

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ltl_automaton_msgs
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  ltl_automaton_msgs::srv::TaskReplanningModify_Request & ros_message);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ltl_automaton_msgs
get_serialized_size(
  const ltl_automaton_msgs::srv::TaskReplanningModify_Request & ros_message,
  size_t current_alignment);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ltl_automaton_msgs
max_serialized_size_TaskReplanningModify_Request(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

}  // namespace typesupport_fastrtps_cpp

}  // namespace srv

}  // namespace ltl_automaton_msgs

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ltl_automaton_msgs
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, ltl_automaton_msgs, srv, TaskReplanningModify_Request)();

#ifdef __cplusplus
}
#endif

// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"
// already included above
// #include "ltl_automaton_msgs/msg/rosidl_typesupport_fastrtps_cpp__visibility_control.h"
// already included above
// #include "ltl_automaton_msgs/srv/detail/task_replanning_modify__struct.hpp"

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

// already included above
// #include "fastcdr/Cdr.h"

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
  eprosima::fastcdr::Cdr & cdr);

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ltl_automaton_msgs
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  ltl_automaton_msgs::srv::TaskReplanningModify_Response & ros_message);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ltl_automaton_msgs
get_serialized_size(
  const ltl_automaton_msgs::srv::TaskReplanningModify_Response & ros_message,
  size_t current_alignment);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ltl_automaton_msgs
max_serialized_size_TaskReplanningModify_Response(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

}  // namespace typesupport_fastrtps_cpp

}  // namespace srv

}  // namespace ltl_automaton_msgs

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ltl_automaton_msgs
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, ltl_automaton_msgs, srv, TaskReplanningModify_Response)();

#ifdef __cplusplus
}
#endif

#include "rmw/types.h"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_interface/macros.h"
// already included above
// #include "ltl_automaton_msgs/msg/rosidl_typesupport_fastrtps_cpp__visibility_control.h"

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_ltl_automaton_msgs
const rosidl_service_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, ltl_automaton_msgs, srv, TaskReplanningModify)();

#ifdef __cplusplus
}
#endif

#endif  // LTL_AUTOMATON_MSGS__SRV__DETAIL__TASK_REPLANNING_MODIFY__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
