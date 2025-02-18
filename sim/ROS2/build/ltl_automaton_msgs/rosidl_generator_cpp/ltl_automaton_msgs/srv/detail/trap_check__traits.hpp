// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from ltl_automaton_msgs:srv/TrapCheck.idl
// generated code does not contain a copyright notice

#ifndef LTL_AUTOMATON_MSGS__SRV__DETAIL__TRAP_CHECK__TRAITS_HPP_
#define LTL_AUTOMATON_MSGS__SRV__DETAIL__TRAP_CHECK__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "ltl_automaton_msgs/srv/detail/trap_check__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'ts_state'
#include "ltl_automaton_msgs/msg/detail/transition_system_state__traits.hpp"

namespace ltl_automaton_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const TrapCheck_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: ts_state
  {
    out << "ts_state: ";
    to_flow_style_yaml(msg.ts_state, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const TrapCheck_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: ts_state
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ts_state:\n";
    to_block_style_yaml(msg.ts_state, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const TrapCheck_Request & msg, bool use_flow_style = false)
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
  const ltl_automaton_msgs::srv::TrapCheck_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  ltl_automaton_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use ltl_automaton_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const ltl_automaton_msgs::srv::TrapCheck_Request & msg)
{
  return ltl_automaton_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<ltl_automaton_msgs::srv::TrapCheck_Request>()
{
  return "ltl_automaton_msgs::srv::TrapCheck_Request";
}

template<>
inline const char * name<ltl_automaton_msgs::srv::TrapCheck_Request>()
{
  return "ltl_automaton_msgs/srv/TrapCheck_Request";
}

template<>
struct has_fixed_size<ltl_automaton_msgs::srv::TrapCheck_Request>
  : std::integral_constant<bool, has_fixed_size<ltl_automaton_msgs::msg::TransitionSystemState>::value> {};

template<>
struct has_bounded_size<ltl_automaton_msgs::srv::TrapCheck_Request>
  : std::integral_constant<bool, has_bounded_size<ltl_automaton_msgs::msg::TransitionSystemState>::value> {};

template<>
struct is_message<ltl_automaton_msgs::srv::TrapCheck_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace ltl_automaton_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const TrapCheck_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: is_connected
  {
    out << "is_connected: ";
    rosidl_generator_traits::value_to_yaml(msg.is_connected, out);
    out << ", ";
  }

  // member: is_trap
  {
    out << "is_trap: ";
    rosidl_generator_traits::value_to_yaml(msg.is_trap, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const TrapCheck_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: is_connected
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "is_connected: ";
    rosidl_generator_traits::value_to_yaml(msg.is_connected, out);
    out << "\n";
  }

  // member: is_trap
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "is_trap: ";
    rosidl_generator_traits::value_to_yaml(msg.is_trap, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const TrapCheck_Response & msg, bool use_flow_style = false)
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
  const ltl_automaton_msgs::srv::TrapCheck_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  ltl_automaton_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use ltl_automaton_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const ltl_automaton_msgs::srv::TrapCheck_Response & msg)
{
  return ltl_automaton_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<ltl_automaton_msgs::srv::TrapCheck_Response>()
{
  return "ltl_automaton_msgs::srv::TrapCheck_Response";
}

template<>
inline const char * name<ltl_automaton_msgs::srv::TrapCheck_Response>()
{
  return "ltl_automaton_msgs/srv/TrapCheck_Response";
}

template<>
struct has_fixed_size<ltl_automaton_msgs::srv::TrapCheck_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<ltl_automaton_msgs::srv::TrapCheck_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<ltl_automaton_msgs::srv::TrapCheck_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<ltl_automaton_msgs::srv::TrapCheck>()
{
  return "ltl_automaton_msgs::srv::TrapCheck";
}

template<>
inline const char * name<ltl_automaton_msgs::srv::TrapCheck>()
{
  return "ltl_automaton_msgs/srv/TrapCheck";
}

template<>
struct has_fixed_size<ltl_automaton_msgs::srv::TrapCheck>
  : std::integral_constant<
    bool,
    has_fixed_size<ltl_automaton_msgs::srv::TrapCheck_Request>::value &&
    has_fixed_size<ltl_automaton_msgs::srv::TrapCheck_Response>::value
  >
{
};

template<>
struct has_bounded_size<ltl_automaton_msgs::srv::TrapCheck>
  : std::integral_constant<
    bool,
    has_bounded_size<ltl_automaton_msgs::srv::TrapCheck_Request>::value &&
    has_bounded_size<ltl_automaton_msgs::srv::TrapCheck_Response>::value
  >
{
};

template<>
struct is_service<ltl_automaton_msgs::srv::TrapCheck>
  : std::true_type
{
};

template<>
struct is_service_request<ltl_automaton_msgs::srv::TrapCheck_Request>
  : std::true_type
{
};

template<>
struct is_service_response<ltl_automaton_msgs::srv::TrapCheck_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // LTL_AUTOMATON_MSGS__SRV__DETAIL__TRAP_CHECK__TRAITS_HPP_
