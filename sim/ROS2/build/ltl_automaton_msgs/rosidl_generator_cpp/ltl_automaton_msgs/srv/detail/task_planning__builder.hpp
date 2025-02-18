// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ltl_automaton_msgs:srv/TaskPlanning.idl
// generated code does not contain a copyright notice

#ifndef LTL_AUTOMATON_MSGS__SRV__DETAIL__TASK_PLANNING__BUILDER_HPP_
#define LTL_AUTOMATON_MSGS__SRV__DETAIL__TASK_PLANNING__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "ltl_automaton_msgs/srv/detail/task_planning__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace ltl_automaton_msgs
{

namespace srv
{

namespace builder
{

class Init_TaskPlanning_Request_soft_task
{
public:
  explicit Init_TaskPlanning_Request_soft_task(::ltl_automaton_msgs::srv::TaskPlanning_Request & msg)
  : msg_(msg)
  {}
  ::ltl_automaton_msgs::srv::TaskPlanning_Request soft_task(::ltl_automaton_msgs::srv::TaskPlanning_Request::_soft_task_type arg)
  {
    msg_.soft_task = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ltl_automaton_msgs::srv::TaskPlanning_Request msg_;
};

class Init_TaskPlanning_Request_hard_task
{
public:
  Init_TaskPlanning_Request_hard_task()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TaskPlanning_Request_soft_task hard_task(::ltl_automaton_msgs::srv::TaskPlanning_Request::_hard_task_type arg)
  {
    msg_.hard_task = std::move(arg);
    return Init_TaskPlanning_Request_soft_task(msg_);
  }

private:
  ::ltl_automaton_msgs::srv::TaskPlanning_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::ltl_automaton_msgs::srv::TaskPlanning_Request>()
{
  return ltl_automaton_msgs::srv::builder::Init_TaskPlanning_Request_hard_task();
}

}  // namespace ltl_automaton_msgs


namespace ltl_automaton_msgs
{

namespace srv
{

namespace builder
{

class Init_TaskPlanning_Response_success
{
public:
  Init_TaskPlanning_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::ltl_automaton_msgs::srv::TaskPlanning_Response success(::ltl_automaton_msgs::srv::TaskPlanning_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ltl_automaton_msgs::srv::TaskPlanning_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::ltl_automaton_msgs::srv::TaskPlanning_Response>()
{
  return ltl_automaton_msgs::srv::builder::Init_TaskPlanning_Response_success();
}

}  // namespace ltl_automaton_msgs

#endif  // LTL_AUTOMATON_MSGS__SRV__DETAIL__TASK_PLANNING__BUILDER_HPP_
