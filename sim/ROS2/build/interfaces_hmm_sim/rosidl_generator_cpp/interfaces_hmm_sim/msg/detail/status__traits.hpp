// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from interfaces_hmm_sim:msg/Status.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES_HMM_SIM__MSG__DETAIL__STATUS__TRAITS_HPP_
#define INTERFACES_HMM_SIM__MSG__DETAIL__STATUS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "interfaces_hmm_sim/msg/detail/status__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace interfaces_hmm_sim
{

namespace msg
{

inline void to_flow_style_yaml(
  const Status & msg,
  std::ostream & out)
{
  out << "{";
  // member: agent
  {
    out << "agent: ";
    rosidl_generator_traits::value_to_yaml(msg.agent, out);
    out << ", ";
  }

  // member: start
  {
    out << "start: ";
    rosidl_generator_traits::value_to_yaml(msg.start, out);
    out << ", ";
  }

  // member: arrived
  {
    out << "arrived: ";
    rosidl_generator_traits::value_to_yaml(msg.arrived, out);
    out << ", ";
  }

  // member: replan_received
  {
    out << "replan_received: ";
    rosidl_generator_traits::value_to_yaml(msg.replan_received, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Status & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: agent
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "agent: ";
    rosidl_generator_traits::value_to_yaml(msg.agent, out);
    out << "\n";
  }

  // member: start
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "start: ";
    rosidl_generator_traits::value_to_yaml(msg.start, out);
    out << "\n";
  }

  // member: arrived
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "arrived: ";
    rosidl_generator_traits::value_to_yaml(msg.arrived, out);
    out << "\n";
  }

  // member: replan_received
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "replan_received: ";
    rosidl_generator_traits::value_to_yaml(msg.replan_received, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Status & msg, bool use_flow_style = false)
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
  const interfaces_hmm_sim::msg::Status & msg,
  std::ostream & out, size_t indentation = 0)
{
  interfaces_hmm_sim::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use interfaces_hmm_sim::msg::to_yaml() instead")]]
inline std::string to_yaml(const interfaces_hmm_sim::msg::Status & msg)
{
  return interfaces_hmm_sim::msg::to_yaml(msg);
}

template<>
inline const char * data_type<interfaces_hmm_sim::msg::Status>()
{
  return "interfaces_hmm_sim::msg::Status";
}

template<>
inline const char * name<interfaces_hmm_sim::msg::Status>()
{
  return "interfaces_hmm_sim/msg/Status";
}

template<>
struct has_fixed_size<interfaces_hmm_sim::msg::Status>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<interfaces_hmm_sim::msg::Status>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<interfaces_hmm_sim::msg::Status>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // INTERFACES_HMM_SIM__MSG__DETAIL__STATUS__TRAITS_HPP_
