// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from ltl_automaton_msgs:srv/TrapCheck.idl
// generated code does not contain a copyright notice

#ifndef LTL_AUTOMATON_MSGS__SRV__DETAIL__TRAP_CHECK__STRUCT_HPP_
#define LTL_AUTOMATON_MSGS__SRV__DETAIL__TRAP_CHECK__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'ts_state'
#include "ltl_automaton_msgs/msg/detail/transition_system_state__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__ltl_automaton_msgs__srv__TrapCheck_Request __attribute__((deprecated))
#else
# define DEPRECATED__ltl_automaton_msgs__srv__TrapCheck_Request __declspec(deprecated)
#endif

namespace ltl_automaton_msgs
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct TrapCheck_Request_
{
  using Type = TrapCheck_Request_<ContainerAllocator>;

  explicit TrapCheck_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : ts_state(_init)
  {
    (void)_init;
  }

  explicit TrapCheck_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : ts_state(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _ts_state_type =
    ltl_automaton_msgs::msg::TransitionSystemState_<ContainerAllocator>;
  _ts_state_type ts_state;

  // setters for named parameter idiom
  Type & set__ts_state(
    const ltl_automaton_msgs::msg::TransitionSystemState_<ContainerAllocator> & _arg)
  {
    this->ts_state = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ltl_automaton_msgs::srv::TrapCheck_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const ltl_automaton_msgs::srv::TrapCheck_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ltl_automaton_msgs::srv::TrapCheck_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ltl_automaton_msgs::srv::TrapCheck_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ltl_automaton_msgs::srv::TrapCheck_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ltl_automaton_msgs::srv::TrapCheck_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ltl_automaton_msgs::srv::TrapCheck_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ltl_automaton_msgs::srv::TrapCheck_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ltl_automaton_msgs::srv::TrapCheck_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ltl_automaton_msgs::srv::TrapCheck_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ltl_automaton_msgs__srv__TrapCheck_Request
    std::shared_ptr<ltl_automaton_msgs::srv::TrapCheck_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ltl_automaton_msgs__srv__TrapCheck_Request
    std::shared_ptr<ltl_automaton_msgs::srv::TrapCheck_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const TrapCheck_Request_ & other) const
  {
    if (this->ts_state != other.ts_state) {
      return false;
    }
    return true;
  }
  bool operator!=(const TrapCheck_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct TrapCheck_Request_

// alias to use template instance with default allocator
using TrapCheck_Request =
  ltl_automaton_msgs::srv::TrapCheck_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace ltl_automaton_msgs


#ifndef _WIN32
# define DEPRECATED__ltl_automaton_msgs__srv__TrapCheck_Response __attribute__((deprecated))
#else
# define DEPRECATED__ltl_automaton_msgs__srv__TrapCheck_Response __declspec(deprecated)
#endif

namespace ltl_automaton_msgs
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct TrapCheck_Response_
{
  using Type = TrapCheck_Response_<ContainerAllocator>;

  explicit TrapCheck_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->is_connected = false;
      this->is_trap = false;
    }
  }

  explicit TrapCheck_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->is_connected = false;
      this->is_trap = false;
    }
  }

  // field types and members
  using _is_connected_type =
    bool;
  _is_connected_type is_connected;
  using _is_trap_type =
    bool;
  _is_trap_type is_trap;

  // setters for named parameter idiom
  Type & set__is_connected(
    const bool & _arg)
  {
    this->is_connected = _arg;
    return *this;
  }
  Type & set__is_trap(
    const bool & _arg)
  {
    this->is_trap = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ltl_automaton_msgs::srv::TrapCheck_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const ltl_automaton_msgs::srv::TrapCheck_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ltl_automaton_msgs::srv::TrapCheck_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ltl_automaton_msgs::srv::TrapCheck_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ltl_automaton_msgs::srv::TrapCheck_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ltl_automaton_msgs::srv::TrapCheck_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ltl_automaton_msgs::srv::TrapCheck_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ltl_automaton_msgs::srv::TrapCheck_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ltl_automaton_msgs::srv::TrapCheck_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ltl_automaton_msgs::srv::TrapCheck_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ltl_automaton_msgs__srv__TrapCheck_Response
    std::shared_ptr<ltl_automaton_msgs::srv::TrapCheck_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ltl_automaton_msgs__srv__TrapCheck_Response
    std::shared_ptr<ltl_automaton_msgs::srv::TrapCheck_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const TrapCheck_Response_ & other) const
  {
    if (this->is_connected != other.is_connected) {
      return false;
    }
    if (this->is_trap != other.is_trap) {
      return false;
    }
    return true;
  }
  bool operator!=(const TrapCheck_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct TrapCheck_Response_

// alias to use template instance with default allocator
using TrapCheck_Response =
  ltl_automaton_msgs::srv::TrapCheck_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace ltl_automaton_msgs

namespace ltl_automaton_msgs
{

namespace srv
{

struct TrapCheck
{
  using Request = ltl_automaton_msgs::srv::TrapCheck_Request;
  using Response = ltl_automaton_msgs::srv::TrapCheck_Response;
};

}  // namespace srv

}  // namespace ltl_automaton_msgs

#endif  // LTL_AUTOMATON_MSGS__SRV__DETAIL__TRAP_CHECK__STRUCT_HPP_
