// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from ltl_automaton_msgs:msg/LTLState.idl
// generated code does not contain a copyright notice

#ifndef LTL_AUTOMATON_MSGS__MSG__DETAIL__LTL_STATE__TRAITS_HPP_
#define LTL_AUTOMATON_MSGS__MSG__DETAIL__LTL_STATE__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "ltl_automaton_msgs/msg/detail/ltl_state__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'ts_state'
#include "ltl_automaton_msgs/msg/detail/transition_system_state__traits.hpp"

namespace ltl_automaton_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const LTLState & msg,
  std::ostream & out)
{
  out << "{";
  // member: ts_state
  {
    out << "ts_state: ";
    to_flow_style_yaml(msg.ts_state, out);
    out << ", ";
  }

  // member: buchi_state
  {
    out << "buchi_state: ";
    rosidl_generator_traits::value_to_yaml(msg.buchi_state, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const LTLState & msg,
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

  // member: buchi_state
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "buchi_state: ";
    rosidl_generator_traits::value_to_yaml(msg.buchi_state, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const LTLState & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace ltl_automaton_msgs

namespace rosidl_generator_traits
{

[[deprecated("use ltl_automaton_msgs::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const ltl_automaton_msgs::msg::LTLState & msg,
  std::ostream & out, size_t indentation = 0)
{
  ltl_automaton_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use ltl_automaton_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const ltl_automaton_msgs::msg::LTLState & msg)
{
  return ltl_automaton_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<ltl_automaton_msgs::msg::LTLState>()
{
  return "ltl_automaton_msgs::msg::LTLState";
}

template<>
inline const char * name<ltl_automaton_msgs::msg::LTLState>()
{
  return "ltl_automaton_msgs/msg/LTLState";
}

template<>
struct has_fixed_size<ltl_automaton_msgs::msg::LTLState>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<ltl_automaton_msgs::msg::LTLState>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<ltl_automaton_msgs::msg::LTLState>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // LTL_AUTOMATON_MSGS__MSG__DETAIL__LTL_STATE__TRAITS_HPP_
