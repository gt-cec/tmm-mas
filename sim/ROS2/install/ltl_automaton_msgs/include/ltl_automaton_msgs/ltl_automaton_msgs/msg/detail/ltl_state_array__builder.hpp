// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ltl_automaton_msgs:msg/LTLStateArray.idl
// generated code does not contain a copyright notice

#ifndef LTL_AUTOMATON_MSGS__MSG__DETAIL__LTL_STATE_ARRAY__BUILDER_HPP_
#define LTL_AUTOMATON_MSGS__MSG__DETAIL__LTL_STATE_ARRAY__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "ltl_automaton_msgs/msg/detail/ltl_state_array__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace ltl_automaton_msgs
{

namespace msg
{

namespace builder
{

class Init_LTLStateArray_ltl_states
{
public:
  Init_LTLStateArray_ltl_states()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::ltl_automaton_msgs::msg::LTLStateArray ltl_states(::ltl_automaton_msgs::msg::LTLStateArray::_ltl_states_type arg)
  {
    msg_.ltl_states = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ltl_automaton_msgs::msg::LTLStateArray msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::ltl_automaton_msgs::msg::LTLStateArray>()
{
  return ltl_automaton_msgs::msg::builder::Init_LTLStateArray_ltl_states();
}

}  // namespace ltl_automaton_msgs

#endif  // LTL_AUTOMATON_MSGS__MSG__DETAIL__LTL_STATE_ARRAY__BUILDER_HPP_
