// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ltl_automaton_msgs:msg/LTLState.idl
// generated code does not contain a copyright notice

#ifndef LTL_AUTOMATON_MSGS__MSG__DETAIL__LTL_STATE__BUILDER_HPP_
#define LTL_AUTOMATON_MSGS__MSG__DETAIL__LTL_STATE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "ltl_automaton_msgs/msg/detail/ltl_state__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace ltl_automaton_msgs
{

namespace msg
{

namespace builder
{

class Init_LTLState_buchi_state
{
public:
  explicit Init_LTLState_buchi_state(::ltl_automaton_msgs::msg::LTLState & msg)
  : msg_(msg)
  {}
  ::ltl_automaton_msgs::msg::LTLState buchi_state(::ltl_automaton_msgs::msg::LTLState::_buchi_state_type arg)
  {
    msg_.buchi_state = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ltl_automaton_msgs::msg::LTLState msg_;
};

class Init_LTLState_ts_state
{
public:
  Init_LTLState_ts_state()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_LTLState_buchi_state ts_state(::ltl_automaton_msgs::msg::LTLState::_ts_state_type arg)
  {
    msg_.ts_state = std::move(arg);
    return Init_LTLState_buchi_state(msg_);
  }

private:
  ::ltl_automaton_msgs::msg::LTLState msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::ltl_automaton_msgs::msg::LTLState>()
{
  return ltl_automaton_msgs::msg::builder::Init_LTLState_ts_state();
}

}  // namespace ltl_automaton_msgs

#endif  // LTL_AUTOMATON_MSGS__MSG__DETAIL__LTL_STATE__BUILDER_HPP_
