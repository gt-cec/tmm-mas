// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from ltl_automaton_msgs:srv/TaskReplanningDelete.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "ltl_automaton_msgs/srv/detail/task_replanning_delete__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace ltl_automaton_msgs
{

namespace srv
{

namespace rosidl_typesupport_introspection_cpp
{

void TaskReplanningDelete_Request_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) ltl_automaton_msgs::srv::TaskReplanningDelete_Request(_init);
}

void TaskReplanningDelete_Request_fini_function(void * message_memory)
{
  auto typed_message = static_cast<ltl_automaton_msgs::srv::TaskReplanningDelete_Request *>(message_memory);
  typed_message->~TaskReplanningDelete_Request();
}

size_t size_function__TaskReplanningDelete_Request__delete_from(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<int32_t> *>(untyped_member);
  return member->size();
}

const void * get_const_function__TaskReplanningDelete_Request__delete_from(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<int32_t> *>(untyped_member);
  return &member[index];
}

void * get_function__TaskReplanningDelete_Request__delete_from(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<int32_t> *>(untyped_member);
  return &member[index];
}

void fetch_function__TaskReplanningDelete_Request__delete_from(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const int32_t *>(
    get_const_function__TaskReplanningDelete_Request__delete_from(untyped_member, index));
  auto & value = *reinterpret_cast<int32_t *>(untyped_value);
  value = item;
}

void assign_function__TaskReplanningDelete_Request__delete_from(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<int32_t *>(
    get_function__TaskReplanningDelete_Request__delete_from(untyped_member, index));
  const auto & value = *reinterpret_cast<const int32_t *>(untyped_value);
  item = value;
}

void resize_function__TaskReplanningDelete_Request__delete_from(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<int32_t> *>(untyped_member);
  member->resize(size);
}

size_t size_function__TaskReplanningDelete_Request__delete_to(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<int32_t> *>(untyped_member);
  return member->size();
}

const void * get_const_function__TaskReplanningDelete_Request__delete_to(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<int32_t> *>(untyped_member);
  return &member[index];
}

void * get_function__TaskReplanningDelete_Request__delete_to(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<int32_t> *>(untyped_member);
  return &member[index];
}

void fetch_function__TaskReplanningDelete_Request__delete_to(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const int32_t *>(
    get_const_function__TaskReplanningDelete_Request__delete_to(untyped_member, index));
  auto & value = *reinterpret_cast<int32_t *>(untyped_value);
  value = item;
}

void assign_function__TaskReplanningDelete_Request__delete_to(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<int32_t *>(
    get_function__TaskReplanningDelete_Request__delete_to(untyped_member, index));
  const auto & value = *reinterpret_cast<const int32_t *>(untyped_value);
  item = value;
}

void resize_function__TaskReplanningDelete_Request__delete_to(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<int32_t> *>(untyped_member);
  member->resize(size);
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember TaskReplanningDelete_Request_message_member_array[4] = {
  {
    "delete_from",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ltl_automaton_msgs::srv::TaskReplanningDelete_Request, delete_from),  // bytes offset in struct
    nullptr,  // default value
    size_function__TaskReplanningDelete_Request__delete_from,  // size() function pointer
    get_const_function__TaskReplanningDelete_Request__delete_from,  // get_const(index) function pointer
    get_function__TaskReplanningDelete_Request__delete_from,  // get(index) function pointer
    fetch_function__TaskReplanningDelete_Request__delete_from,  // fetch(index, &value) function pointer
    assign_function__TaskReplanningDelete_Request__delete_from,  // assign(index, value) function pointer
    resize_function__TaskReplanningDelete_Request__delete_from  // resize(index) function pointer
  },
  {
    "delete_to",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ltl_automaton_msgs::srv::TaskReplanningDelete_Request, delete_to),  // bytes offset in struct
    nullptr,  // default value
    size_function__TaskReplanningDelete_Request__delete_to,  // size() function pointer
    get_const_function__TaskReplanningDelete_Request__delete_to,  // get_const(index) function pointer
    get_function__TaskReplanningDelete_Request__delete_to,  // get(index) function pointer
    fetch_function__TaskReplanningDelete_Request__delete_to,  // fetch(index, &value) function pointer
    assign_function__TaskReplanningDelete_Request__delete_to,  // assign(index, value) function pointer
    resize_function__TaskReplanningDelete_Request__delete_to  // resize(index) function pointer
  },
  {
    "current_state",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<ltl_automaton_msgs::msg::TransitionSystemState>(),  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ltl_automaton_msgs::srv::TaskReplanningDelete_Request, current_state),  // bytes offset in struct
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
    offsetof(ltl_automaton_msgs::srv::TaskReplanningDelete_Request, exec_index),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers TaskReplanningDelete_Request_message_members = {
  "ltl_automaton_msgs::srv",  // message namespace
  "TaskReplanningDelete_Request",  // message name
  4,  // number of fields
  sizeof(ltl_automaton_msgs::srv::TaskReplanningDelete_Request),
  TaskReplanningDelete_Request_message_member_array,  // message members
  TaskReplanningDelete_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  TaskReplanningDelete_Request_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t TaskReplanningDelete_Request_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &TaskReplanningDelete_Request_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace srv

}  // namespace ltl_automaton_msgs


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<ltl_automaton_msgs::srv::TaskReplanningDelete_Request>()
{
  return &::ltl_automaton_msgs::srv::rosidl_typesupport_introspection_cpp::TaskReplanningDelete_Request_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, ltl_automaton_msgs, srv, TaskReplanningDelete_Request)() {
  return &::ltl_automaton_msgs::srv::rosidl_typesupport_introspection_cpp::TaskReplanningDelete_Request_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

// already included above
// #include "array"
// already included above
// #include "cstddef"
// already included above
// #include "string"
// already included above
// #include "vector"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_interface/macros.h"
// already included above
// #include "ltl_automaton_msgs/srv/detail/task_replanning_delete__struct.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/field_types.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace ltl_automaton_msgs
{

namespace srv
{

namespace rosidl_typesupport_introspection_cpp
{

void TaskReplanningDelete_Response_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) ltl_automaton_msgs::srv::TaskReplanningDelete_Response(_init);
}

void TaskReplanningDelete_Response_fini_function(void * message_memory)
{
  auto typed_message = static_cast<ltl_automaton_msgs::srv::TaskReplanningDelete_Response *>(message_memory);
  typed_message->~TaskReplanningDelete_Response();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember TaskReplanningDelete_Response_message_member_array[3] = {
  {
    "success",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ltl_automaton_msgs::srv::TaskReplanningDelete_Response, success),  // bytes offset in struct
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
    offsetof(ltl_automaton_msgs::srv::TaskReplanningDelete_Response, new_plan_prefix),  // bytes offset in struct
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
    offsetof(ltl_automaton_msgs::srv::TaskReplanningDelete_Response, new_plan_suffix),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers TaskReplanningDelete_Response_message_members = {
  "ltl_automaton_msgs::srv",  // message namespace
  "TaskReplanningDelete_Response",  // message name
  3,  // number of fields
  sizeof(ltl_automaton_msgs::srv::TaskReplanningDelete_Response),
  TaskReplanningDelete_Response_message_member_array,  // message members
  TaskReplanningDelete_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  TaskReplanningDelete_Response_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t TaskReplanningDelete_Response_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &TaskReplanningDelete_Response_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace srv

}  // namespace ltl_automaton_msgs


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<ltl_automaton_msgs::srv::TaskReplanningDelete_Response>()
{
  return &::ltl_automaton_msgs::srv::rosidl_typesupport_introspection_cpp::TaskReplanningDelete_Response_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, ltl_automaton_msgs, srv, TaskReplanningDelete_Response)() {
  return &::ltl_automaton_msgs::srv::rosidl_typesupport_introspection_cpp::TaskReplanningDelete_Response_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_interface/macros.h"
// already included above
// #include "rosidl_typesupport_introspection_cpp/visibility_control.h"
// already included above
// #include "ltl_automaton_msgs/srv/detail/task_replanning_delete__struct.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/service_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/service_type_support_decl.hpp"

namespace ltl_automaton_msgs
{

namespace srv
{

namespace rosidl_typesupport_introspection_cpp
{

// this is intentionally not const to allow initialization later to prevent an initialization race
static ::rosidl_typesupport_introspection_cpp::ServiceMembers TaskReplanningDelete_service_members = {
  "ltl_automaton_msgs::srv",  // service namespace
  "TaskReplanningDelete",  // service name
  // these two fields are initialized below on the first access
  // see get_service_type_support_handle<ltl_automaton_msgs::srv::TaskReplanningDelete>()
  nullptr,  // request message
  nullptr  // response message
};

static const rosidl_service_type_support_t TaskReplanningDelete_service_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &TaskReplanningDelete_service_members,
  get_service_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace srv

}  // namespace ltl_automaton_msgs


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_service_type_support_t *
get_service_type_support_handle<ltl_automaton_msgs::srv::TaskReplanningDelete>()
{
  // get a handle to the value to be returned
  auto service_type_support =
    &::ltl_automaton_msgs::srv::rosidl_typesupport_introspection_cpp::TaskReplanningDelete_service_type_support_handle;
  // get a non-const and properly typed version of the data void *
  auto service_members = const_cast<::rosidl_typesupport_introspection_cpp::ServiceMembers *>(
    static_cast<const ::rosidl_typesupport_introspection_cpp::ServiceMembers *>(
      service_type_support->data));
  // make sure that both the request_members_ and the response_members_ are initialized
  // if they are not, initialize them
  if (
    service_members->request_members_ == nullptr ||
    service_members->response_members_ == nullptr)
  {
    // initialize the request_members_ with the static function from the external library
    service_members->request_members_ = static_cast<
      const ::rosidl_typesupport_introspection_cpp::MessageMembers *
      >(
      ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<
        ::ltl_automaton_msgs::srv::TaskReplanningDelete_Request
      >()->data
      );
    // initialize the response_members_ with the static function from the external library
    service_members->response_members_ = static_cast<
      const ::rosidl_typesupport_introspection_cpp::MessageMembers *
      >(
      ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<
        ::ltl_automaton_msgs::srv::TaskReplanningDelete_Response
      >()->data
      );
  }
  // finally return the properly initialized service_type_support handle
  return service_type_support;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, ltl_automaton_msgs, srv, TaskReplanningDelete)() {
  return ::rosidl_typesupport_introspection_cpp::get_service_type_support_handle<ltl_automaton_msgs::srv::TaskReplanningDelete>();
}

#ifdef __cplusplus
}
#endif
