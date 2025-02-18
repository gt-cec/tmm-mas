// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from ltl_automaton_msgs:srv/TaskReplanningModify.idl
// generated code does not contain a copyright notice

#ifndef LTL_AUTOMATON_MSGS__SRV__DETAIL__TASK_REPLANNING_MODIFY__STRUCT_HPP_
#define LTL_AUTOMATON_MSGS__SRV__DETAIL__TASK_REPLANNING_MODIFY__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'current_state'
#include "ltl_automaton_msgs/msg/detail/transition_system_state__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__ltl_automaton_msgs__srv__TaskReplanningModify_Request __attribute__((deprecated))
#else
# define DEPRECATED__ltl_automaton_msgs__srv__TaskReplanningModify_Request __declspec(deprecated)
#endif

namespace ltl_automaton_msgs
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct TaskReplanningModify_Request_
{
  using Type = TaskReplanningModify_Request_<ContainerAllocator>;

  explicit TaskReplanningModify_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : current_state(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->cost = 0.0;
      this->exec_index = 0l;
    }
  }

  explicit TaskReplanningModify_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : current_state(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->cost = 0.0;
      this->exec_index = 0l;
    }
  }

  // field types and members
  using _mod_from_type =
    std::vector<int32_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<int32_t>>;
  _mod_from_type mod_from;
  using _mod_to_type =
    std::vector<int32_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<int32_t>>;
  _mod_to_type mod_to;
  using _cost_type =
    double;
  _cost_type cost;
  using _current_state_type =
    ltl_automaton_msgs::msg::TransitionSystemState_<ContainerAllocator>;
  _current_state_type current_state;
  using _exec_index_type =
    int32_t;
  _exec_index_type exec_index;

  // setters for named parameter idiom
  Type & set__mod_from(
    const std::vector<int32_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<int32_t>> & _arg)
  {
    this->mod_from = _arg;
    return *this;
  }
  Type & set__mod_to(
    const std::vector<int32_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<int32_t>> & _arg)
  {
    this->mod_to = _arg;
    return *this;
  }
  Type & set__cost(
    const double & _arg)
  {
    this->cost = _arg;
    return *this;
  }
  Type & set__current_state(
    const ltl_automaton_msgs::msg::TransitionSystemState_<ContainerAllocator> & _arg)
  {
    this->current_state = _arg;
    return *this;
  }
  Type & set__exec_index(
    const int32_t & _arg)
  {
    this->exec_index = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ltl_automaton_msgs::srv::TaskReplanningModify_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const ltl_automaton_msgs::srv::TaskReplanningModify_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ltl_automaton_msgs::srv::TaskReplanningModify_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ltl_automaton_msgs::srv::TaskReplanningModify_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ltl_automaton_msgs::srv::TaskReplanningModify_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ltl_automaton_msgs::srv::TaskReplanningModify_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ltl_automaton_msgs::srv::TaskReplanningModify_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ltl_automaton_msgs::srv::TaskReplanningModify_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ltl_automaton_msgs::srv::TaskReplanningModify_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ltl_automaton_msgs::srv::TaskReplanningModify_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ltl_automaton_msgs__srv__TaskReplanningModify_Request
    std::shared_ptr<ltl_automaton_msgs::srv::TaskReplanningModify_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ltl_automaton_msgs__srv__TaskReplanningModify_Request
    std::shared_ptr<ltl_automaton_msgs::srv::TaskReplanningModify_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const TaskReplanningModify_Request_ & other) const
  {
    if (this->mod_from != other.mod_from) {
      return false;
    }
    if (this->mod_to != other.mod_to) {
      return false;
    }
    if (this->cost != other.cost) {
      return false;
    }
    if (this->current_state != other.current_state) {
      return false;
    }
    if (this->exec_index != other.exec_index) {
      return false;
    }
    return true;
  }
  bool operator!=(const TaskReplanningModify_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct TaskReplanningModify_Request_

// alias to use template instance with default allocator
using TaskReplanningModify_Request =
  ltl_automaton_msgs::srv::TaskReplanningModify_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace ltl_automaton_msgs


// Include directives for member types
// Member 'new_plan_prefix'
// Member 'new_plan_suffix'
#include "ltl_automaton_msgs/msg/detail/ltl_plan__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__ltl_automaton_msgs__srv__TaskReplanningModify_Response __attribute__((deprecated))
#else
# define DEPRECATED__ltl_automaton_msgs__srv__TaskReplanningModify_Response __declspec(deprecated)
#endif

namespace ltl_automaton_msgs
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct TaskReplanningModify_Response_
{
  using Type = TaskReplanningModify_Response_<ContainerAllocator>;

  explicit TaskReplanningModify_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : new_plan_prefix(_init),
    new_plan_suffix(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
    }
  }

  explicit TaskReplanningModify_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : new_plan_prefix(_alloc, _init),
    new_plan_suffix(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
    }
  }

  // field types and members
  using _success_type =
    bool;
  _success_type success;
  using _new_plan_prefix_type =
    ltl_automaton_msgs::msg::LTLPlan_<ContainerAllocator>;
  _new_plan_prefix_type new_plan_prefix;
  using _new_plan_suffix_type =
    ltl_automaton_msgs::msg::LTLPlan_<ContainerAllocator>;
  _new_plan_suffix_type new_plan_suffix;

  // setters for named parameter idiom
  Type & set__success(
    const bool & _arg)
  {
    this->success = _arg;
    return *this;
  }
  Type & set__new_plan_prefix(
    const ltl_automaton_msgs::msg::LTLPlan_<ContainerAllocator> & _arg)
  {
    this->new_plan_prefix = _arg;
    return *this;
  }
  Type & set__new_plan_suffix(
    const ltl_automaton_msgs::msg::LTLPlan_<ContainerAllocator> & _arg)
  {
    this->new_plan_suffix = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ltl_automaton_msgs::srv::TaskReplanningModify_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const ltl_automaton_msgs::srv::TaskReplanningModify_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ltl_automaton_msgs::srv::TaskReplanningModify_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ltl_automaton_msgs::srv::TaskReplanningModify_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ltl_automaton_msgs::srv::TaskReplanningModify_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ltl_automaton_msgs::srv::TaskReplanningModify_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ltl_automaton_msgs::srv::TaskReplanningModify_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ltl_automaton_msgs::srv::TaskReplanningModify_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ltl_automaton_msgs::srv::TaskReplanningModify_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ltl_automaton_msgs::srv::TaskReplanningModify_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ltl_automaton_msgs__srv__TaskReplanningModify_Response
    std::shared_ptr<ltl_automaton_msgs::srv::TaskReplanningModify_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ltl_automaton_msgs__srv__TaskReplanningModify_Response
    std::shared_ptr<ltl_automaton_msgs::srv::TaskReplanningModify_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const TaskReplanningModify_Response_ & other) const
  {
    if (this->success != other.success) {
      return false;
    }
    if (this->new_plan_prefix != other.new_plan_prefix) {
      return false;
    }
    if (this->new_plan_suffix != other.new_plan_suffix) {
      return false;
    }
    return true;
  }
  bool operator!=(const TaskReplanningModify_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct TaskReplanningModify_Response_

// alias to use template instance with default allocator
using TaskReplanningModify_Response =
  ltl_automaton_msgs::srv::TaskReplanningModify_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace ltl_automaton_msgs

namespace ltl_automaton_msgs
{

namespace srv
{

struct TaskReplanningModify
{
  using Request = ltl_automaton_msgs::srv::TaskReplanningModify_Request;
  using Response = ltl_automaton_msgs::srv::TaskReplanningModify_Response;
};

}  // namespace srv

}  // namespace ltl_automaton_msgs

#endif  // LTL_AUTOMATON_MSGS__SRV__DETAIL__TASK_REPLANNING_MODIFY__STRUCT_HPP_
