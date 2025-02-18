// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ltl_automaton_msgs:srv/TaskReplanningModify.idl
// generated code does not contain a copyright notice

#ifndef LTL_AUTOMATON_MSGS__SRV__DETAIL__TASK_REPLANNING_MODIFY__BUILDER_HPP_
#define LTL_AUTOMATON_MSGS__SRV__DETAIL__TASK_REPLANNING_MODIFY__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "ltl_automaton_msgs/srv/detail/task_replanning_modify__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace ltl_automaton_msgs
{

namespace srv
{

namespace builder
{

class Init_TaskReplanningModify_Request_exec_index
{
public:
  explicit Init_TaskReplanningModify_Request_exec_index(::ltl_automaton_msgs::srv::TaskReplanningModify_Request & msg)
  : msg_(msg)
  {}
  ::ltl_automaton_msgs::srv::TaskReplanningModify_Request exec_index(::ltl_automaton_msgs::srv::TaskReplanningModify_Request::_exec_index_type arg)
  {
    msg_.exec_index = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ltl_automaton_msgs::srv::TaskReplanningModify_Request msg_;
};

class Init_TaskReplanningModify_Request_current_state
{
public:
  explicit Init_TaskReplanningModify_Request_current_state(::ltl_automaton_msgs::srv::TaskReplanningModify_Request & msg)
  : msg_(msg)
  {}
  Init_TaskReplanningModify_Request_exec_index current_state(::ltl_automaton_msgs::srv::TaskReplanningModify_Request::_current_state_type arg)
  {
    msg_.current_state = std::move(arg);
    return Init_TaskReplanningModify_Request_exec_index(msg_);
  }

private:
  ::ltl_automaton_msgs::srv::TaskReplanningModify_Request msg_;
};

class Init_TaskReplanningModify_Request_cost
{
public:
  explicit Init_TaskReplanningModify_Request_cost(::ltl_automaton_msgs::srv::TaskReplanningModify_Request & msg)
  : msg_(msg)
  {}
  Init_TaskReplanningModify_Request_current_state cost(::ltl_automaton_msgs::srv::TaskReplanningModify_Request::_cost_type arg)
  {
    msg_.cost = std::move(arg);
    return Init_TaskReplanningModify_Request_current_state(msg_);
  }

private:
  ::ltl_automaton_msgs::srv::TaskReplanningModify_Request msg_;
};

class Init_TaskReplanningModify_Request_mod_to
{
public:
  explicit Init_TaskReplanningModify_Request_mod_to(::ltl_automaton_msgs::srv::TaskReplanningModify_Request & msg)
  : msg_(msg)
  {}
  Init_TaskReplanningModify_Request_cost mod_to(::ltl_automaton_msgs::srv::TaskReplanningModify_Request::_mod_to_type arg)
  {
    msg_.mod_to = std::move(arg);
    return Init_TaskReplanningModify_Request_cost(msg_);
  }

private:
  ::ltl_automaton_msgs::srv::TaskReplanningModify_Request msg_;
};

class Init_TaskReplanningModify_Request_mod_from
{
public:
  Init_TaskReplanningModify_Request_mod_from()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TaskReplanningModify_Request_mod_to mod_from(::ltl_automaton_msgs::srv::TaskReplanningModify_Request::_mod_from_type arg)
  {
    msg_.mod_from = std::move(arg);
    return Init_TaskReplanningModify_Request_mod_to(msg_);
  }

private:
  ::ltl_automaton_msgs::srv::TaskReplanningModify_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::ltl_automaton_msgs::srv::TaskReplanningModify_Request>()
{
  return ltl_automaton_msgs::srv::builder::Init_TaskReplanningModify_Request_mod_from();
}

}  // namespace ltl_automaton_msgs


namespace ltl_automaton_msgs
{

namespace srv
{

namespace builder
{

class Init_TaskReplanningModify_Response_new_plan_suffix
{
public:
  explicit Init_TaskReplanningModify_Response_new_plan_suffix(::ltl_automaton_msgs::srv::TaskReplanningModify_Response & msg)
  : msg_(msg)
  {}
  ::ltl_automaton_msgs::srv::TaskReplanningModify_Response new_plan_suffix(::ltl_automaton_msgs::srv::TaskReplanningModify_Response::_new_plan_suffix_type arg)
  {
    msg_.new_plan_suffix = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ltl_automaton_msgs::srv::TaskReplanningModify_Response msg_;
};

class Init_TaskReplanningModify_Response_new_plan_prefix
{
public:
  explicit Init_TaskReplanningModify_Response_new_plan_prefix(::ltl_automaton_msgs::srv::TaskReplanningModify_Response & msg)
  : msg_(msg)
  {}
  Init_TaskReplanningModify_Response_new_plan_suffix new_plan_prefix(::ltl_automaton_msgs::srv::TaskReplanningModify_Response::_new_plan_prefix_type arg)
  {
    msg_.new_plan_prefix = std::move(arg);
    return Init_TaskReplanningModify_Response_new_plan_suffix(msg_);
  }

private:
  ::ltl_automaton_msgs::srv::TaskReplanningModify_Response msg_;
};

class Init_TaskReplanningModify_Response_success
{
public:
  Init_TaskReplanningModify_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TaskReplanningModify_Response_new_plan_prefix success(::ltl_automaton_msgs::srv::TaskReplanningModify_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_TaskReplanningModify_Response_new_plan_prefix(msg_);
  }

private:
  ::ltl_automaton_msgs::srv::TaskReplanningModify_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::ltl_automaton_msgs::srv::TaskReplanningModify_Response>()
{
  return ltl_automaton_msgs::srv::builder::Init_TaskReplanningModify_Response_success();
}

}  // namespace ltl_automaton_msgs

#endif  // LTL_AUTOMATON_MSGS__SRV__DETAIL__TASK_REPLANNING_MODIFY__BUILDER_HPP_
