// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from ltl_automaton_msgs:msg/RelayResponse.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "ltl_automaton_msgs/msg/detail/relay_response__struct.hpp"
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

void RelayResponse_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) ltl_automaton_msgs::msg::RelayResponse(_init);
}

void RelayResponse_fini_function(void * message_memory)
{
  auto typed_message = static_cast<ltl_automaton_msgs::msg::RelayResponse *>(message_memory);
  typed_message->~RelayResponse();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember RelayResponse_message_member_array[3] = {
  {
    "success",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ltl_automaton_msgs::msg::RelayResponse, success),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "new_plan_prefix",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<ltl_automaton_msgs::msg::LTLPlan>(),  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ltl_automaton_msgs::msg::RelayResponse, new_plan_prefix),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "new_plan_suffix",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<ltl_automaton_msgs::msg::LTLPlan>(),  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ltl_automaton_msgs::msg::RelayResponse, new_plan_suffix),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers RelayResponse_message_members = {
  "ltl_automaton_msgs::msg",  // message namespace
  "RelayResponse",  // message name
  3,  // number of fields
  sizeof(ltl_automaton_msgs::msg::RelayResponse),
  RelayResponse_message_member_array,  // message members
  RelayResponse_init_function,  // function to initialize message memory (memory has to be allocated)
  RelayResponse_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t RelayResponse_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &RelayResponse_message_members,
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
get_message_type_support_handle<ltl_automaton_msgs::msg::RelayResponse>()
{
  return &::ltl_automaton_msgs::msg::rosidl_typesupport_introspection_cpp::RelayResponse_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, ltl_automaton_msgs, msg, RelayResponse)() {
  return &::ltl_automaton_msgs::msg::rosidl_typesupport_introspection_cpp::RelayResponse_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
