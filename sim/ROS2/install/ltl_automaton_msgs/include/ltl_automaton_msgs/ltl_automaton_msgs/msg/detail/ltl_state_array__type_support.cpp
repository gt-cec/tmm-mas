// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from ltl_automaton_msgs:msg/LTLStateArray.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "ltl_automaton_msgs/msg/detail/ltl_state_array__struct.hpp"
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

void LTLStateArray_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) ltl_automaton_msgs::msg::LTLStateArray(_init);
}

void LTLStateArray_fini_function(void * message_memory)
{
  auto typed_message = static_cast<ltl_automaton_msgs::msg::LTLStateArray *>(message_memory);
  typed_message->~LTLStateArray();
}

size_t size_function__LTLStateArray__ltl_states(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<ltl_automaton_msgs::msg::LTLState> *>(untyped_member);
  return member->size();
}

const void * get_const_function__LTLStateArray__ltl_states(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<ltl_automaton_msgs::msg::LTLState> *>(untyped_member);
  return &member[index];
}

void * get_function__LTLStateArray__ltl_states(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<ltl_automaton_msgs::msg::LTLState> *>(untyped_member);
  return &member[index];
}

void fetch_function__LTLStateArray__ltl_states(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const ltl_automaton_msgs::msg::LTLState *>(
    get_const_function__LTLStateArray__ltl_states(untyped_member, index));
  auto & value = *reinterpret_cast<ltl_automaton_msgs::msg::LTLState *>(untyped_value);
  value = item;
}

void assign_function__LTLStateArray__ltl_states(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<ltl_automaton_msgs::msg::LTLState *>(
    get_function__LTLStateArray__ltl_states(untyped_member, index));
  const auto & value = *reinterpret_cast<const ltl_automaton_msgs::msg::LTLState *>(untyped_value);
  item = value;
}

void resize_function__LTLStateArray__ltl_states(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<ltl_automaton_msgs::msg::LTLState> *>(untyped_member);
  member->resize(size);
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember LTLStateArray_message_member_array[1] = {
  {
    "ltl_states",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<ltl_automaton_msgs::msg::LTLState>(),  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ltl_automaton_msgs::msg::LTLStateArray, ltl_states),  // bytes offset in struct
    nullptr,  // default value
    size_function__LTLStateArray__ltl_states,  // size() function pointer
    get_const_function__LTLStateArray__ltl_states,  // get_const(index) function pointer
    get_function__LTLStateArray__ltl_states,  // get(index) function pointer
    fetch_function__LTLStateArray__ltl_states,  // fetch(index, &value) function pointer
    assign_function__LTLStateArray__ltl_states,  // assign(index, value) function pointer
    resize_function__LTLStateArray__ltl_states  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers LTLStateArray_message_members = {
  "ltl_automaton_msgs::msg",  // message namespace
  "LTLStateArray",  // message name
  1,  // number of fields
  sizeof(ltl_automaton_msgs::msg::LTLStateArray),
  LTLStateArray_message_member_array,  // message members
  LTLStateArray_init_function,  // function to initialize message memory (memory has to be allocated)
  LTLStateArray_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t LTLStateArray_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &LTLStateArray_message_members,
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
get_message_type_support_handle<ltl_automaton_msgs::msg::LTLStateArray>()
{
  return &::ltl_automaton_msgs::msg::rosidl_typesupport_introspection_cpp::LTLStateArray_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, ltl_automaton_msgs, msg, LTLStateArray)() {
  return &::ltl_automaton_msgs::msg::rosidl_typesupport_introspection_cpp::LTLStateArray_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
