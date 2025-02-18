// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from ltl_automaton_msgs:msg/LTLStateArray.idl
// generated code does not contain a copyright notice

#ifndef LTL_AUTOMATON_MSGS__MSG__DETAIL__LTL_STATE_ARRAY__TRAITS_HPP_
#define LTL_AUTOMATON_MSGS__MSG__DETAIL__LTL_STATE_ARRAY__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "ltl_automaton_msgs/msg/detail/ltl_state_array__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'ltl_states'
#include "ltl_automaton_msgs/msg/detail/ltl_state__traits.hpp"

namespace ltl_automaton_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const LTLStateArray & msg,
  std::ostream & out)
{
  out << "{";
  // member: ltl_states
  {
    if (msg.ltl_states.size() == 0) {
      out << "ltl_states: []";
    } else {
      out << "ltl_states: [";
      size_t pending_items = msg.ltl_states.size();
      for (auto item : msg.ltl_states) {
        to_flow_style_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const LTLStateArray & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: ltl_states
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.ltl_states.size() == 0) {
      out << "ltl_states: []\n";
    } else {
      out << "ltl_states:\n";
      for (auto item : msg.ltl_states) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const LTLStateArray & msg, bool use_flow_style = false)
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
  const ltl_automaton_msgs::msg::LTLStateArray & msg,
  std::ostream & out, size_t indentation = 0)
{
  ltl_automaton_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use ltl_automaton_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const ltl_automaton_msgs::msg::LTLStateArray & msg)
{
  return ltl_automaton_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<ltl_automaton_msgs::msg::LTLStateArray>()
{
  return "ltl_automaton_msgs::msg::LTLStateArray";
}

template<>
inline const char * name<ltl_automaton_msgs::msg::LTLStateArray>()
{
  return "ltl_automaton_msgs/msg/LTLStateArray";
}

template<>
struct has_fixed_size<ltl_automaton_msgs::msg::LTLStateArray>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<ltl_automaton_msgs::msg::LTLStateArray>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<ltl_automaton_msgs::msg::LTLStateArray>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // LTL_AUTOMATON_MSGS__MSG__DETAIL__LTL_STATE_ARRAY__TRAITS_HPP_
