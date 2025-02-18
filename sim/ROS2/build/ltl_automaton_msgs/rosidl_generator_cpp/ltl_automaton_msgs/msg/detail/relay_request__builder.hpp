// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ltl_automaton_msgs:msg/RelayRequest.idl
// generated code does not contain a copyright notice

#ifndef LTL_AUTOMATON_MSGS__MSG__DETAIL__RELAY_REQUEST__BUILDER_HPP_
#define LTL_AUTOMATON_MSGS__MSG__DETAIL__RELAY_REQUEST__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "ltl_automaton_msgs/msg/detail/relay_request__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace ltl_automaton_msgs
{

namespace msg
{

namespace builder
{

class Init_RelayRequest_type
{
public:
  explicit Init_RelayRequest_type(::ltl_automaton_msgs::msg::RelayRequest & msg)
  : msg_(msg)
  {}
  ::ltl_automaton_msgs::msg::RelayRequest type(::ltl_automaton_msgs::msg::RelayRequest::_type_type arg)
  {
    msg_.type = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ltl_automaton_msgs::msg::RelayRequest msg_;
};

class Init_RelayRequest_exec_index
{
public:
  explicit Init_RelayRequest_exec_index(::ltl_automaton_msgs::msg::RelayRequest & msg)
  : msg_(msg)
  {}
  Init_RelayRequest_type exec_index(::ltl_automaton_msgs::msg::RelayRequest::_exec_index_type arg)
  {
    msg_.exec_index = std::move(arg);
    return Init_RelayRequest_type(msg_);
  }

private:
  ::ltl_automaton_msgs::msg::RelayRequest msg_;
};

class Init_RelayRequest_current_state
{
public:
  explicit Init_RelayRequest_current_state(::ltl_automaton_msgs::msg::RelayRequest & msg)
  : msg_(msg)
  {}
  Init_RelayRequest_exec_index current_state(::ltl_automaton_msgs::msg::RelayRequest::_current_state_type arg)
  {
    msg_.current_state = std::move(arg);
    return Init_RelayRequest_exec_index(msg_);
  }

private:
  ::ltl_automaton_msgs::msg::RelayRequest msg_;
};

class Init_RelayRequest_cost
{
public:
  explicit Init_RelayRequest_cost(::ltl_automaton_msgs::msg::RelayRequest & msg)
  : msg_(msg)
  {}
  Init_RelayRequest_current_state cost(::ltl_automaton_msgs::msg::RelayRequest::_cost_type arg)
  {
    msg_.cost = std::move(arg);
    return Init_RelayRequest_current_state(msg_);
  }

private:
  ::ltl_automaton_msgs::msg::RelayRequest msg_;
};

class Init_RelayRequest_to_pose
{
public:
  explicit Init_RelayRequest_to_pose(::ltl_automaton_msgs::msg::RelayRequest & msg)
  : msg_(msg)
  {}
  Init_RelayRequest_cost to_pose(::ltl_automaton_msgs::msg::RelayRequest::_to_pose_type arg)
  {
    msg_.to_pose = std::move(arg);
    return Init_RelayRequest_cost(msg_);
  }

private:
  ::ltl_automaton_msgs::msg::RelayRequest msg_;
};

class Init_RelayRequest_from_pose
{
public:
  Init_RelayRequest_from_pose()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RelayRequest_to_pose from_pose(::ltl_automaton_msgs::msg::RelayRequest::_from_pose_type arg)
  {
    msg_.from_pose = std::move(arg);
    return Init_RelayRequest_to_pose(msg_);
  }

private:
  ::ltl_automaton_msgs::msg::RelayRequest msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::ltl_automaton_msgs::msg::RelayRequest>()
{
  return ltl_automaton_msgs::msg::builder::Init_RelayRequest_from_pose();
}

}  // namespace ltl_automaton_msgs

#endif  // LTL_AUTOMATON_MSGS__MSG__DETAIL__RELAY_REQUEST__BUILDER_HPP_
