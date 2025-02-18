// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interfaces_hmm_sim:msg/AgentPoses.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES_HMM_SIM__MSG__DETAIL__AGENT_POSES__BUILDER_HPP_
#define INTERFACES_HMM_SIM__MSG__DETAIL__AGENT_POSES__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "interfaces_hmm_sim/msg/detail/agent_poses__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace interfaces_hmm_sim
{

namespace msg
{

namespace builder
{

class Init_AgentPoses_z
{
public:
  explicit Init_AgentPoses_z(::interfaces_hmm_sim::msg::AgentPoses & msg)
  : msg_(msg)
  {}
  ::interfaces_hmm_sim::msg::AgentPoses z(::interfaces_hmm_sim::msg::AgentPoses::_z_type arg)
  {
    msg_.z = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces_hmm_sim::msg::AgentPoses msg_;
};

class Init_AgentPoses_y
{
public:
  explicit Init_AgentPoses_y(::interfaces_hmm_sim::msg::AgentPoses & msg)
  : msg_(msg)
  {}
  Init_AgentPoses_z y(::interfaces_hmm_sim::msg::AgentPoses::_y_type arg)
  {
    msg_.y = std::move(arg);
    return Init_AgentPoses_z(msg_);
  }

private:
  ::interfaces_hmm_sim::msg::AgentPoses msg_;
};

class Init_AgentPoses_x
{
public:
  explicit Init_AgentPoses_x(::interfaces_hmm_sim::msg::AgentPoses & msg)
  : msg_(msg)
  {}
  Init_AgentPoses_y x(::interfaces_hmm_sim::msg::AgentPoses::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_AgentPoses_y(msg_);
  }

private:
  ::interfaces_hmm_sim::msg::AgentPoses msg_;
};

class Init_AgentPoses_agents
{
public:
  Init_AgentPoses_agents()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_AgentPoses_x agents(::interfaces_hmm_sim::msg::AgentPoses::_agents_type arg)
  {
    msg_.agents = std::move(arg);
    return Init_AgentPoses_x(msg_);
  }

private:
  ::interfaces_hmm_sim::msg::AgentPoses msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces_hmm_sim::msg::AgentPoses>()
{
  return interfaces_hmm_sim::msg::builder::Init_AgentPoses_agents();
}

}  // namespace interfaces_hmm_sim

#endif  // INTERFACES_HMM_SIM__MSG__DETAIL__AGENT_POSES__BUILDER_HPP_
