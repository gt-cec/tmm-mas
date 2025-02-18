// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ltl_automaton_msgs:msg/RelayResponse.idl
// generated code does not contain a copyright notice

#ifndef LTL_AUTOMATON_MSGS__MSG__DETAIL__RELAY_RESPONSE__BUILDER_HPP_
#define LTL_AUTOMATON_MSGS__MSG__DETAIL__RELAY_RESPONSE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "ltl_automaton_msgs/msg/detail/relay_response__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace ltl_automaton_msgs
{

namespace msg
{

namespace builder
{

class Init_RelayResponse_new_plan_suffix
{
public:
  explicit Init_RelayResponse_new_plan_suffix(::ltl_automaton_msgs::msg::RelayResponse & msg)
  : msg_(msg)
  {}
  ::ltl_automaton_msgs::msg::RelayResponse new_plan_suffix(::ltl_automaton_msgs::msg::RelayResponse::_new_plan_suffix_type arg)
  {
    msg_.new_plan_suffix = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ltl_automaton_msgs::msg::RelayResponse msg_;
};

class Init_RelayResponse_new_plan_prefix
{
public:
  explicit Init_RelayResponse_new_plan_prefix(::ltl_automaton_msgs::msg::RelayResponse & msg)
  : msg_(msg)
  {}
  Init_RelayResponse_new_plan_suffix new_plan_prefix(::ltl_automaton_msgs::msg::RelayResponse::_new_plan_prefix_type arg)
  {
    msg_.new_plan_prefix = std::move(arg);
    return Init_RelayResponse_new_plan_suffix(msg_);
  }

private:
  ::ltl_automaton_msgs::msg::RelayResponse msg_;
};

class Init_RelayResponse_success
{
public:
  Init_RelayResponse_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RelayResponse_new_plan_prefix success(::ltl_automaton_msgs::msg::RelayResponse::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_RelayResponse_new_plan_prefix(msg_);
  }

private:
  ::ltl_automaton_msgs::msg::RelayResponse msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::ltl_automaton_msgs::msg::RelayResponse>()
{
  return ltl_automaton_msgs::msg::builder::Init_RelayResponse_success();
}

}  // namespace ltl_automaton_msgs

#endif  // LTL_AUTOMATON_MSGS__MSG__DETAIL__RELAY_RESPONSE__BUILDER_HPP_
