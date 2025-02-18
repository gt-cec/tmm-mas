// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from ltl_automaton_msgs:srv/TaskReplanningRelabel.idl
// generated code does not contain a copyright notice

#ifndef LTL_AUTOMATON_MSGS__SRV__DETAIL__TASK_REPLANNING_RELABEL__TRAITS_HPP_
#define LTL_AUTOMATON_MSGS__SRV__DETAIL__TASK_REPLANNING_RELABEL__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "ltl_automaton_msgs/srv/detail/task_replanning_relabel__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'current_state'
#include "ltl_automaton_msgs/msg/detail/transition_system_state__traits.hpp"

namespace ltl_automaton_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const TaskReplanningRelabel_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: state
  {
    if (msg.state.size() == 0) {
      out << "state: []";
    } else {
      out << "state: [";
      size_t pending_items = msg.state.size();
      for (auto item : msg.state) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: label
  {
    if (msg.label.size() == 0) {
      out << "label: []";
    } else {
      out << "label: [";
      size_t pending_items = msg.label.size();
      for (auto item : msg.label) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: current_state
  {
    out << "current_state: ";
    to_flow_style_yaml(msg.current_state, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const TaskReplanningRelabel_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: state
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.state.size() == 0) {
      out << "state: []\n";
    } else {
      out << "state:\n";
      for (auto item : msg.state) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: label
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.label.size() == 0) {
      out << "label: []\n";
    } else {
      out << "label:\n";
      for (auto item : msg.label) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: current_state
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "current_state:\n";
    to_block_style_yaml(msg.current_state, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const TaskReplanningRelabel_Request & msg, bool use_flow_style = false)
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
  const ltl_automaton_msgs::srv::TaskReplanningRelabel_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  ltl_automaton_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use ltl_automaton_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const ltl_automaton_msgs::srv::TaskReplanningRelabel_Request & msg)
{
  return ltl_automaton_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<ltl_automaton_msgs::srv::TaskReplanningRelabel_Request>()
{
  return "ltl_automaton_msgs::srv::TaskReplanningRelabel_Request";
}

template<>
inline const char * name<ltl_automaton_msgs::srv::TaskReplanningRelabel_Request>()
{
  return "ltl_automaton_msgs/srv/TaskReplanningRelabel_Request";
}

template<>
struct has_fixed_size<ltl_automaton_msgs::srv::TaskReplanningRelabel_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<ltl_automaton_msgs::srv::TaskReplanningRelabel_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<ltl_automaton_msgs::srv::TaskReplanningRelabel_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'new_plan'
#include "ltl_automaton_msgs/msg/detail/ltl_plan__traits.hpp"

namespace ltl_automaton_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const TaskReplanningRelabel_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: success
  {
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
    out << ", ";
  }

  // member: new_plan
  {
    out << "new_plan: ";
    to_flow_style_yaml(msg.new_plan, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const TaskReplanningRelabel_Response & msg,
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

  // member: new_plan
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "new_plan:\n";
    to_block_style_yaml(msg.new_plan, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const TaskReplanningRelabel_Response & msg, bool use_flow_style = false)
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
  const ltl_automaton_msgs::srv::TaskReplanningRelabel_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  ltl_automaton_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use ltl_automaton_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const ltl_automaton_msgs::srv::TaskReplanningRelabel_Response & msg)
{
  return ltl_automaton_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<ltl_automaton_msgs::srv::TaskReplanningRelabel_Response>()
{
  return "ltl_automaton_msgs::srv::TaskReplanningRelabel_Response";
}

template<>
inline const char * name<ltl_automaton_msgs::srv::TaskReplanningRelabel_Response>()
{
  return "ltl_automaton_msgs/srv/TaskReplanningRelabel_Response";
}

template<>
struct has_fixed_size<ltl_automaton_msgs::srv::TaskReplanningRelabel_Response>
  : std::integral_constant<bool, has_fixed_size<ltl_automaton_msgs::msg::LTLPlan>::value> {};

template<>
struct has_bounded_size<ltl_automaton_msgs::srv::TaskReplanningRelabel_Response>
  : std::integral_constant<bool, has_bounded_size<ltl_automaton_msgs::msg::LTLPlan>::value> {};

template<>
struct is_message<ltl_automaton_msgs::srv::TaskReplanningRelabel_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<ltl_automaton_msgs::srv::TaskReplanningRelabel>()
{
  return "ltl_automaton_msgs::srv::TaskReplanningRelabel";
}

template<>
inline const char * name<ltl_automaton_msgs::srv::TaskReplanningRelabel>()
{
  return "ltl_automaton_msgs/srv/TaskReplanningRelabel";
}

template<>
struct has_fixed_size<ltl_automaton_msgs::srv::TaskReplanningRelabel>
  : std::integral_constant<
    bool,
    has_fixed_size<ltl_automaton_msgs::srv::TaskReplanningRelabel_Request>::value &&
    has_fixed_size<ltl_automaton_msgs::srv::TaskReplanningRelabel_Response>::value
  >
{
};

template<>
struct has_bounded_size<ltl_automaton_msgs::srv::TaskReplanningRelabel>
  : std::integral_constant<
    bool,
    has_bounded_size<ltl_automaton_msgs::srv::TaskReplanningRelabel_Request>::value &&
    has_bounded_size<ltl_automaton_msgs::srv::TaskReplanningRelabel_Response>::value
  >
{
};

template<>
struct is_service<ltl_automaton_msgs::srv::TaskReplanningRelabel>
  : std::true_type
{
};

template<>
struct is_service_request<ltl_automaton_msgs::srv::TaskReplanningRelabel_Request>
  : std::true_type
{
};

template<>
struct is_service_response<ltl_automaton_msgs::srv::TaskReplanningRelabel_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // LTL_AUTOMATON_MSGS__SRV__DETAIL__TASK_REPLANNING_RELABEL__TRAITS_HPP_
