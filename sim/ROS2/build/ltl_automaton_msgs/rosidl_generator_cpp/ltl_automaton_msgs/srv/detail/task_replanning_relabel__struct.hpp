// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from ltl_automaton_msgs:srv/TaskReplanningRelabel.idl
// generated code does not contain a copyright notice

#ifndef LTL_AUTOMATON_MSGS__SRV__DETAIL__TASK_REPLANNING_RELABEL__STRUCT_HPP_
#define LTL_AUTOMATON_MSGS__SRV__DETAIL__TASK_REPLANNING_RELABEL__STRUCT_HPP_

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
# define DEPRECATED__ltl_automaton_msgs__srv__TaskReplanningRelabel_Request __attribute__((deprecated))
#else
# define DEPRECATED__ltl_automaton_msgs__srv__TaskReplanningRelabel_Request __declspec(deprecated)
#endif

namespace ltl_automaton_msgs
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct TaskReplanningRelabel_Request_
{
  using Type = TaskReplanningRelabel_Request_<ContainerAllocator>;

  explicit TaskReplanningRelabel_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : current_state(_init)
  {
    (void)_init;
  }

  explicit TaskReplanningRelabel_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : current_state(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _state_type =
    std::vector<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>>;
  _state_type state;
  using _label_type =
    std::vector<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>>;
  _label_type label;
  using _current_state_type =
    ltl_automaton_msgs::msg::TransitionSystemState_<ContainerAllocator>;
  _current_state_type current_state;

  // setters for named parameter idiom
  Type & set__state(
    const std::vector<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>> & _arg)
  {
    this->state = _arg;
    return *this;
  }
  Type & set__label(
    const std::vector<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>> & _arg)
  {
    this->label = _arg;
    return *this;
  }
  Type & set__current_state(
    const ltl_automaton_msgs::msg::TransitionSystemState_<ContainerAllocator> & _arg)
  {
    this->current_state = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ltl_automaton_msgs::srv::TaskReplanningRelabel_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const ltl_automaton_msgs::srv::TaskReplanningRelabel_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ltl_automaton_msgs::srv::TaskReplanningRelabel_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ltl_automaton_msgs::srv::TaskReplanningRelabel_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ltl_automaton_msgs::srv::TaskReplanningRelabel_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ltl_automaton_msgs::srv::TaskReplanningRelabel_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ltl_automaton_msgs::srv::TaskReplanningRelabel_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ltl_automaton_msgs::srv::TaskReplanningRelabel_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ltl_automaton_msgs::srv::TaskReplanningRelabel_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ltl_automaton_msgs::srv::TaskReplanningRelabel_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ltl_automaton_msgs__srv__TaskReplanningRelabel_Request
    std::shared_ptr<ltl_automaton_msgs::srv::TaskReplanningRelabel_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ltl_automaton_msgs__srv__TaskReplanningRelabel_Request
    std::shared_ptr<ltl_automaton_msgs::srv::TaskReplanningRelabel_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const TaskReplanningRelabel_Request_ & other) const
  {
    if (this->state != other.state) {
      return false;
    }
    if (this->label != other.label) {
      return false;
    }
    if (this->current_state != other.current_state) {
      return false;
    }
    return true;
  }
  bool operator!=(const TaskReplanningRelabel_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct TaskReplanningRelabel_Request_

// alias to use template instance with default allocator
using TaskReplanningRelabel_Request =
  ltl_automaton_msgs::srv::TaskReplanningRelabel_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace ltl_automaton_msgs


// Include directives for member types
// Member 'new_plan'
#include "ltl_automaton_msgs/msg/detail/ltl_plan__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__ltl_automaton_msgs__srv__TaskReplanningRelabel_Response __attribute__((deprecated))
#else
# define DEPRECATED__ltl_automaton_msgs__srv__TaskReplanningRelabel_Response __declspec(deprecated)
#endif

namespace ltl_automaton_msgs
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct TaskReplanningRelabel_Response_
{
  using Type = TaskReplanningRelabel_Response_<ContainerAllocator>;

  explicit TaskReplanningRelabel_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : new_plan(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
    }
  }

  explicit TaskReplanningRelabel_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : new_plan(_alloc, _init)
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
  using _new_plan_type =
    ltl_automaton_msgs::msg::LTLPlan_<ContainerAllocator>;
  _new_plan_type new_plan;

  // setters for named parameter idiom
  Type & set__success(
    const bool & _arg)
  {
    this->success = _arg;
    return *this;
  }
  Type & set__new_plan(
    const ltl_automaton_msgs::msg::LTLPlan_<ContainerAllocator> & _arg)
  {
    this->new_plan = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ltl_automaton_msgs::srv::TaskReplanningRelabel_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const ltl_automaton_msgs::srv::TaskReplanningRelabel_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ltl_automaton_msgs::srv::TaskReplanningRelabel_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ltl_automaton_msgs::srv::TaskReplanningRelabel_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ltl_automaton_msgs::srv::TaskReplanningRelabel_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ltl_automaton_msgs::srv::TaskReplanningRelabel_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ltl_automaton_msgs::srv::TaskReplanningRelabel_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ltl_automaton_msgs::srv::TaskReplanningRelabel_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ltl_automaton_msgs::srv::TaskReplanningRelabel_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ltl_automaton_msgs::srv::TaskReplanningRelabel_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ltl_automaton_msgs__srv__TaskReplanningRelabel_Response
    std::shared_ptr<ltl_automaton_msgs::srv::TaskReplanningRelabel_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ltl_automaton_msgs__srv__TaskReplanningRelabel_Response
    std::shared_ptr<ltl_automaton_msgs::srv::TaskReplanningRelabel_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const TaskReplanningRelabel_Response_ & other) const
  {
    if (this->success != other.success) {
      return false;
    }
    if (this->new_plan != other.new_plan) {
      return false;
    }
    return true;
  }
  bool operator!=(const TaskReplanningRelabel_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct TaskReplanningRelabel_Response_

// alias to use template instance with default allocator
using TaskReplanningRelabel_Response =
  ltl_automaton_msgs::srv::TaskReplanningRelabel_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace ltl_automaton_msgs

namespace ltl_automaton_msgs
{

namespace srv
{

struct TaskReplanningRelabel
{
  using Request = ltl_automaton_msgs::srv::TaskReplanningRelabel_Request;
  using Response = ltl_automaton_msgs::srv::TaskReplanningRelabel_Response;
};

}  // namespace srv

}  // namespace ltl_automaton_msgs

#endif  // LTL_AUTOMATON_MSGS__SRV__DETAIL__TASK_REPLANNING_RELABEL__STRUCT_HPP_
