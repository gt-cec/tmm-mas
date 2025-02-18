// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from ltl_automaton_msgs:msg/TransitionSystemState.idl
// generated code does not contain a copyright notice

#ifndef LTL_AUTOMATON_MSGS__MSG__DETAIL__TRANSITION_SYSTEM_STATE__TRAITS_HPP_
#define LTL_AUTOMATON_MSGS__MSG__DETAIL__TRANSITION_SYSTEM_STATE__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "ltl_automaton_msgs/msg/detail/transition_system_state__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace ltl_automaton_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const TransitionSystemState & msg,
  std::ostream & out)
{
  out << "{";
  // member: states
  {
    if (msg.states.size() == 0) {
      out << "states: []";
    } else {
      out << "states: [";
      size_t pending_items = msg.states.size();
      for (auto item : msg.states) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: state_dimension_names
  {
    if (msg.state_dimension_names.size() == 0) {
      out << "state_dimension_names: []";
    } else {
      out << "state_dimension_names: [";
      size_t pending_items = msg.state_dimension_names.size();
      for (auto item : msg.state_dimension_names) {
        rosidl_generator_traits::value_to_yaml(item, out);
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
  const TransitionSystemState & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: states
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.states.size() == 0) {
      out << "states: []\n";
    } else {
      out << "states:\n";
      for (auto item : msg.states) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: state_dimension_names
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.state_dimension_names.size() == 0) {
      out << "state_dimension_names: []\n";
    } else {
      out << "state_dimension_names:\n";
      for (auto item : msg.state_dimension_names) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const TransitionSystemState & msg, bool use_flow_style = false)
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
  const ltl_automaton_msgs::msg::TransitionSystemState & msg,
  std::ostream & out, size_t indentation = 0)
{
  ltl_automaton_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use ltl_automaton_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const ltl_automaton_msgs::msg::TransitionSystemState & msg)
{
  return ltl_automaton_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<ltl_automaton_msgs::msg::TransitionSystemState>()
{
  return "ltl_automaton_msgs::msg::TransitionSystemState";
}

template<>
inline const char * name<ltl_automaton_msgs::msg::TransitionSystemState>()
{
  return "ltl_automaton_msgs/msg/TransitionSystemState";
}

template<>
struct has_fixed_size<ltl_automaton_msgs::msg::TransitionSystemState>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<ltl_automaton_msgs::msg::TransitionSystemState>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<ltl_automaton_msgs::msg::TransitionSystemState>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // LTL_AUTOMATON_MSGS__MSG__DETAIL__TRANSITION_SYSTEM_STATE__TRAITS_HPP_
