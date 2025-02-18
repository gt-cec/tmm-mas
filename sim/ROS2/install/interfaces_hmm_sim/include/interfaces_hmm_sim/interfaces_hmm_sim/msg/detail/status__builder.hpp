// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interfaces_hmm_sim:msg/Status.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES_HMM_SIM__MSG__DETAIL__STATUS__BUILDER_HPP_
#define INTERFACES_HMM_SIM__MSG__DETAIL__STATUS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "interfaces_hmm_sim/msg/detail/status__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace interfaces_hmm_sim
{

namespace msg
{

namespace builder
{

class Init_Status_replan_received
{
public:
  explicit Init_Status_replan_received(::interfaces_hmm_sim::msg::Status & msg)
  : msg_(msg)
  {}
  ::interfaces_hmm_sim::msg::Status replan_received(::interfaces_hmm_sim::msg::Status::_replan_received_type arg)
  {
    msg_.replan_received = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces_hmm_sim::msg::Status msg_;
};

class Init_Status_arrived
{
public:
  explicit Init_Status_arrived(::interfaces_hmm_sim::msg::Status & msg)
  : msg_(msg)
  {}
  Init_Status_replan_received arrived(::interfaces_hmm_sim::msg::Status::_arrived_type arg)
  {
    msg_.arrived = std::move(arg);
    return Init_Status_replan_received(msg_);
  }

private:
  ::interfaces_hmm_sim::msg::Status msg_;
};

class Init_Status_start
{
public:
  explicit Init_Status_start(::interfaces_hmm_sim::msg::Status & msg)
  : msg_(msg)
  {}
  Init_Status_arrived start(::interfaces_hmm_sim::msg::Status::_start_type arg)
  {
    msg_.start = std::move(arg);
    return Init_Status_arrived(msg_);
  }

private:
  ::interfaces_hmm_sim::msg::Status msg_;
};

class Init_Status_agent
{
public:
  Init_Status_agent()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Status_start agent(::interfaces_hmm_sim::msg::Status::_agent_type arg)
  {
    msg_.agent = std::move(arg);
    return Init_Status_start(msg_);
  }

private:
  ::interfaces_hmm_sim::msg::Status msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces_hmm_sim::msg::Status>()
{
  return interfaces_hmm_sim::msg::builder::Init_Status_agent();
}

}  // namespace interfaces_hmm_sim

#endif  // INTERFACES_HMM_SIM__MSG__DETAIL__STATUS__BUILDER_HPP_
