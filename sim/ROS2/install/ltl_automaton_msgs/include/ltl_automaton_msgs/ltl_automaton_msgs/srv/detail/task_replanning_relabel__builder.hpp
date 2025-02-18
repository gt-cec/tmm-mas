// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ltl_automaton_msgs:srv/TaskReplanningRelabel.idl
// generated code does not contain a copyright notice

#ifndef LTL_AUTOMATON_MSGS__SRV__DETAIL__TASK_REPLANNING_RELABEL__BUILDER_HPP_
#define LTL_AUTOMATON_MSGS__SRV__DETAIL__TASK_REPLANNING_RELABEL__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "ltl_automaton_msgs/srv/detail/task_replanning_relabel__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace ltl_automaton_msgs
{

namespace srv
{

namespace builder
{

class Init_TaskReplanningRelabel_Request_current_state
{
public:
  explicit Init_TaskReplanningRelabel_Request_current_state(::ltl_automaton_msgs::srv::TaskReplanningRelabel_Request & msg)
  : msg_(msg)
  {}
  ::ltl_automaton_msgs::srv::TaskReplanningRelabel_Request current_state(::ltl_automaton_msgs::srv::TaskReplanningRelabel_Request::_current_state_type arg)
  {
    msg_.current_state = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ltl_automaton_msgs::srv::TaskReplanningRelabel_Request msg_;
};

class Init_TaskReplanningRelabel_Request_label
{
public:
  explicit Init_TaskReplanningRelabel_Request_label(::ltl_automaton_msgs::srv::TaskReplanningRelabel_Request & msg)
  : msg_(msg)
  {}
  Init_TaskReplanningRelabel_Request_current_state label(::ltl_automaton_msgs::srv::TaskReplanningRelabel_Request::_label_type arg)
  {
    msg_.label = std::move(arg);
    return Init_TaskReplanningRelabel_Request_current_state(msg_);
  }

private:
  ::ltl_automaton_msgs::srv::TaskReplanningRelabel_Request msg_;
};

class Init_TaskReplanningRelabel_Request_state
{
public:
  Init_TaskReplanningRelabel_Request_state()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TaskReplanningRelabel_Request_label state(::ltl_automaton_msgs::srv::TaskReplanningRelabel_Request::_state_type arg)
  {
    msg_.state = std::move(arg);
    return Init_TaskReplanningRelabel_Request_label(msg_);
  }

private:
  ::ltl_automaton_msgs::srv::TaskReplanningRelabel_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::ltl_automaton_msgs::srv::TaskReplanningRelabel_Request>()
{
  return ltl_automaton_msgs::srv::builder::Init_TaskReplanningRelabel_Request_state();
}

}  // namespace ltl_automaton_msgs


namespace ltl_automaton_msgs
{

namespace srv
{

namespace builder
{

class Init_TaskReplanningRelabel_Response_new_plan
{
public:
  explicit Init_TaskReplanningRelabel_Response_new_plan(::ltl_automaton_msgs::srv::TaskReplanningRelabel_Response & msg)
  : msg_(msg)
  {}
  ::ltl_automaton_msgs::srv::TaskReplanningRelabel_Response new_plan(::ltl_automaton_msgs::srv::TaskReplanningRelabel_Response::_new_plan_type arg)
  {
    msg_.new_plan = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ltl_automaton_msgs::srv::TaskReplanningRelabel_Response msg_;
};

class Init_TaskReplanningRelabel_Response_success
{
public:
  Init_TaskReplanningRelabel_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TaskReplanningRelabel_Response_new_plan success(::ltl_automaton_msgs::srv::TaskReplanningRelabel_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_TaskReplanningRelabel_Response_new_plan(msg_);
  }

private:
  ::ltl_automaton_msgs::srv::TaskReplanningRelabel_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::ltl_automaton_msgs::srv::TaskReplanningRelabel_Response>()
{
  return ltl_automaton_msgs::srv::builder::Init_TaskReplanningRelabel_Response_success();
}

}  // namespace ltl_automaton_msgs

#endif  // LTL_AUTOMATON_MSGS__SRV__DETAIL__TASK_REPLANNING_RELABEL__BUILDER_HPP_
