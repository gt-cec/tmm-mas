// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ltl_automaton_msgs:srv/TaskReplanningDelete.idl
// generated code does not contain a copyright notice

#ifndef LTL_AUTOMATON_MSGS__SRV__DETAIL__TASK_REPLANNING_DELETE__BUILDER_HPP_
#define LTL_AUTOMATON_MSGS__SRV__DETAIL__TASK_REPLANNING_DELETE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "ltl_automaton_msgs/srv/detail/task_replanning_delete__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace ltl_automaton_msgs
{

namespace srv
{

namespace builder
{

class Init_TaskReplanningDelete_Request_exec_index
{
public:
  explicit Init_TaskReplanningDelete_Request_exec_index(::ltl_automaton_msgs::srv::TaskReplanningDelete_Request & msg)
  : msg_(msg)
  {}
  ::ltl_automaton_msgs::srv::TaskReplanningDelete_Request exec_index(::ltl_automaton_msgs::srv::TaskReplanningDelete_Request::_exec_index_type arg)
  {
    msg_.exec_index = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ltl_automaton_msgs::srv::TaskReplanningDelete_Request msg_;
};

class Init_TaskReplanningDelete_Request_current_state
{
public:
  explicit Init_TaskReplanningDelete_Request_current_state(::ltl_automaton_msgs::srv::TaskReplanningDelete_Request & msg)
  : msg_(msg)
  {}
  Init_TaskReplanningDelete_Request_exec_index current_state(::ltl_automaton_msgs::srv::TaskReplanningDelete_Request::_current_state_type arg)
  {
    msg_.current_state = std::move(arg);
    return Init_TaskReplanningDelete_Request_exec_index(msg_);
  }

private:
  ::ltl_automaton_msgs::srv::TaskReplanningDelete_Request msg_;
};

class Init_TaskReplanningDelete_Request_delete_to
{
public:
  explicit Init_TaskReplanningDelete_Request_delete_to(::ltl_automaton_msgs::srv::TaskReplanningDelete_Request & msg)
  : msg_(msg)
  {}
  Init_TaskReplanningDelete_Request_current_state delete_to(::ltl_automaton_msgs::srv::TaskReplanningDelete_Request::_delete_to_type arg)
  {
    msg_.delete_to = std::move(arg);
    return Init_TaskReplanningDelete_Request_current_state(msg_);
  }

private:
  ::ltl_automaton_msgs::srv::TaskReplanningDelete_Request msg_;
};

class Init_TaskReplanningDelete_Request_delete_from
{
public:
  Init_TaskReplanningDelete_Request_delete_from()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TaskReplanningDelete_Request_delete_to delete_from(::ltl_automaton_msgs::srv::TaskReplanningDelete_Request::_delete_from_type arg)
  {
    msg_.delete_from = std::move(arg);
    return Init_TaskReplanningDelete_Request_delete_to(msg_);
  }

private:
  ::ltl_automaton_msgs::srv::TaskReplanningDelete_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::ltl_automaton_msgs::srv::TaskReplanningDelete_Request>()
{
  return ltl_automaton_msgs::srv::builder::Init_TaskReplanningDelete_Request_delete_from();
}

}  // namespace ltl_automaton_msgs


namespace ltl_automaton_msgs
{

namespace srv
{

namespace builder
{

class Init_TaskReplanningDelete_Response_new_plan_suffix
{
public:
  explicit Init_TaskReplanningDelete_Response_new_plan_suffix(::ltl_automaton_msgs::srv::TaskReplanningDelete_Response & msg)
  : msg_(msg)
  {}
  ::ltl_automaton_msgs::srv::TaskReplanningDelete_Response new_plan_suffix(::ltl_automaton_msgs::srv::TaskReplanningDelete_Response::_new_plan_suffix_type arg)
  {
    msg_.new_plan_suffix = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ltl_automaton_msgs::srv::TaskReplanningDelete_Response msg_;
};

class Init_TaskReplanningDelete_Response_new_plan_prefix
{
public:
  explicit Init_TaskReplanningDelete_Response_new_plan_prefix(::ltl_automaton_msgs::srv::TaskReplanningDelete_Response & msg)
  : msg_(msg)
  {}
  Init_TaskReplanningDelete_Response_new_plan_suffix new_plan_prefix(::ltl_automaton_msgs::srv::TaskReplanningDelete_Response::_new_plan_prefix_type arg)
  {
    msg_.new_plan_prefix = std::move(arg);
    return Init_TaskReplanningDelete_Response_new_plan_suffix(msg_);
  }

private:
  ::ltl_automaton_msgs::srv::TaskReplanningDelete_Response msg_;
};

class Init_TaskReplanningDelete_Response_success
{
public:
  Init_TaskReplanningDelete_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TaskReplanningDelete_Response_new_plan_prefix success(::ltl_automaton_msgs::srv::TaskReplanningDelete_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_TaskReplanningDelete_Response_new_plan_prefix(msg_);
  }

private:
  ::ltl_automaton_msgs::srv::TaskReplanningDelete_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::ltl_automaton_msgs::srv::TaskReplanningDelete_Response>()
{
  return ltl_automaton_msgs::srv::builder::Init_TaskReplanningDelete_Response_success();
}

}  // namespace ltl_automaton_msgs

#endif  // LTL_AUTOMATON_MSGS__SRV__DETAIL__TASK_REPLANNING_DELETE__BUILDER_HPP_
