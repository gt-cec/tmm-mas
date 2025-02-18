// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from ltl_automaton_msgs:msg/RelayRequest.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "ltl_automaton_msgs/msg/detail/relay_request__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace ltl_automaton_msgs
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void RelayRequest_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) ltl_automaton_msgs::msg::RelayRequest(_init);
}

void RelayRequest_fini_function(void * message_memory)
{
  auto typed_message = static_cast<ltl_automaton_msgs::msg::RelayRequest *>(message_memory);
  typed_message->~RelayRequest();
}

size_t size_function__RelayRequest__from_pose(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<int32_t> *>(untyped_member);
  return member->size();
}

const void * get_const_function__RelayRequest__from_pose(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<int32_t> *>(untyped_member);
  return &member[index];
}

void * get_function__RelayRequest__from_pose(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<int32_t> *>(untyped_member);
  return &member[index];
}

void fetch_function__RelayRequest__from_pose(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const int32_t *>(
    get_const_function__RelayRequest__from_pose(untyped_member, index));
  auto & value = *reinterpret_cast<int32_t *>(untyped_value);
  value = item;
}

void assign_function__RelayRequest__from_pose(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<int32_t *>(
    get_function__RelayRequest__from_pose(untyped_member, index));
  const auto & value = *reinterpret_cast<const int32_t *>(untyped_value);
  item = value;
}

void resize_function__RelayRequest__from_pose(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<int32_t> *>(untyped_member);
  member->resize(size);
}

size_t size_function__RelayRequest__to_pose(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<int32_t> *>(untyped_member);
  return member->size();
}

const void * get_const_function__RelayRequest__to_pose(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<int32_t> *>(untyped_member);
  return &member[index];
}

void * get_function__RelayRequest__to_pose(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<int32_t> *>(untyped_member);
  return &member[index];
}

void fetch_function__RelayRequest__to_pose(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const int32_t *>(
    get_const_function__RelayRequest__to_pose(untyped_member, index));
  auto & value = *reinterpret_cast<int32_t *>(untyped_value);
  value = item;
}

void assign_function__RelayRequest__to_pose(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<int32_t *>(
    get_function__RelayRequest__to_pose(untyped_member, index));
  const auto & value = *reinterpret_cast<const int32_t *>(untyped_value);
  item = value;
}

void resize_function__RelayRequest__to_pose(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<int32_t> *>(untyped_member);
  member->resize(size);
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember RelayRequest_message_member_array[6] = {
  {
    "from_pose",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ltl_automaton_msgs::msg::RelayRequest, from_pose),  // bytes offset in struct
    nullptr,  // default value
    size_function__RelayRequest__from_pose,  // size() function pointer
    get_const_function__RelayRequest__from_pose,  // get_const(index) function pointer
    get_function__RelayRequest__from_pose,  // get(index) function pointer
    fetch_function__RelayRequest__from_pose,  // fetch(index, &value) function pointer
    assign_function__RelayRequest__from_pose,  // assign(index, value) function pointer
    resize_function__RelayRequest__from_pose  // resize(index) function pointer
  },
  {
    "to_pose",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ltl_automaton_msgs::msg::RelayRequest, to_pose),  // bytes offset in struct
    nullptr,  // default value
    size_function__RelayRequest__to_pose,  // size() function pointer
    get_const_function__RelayRequest__to_pose,  // get_const(index) function pointer
    get_function__RelayRequest__to_pose,  // get(index) function pointer
    fetch_function__RelayRequest__to_pose,  // fetch(index, &value) function pointer
    assign_function__RelayRequest__to_pose,  // assign(index, value) function pointer
    resize_function__RelayRequest__to_pose  // resize(index) function pointer
  },
  {
    "cost",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ltl_automaton_msgs::msg::RelayRequest, cost),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "current_state",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<ltl_automaton_msgs::msg::TransitionSystemState>(),  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ltl_automaton_msgs::msg::RelayRequest, current_state),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "exec_index",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ltl_automaton_msgs::msg::RelayRequest, exec_index),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "type",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ltl_automaton_msgs::msg::RelayRequest, type),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers RelayRequest_message_members = {
  "ltl_automaton_msgs::msg",  // message namespace
  "RelayRequest",  // message name
  6,  // number of fields
  sizeof(ltl_automaton_msgs::msg::RelayRequest),
  RelayRequest_message_member_array,  // message members
  RelayRequest_init_function,  // function to initialize message memory (memory has to be allocated)
  RelayRequest_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t RelayRequest_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &RelayRequest_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace ltl_automaton_msgs


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<ltl_automaton_msgs::msg::RelayRequest>()
{
  return &::ltl_automaton_msgs::msg::rosidl_typesupport_introspection_cpp::RelayRequest_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, ltl_automaton_msgs, msg, RelayRequest)() {
  return &::ltl_automaton_msgs::msg::rosidl_typesupport_introspection_cpp::RelayRequest_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
