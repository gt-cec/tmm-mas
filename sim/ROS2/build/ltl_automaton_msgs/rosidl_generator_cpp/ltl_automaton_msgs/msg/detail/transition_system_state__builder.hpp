// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ltl_automaton_msgs:msg/TransitionSystemState.idl
// generated code does not contain a copyright notice

#ifndef LTL_AUTOMATON_MSGS__MSG__DETAIL__TRANSITION_SYSTEM_STATE__BUILDER_HPP_
#define LTL_AUTOMATON_MSGS__MSG__DETAIL__TRANSITION_SYSTEM_STATE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "ltl_automaton_msgs/msg/detail/transition_system_state__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace ltl_automaton_msgs
{

namespace msg
{

namespace builder
{

class Init_TransitionSystemState_state_dimension_names
{
public:
  explicit Init_TransitionSystemState_state_dimension_names(::ltl_automaton_msgs::msg::TransitionSystemState & msg)
  : msg_(msg)
  {}
  ::ltl_automaton_msgs::msg::TransitionSystemState state_dimension_names(::ltl_automaton_msgs::msg::TransitionSystemState::_state_dimension_names_type arg)
  {
    msg_.state_dimension_names = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ltl_automaton_msgs::msg::TransitionSystemState msg_;
};

class Init_TransitionSystemState_states
{
public:
  Init_TransitionSystemState_states()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TransitionSystemState_state_dimension_names states(::ltl_automaton_msgs::msg::TransitionSystemState::_states_type arg)
  {
    msg_.states = std::move(arg);
    return Init_TransitionSystemState_state_dimension_names(msg_);
  }

private:
  ::ltl_automaton_msgs::msg::TransitionSystemState msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::ltl_automaton_msgs::msg::TransitionSystemState>()
{
  return ltl_automaton_msgs::msg::builder::Init_TransitionSystemState_states();
}

}  // namespace ltl_automaton_msgs

#endif  // LTL_AUTOMATON_MSGS__MSG__DETAIL__TRANSITION_SYSTEM_STATE__BUILDER_HPP_
