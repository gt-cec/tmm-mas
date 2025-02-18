// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from ltl_automaton_msgs:srv/TaskReplanningModify.idl
// generated code does not contain a copyright notice

#ifndef LTL_AUTOMATON_MSGS__SRV__DETAIL__TASK_REPLANNING_MODIFY__TRAITS_HPP_
#define LTL_AUTOMATON_MSGS__SRV__DETAIL__TASK_REPLANNING_MODIFY__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "ltl_automaton_msgs/srv/detail/task_replanning_modify__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'current_state'
#include "ltl_automaton_msgs/msg/detail/transition_system_state__traits.hpp"

namespace ltl_automaton_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const TaskReplanningModify_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: mod_from
  {
    if (msg.mod_from.size() == 0) {
      out << "mod_from: []";
    } else {
      out << "mod_from: [";
      size_t pending_items = msg.mod_from.size();
      for (auto item : msg.mod_from) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: mod_to
  {
    if (msg.mod_to.size() == 0) {
      out << "mod_to: []";
    } else {
      out << "mod_to: [";
      size_t pending_items = msg.mod_to.size();
      for (auto item : msg.mod_to) {
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
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const TaskReplanningModify_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: mod_from
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.mod_from.size() == 0) {
      out << "mod_from: []\n";
    } else {
      out << "mod_from:\n";
      for (auto item : msg.mod_from) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: mod_to
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.mod_to.size() == 0) {
      out << "mod_to: []\n";
    } else {
      out << "mod_to:\n";
      for (auto item : msg.mod_to) {
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
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const TaskReplanningModify_Request & msg, bool use_flow_style = false)
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
  const ltl_automaton_msgs::srv::TaskReplanningModify_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  ltl_automaton_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use ltl_automaton_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const ltl_automaton_msgs::srv::TaskReplanningModify_Request & msg)
{
  return ltl_automaton_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<ltl_automaton_msgs::srv::TaskReplanningModify_Request>()
{
  return "ltl_automaton_msgs::srv::TaskReplanningModify_Request";
}

template<>
inline const char * name<ltl_automaton_msgs::srv::TaskReplanningModify_Request>()
{
  return "ltl_automaton_msgs/srv/TaskReplanningModify_Request";
}

template<>
struct has_fixed_size<ltl_automaton_msgs::srv::TaskReplanningModify_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<ltl_automaton_msgs::srv::TaskReplanningModify_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<ltl_automaton_msgs::srv::TaskReplanningModify_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'new_plan_prefix'
// Member 'new_plan_suffix'
#include "ltl_automaton_msgs/msg/detail/ltl_plan__traits.hpp"

namespace ltl_automaton_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const TaskReplanningModify_Response & msg,
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
  const TaskReplanningModify_Response & msg,
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

inline std::string to_yaml(const TaskReplanningModify_Response & msg, bool use_flow_style = false)
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
  const ltl_automaton_msgs::srv::TaskReplanningModify_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  ltl_automaton_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use ltl_automaton_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const ltl_automaton_msgs::srv::TaskReplanningModify_Response & msg)
{
  return ltl_automaton_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<ltl_automaton_msgs::srv::TaskReplanningModify_Response>()
{
  return "ltl_automaton_msgs::srv::TaskReplanningModify_Response";
}

template<>
inline const char * name<ltl_automaton_msgs::srv::TaskReplanningModify_Response>()
{
  return "ltl_automaton_msgs/srv/TaskReplanningModify_Response";
}

template<>
struct has_fixed_size<ltl_automaton_msgs::srv::TaskReplanningModify_Response>
  : std::integral_constant<bool, has_fixed_size<ltl_automaton_msgs::msg::LTLPlan>::value> {};

template<>
struct has_bounded_size<ltl_automaton_msgs::srv::TaskReplanningModify_Response>
  : std::integral_constant<bool, has_bounded_size<ltl_automaton_msgs::msg::LTLPlan>::value> {};

template<>
struct is_message<ltl_automaton_msgs::srv::TaskReplanningModify_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<ltl_automaton_msgs::srv::TaskReplanningModify>()
{
  return "ltl_automaton_msgs::srv::TaskReplanningModify";
}

template<>
inline const char * name<ltl_automaton_msgs::srv::TaskReplanningModify>()
{
  return "ltl_automaton_msgs/srv/TaskReplanningModify";
}

template<>
struct has_fixed_size<ltl_automaton_msgs::srv::TaskReplanningModify>
  : std::integral_constant<
    bool,
    has_fixed_size<ltl_automaton_msgs::srv::TaskReplanningModify_Request>::value &&
    has_fixed_size<ltl_automaton_msgs::srv::TaskReplanningModify_Response>::value
  >
{
};

template<>
struct has_bounded_size<ltl_automaton_msgs::srv::TaskReplanningModify>
  : std::integral_constant<
    bool,
    has_bounded_size<ltl_automaton_msgs::srv::TaskReplanningModify_Request>::value &&
    has_bounded_size<ltl_automaton_msgs::srv::TaskReplanningModify_Response>::value
  >
{
};

template<>
struct is_service<ltl_automaton_msgs::srv::TaskReplanningModify>
  : std::true_type
{
};

template<>
struct is_service_request<ltl_automaton_msgs::srv::TaskReplanningModify_Request>
  : std::true_type
{
};

template<>
struct is_service_response<ltl_automaton_msgs::srv::TaskReplanningModify_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // LTL_AUTOMATON_MSGS__SRV__DETAIL__TASK_REPLANNING_MODIFY__TRAITS_HPP_
