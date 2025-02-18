// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from ltl_automaton_msgs:msg/LTLStateRuns.idl
// generated code does not contain a copyright notice

#ifndef LTL_AUTOMATON_MSGS__MSG__DETAIL__LTL_STATE_RUNS__STRUCT_HPP_
#define LTL_AUTOMATON_MSGS__MSG__DETAIL__LTL_STATE_RUNS__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'runs'
#include "ltl_automaton_msgs/msg/detail/ltl_state_array__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__ltl_automaton_msgs__msg__LTLStateRuns __attribute__((deprecated))
#else
# define DEPRECATED__ltl_automaton_msgs__msg__LTLStateRuns __declspec(deprecated)
#endif

namespace ltl_automaton_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct LTLStateRuns_
{
  using Type = LTLStateRuns_<ContainerAllocator>;

  explicit LTLStateRuns_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
  }

  explicit LTLStateRuns_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
    (void)_alloc;
  }

  // field types and members
  using _runs_type =
    std::vector<ltl_automaton_msgs::msg::LTLStateArray_<ContainerAllocator>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<ltl_automaton_msgs::msg::LTLStateArray_<ContainerAllocator>>>;
  _runs_type runs;

  // setters for named parameter idiom
  Type & set__runs(
    const std::vector<ltl_automaton_msgs::msg::LTLStateArray_<ContainerAllocator>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<ltl_automaton_msgs::msg::LTLStateArray_<ContainerAllocator>>> & _arg)
  {
    this->runs = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ltl_automaton_msgs::msg::LTLStateRuns_<ContainerAllocator> *;
  using ConstRawPtr =
    const ltl_automaton_msgs::msg::LTLStateRuns_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ltl_automaton_msgs::msg::LTLStateRuns_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ltl_automaton_msgs::msg::LTLStateRuns_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ltl_automaton_msgs::msg::LTLStateRuns_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ltl_automaton_msgs::msg::LTLStateRuns_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ltl_automaton_msgs::msg::LTLStateRuns_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ltl_automaton_msgs::msg::LTLStateRuns_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ltl_automaton_msgs::msg::LTLStateRuns_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ltl_automaton_msgs::msg::LTLStateRuns_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ltl_automaton_msgs__msg__LTLStateRuns
    std::shared_ptr<ltl_automaton_msgs::msg::LTLStateRuns_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ltl_automaton_msgs__msg__LTLStateRuns
    std::shared_ptr<ltl_automaton_msgs::msg::LTLStateRuns_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const LTLStateRuns_ & other) const
  {
    if (this->runs != other.runs) {
      return false;
    }
    return true;
  }
  bool operator!=(const LTLStateRuns_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct LTLStateRuns_

// alias to use template instance with default allocator
using LTLStateRuns =
  ltl_automaton_msgs::msg::LTLStateRuns_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace ltl_automaton_msgs

#endif  // LTL_AUTOMATON_MSGS__MSG__DETAIL__LTL_STATE_RUNS__STRUCT_HPP_
