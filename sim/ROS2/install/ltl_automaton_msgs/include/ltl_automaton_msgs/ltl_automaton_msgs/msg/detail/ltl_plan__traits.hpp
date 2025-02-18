// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from ltl_automaton_msgs:msg/LTLPlan.idl
// generated code does not contain a copyright notice

#ifndef LTL_AUTOMATON_MSGS__MSG__DETAIL__LTL_PLAN__TRAITS_HPP_
#define LTL_AUTOMATON_MSGS__MSG__DETAIL__LTL_PLAN__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "ltl_automaton_msgs/msg/detail/ltl_plan__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"
// Member 'ts_state_sequence'
#include "ltl_automaton_msgs/msg/detail/transition_system_state__traits.hpp"

namespace ltl_automaton_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const LTLPlan & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: action_sequence
  {
    if (msg.action_sequence.size() == 0) {
      out << "action_sequence: []";
    } else {
      out << "action_sequence: [";
      size_t pending_items = msg.action_sequence.size();
      for (auto item : msg.action_sequence) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: ts_state_sequence
  {
    if (msg.ts_state_sequence.size() == 0) {
      out << "ts_state_sequence: []";
    } else {
      out << "ts_state_sequence: [";
      size_t pending_items = msg.ts_state_sequence.size();
      for (auto item : msg.ts_state_sequence) {
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
  const LTLPlan & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: header
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "header:\n";
    to_block_style_yaml(msg.header, out, indentation + 2);
  }

  // member: action_sequence
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.action_sequence.size() == 0) {
      out << "action_sequence: []\n";
    } else {
      out << "action_sequence:\n";
      for (auto item : msg.action_sequence) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: ts_state_sequence
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.ts_state_sequence.size() == 0) {
      out << "ts_state_sequence: []\n";
    } else {
      out << "ts_state_sequence:\n";
      for (auto item : msg.ts_state_sequence) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const LTLPlan & msg, bool use_flow_style = false)
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
  const ltl_automaton_msgs::msg::LTLPlan & msg,
  std::ostream & out, size_t indentation = 0)
{
  ltl_automaton_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use ltl_automaton_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const ltl_automaton_msgs::msg::LTLPlan & msg)
{
  return ltl_automaton_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<ltl_automaton_msgs::msg::LTLPlan>()
{
  return "ltl_automaton_msgs::msg::LTLPlan";
}

template<>
inline const char * name<ltl_automaton_msgs::msg::LTLPlan>()
{
  return "ltl_automaton_msgs/msg/LTLPlan";
}

template<>
struct has_fixed_size<ltl_automaton_msgs::msg::LTLPlan>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<ltl_automaton_msgs::msg::LTLPlan>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<ltl_automaton_msgs::msg::LTLPlan>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // LTL_AUTOMATON_MSGS__MSG__DETAIL__LTL_PLAN__TRAITS_HPP_
