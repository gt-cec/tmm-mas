// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ltl_automaton_msgs:msg/LTLPlan.idl
// generated code does not contain a copyright notice

#ifndef LTL_AUTOMATON_MSGS__MSG__DETAIL__LTL_PLAN__BUILDER_HPP_
#define LTL_AUTOMATON_MSGS__MSG__DETAIL__LTL_PLAN__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "ltl_automaton_msgs/msg/detail/ltl_plan__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace ltl_automaton_msgs
{

namespace msg
{

namespace builder
{

class Init_LTLPlan_ts_state_sequence
{
public:
  explicit Init_LTLPlan_ts_state_sequence(::ltl_automaton_msgs::msg::LTLPlan & msg)
  : msg_(msg)
  {}
  ::ltl_automaton_msgs::msg::LTLPlan ts_state_sequence(::ltl_automaton_msgs::msg::LTLPlan::_ts_state_sequence_type arg)
  {
    msg_.ts_state_sequence = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ltl_automaton_msgs::msg::LTLPlan msg_;
};

class Init_LTLPlan_action_sequence
{
public:
  explicit Init_LTLPlan_action_sequence(::ltl_automaton_msgs::msg::LTLPlan & msg)
  : msg_(msg)
  {}
  Init_LTLPlan_ts_state_sequence action_sequence(::ltl_automaton_msgs::msg::LTLPlan::_action_sequence_type arg)
  {
    msg_.action_sequence = std::move(arg);
    return Init_LTLPlan_ts_state_sequence(msg_);
  }

private:
  ::ltl_automaton_msgs::msg::LTLPlan msg_;
};

class Init_LTLPlan_header
{
public:
  Init_LTLPlan_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_LTLPlan_action_sequence header(::ltl_automaton_msgs::msg::LTLPlan::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_LTLPlan_action_sequence(msg_);
  }

private:
  ::ltl_automaton_msgs::msg::LTLPlan msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::ltl_automaton_msgs::msg::LTLPlan>()
{
  return ltl_automaton_msgs::msg::builder::Init_LTLPlan_header();
}

}  // namespace ltl_automaton_msgs

#endif  // LTL_AUTOMATON_MSGS__MSG__DETAIL__LTL_PLAN__BUILDER_HPP_
