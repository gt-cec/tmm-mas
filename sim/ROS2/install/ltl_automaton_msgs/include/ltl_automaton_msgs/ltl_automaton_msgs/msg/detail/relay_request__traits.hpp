// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from ltl_automaton_msgs:msg/RelayRequest.idl
// generated code does not contain a copyright notice

#ifndef LTL_AUTOMATON_MSGS__MSG__DETAIL__RELAY_REQUEST__TRAITS_HPP_
#define LTL_AUTOMATON_MSGS__MSG__DETAIL__RELAY_REQUEST__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "ltl_automaton_msgs/msg/detail/relay_request__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'current_state'
#include "ltl_automaton_msgs/msg/detail/transition_system_state__traits.hpp"

namespace ltl_automaton_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const RelayRequest & msg,
  std::ostream & out)
{
  out << "{";
  // member: from_pose
  {
    if (msg.from_pose.size() == 0) {
      out << "from_pose: []";
    } else {
      out << "from_pose: [";
      size_t pending_items = msg.from_pose.size();
      for (auto item : msg.from_pose) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: to_pose
  {
    if (msg.to_pose.size() == 0) {
      out << "to_pose: []";
    } else {
      out << "to_pose: [";
      size_t pending_items = msg.to_pose.size();
      for (auto item : msg.to_pose) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: cost
  {
    out << "cost: ";
    rosidl_generator_traits::value_to_yaml(msg.cost, out);
    out << ", ";
  }

  // member: current_state
  {
    out << "current_state: ";
    to_flow_style_yaml(msg.current_state, out);
    out << ", ";
  }

  // member: exec_index
  {
    out << "exec_index: ";
    rosidl_generator_traits::value_to_yaml(msg.exec_index, out);
    out << ", ";
  }

  // member: type
  {
    out << "type: ";
    rosidl_generator_traits::value_to_yaml(msg.type, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const RelayRequest & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: from_pose
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.from_pose.size() == 0) {
      out << "from_pose: []\n";
    } else {
      out << "from_pose:\n";
      for (auto item : msg.from_pose) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: to_pose
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.to_pose.size() == 0) {
      out << "to_pose: []\n";
    } else {
      out << "to_pose:\n";
      for (auto item : msg.to_pose) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: cost
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "cost: ";
    rosidl_generator_traits::value_to_yaml(msg.cost, out);
    out << "\n";
  }

  // member: current_state
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "current_state:\n";
    to_block_style_yaml(msg.current_state, out, indentation + 2);
  }

  // member: exec_index
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "exec_index: ";
    rosidl_generator_traits::value_to_yaml(msg.exec_index, out);
    out << "\n";
  }

  // member: type
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "type: ";
    rosidl_generator_traits::value_to_yaml(msg.type, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const RelayRequest & msg, bool use_flow_style = false)
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
  const ltl_automaton_msgs::msg::RelayRequest & msg,
  std::ostream & out, size_t indentation = 0)
{
  ltl_automaton_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use ltl_automaton_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const ltl_automaton_msgs::msg::RelayRequest & msg)
{
  return ltl_automaton_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<ltl_automaton_msgs::msg::RelayRequest>()
{
  return "ltl_automaton_msgs::msg::RelayRequest";
}

template<>
inline const char * name<ltl_automaton_msgs::msg::RelayRequest>()
{
  return "ltl_automaton_msgs/msg/RelayRequest";
}

template<>
struct has_fixed_size<ltl_automaton_msgs::msg::RelayRequest>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<ltl_automaton_msgs::msg::RelayRequest>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<ltl_automaton_msgs::msg::RelayRequest>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // LTL_AUTOMATON_MSGS__MSG__DETAIL__RELAY_REQUEST__TRAITS_HPP_
