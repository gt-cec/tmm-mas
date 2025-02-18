// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from ltl_automaton_msgs:srv/TaskPlanning.idl
// generated code does not contain a copyright notice

#ifndef LTL_AUTOMATON_MSGS__SRV__DETAIL__TASK_PLANNING__TRAITS_HPP_
#define LTL_AUTOMATON_MSGS__SRV__DETAIL__TASK_PLANNING__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "ltl_automaton_msgs/srv/detail/task_planning__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace ltl_automaton_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const TaskPlanning_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: hard_task
  {
    out << "hard_task: ";
    rosidl_generator_traits::value_to_yaml(msg.hard_task, out);
    out << ", ";
  }

  // member: soft_task
  {
    out << "soft_task: ";
    rosidl_generator_traits::value_to_yaml(msg.soft_task, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const TaskPlanning_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: hard_task
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "hard_task: ";
    rosidl_generator_traits::value_to_yaml(msg.hard_task, out);
    out << "\n";
  }

  // member: soft_task
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "soft_task: ";
    rosidl_generator_traits::value_to_yaml(msg.soft_task, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const TaskPlanning_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace ltl_automaton_msgs

namespace rosidl_generator_traits
{

[[deprecated("use ltl_automaton_msgs::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const ltl_automaton_msgs::srv::TaskPlanning_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  ltl_automaton_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use ltl_automaton_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const ltl_automaton_msgs::srv::TaskPlanning_Request & msg)
{
  return ltl_automaton_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<ltl_automaton_msgs::srv::TaskPlanning_Request>()
{
  return "ltl_automaton_msgs::srv::TaskPlanning_Request";
}

template<>
inline const char * name<ltl_automaton_msgs::srv::TaskPlanning_Request>()
{
  return "ltl_automaton_msgs/srv/TaskPlanning_Request";
}

template<>
struct has_fixed_size<ltl_automaton_msgs::srv::TaskPlanning_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<ltl_automaton_msgs::srv::TaskPlanning_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<ltl_automaton_msgs::srv::TaskPlanning_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace ltl_automaton_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const TaskPlanning_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: success
  {
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const TaskPlanning_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: success
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const TaskPlanning_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace ltl_automaton_msgs

namespace rosidl_generator_traits
{

[[deprecated("use ltl_automaton_msgs::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const ltl_automaton_msgs::srv::TaskPlanning_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  ltl_automaton_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use ltl_automaton_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const ltl_automaton_msgs::srv::TaskPlanning_Response & msg)
{
  return ltl_automaton_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<ltl_automaton_msgs::srv::TaskPlanning_Response>()
{
  return "ltl_automaton_msgs::srv::TaskPlanning_Response";
}

template<>
inline const char * name<ltl_automaton_msgs::srv::TaskPlanning_Response>()
{
  return "ltl_automaton_msgs/srv/TaskPlanning_Response";
}

template<>
struct has_fixed_size<ltl_automaton_msgs::srv::TaskPlanning_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<ltl_automaton_msgs::srv::TaskPlanning_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<ltl_automaton_msgs::srv::TaskPlanning_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<ltl_automaton_msgs::srv::TaskPlanning>()
{
  return "ltl_automaton_msgs::srv::TaskPlanning";
}

template<>
inline const char * name<ltl_automaton_msgs::srv::TaskPlanning>()
{
  return "ltl_automaton_msgs/srv/TaskPlanning";
}

template<>
struct has_fixed_size<ltl_automaton_msgs::srv::TaskPlanning>
  : std::integral_constant<
    bool,
    has_fixed_size<ltl_automaton_msgs::srv::TaskPlanning_Request>::value &&
    has_fixed_size<ltl_automaton_msgs::srv::TaskPlanning_Response>::value
  >
{
};

template<>
struct has_bounded_size<ltl_automaton_msgs::srv::TaskPlanning>
  : std::integral_constant<
    bool,
    has_bounded_size<ltl_automaton_msgs::srv::TaskPlanning_Request>::value &&
    has_bounded_size<ltl_automaton_msgs::srv::TaskPlanning_Response>::value
  >
{
};

template<>
struct is_service<ltl_automaton_msgs::srv::TaskPlanning>
  : std::true_type
{
};

template<>
struct is_service_request<ltl_automaton_msgs::srv::TaskPlanning_Request>
  : std::true_type
{
};

template<>
struct is_service_response<ltl_automaton_msgs::srv::TaskPlanning_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // LTL_AUTOMATON_MSGS__SRV__DETAIL__TASK_PLANNING__TRAITS_HPP_
