// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from ltl_automaton_msgs:msg/LTLState.idl
// generated code does not contain a copyright notice

#ifndef LTL_AUTOMATON_MSGS__MSG__DETAIL__LTL_STATE__STRUCT_HPP_
#define LTL_AUTOMATON_MSGS__MSG__DETAIL__LTL_STATE__STRUCT_HPP_

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
# define DEPRECATED__ltl_automaton_msgs__msg__LTLState __attribute__((deprecated))
#else
# define DEPRECATED__ltl_automaton_msgs__msg__LTLState __declspec(deprecated)
#endif

namespace ltl_automaton_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct LTLState_
{
  using Type = LTLState_<ContainerAllocator>;

  explicit LTLState_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : ts_state(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->buchi_state = "";
    }
  }

  explicit LTLState_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : ts_state(_alloc, _init),
    buchi_state(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->buchi_state = "";
    }
  }

  // field types and members
  using _ts_state_type =
    ltl_automaton_msgs::msg::TransitionSystemState_<ContainerAllocator>;
  _ts_state_type ts_state;
  using _buchi_state_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _buchi_state_type buchi_state;

  // setters for named parameter idiom
  Type & set__ts_state(
    const ltl_automaton_msgs::msg::TransitionSystemState_<ContainerAllocator> & _arg)
  {
    this->ts_state = _arg;
    return *this;
  }
  Type & set__buchi_state(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->buchi_state = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ltl_automaton_msgs::msg::LTLState_<ContainerAllocator> *;
  using ConstRawPtr =
    const ltl_automaton_msgs::msg::LTLState_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ltl_automaton_msgs::msg::LTLState_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ltl_automaton_msgs::msg::LTLState_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ltl_automaton_msgs::msg::LTLState_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ltl_automaton_msgs::msg::LTLState_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ltl_automaton_msgs::msg::LTLState_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ltl_automaton_msgs::msg::LTLState_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ltl_automaton_msgs::msg::LTLState_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ltl_automaton_msgs::msg::LTLState_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ltl_automaton_msgs__msg__LTLState
    std::shared_ptr<ltl_automaton_msgs::msg::LTLState_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ltl_automaton_msgs__msg__LTLState
    std::shared_ptr<ltl_automaton_msgs::msg::LTLState_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const LTLState_ & other) const
  {
    if (this->ts_state != other.ts_state) {
      return false;
    }
    if (this->buchi_state != other.buchi_state) {
      return false;
    }
    return true;
  }
  bool operator!=(const LTLState_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct LTLState_

// alias to use template instance with default allocator
using LTLState =
  ltl_automaton_msgs::msg::LTLState_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace ltl_automaton_msgs

#endif  // LTL_AUTOMATON_MSGS__MSG__DETAIL__LTL_STATE__STRUCT_HPP_
