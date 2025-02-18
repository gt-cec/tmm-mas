// generated from rosidl_typesupport_cpp/resource/idl__type_support.cpp.em
// with input from ltl_automaton_msgs:srv/TrapCheck.idl
// generated code does not contain a copyright notice

#include "cstddef"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "ltl_automaton_msgs/srv/detail/trap_check__struct.hpp"
#include "rosidl_typesupport_cpp/identifier.hpp"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_c/type_support_map.h"
#include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
#include "rosidl_typesupport_cpp/visibility_control.h"
#include "rosidl_typesupport_interface/macros.h"

namespace ltl_automaton_msgs
{

namespace srv
{

namespace rosidl_typesupport_cpp
{

typedef struct _TrapCheck_Request_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _TrapCheck_Request_type_support_ids_t;

static const _TrapCheck_Request_type_support_ids_t _TrapCheck_Request_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _TrapCheck_Request_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _TrapCheck_Request_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _TrapCheck_Request_type_support_symbol_names_t _TrapCheck_Request_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, ltl_automaton_msgs, srv, TrapCheck_Request)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, ltl_automaton_msgs, srv, TrapCheck_Request)),
  }
};

typedef struct _TrapCheck_Request_type_support_data_t
{
  void * data[2];
} _TrapCheck_Request_type_support_data_t;

static _TrapCheck_Request_type_support_data_t _TrapCheck_Request_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _TrapCheck_Request_message_typesupport_map = {
  2,
  "ltl_automaton_msgs",
  &_TrapCheck_Request_message_typesupport_ids.typesupport_identifier[0],
  &_TrapCheck_Request_message_typesupport_symbol_names.symbol_name[0],
  &_TrapCheck_Request_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t TrapCheck_Request_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_TrapCheck_Request_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace srv

}  // namespace ltl_automaton_msgs

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<ltl_automaton_msgs::srv::TrapCheck_Request>()
{
  return &::ltl_automaton_msgs::srv::rosidl_typesupport_cpp::TrapCheck_Request_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, ltl_automaton_msgs, srv, TrapCheck_Request)() {
  return get_message_type_support_handle<ltl_automaton_msgs::srv::TrapCheck_Request>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "ltl_automaton_msgs/srv/detail/trap_check__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace ltl_automaton_msgs
{

namespace srv
{

namespace rosidl_typesupport_cpp
{

typedef struct _TrapCheck_Response_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _TrapCheck_Response_type_support_ids_t;

static const _TrapCheck_Response_type_support_ids_t _TrapCheck_Response_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _TrapCheck_Response_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _TrapCheck_Response_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _TrapCheck_Response_type_support_symbol_names_t _TrapCheck_Response_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, ltl_automaton_msgs, srv, TrapCheck_Response)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, ltl_automaton_msgs, srv, TrapCheck_Response)),
  }
};

typedef struct _TrapCheck_Response_type_support_data_t
{
  void * data[2];
} _TrapCheck_Response_type_support_data_t;

static _TrapCheck_Response_type_support_data_t _TrapCheck_Response_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _TrapCheck_Response_message_typesupport_map = {
  2,
  "ltl_automaton_msgs",
  &_TrapCheck_Response_message_typesupport_ids.typesupport_identifier[0],
  &_TrapCheck_Response_message_typesupport_symbol_names.symbol_name[0],
  &_TrapCheck_Response_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t TrapCheck_Response_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_TrapCheck_Response_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace srv

}  // namespace ltl_automaton_msgs

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<ltl_automaton_msgs::srv::TrapCheck_Response>()
{
  return &::ltl_automaton_msgs::srv::rosidl_typesupport_cpp::TrapCheck_Response_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, ltl_automaton_msgs, srv, TrapCheck_Response)() {
  return get_message_type_support_handle<ltl_automaton_msgs::srv::TrapCheck_Response>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "ltl_automaton_msgs/srv/detail/trap_check__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
#include "rosidl_typesupport_cpp/service_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace ltl_automaton_msgs
{

namespace srv
{

namespace rosidl_typesupport_cpp
{

typedef struct _TrapCheck_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _TrapCheck_type_support_ids_t;

static const _TrapCheck_type_support_ids_t _TrapCheck_service_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _TrapCheck_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _TrapCheck_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _TrapCheck_type_support_symbol_names_t _TrapCheck_service_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, ltl_automaton_msgs, srv, TrapCheck)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, ltl_automaton_msgs, srv, TrapCheck)),
  }
};

typedef struct _TrapCheck_type_support_data_t
{
  void * data[2];
} _TrapCheck_type_support_data_t;

static _TrapCheck_type_support_data_t _TrapCheck_service_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _TrapCheck_service_typesupport_map = {
  2,
  "ltl_automaton_msgs",
  &_TrapCheck_service_typesupport_ids.typesupport_identifier[0],
  &_TrapCheck_service_typesupport_symbol_names.symbol_name[0],
  &_TrapCheck_service_typesupport_data.data[0],
};

static const rosidl_service_type_support_t TrapCheck_service_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_TrapCheck_service_typesupport_map),
  ::rosidl_typesupport_cpp::get_service_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace srv

}  // namespace ltl_automaton_msgs

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_service_type_support_t *
get_service_type_support_handle<ltl_automaton_msgs::srv::TrapCheck>()
{
  return &::ltl_automaton_msgs::srv::rosidl_typesupport_cpp::TrapCheck_service_type_support_handle;
}

}  // namespace rosidl_typesupport_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_cpp, ltl_automaton_msgs, srv, TrapCheck)() {
  return ::rosidl_typesupport_cpp::get_service_type_support_handle<ltl_automaton_msgs::srv::TrapCheck>();
}

#ifdef __cplusplus
}
#endif
