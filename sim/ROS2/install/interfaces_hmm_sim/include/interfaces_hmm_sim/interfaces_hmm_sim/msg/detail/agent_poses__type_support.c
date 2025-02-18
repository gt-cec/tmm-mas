// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from interfaces_hmm_sim:msg/AgentPoses.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "interfaces_hmm_sim/msg/detail/agent_poses__rosidl_typesupport_introspection_c.h"
#include "interfaces_hmm_sim/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "interfaces_hmm_sim/msg/detail/agent_poses__functions.h"
#include "interfaces_hmm_sim/msg/detail/agent_poses__struct.h"


// Include directives for member types
// Member `agents`
// Member `x`
// Member `y`
// Member `z`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__AgentPoses_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  interfaces_hmm_sim__msg__AgentPoses__init(message_memory);
}

void interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__AgentPoses_fini_function(void * message_memory)
{
  interfaces_hmm_sim__msg__AgentPoses__fini(message_memory);
}

size_t interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__size_function__AgentPoses__agents(
  const void * untyped_member)
{
  const rosidl_runtime_c__int32__Sequence * member =
    (const rosidl_runtime_c__int32__Sequence *)(untyped_member);
  return member->size;
}

const void * interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__get_const_function__AgentPoses__agents(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__int32__Sequence * member =
    (const rosidl_runtime_c__int32__Sequence *)(untyped_member);
  return &member->data[index];
}

void * interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__get_function__AgentPoses__agents(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__int32__Sequence * member =
    (rosidl_runtime_c__int32__Sequence *)(untyped_member);
  return &member->data[index];
}

void interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__fetch_function__AgentPoses__agents(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const int32_t * item =
    ((const int32_t *)
    interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__get_const_function__AgentPoses__agents(untyped_member, index));
  int32_t * value =
    (int32_t *)(untyped_value);
  *value = *item;
}

void interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__assign_function__AgentPoses__agents(
  void * untyped_member, size_t index, const void * untyped_value)
{
  int32_t * item =
    ((int32_t *)
    interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__get_function__AgentPoses__agents(untyped_member, index));
  const int32_t * value =
    (const int32_t *)(untyped_value);
  *item = *value;
}

bool interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__resize_function__AgentPoses__agents(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__int32__Sequence * member =
    (rosidl_runtime_c__int32__Sequence *)(untyped_member);
  rosidl_runtime_c__int32__Sequence__fini(member);
  return rosidl_runtime_c__int32__Sequence__init(member, size);
}

size_t interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__size_function__AgentPoses__x(
  const void * untyped_member)
{
  const rosidl_runtime_c__float__Sequence * member =
    (const rosidl_runtime_c__float__Sequence *)(untyped_member);
  return member->size;
}

const void * interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__get_const_function__AgentPoses__x(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__float__Sequence * member =
    (const rosidl_runtime_c__float__Sequence *)(untyped_member);
  return &member->data[index];
}

void * interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__get_function__AgentPoses__x(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__float__Sequence * member =
    (rosidl_runtime_c__float__Sequence *)(untyped_member);
  return &member->data[index];
}

void interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__fetch_function__AgentPoses__x(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const float * item =
    ((const float *)
    interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__get_const_function__AgentPoses__x(untyped_member, index));
  float * value =
    (float *)(untyped_value);
  *value = *item;
}

void interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__assign_function__AgentPoses__x(
  void * untyped_member, size_t index, const void * untyped_value)
{
  float * item =
    ((float *)
    interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__get_function__AgentPoses__x(untyped_member, index));
  const float * value =
    (const float *)(untyped_value);
  *item = *value;
}

bool interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__resize_function__AgentPoses__x(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__float__Sequence * member =
    (rosidl_runtime_c__float__Sequence *)(untyped_member);
  rosidl_runtime_c__float__Sequence__fini(member);
  return rosidl_runtime_c__float__Sequence__init(member, size);
}

size_t interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__size_function__AgentPoses__y(
  const void * untyped_member)
{
  const rosidl_runtime_c__float__Sequence * member =
    (const rosidl_runtime_c__float__Sequence *)(untyped_member);
  return member->size;
}

const void * interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__get_const_function__AgentPoses__y(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__float__Sequence * member =
    (const rosidl_runtime_c__float__Sequence *)(untyped_member);
  return &member->data[index];
}

void * interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__get_function__AgentPoses__y(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__float__Sequence * member =
    (rosidl_runtime_c__float__Sequence *)(untyped_member);
  return &member->data[index];
}

void interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__fetch_function__AgentPoses__y(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const float * item =
    ((const float *)
    interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__get_const_function__AgentPoses__y(untyped_member, index));
  float * value =
    (float *)(untyped_value);
  *value = *item;
}

void interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__assign_function__AgentPoses__y(
  void * untyped_member, size_t index, const void * untyped_value)
{
  float * item =
    ((float *)
    interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__get_function__AgentPoses__y(untyped_member, index));
  const float * value =
    (const float *)(untyped_value);
  *item = *value;
}

