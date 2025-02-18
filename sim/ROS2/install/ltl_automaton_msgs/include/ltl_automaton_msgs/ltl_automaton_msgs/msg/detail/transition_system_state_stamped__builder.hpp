// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ltl_automaton_msgs:msg/TransitionSystemStateStamped.idl
// generated code does not contain a copyright notice

#ifndef LTL_AUTOMATON_MSGS__MSG__DETAIL__TRANSITION_SYSTEM_STATE_STAMPED__BUILDER_HPP_
#define LTL_AUTOMATON_MSGS__MSG__DETAIL__TRANSITION_SYSTEM_STATE_STAMPED__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "ltl_automaton_msgs/msg/detail/transition_system_state_stamped__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace ltl_automaton_msgs
{

namespace msg
{

namespace builder
{

class Init_TransitionSystemStateStamped_ts_state
{
public:
  explicit Init_TransitionSystemStateStamped_ts_state(::ltl_automaton_msgs::msg::TransitionSystemStateStamped & msg)
  : msg_(msg)
  {}
  ::ltl_automaton_msgs::msg::TransitionSystemStateStamped ts_state(::ltl_automaton_msgs::msg::TransitionSystemStateStamped::_ts_state_type arg)
  {
    msg_.ts_state = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ltl_automaton_msgs::msg::TransitionSystemStateStamped msg_;
};

class Init_TransitionSystemStateStamped_header
{
public:
  Init_TransitionSystemStateStamped_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TransitionSystemStateStamped_ts_state header(::ltl_automaton_msgs::msg::TransitionSystemStateStamped::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_TransitionSystemStateStamped_ts_state(msg_);
  }

private:
  ::ltl_automaton_msgs::msg::TransitionSystemStateStamped msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::ltl_automaton_msgs::msg::TransitionSystemStateStamped>()
{
  return ltl_automaton_msgs::msg::builder::Init_TransitionSystemStateStamped_header();
}

}  // namespace ltl_automaton_msgs

#endif  // LTL_AUTOMATON_MSGS__MSG__DETAIL__TRANSITION_SYSTEM_STATE_STAMPED__BUILDER_HPP_
