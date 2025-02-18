// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from ltl_automaton_msgs:msg/TransitionSystemState.idl
// generated code does not contain a copyright notice

#ifndef LTL_AUTOMATON_MSGS__MSG__DETAIL__TRANSITION_SYSTEM_STATE__STRUCT_HPP_
#define LTL_AUTOMATON_MSGS__MSG__DETAIL__TRANSITION_SYSTEM_STATE__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__ltl_automaton_msgs__msg__TransitionSystemState __attribute__((deprecated))
#else
# define DEPRECATED__ltl_automaton_msgs__msg__TransitionSystemState __declspec(deprecated)
#endif

namespace ltl_automaton_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct TransitionSystemState_
{
  using Type = TransitionSystemState_<ContainerAllocator>;

  explicit TransitionSystemState_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
  }

  explicit TransitionSystemState_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
    (void)_alloc;
  }

  // field types and members
  using _states_type =
    std::vector<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>>;
  _states_type states;
  using _state_dimension_names_type =
    std::vector<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>>;
  _state_dimension_names_type state_dimension_names;

  // setters for named parameter idiom
  Type & set__states(
    const std::vector<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>> & _arg)
  {
    this->states = _arg;
    return *this;
  }
  Type & set__state_dimension_names(
    const std::vector<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>> & _arg)
  {
    this->state_dimension_names = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ltl_automaton_msgs::msg::TransitionSystemState_<ContainerAllocator> *;
  using ConstRawPtr =
    const ltl_automaton_msgs::msg::TransitionSystemState_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ltl_automaton_msgs::msg::TransitionSystemState_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ltl_automaton_msgs::msg::TransitionSystemState_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ltl_automaton_msgs::msg::TransitionSystemState_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ltl_automaton_msgs::msg::TransitionSystemState_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ltl_automaton_msgs::msg::TransitionSystemState_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ltl_automaton_msgs::msg::TransitionSystemState_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ltl_automaton_msgs::msg::TransitionSystemState_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ltl_automaton_msgs::msg::TransitionSystemState_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ltl_automaton_msgs__msg__TransitionSystemState
    std::shared_ptr<ltl_automaton_msgs::msg::TransitionSystemState_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ltl_automaton_msgs__msg__TransitionSystemState
    std::shared_ptr<ltl_automaton_msgs::msg::TransitionSystemState_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const TransitionSystemState_ & other) const
  {
    if (this->states != other.states) {
      return false;
    }
    if (this->state_dimension_names != other.state_dimension_names) {
      return false;
    }
    return true;
  }
  bool operator!=(const TransitionSystemState_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct TransitionSystemState_

// alias to use template instance with default allocator
using TransitionSystemState =
  ltl_automaton_msgs::msg::TransitionSystemState_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace ltl_automaton_msgs

#endif  // LTL_AUTOMATON_MSGS__MSG__DETAIL__TRANSITION_SYSTEM_STATE__STRUCT_HPP_
