// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from ltl_automaton_msgs:msg/RelayResponse.idl
// generated code does not contain a copyright notice

#ifndef LTL_AUTOMATON_MSGS__MSG__DETAIL__RELAY_RESPONSE__STRUCT_HPP_
#define LTL_AUTOMATON_MSGS__MSG__DETAIL__RELAY_RESPONSE__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'new_plan_prefix'
// Member 'new_plan_suffix'
#include "ltl_automaton_msgs/msg/detail/ltl_plan__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__ltl_automaton_msgs__msg__RelayResponse __attribute__((deprecated))
#else
# define DEPRECATED__ltl_automaton_msgs__msg__RelayResponse __declspec(deprecated)
#endif

namespace ltl_automaton_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct RelayResponse_
{
  using Type = RelayResponse_<ContainerAllocator>;

  explicit RelayResponse_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : new_plan_prefix(_init),
    new_plan_suffix(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
    }
  }

  explicit RelayResponse_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
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
    ltl_automaton_msgs::msg::RelayResponse_<ContainerAllocator> *;
  using ConstRawPtr =
    const ltl_automaton_msgs::msg::RelayResponse_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ltl_automaton_msgs::msg::RelayResponse_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ltl_automaton_msgs::msg::RelayResponse_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ltl_automaton_msgs::msg::RelayResponse_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ltl_automaton_msgs::msg::RelayResponse_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ltl_automaton_msgs::msg::RelayResponse_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ltl_automaton_msgs::msg::RelayResponse_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ltl_automaton_msgs::msg::RelayResponse_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ltl_automaton_msgs::msg::RelayResponse_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ltl_automaton_msgs__msg__RelayResponse
    std::shared_ptr<ltl_automaton_msgs::msg::RelayResponse_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ltl_automaton_msgs__msg__RelayResponse
    std::shared_ptr<ltl_automaton_msgs::msg::RelayResponse_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const RelayResponse_ & other) const
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
  bool operator!=(const RelayResponse_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct RelayResponse_

// alias to use template instance with default allocator
using RelayResponse =
  ltl_automaton_msgs::msg::RelayResponse_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace ltl_automaton_msgs

#endif  // LTL_AUTOMATON_MSGS__MSG__DETAIL__RELAY_RESPONSE__STRUCT_HPP_
