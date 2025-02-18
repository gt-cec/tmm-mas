// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from interfaces_hmm_sim:msg/AgentPoses.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES_HMM_SIM__MSG__DETAIL__AGENT_POSES__TRAITS_HPP_
#define INTERFACES_HMM_SIM__MSG__DETAIL__AGENT_POSES__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "interfaces_hmm_sim/msg/detail/agent_poses__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace interfaces_hmm_sim
{

namespace msg
{

inline void to_flow_style_yaml(
  const AgentPoses & msg,
  std::ostream & out)
{
  out << "{";
  // member: agents
  {
    if (msg.agents.size() == 0) {
      out << "agents: []";
    } else {
      out << "agents: [";
      size_t pending_items = msg.agents.size();
      for (auto item : msg.agents) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: x
  {
    if (msg.x.size() == 0) {
      out << "x: []";
    } else {
      out << "x: [";
      size_t pending_items = msg.x.size();
      for (auto item : msg.x) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: y
  {
    if (msg.y.size() == 0) {
      out << "y: []";
    } else {
      out << "y: [";
      size_t pending_items = msg.y.size();
      for (auto item : msg.y) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: z
  {
    if (msg.z.size() == 0) {
      out << "z: []";
    } else {
      out << "z: [";
      size_t pending_items = msg.z.size();
      for (auto item : msg.z) {
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
  const AgentPoses & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: agents
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.agents.size() == 0) {
      out << "agents: []\n";
    } else {
      out << "agents:\n";
      for (auto item : msg.agents) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: x
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.x.size() == 0) {
      out << "x: []\n";
    } else {
      out << "x:\n";
      for (auto item : msg.x) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: y
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.y.size() == 0) {
      out << "y: []\n";
    } else {
      out << "y:\n";
      for (auto item : msg.y) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: z
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.z.size() == 0) {
      out << "z: []\n";
    } else {
      out << "z:\n";
      for (auto item : msg.z) {
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

inline std::string to_yaml(const AgentPoses & msg, bool use_flow_style = false)
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

}  // namespace interfaces_hmm_sim

namespace rosidl_generator_traits
{

[[deprecated("use interfaces_hmm_sim::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const interfaces_hmm_sim::msg::AgentPoses & msg,
  std::ostream & out, size_t indentation = 0)
{
  interfaces_hmm_sim::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use interfaces_hmm_sim::msg::to_yaml() instead")]]
inline std::string to_yaml(const interfaces_hmm_sim::msg::AgentPoses & msg)
{
  return interfaces_hmm_sim::msg::to_yaml(msg);
}

template<>
inline const char * data_type<interfaces_hmm_sim::msg::AgentPoses>()
{
  return "interfaces_hmm_sim::msg::AgentPoses";
}

template<>
inline const char * name<interfaces_hmm_sim::msg::AgentPoses>()
{
  return "interfaces_hmm_sim/msg/AgentPoses";
}

template<>
struct has_fixed_size<interfaces_hmm_sim::msg::AgentPoses>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<interfaces_hmm_sim::msg::AgentPoses>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<interfaces_hmm_sim::msg::AgentPoses>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // INTERFACES_HMM_SIM__MSG__DETAIL__AGENT_POSES__TRAITS_HPP_