bool interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__resize_function__AgentPoses__y(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__float__Sequence * member =
    (rosidl_runtime_c__float__Sequence *)(untyped_member);
  rosidl_runtime_c__float__Sequence__fini(member);
  return rosidl_runtime_c__float__Sequence__init(member, size);
}

size_t interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__size_function__AgentPoses__z(
  const void * untyped_member)
{
  const rosidl_runtime_c__float__Sequence * member =
    (const rosidl_runtime_c__float__Sequence *)(untyped_member);
  return member->size;
}

const void * interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__get_const_function__AgentPoses__z(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__float__Sequence * member =
    (const rosidl_runtime_c__float__Sequence *)(untyped_member);
  return &member->data[index];
}

void * interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__get_function__AgentPoses__z(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__float__Sequence * member =
    (rosidl_runtime_c__float__Sequence *)(untyped_member);
  return &member->data[index];
}

void interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__fetch_function__AgentPoses__z(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const float * item =
    ((const float *)
    interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__get_const_function__AgentPoses__z(untyped_member, index));
  float * value =
    (float *)(untyped_value);
  *value = *item;
}

void interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__assign_function__AgentPoses__z(
  void * untyped_member, size_t index, const void * untyped_value)
{
  float * item =
    ((float *)
    interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__get_function__AgentPoses__z(untyped_member, index));
  const float * value =
    (const float *)(untyped_value);
  *item = *value;
}

bool interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__resize_function__AgentPoses__z(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__float__Sequence * member =
    (rosidl_runtime_c__float__Sequence *)(untyped_member);
  rosidl_runtime_c__float__Sequence__fini(member);
  return rosidl_runtime_c__float__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__AgentPoses_message_member_array[4] = {
  {
    "agents",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces_hmm_sim__msg__AgentPoses, agents),  // bytes offset in struct
    NULL,  // default value
    interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__size_function__AgentPoses__agents,  // size() function pointer
    interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__get_const_function__AgentPoses__agents,  // get_const(index) function pointer
    interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__get_function__AgentPoses__agents,  // get(index) function pointer
    interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__fetch_function__AgentPoses__agents,  // fetch(index, &value) function pointer
    interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__assign_function__AgentPoses__agents,  // assign(index, value) function pointer
    interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__resize_function__AgentPoses__agents  // resize(index) function pointer
  },
  {
    "x",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces_hmm_sim__msg__AgentPoses, x),  // bytes offset in struct
    NULL,  // default value
    interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__size_function__AgentPoses__x,  // size() function pointer
    interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__get_const_function__AgentPoses__x,  // get_const(index) function pointer
    interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__get_function__AgentPoses__x,  // get(index) function pointer
    interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__fetch_function__AgentPoses__x,  // fetch(index, &value) function pointer
    interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__assign_function__AgentPoses__x,  // assign(index, value) function pointer
    interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__resize_function__AgentPoses__x  // resize(index) function pointer
  },
  {
    "y",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces_hmm_sim__msg__AgentPoses, y),  // bytes offset in struct
    NULL,  // default value
    interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__size_function__AgentPoses__y,  // size() function pointer
    interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__get_const_function__AgentPoses__y,  // get_const(index) function pointer
    interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__get_function__AgentPoses__y,  // get(index) function pointer
    interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__fetch_function__AgentPoses__y,  // fetch(index, &value) function pointer
    interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__assign_function__AgentPoses__y,  // assign(index, value) function pointer
    interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__resize_function__AgentPoses__y  // resize(index) function pointer
  },
  {
    "z",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces_hmm_sim__msg__AgentPoses, z),  // bytes offset in struct
    NULL,  // default value
    interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__size_function__AgentPoses__z,  // size() function pointer
    interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__get_const_function__AgentPoses__z,  // get_const(index) function pointer
    interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__get_function__AgentPoses__z,  // get(index) function pointer
    interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__fetch_function__AgentPoses__z,  // fetch(index, &value) function pointer
    interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__assign_function__AgentPoses__z,  // assign(index, value) function pointer
    interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__resize_function__AgentPoses__z  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__AgentPoses_message_members = {
  "interfaces_hmm_sim__msg",  // message namespace
  "AgentPoses",  // message name
  4,  // number of fields
  sizeof(interfaces_hmm_sim__msg__AgentPoses),
  interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__AgentPoses_message_member_array,  // message members
  interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__AgentPoses_init_function,  // function to initialize message memory (memory has to be allocated)
  interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__AgentPoses_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__AgentPoses_message_type_support_handle = {
  0,
  &interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__AgentPoses_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interfaces_hmm_sim
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces_hmm_sim, msg, AgentPoses)() {
  if (!interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__AgentPoses_message_type_support_handle.typesupport_identifier) {
    interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__AgentPoses_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &interfaces_hmm_sim__msg__AgentPoses__rosidl_typesupport_introspection_c__AgentPoses_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
