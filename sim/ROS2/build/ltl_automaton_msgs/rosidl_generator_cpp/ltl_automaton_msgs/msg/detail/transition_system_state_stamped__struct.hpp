// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from ltl_automaton_msgs:msg/TransitionSystemStateStamped.idl
// generated code does not contain a copyright notice

#ifndef LTL_AUTOMATON_MSGS__MSG__DETAIL__TRANSITION_SYSTEM_STATE_STAMPED__STRUCT_HPP_
#define LTL_AUTOMATON_MSGS__MSG__DETAIL__TRANSITION_SYSTEM_STATE_STAMPED__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.hpp"
// Member 'ts_state'
#include "ltl_automaton_msgs/msg/detail/transition_system_state__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__ltl_automaton_msgs__msg__TransitionSystemStateStamped __attribute__((deprecated))
#else
# define DEPRECATED__ltl_automaton_msgs__msg__TransitionSystemStateStamped __declspec(deprecated)
#endif

namespace ltl_automaton_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct TransitionSystemStateStamped_
{
  using Type = TransitionSystemStateStamped_<ContainerAllocator>;

  explicit TransitionSystemStateStamped_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init),
    ts_state(_init)
  {
    (void)_init;
  }

  explicit TransitionSystemStateStamped_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init),
    ts_state(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _ts_state_type =
    ltl_automaton_msgs::msg::TransitionSystemState_<ContainerAllocator>;
  _ts_state_type ts_state;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__ts_state(
    const ltl_automaton_msgs::msg::TransitionSystemState_<ContainerAllocator> & _arg)
  {
    this->ts_state = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ltl_automaton_msgs::msg::TransitionSystemStateStamped_<ContainerAllocator> *;
  using ConstRawPtr =
    const ltl_automaton_msgs::msg::TransitionSystemStateStamped_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ltl_automaton_msgs::msg::TransitionSystemStateStamped_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ltl_automaton_msgs::msg::TransitionSystemStateStamped_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ltl_automaton_msgs::msg::TransitionSystemStateStamped_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ltl_automaton_msgs::msg::TransitionSystemStateStamped_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ltl_automaton_msgs::msg::TransitionSystemStateStamped_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ltl_automaton_msgs::msg::TransitionSystemStateStamped_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ltl_automaton_msgs::msg::TransitionSystemStateStamped_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ltl_automaton_msgs::msg::TransitionSystemStateStamped_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ltl_automaton_msgs__msg__TransitionSystemStateStamped
    std::shared_ptr<ltl_automaton_msgs::msg::TransitionSystemStateStamped_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ltl_automaton_msgs__msg__TransitionSystemStateStamped
    std::shared_ptr<ltl_automaton_msgs::msg::TransitionSystemStateStamped_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const TransitionSystemStateStamped_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->ts_state != other.ts_state) {
      return false;
    }
    return true;
  }
  bool operator!=(const TransitionSystemStateStamped_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct TransitionSystemStateStamped_

// alias to use template instance with default allocator
using TransitionSystemStateStamped =
  ltl_automaton_msgs::msg::TransitionSystemStateStamped_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace ltl_automaton_msgs

#endif  // LTL_AUTOMATON_MSGS__MSG__DETAIL__TRANSITION_SYSTEM_STATE_STAMPED__STRUCT_HPP_
