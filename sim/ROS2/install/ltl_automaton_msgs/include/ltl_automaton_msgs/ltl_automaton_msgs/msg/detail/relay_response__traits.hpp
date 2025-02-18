// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from ltl_automaton_msgs:msg/RelayResponse.idl
// generated code does not contain a copyright notice

#ifndef LTL_AUTOMATON_MSGS__MSG__DETAIL__RELAY_RESPONSE__TRAITS_HPP_
#define LTL_AUTOMATON_MSGS__MSG__DETAIL__RELAY_RESPONSE__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "ltl_automaton_msgs/msg/detail/relay_response__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'new_plan_prefix'
// Member 'new_plan_suffix'
#include "ltl_automaton_msgs/msg/detail/ltl_plan__traits.hpp"

namespace ltl_automaton_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const RelayResponse & msg,
  std::ostream & out)
{
  out << "{";
  // member: success
  {
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
    out << ", ";
  }

  // member: new_plan_prefix
  {
    out << "new_plan_prefix: ";
    to_flow_style_yaml(msg.new_plan_prefix, out);
    out << ", ";
  }

  // member: new_plan_suffix
  {
    out << "new_plan_suffix: ";
    to_flow_style_yaml(msg.new_plan_suffix, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const RelayResponse & msg,
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

  // member: new_plan_prefix
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "new_plan_prefix:\n";
    to_block_style_yaml(msg.new_plan_prefix, out, indentation + 2);
  }

  // member: new_plan_suffix
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "new_plan_suffix:\n";
    to_block_style_yaml(msg.new_plan_suffix, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const RelayResponse & msg, bool use_flow_style = false)
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
  const ltl_automaton_msgs::msg::RelayResponse & msg,
  std::ostream & out, size_t indentation = 0)
{
  ltl_automaton_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use ltl_automaton_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const ltl_automaton_msgs::msg::RelayResponse & msg)
{
  return ltl_automaton_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<ltl_automaton_msgs::msg::RelayResponse>()
{
  return "ltl_automaton_msgs::msg::RelayResponse";
}

template<>
inline const char * name<ltl_automaton_msgs::msg::RelayResponse>()
{
  return "ltl_automaton_msgs/msg/RelayResponse";
}

template<>
struct has_fixed_size<ltl_automaton_msgs::msg::RelayResponse>
  : std::integral_constant<bool, has_fixed_size<ltl_automaton_msgs::msg::LTLPlan>::value> {};

template<>
struct has_bounded_size<ltl_automaton_msgs::msg::RelayResponse>
  : std::integral_constant<bool, has_bounded_size<ltl_automaton_msgs::msg::LTLPlan>::value> {};

template<>
struct is_message<ltl_automaton_msgs::msg::RelayResponse>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // LTL_AUTOMATON_MSGS__MSG__DETAIL__RELAY_RESPONSE__TRAITS_HPP_
