// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ltl_automaton_msgs:msg/LTLStateRuns.idl
// generated code does not contain a copyright notice

#ifndef LTL_AUTOMATON_MSGS__MSG__DETAIL__LTL_STATE_RUNS__BUILDER_HPP_
#define LTL_AUTOMATON_MSGS__MSG__DETAIL__LTL_STATE_RUNS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "ltl_automaton_msgs/msg/detail/ltl_state_runs__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace ltl_automaton_msgs
{

namespace msg
{

namespace builder
{

class Init_LTLStateRuns_runs
{
public:
  Init_LTLStateRuns_runs()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::ltl_automaton_msgs::msg::LTLStateRuns runs(::ltl_automaton_msgs::msg::LTLStateRuns::_runs_type arg)
  {
    msg_.runs = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ltl_automaton_msgs::msg::LTLStateRuns msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::ltl_automaton_msgs::msg::LTLStateRuns>()
{
  return ltl_automaton_msgs::msg::builder::Init_LTLStateRuns_runs();
}

}  // namespace ltl_automaton_msgs

#endif  // LTL_AUTOMATON_MSGS__MSG__DETAIL__LTL_STATE_RUNS__BUILDER_HPP_
