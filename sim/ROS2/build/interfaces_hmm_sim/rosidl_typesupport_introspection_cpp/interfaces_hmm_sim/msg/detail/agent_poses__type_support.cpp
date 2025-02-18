// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from interfaces_hmm_sim:msg/AgentPoses.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "interfaces_hmm_sim/msg/detail/agent_poses__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace interfaces_hmm_sim
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void AgentPoses_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) interfaces_hmm_sim::msg::AgentPoses(_init);
}

void AgentPoses_fini_function(void * message_memory)
{
  auto typed_message = static_cast<interfaces_hmm_sim::msg::AgentPoses *>(message_memory);
  typed_message->~AgentPoses();
}

size_t size_function__AgentPoses__agents(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<int32_t> *>(untyped_member);
  return member->size();
}

const void * get_const_function__AgentPoses__agents(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<int32_t> *>(untyped_member);
  return &member[index];
}

void * get_function__AgentPoses__agents(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<int32_t> *>(untyped_member);
  return &member[index];
}

void fetch_function__AgentPoses__agents(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const int32_t *>(
    get_const_function__AgentPoses__agents(untyped_member, index));
  auto & value = *reinterpret_cast<int32_t *>(untyped_value);
  value = item;
}

void assign_function__AgentPoses__agents(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<int32_t *>(
    get_function__AgentPoses__agents(untyped_member, index));
  const auto & value = *reinterpret_cast<const int32_t *>(untyped_value);
  item = value;
}

void resize_function__AgentPoses__agents(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<int32_t> *>(untyped_member);
  member->resize(size);
}

size_t size_function__AgentPoses__x(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<float> *>(untyped_member);
  return member->size();
}

const void * get_const_function__AgentPoses__x(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<float> *>(untyped_member);
  return &member[index];
}

void * get_function__AgentPoses__x(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<float> *>(untyped_member);
  return &member[index];
}

void fetch_function__AgentPoses__x(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const float *>(
    get_const_function__AgentPoses__x(untyped_member, index));
  auto & value = *reinterpret_cast<float *>(untyped_value);
  value = item;
}

void assign_function__AgentPoses__x(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<float *>(
    get_function__AgentPoses__x(untyped_member, index));
  const auto & value = *reinterpret_cast<const float *>(untyped_value);
  item = value;
}

void resize_function__AgentPoses__x(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<float> *>(untyped_member);
  member->resize(size);
}

size_t size_function__AgentPoses__y(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<float> *>(untyped_member);
  return member->size();
}

const void * get_const_function__AgentPoses__y(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<float> *>(untyped_member);
  return &member[index];
}

void * get_function__AgentPoses__y(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<float> *>(untyped_member);
  return &member[index];
}

void fetch_function__AgentPoses__y(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const float *>(
    get_const_function__AgentPoses__y(untyped_member, index));
  auto & value = *reinterpret_cast<float *>(untyped_value);
  value = item;
}

void assign_function__AgentPoses__y(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<float *>(
    get_function__AgentPoses__y(untyped_member, index));
  const auto & value = *reinterpret_cast<const float *>(untyped_value);
  item = value;
}

void resize_function__AgentPoses__y(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<float> *>(untyped_member);
  member->resize(size);
}

size_t size_function__AgentPoses__z(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<float> *>(untyped_member);
  return member->size();
}

const void * get_const_function__AgentPoses__z(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<float> *>(untyped_member);
  return &member[index];
}

void * get_function__AgentPoses__z(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<float> *>(untyped_member);
  return &member[index];
}

void fetch_function__AgentPoses__z(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const float *>(
    get_const_function__AgentPoses__z(untyped_member, index));
  auto & value = *reinterpret_cast<float *>(untyped_value);
  value = item;
}

void assign_function__AgentPoses__z(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<float *>(
    get_function__AgentPoses__z(untyped_member, index));
  const auto & value = *reinterpret_cast<const float *>(untyped_value);
  item = value;
}

void resize_function__AgentPoses__z(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<float> *>(untyped_member);
  member->resize(size);
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember AgentPoses_message_member_array[4] = {
  {
    "agents",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces_hmm_sim::msg::AgentPoses, agents),  // bytes offset in struct
    nullptr,  // default value
    size_function__AgentPoses__agents,  // size() function pointer
    get_const_function__AgentPoses__agents,  // get_const(index) function pointer
    get_function__AgentPoses__agents,  // get(index) function pointer
    fetch_function__AgentPoses__agents,  // fetch(index, &value) function pointer
    assign_function__AgentPoses__agents,  // assign(index, value) function pointer
    resize_function__AgentPoses__agents  // resize(index) function pointer
  },
  {
    "x",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces_hmm_sim::msg::AgentPoses, x),  // bytes offset in struct
    nullptr,  // default value
    size_function__AgentPoses__x,  // size() function pointer
    get_const_function__AgentPoses__x,  // get_const(index) function pointer
    get_function__AgentPoses__x,  // get(index) function pointer
    fetch_function__AgentPoses__x,  // fetch(index, &value) function pointer
    assign_function__AgentPoses__x,  // assign(index, value) function pointer
    resize_function__AgentPoses__x  // resize(index) function pointer
  },
  {
    "y",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces_hmm_sim::msg::AgentPoses, y),  // bytes offset in struct
    nullptr,  // default value
    size_function__AgentPoses__y,  // size() function pointer
    get_const_function__AgentPoses__y,  // get_const(index) function pointer
    get_function__AgentPoses__y,  // get(index) function pointer
    fetch_function__AgentPoses__y,  // fetch(index, &value) function pointer
    assign_function__AgentPoses__y,  // assign(index, value) function pointer
    resize_function__AgentPoses__y  // resize(index) function pointer
  },
  {
    "z",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces_hmm_sim::msg::AgentPoses, z),  // bytes offset in struct
    nullptr,  // default value
    size_function__AgentPoses__z,  // size() function pointer
    get_const_function__AgentPoses__z,  // get_const(index) function pointer
    get_function__AgentPoses__z,  // get(index) function pointer
    fetch_function__AgentPoses__z,  // fetch(index, &value) function pointer
    assign_function__AgentPoses__z,  // assign(index, value) function pointer
    resize_function__AgentPoses__z  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers AgentPoses_message_members = {
  "interfaces_hmm_sim::msg",  // message namespace
  "AgentPoses",  // message name
  4,  // number of fields
  sizeof(interfaces_hmm_sim::msg::AgentPoses),
  AgentPoses_message_member_array,  // message members
  AgentPoses_init_function,  // function to initialize message memory (memory has to be allocated)
  AgentPoses_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t AgentPoses_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &AgentPoses_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace interfaces_hmm_sim


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<interfaces_hmm_sim::msg::AgentPoses>()
{
  return &::interfaces_hmm_sim::msg::rosidl_typesupport_introspection_cpp::AgentPoses_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, interfaces_hmm_sim, msg, AgentPoses)() {
  return &::interfaces_hmm_sim::msg::rosidl_typesupport_introspection_cpp::AgentPoses_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
