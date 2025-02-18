// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__rosidl_typesupport_fastrtps_cpp.hpp.em
// with input from interfaces_hmm_sim:msg/AgentPoses.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES_HMM_SIM__MSG__DETAIL__AGENT_POSES__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
#define INTERFACES_HMM_SIM__MSG__DETAIL__AGENT_POSES__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_

#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "interfaces_hmm_sim/msg/rosidl_typesupport_fastrtps_cpp__visibility_control.h"
#include "interfaces_hmm_sim/msg/detail/agent_poses__struct.hpp"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

#include "fastcdr/Cdr.h"

namespace interfaces_hmm_sim
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_interfaces_hmm_sim
cdr_serialize(
  const interfaces_hmm_sim::msg::AgentPoses & ros_message,
  eprosima::fastcdr::Cdr & cdr);

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_interfaces_hmm_sim
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  interfaces_hmm_sim::msg::AgentPoses & ros_message);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_interfaces_hmm_sim
get_serialized_size(
  const interfaces_hmm_sim::msg::AgentPoses & ros_message,
  size_t current_alignment);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_interfaces_hmm_sim
max_serialized_size_AgentPoses(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace interfaces_hmm_sim

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_interfaces_hmm_sim
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, interfaces_hmm_sim, msg, AgentPoses)();

#ifdef __cplusplus
}
#endif

#endif  // INTERFACES_HMM_SIM__MSG__DETAIL__AGENT_POSES__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
