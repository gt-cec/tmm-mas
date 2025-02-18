// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from ltl_automaton_msgs:srv/TaskPlanning.idl
// generated code does not contain a copyright notice

#ifndef LTL_AUTOMATON_MSGS__SRV__DETAIL__TASK_PLANNING__STRUCT_HPP_
#define LTL_AUTOMATON_MSGS__SRV__DETAIL__TASK_PLANNING__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__ltl_automaton_msgs__srv__TaskPlanning_Request __attribute__((deprecated))
#else
# define DEPRECATED__ltl_automaton_msgs__srv__TaskPlanning_Request __declspec(deprecated)
#endif

namespace ltl_automaton_msgs
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct TaskPlanning_Request_
{
  using Type = TaskPlanning_Request_<ContainerAllocator>;

  explicit TaskPlanning_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->hard_task = "";
      this->soft_task = "";
    }
  }

  explicit TaskPlanning_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : hard_task(_alloc),
    soft_task(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->hard_task = "";
      this->soft_task = "";
    }
  }

  // field types and members
  using _hard_task_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _hard_task_type hard_task;
  using _soft_task_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _soft_task_type soft_task;

  // setters for named parameter idiom
  Type & set__hard_task(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->hard_task = _arg;
    return *this;
  }
  Type & set__soft_task(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->soft_task = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ltl_automaton_msgs::srv::TaskPlanning_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const ltl_automaton_msgs::srv::TaskPlanning_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ltl_automaton_msgs::srv::TaskPlanning_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ltl_automaton_msgs::srv::TaskPlanning_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ltl_automaton_msgs::srv::TaskPlanning_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ltl_automaton_msgs::srv::TaskPlanning_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ltl_automaton_msgs::srv::TaskPlanning_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ltl_automaton_msgs::srv::TaskPlanning_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ltl_automaton_msgs::srv::TaskPlanning_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ltl_automaton_msgs::srv::TaskPlanning_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ltl_automaton_msgs__srv__TaskPlanning_Request
    std::shared_ptr<ltl_automaton_msgs::srv::TaskPlanning_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ltl_automaton_msgs__srv__TaskPlanning_Request
    std::shared_ptr<ltl_automaton_msgs::srv::TaskPlanning_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const TaskPlanning_Request_ & other) const
  {
    if (this->hard_task != other.hard_task) {
      return false;
    }
    if (this->soft_task != other.soft_task) {
      return false;
    }
    return true;
  }
  bool operator!=(const TaskPlanning_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct TaskPlanning_Request_

// alias to use template instance with default allocator
using TaskPlanning_Request =
  ltl_automaton_msgs::srv::TaskPlanning_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace ltl_automaton_msgs


#ifndef _WIN32
# define DEPRECATED__ltl_automaton_msgs__srv__TaskPlanning_Response __attribute__((deprecated))
#else
# define DEPRECATED__ltl_automaton_msgs__srv__TaskPlanning_Response __declspec(deprecated)
#endif

namespace ltl_automaton_msgs
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct TaskPlanning_Response_
{
  using Type = TaskPlanning_Response_<ContainerAllocator>;

  explicit TaskPlanning_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
    }
  }

  explicit TaskPlanning_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
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

  // setters for named parameter idiom
  Type & set__success(
    const bool & _arg)
  {
    this->success = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ltl_automaton_msgs::srv::TaskPlanning_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const ltl_automaton_msgs::srv::TaskPlanning_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ltl_automaton_msgs::srv::TaskPlanning_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ltl_automaton_msgs::srv::TaskPlanning_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ltl_automaton_msgs::srv::TaskPlanning_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ltl_automaton_msgs::srv::TaskPlanning_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ltl_automaton_msgs::srv::TaskPlanning_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ltl_automaton_msgs::srv::TaskPlanning_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ltl_automaton_msgs::srv::TaskPlanning_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ltl_automaton_msgs::srv::TaskPlanning_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ltl_automaton_msgs__srv__TaskPlanning_Response
    std::shared_ptr<ltl_automaton_msgs::srv::TaskPlanning_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ltl_automaton_msgs__srv__TaskPlanning_Response
    std::shared_ptr<ltl_automaton_msgs::srv::TaskPlanning_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const TaskPlanning_Response_ & other) const
  {
    if (this->success != other.success) {
      return false;
    }
    return true;
  }
  bool operator!=(const TaskPlanning_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct TaskPlanning_Response_

// alias to use template instance with default allocator
using TaskPlanning_Response =
  ltl_automaton_msgs::srv::TaskPlanning_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace ltl_automaton_msgs

namespace ltl_automaton_msgs
{

namespace srv
{

struct TaskPlanning
{
  using Request = ltl_automaton_msgs::srv::TaskPlanning_Request;
  using Response = ltl_automaton_msgs::srv::TaskPlanning_Response;
};

}  // namespace srv

}  // namespace ltl_automaton_msgs

#endif  // LTL_AUTOMATON_MSGS__SRV__DETAIL__TASK_PLANNING__STRUCT_HPP_
