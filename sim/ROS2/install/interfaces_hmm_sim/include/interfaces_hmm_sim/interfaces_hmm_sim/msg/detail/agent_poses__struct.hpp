// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from interfaces_hmm_sim:msg/AgentPoses.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES_HMM_SIM__MSG__DETAIL__AGENT_POSES__STRUCT_HPP_
#define INTERFACES_HMM_SIM__MSG__DETAIL__AGENT_POSES__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__interfaces_hmm_sim__msg__AgentPoses __attribute__((deprecated))
#else
# define DEPRECATED__interfaces_hmm_sim__msg__AgentPoses __declspec(deprecated)
#endif

namespace interfaces_hmm_sim
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct AgentPoses_
{
  using Type = AgentPoses_<ContainerAllocator>;

  explicit AgentPoses_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
  }

  explicit AgentPoses_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
    (void)_alloc;
  }

  // field types and members
  using _agents_type =
    std::vector<int32_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<int32_t>>;
  _agents_type agents;
  using _x_type =
    std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>>;
  _x_type x;
  using _y_type =
    std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>>;
  _y_type y;
  using _z_type =
    std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>>;
  _z_type z;

  // setters for named parameter idiom
  Type & set__agents(
    const std::vector<int32_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<int32_t>> & _arg)
  {
    this->agents = _arg;
    return *this;
  }
  Type & set__x(
    const std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>> & _arg)
  {
    this->x = _arg;
    return *this;
  }
  Type & set__y(
    const std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>> & _arg)
  {
    this->y = _arg;
    return *this;
  }
  Type & set__z(
    const std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>> & _arg)
  {
    this->z = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interfaces_hmm_sim::msg::AgentPoses_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces_hmm_sim::msg::AgentPoses_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces_hmm_sim::msg::AgentPoses_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces_hmm_sim::msg::AgentPoses_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces_hmm_sim::msg::AgentPoses_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces_hmm_sim::msg::AgentPoses_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces_hmm_sim::msg::AgentPoses_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces_hmm_sim::msg::AgentPoses_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces_hmm_sim::msg::AgentPoses_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces_hmm_sim::msg::AgentPoses_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces_hmm_sim__msg__AgentPoses
    std::shared_ptr<interfaces_hmm_sim::msg::AgentPoses_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces_hmm_sim__msg__AgentPoses
    std::shared_ptr<interfaces_hmm_sim::msg::AgentPoses_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const AgentPoses_ & other) const
  {
    if (this->agents != other.agents) {
      return false;
    }
    if (this->x != other.x) {
      return false;
    }
    if (this->y != other.y) {
      return false;
    }
    if (this->z != other.z) {
      return false;
    }
    return true;
  }
  bool operator!=(const AgentPoses_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct AgentPoses_

// alias to use template instance with default allocator
using AgentPoses =
  interfaces_hmm_sim::msg::AgentPoses_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace interfaces_hmm_sim

#endif  // INTERFACES_HMM_SIM__MSG__DETAIL__AGENT_POSES__STRUCT_HPP_
