# generated from rosidl_generator_py/resource/_idl.py.em
# with input from ltl_automaton_msgs:srv/TrapCheck.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_TrapCheck_Request(type):
    """Metaclass of message 'TrapCheck_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('ltl_automaton_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'ltl_automaton_msgs.srv.TrapCheck_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__trap_check__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__trap_check__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__trap_check__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__trap_check__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__trap_check__request

            from ltl_automaton_msgs.msg import TransitionSystemState
            if TransitionSystemState.__class__._TYPE_SUPPORT is None:
                TransitionSystemState.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class TrapCheck_Request(metaclass=Metaclass_TrapCheck_Request):
    """Message class 'TrapCheck_Request'."""

    __slots__ = [
        '_ts_state',
    ]

    _fields_and_field_types = {
        'ts_state': 'ltl_automaton_msgs/TransitionSystemState',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['ltl_automaton_msgs', 'msg'], 'TransitionSystemState'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from ltl_automaton_msgs.msg import TransitionSystemState
        self.ts_state = kwargs.get('ts_state', TransitionSystemState())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.ts_state != other.ts_state:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def ts_state(self):
        """Message field 'ts_state'."""
        return self._ts_state

    @ts_state.setter
    def ts_state(self, value):
        if __debug__:
            from ltl_automaton_msgs.msg import TransitionSystemState
            assert \
                isinstance(value, TransitionSystemState), \
                "The 'ts_state' field must be a sub message of type 'TransitionSystemState'"
        self._ts_state = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_TrapCheck_Response(type):
    """Metaclass of message 'TrapCheck_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('ltl_automaton_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'ltl_automaton_msgs.srv.TrapCheck_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__trap_check__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__trap_check__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__trap_check__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__trap_check__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__trap_check__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class TrapCheck_Response(metaclass=Metaclass_TrapCheck_Response):
    """Message class 'TrapCheck_Response'."""

    __slots__ = [
        '_is_connected',
        '_is_trap',
    ]

    _fields_and_field_types = {
        'is_connected': 'boolean',
        'is_trap': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.is_connected = kwargs.get('is_connected', bool())
        self.is_trap = kwargs.get('is_trap', bool())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.is_connected != other.is_connected:
            return False
        if self.is_trap != other.is_trap:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def is_connected(self):
        """Message field 'is_connected'."""
        return self._is_connected

    @is_connected.setter
    def is_connected(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'is_connected' field must be of type 'bool'"
        self._is_connected = value

    @builtins.property
    def is_trap(self):
        """Message field 'is_trap'."""
        return self._is_trap

    @is_trap.setter
    def is_trap(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'is_trap' field must be of type 'bool'"
        self._is_trap = value


class Metaclass_TrapCheck(type):
    """Metaclass of service 'TrapCheck'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('ltl_automaton_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'ltl_automaton_msgs.srv.TrapCheck')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__trap_check

            from ltl_automaton_msgs.srv import _trap_check
            if _trap_check.Metaclass_TrapCheck_Request._TYPE_SUPPORT is None:
                _trap_check.Metaclass_TrapCheck_Request.__import_type_support__()
            if _trap_check.Metaclass_TrapCheck_Response._TYPE_SUPPORT is None:
                _trap_check.Metaclass_TrapCheck_Response.__import_type_support__()


class TrapCheck(metaclass=Metaclass_TrapCheck):
    from ltl_automaton_msgs.srv._trap_check import TrapCheck_Request as Request
    from ltl_automaton_msgs.srv._trap_check import TrapCheck_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
