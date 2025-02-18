// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from ltl_automaton_msgs:msg/RelayRequest.idl
// generated code does not contain a copyright notice

#ifndef LTL_AUTOMATON_MSGS__MSG__DETAIL__RELAY_REQUEST__STRUCT_HPP_
#define LTL_AUTOMATON_MSGS__MSG__DETAIL__RELAY_REQUEST__STRUCT_HPP_

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
# define DEPRECATED__ltl_automaton_msgs__msg__RelayRequest __attribute__((deprecated))
#else
# define DEPRECATED__ltl_automaton_msgs__msg__RelayRequest __declspec(deprecated)
#endif

namespace ltl_automaton_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct RelayRequest_
{
  using Type = RelayRequest_<ContainerAllocator>;

  explicit RelayRequest_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : current_state(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->cost = 0.0;
      this->exec_index = 0l;
      this->type = "";
    }
  }

  explicit RelayRequest_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : current_state(_alloc, _init),
    type(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->cost = 0.0;
      this->exec_index = 0l;
      this->type = "";
    }
  }

  // field types and members
  using _from_pose_type =
    std::vector<int32_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<int32_t>>;
  _from_pose_type from_pose;
  using _to_pose_type =
    std::vector<int32_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<int32_t>>;
  _to_pose_type to_pose;
  using _cost_type =
    double;
  _cost_type cost;
  using _current_state_type =
    ltl_automaton_msgs::msg::TransitionSystemState_<ContainerAllocator>;
  _current_state_type current_state;
  using _exec_index_type =
    int32_t;
  _exec_index_type exec_index;
  using _type_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _type_type type;

  // setters for named parameter idiom
  Type & set__from_pose(
    const std::vector<int32_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<int32_t>> & _arg)
  {
    this->from_pose = _arg;
    return *this;
  }
  Type & set__to_pose(
    const std::vector<int32_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<int32_t>> & _arg)
  {
    this->to_pose = _arg;
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
  Type & set__type(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->type = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ltl_automaton_msgs::msg::RelayRequest_<ContainerAllocator> *;
  using ConstRawPtr =
    const ltl_automaton_msgs::msg::RelayRequest_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ltl_automaton_msgs::msg::RelayRequest_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ltl_automaton_msgs::msg::RelayRequest_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ltl_automaton_msgs::msg::RelayRequest_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ltl_automaton_msgs::msg::RelayRequest_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ltl_automaton_msgs::msg::RelayRequest_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ltl_automaton_msgs::msg::RelayRequest_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ltl_automaton_msgs::msg::RelayRequest_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ltl_automaton_msgs::msg::RelayRequest_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ltl_automaton_msgs__msg__RelayRequest
    std::shared_ptr<ltl_automaton_msgs::msg::RelayRequest_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ltl_automaton_msgs__msg__RelayRequest
    std::shared_ptr<ltl_automaton_msgs::msg::RelayRequest_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const RelayRequest_ & other) const
  {
    if (this->from_pose != other.from_pose) {
      return false;
    }
    if (this->to_pose != other.to_pose) {
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
    if (this->type != other.type) {
      return false;
    }
    return true;
  }
  bool operator!=(const RelayRequest_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct RelayRequest_

// alias to use template instance with default allocator
using RelayRequest =
  ltl_automaton_msgs::msg::RelayRequest_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace ltl_automaton_msgs

#endif  // LTL_AUTOMATON_MSGS__MSG__DETAIL__RELAY_REQUEST__STRUCT_HPP_
