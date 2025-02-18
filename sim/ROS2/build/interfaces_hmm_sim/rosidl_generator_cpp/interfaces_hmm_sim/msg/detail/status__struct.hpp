// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from interfaces_hmm_sim:msg/Status.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES_HMM_SIM__MSG__DETAIL__STATUS__STRUCT_HPP_
#define INTERFACES_HMM_SIM__MSG__DETAIL__STATUS__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__interfaces_hmm_sim__msg__Status __attribute__((deprecated))
#else
# define DEPRECATED__interfaces_hmm_sim__msg__Status __declspec(deprecated)
#endif

namespace interfaces_hmm_sim
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Status_
{
  using Type = Status_<ContainerAllocator>;

  explicit Status_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->agent = "";
      this->start = false;
      this->arrived = false;
      this->replan_received = false;
    }
  }

  explicit Status_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : agent(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->agent = "";
      this->start = false;
      this->arrived = false;
      this->replan_received = false;
    }
  }

  // field types and members
  using _agent_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _agent_type agent;
  using _start_type =
    bool;
  _start_type start;
  using _arrived_type =
    bool;
  _arrived_type arrived;
  using _replan_received_type =
    bool;
  _replan_received_type replan_received;

  // setters for named parameter idiom
  Type & set__agent(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->agent = _arg;
    return *this;
  }
  Type & set__start(
    const bool & _arg)
  {
    this->start = _arg;
    return *this;
  }
  Type & set__arrived(
    const bool & _arg)
  {
    this->arrived = _arg;
    return *this;
  }
  Type & set__replan_received(
    const bool & _arg)
  {
    this->replan_received = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interfaces_hmm_sim::msg::Status_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces_hmm_sim::msg::Status_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces_hmm_sim::msg::Status_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces_hmm_sim::msg::Status_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces_hmm_sim::msg::Status_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces_hmm_sim::msg::Status_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces_hmm_sim::msg::Status_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces_hmm_sim::msg::Status_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces_hmm_sim::msg::Status_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces_hmm_sim::msg::Status_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces_hmm_sim__msg__Status
    std::shared_ptr<interfaces_hmm_sim::msg::Status_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces_hmm_sim__msg__Status
    std::shared_ptr<interfaces_hmm_sim::msg::Status_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Status_ & other) const
  {
    if (this->agent != other.agent) {
      return false;
    }
    if (this->start != other.start) {
      return false;
    }
    if (this->arrived != other.arrived) {
      return false;
    }
    if (this->replan_received != other.replan_received) {
      return false;
    }
    return true;
  }
  bool operator!=(const Status_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Status_

// alias to use template instance with default allocator
using Status =
  interfaces_hmm_sim::msg::Status_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace interfaces_hmm_sim

#endif  // INTERFACES_HMM_SIM__MSG__DETAIL__STATUS__STRUCT_HPP_
