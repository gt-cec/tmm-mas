// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ltl_automaton_msgs:srv/TrapCheck.idl
// generated code does not contain a copyright notice

#ifndef LTL_AUTOMATON_MSGS__SRV__DETAIL__TRAP_CHECK__BUILDER_HPP_
#define LTL_AUTOMATON_MSGS__SRV__DETAIL__TRAP_CHECK__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "ltl_automaton_msgs/srv/detail/trap_check__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace ltl_automaton_msgs
{

namespace srv
{

namespace builder
{

class Init_TrapCheck_Request_ts_state
{
public:
  Init_TrapCheck_Request_ts_state()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::ltl_automaton_msgs::srv::TrapCheck_Request ts_state(::ltl_automaton_msgs::srv::TrapCheck_Request::_ts_state_type arg)
  {
    msg_.ts_state = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ltl_automaton_msgs::srv::TrapCheck_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::ltl_automaton_msgs::srv::TrapCheck_Request>()
{
  return ltl_automaton_msgs::srv::builder::Init_TrapCheck_Request_ts_state();
}

}  // namespace ltl_automaton_msgs


namespace ltl_automaton_msgs
{

namespace srv
{

namespace builder
{

class Init_TrapCheck_Response_is_trap
{
public:
  explicit Init_TrapCheck_Response_is_trap(::ltl_automaton_msgs::srv::TrapCheck_Response & msg)
  : msg_(msg)
  {}
  ::ltl_automaton_msgs::srv::TrapCheck_Response is_trap(::ltl_automaton_msgs::srv::TrapCheck_Response::_is_trap_type arg)
  {
    msg_.is_trap = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ltl_automaton_msgs::srv::TrapCheck_Response msg_;
};

class Init_TrapCheck_Response_is_connected
{
public:
  Init_TrapCheck_Response_is_connected()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TrapCheck_Response_is_trap is_connected(::ltl_automaton_msgs::srv::TrapCheck_Response::_is_connected_type arg)
  {
    msg_.is_connected = std::move(arg);
    return Init_TrapCheck_Response_is_trap(msg_);
  }

private:
  ::ltl_automaton_msgs::srv::TrapCheck_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::ltl_automaton_msgs::srv::TrapCheck_Response>()
{
  return ltl_automaton_msgs::srv::builder::Init_TrapCheck_Response_is_connected();
}

}  // namespace ltl_automaton_msgs

#endif  // LTL_AUTOMATON_MSGS__SRV__DETAIL__TRAP_CHECK__BUILDER_HPP_
