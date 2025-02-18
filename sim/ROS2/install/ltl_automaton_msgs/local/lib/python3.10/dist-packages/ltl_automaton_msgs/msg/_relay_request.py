# generated from rosidl_generator_py/resource/_idl.py.em
# with input from ltl_automaton_msgs:msg/RelayRequest.idl
# generated code does not contain a copyright notice


# Import statements for member types

# Member 'from_pose'
# Member 'to_pose'
import array  # noqa: E402, I100

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_RelayRequest(type):
    """Metaclass of message 'RelayRequest'."""

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
                'ltl_automaton_msgs.msg.RelayRequest')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__relay_request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__relay_request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__relay_request
            cls._TYPE_SUPPORT = module.type_support_msg__msg__relay_request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__relay_request

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


class RelayRequest(metaclass=Metaclass_RelayRequest):
    """Message class 'RelayRequest'."""

    __slots__ = [
        '_from_pose',
        '_to_pose',
        '_cost',
        '_current_state',
        '_exec_index',
        '_type',
    ]

    _fields_and_field_types = {
        'from_pose': 'sequence<int32>',
        'to_pose': 'sequence<int32>',
        'cost': 'double',
        'current_state': 'ltl_automaton_msgs/TransitionSystemState',
        'exec_index': 'int32',
        'type': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('int32')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('int32')),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['ltl_automaton_msgs', 'msg'], 'TransitionSystemState'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.from_pose = array.array('i', kwargs.get('from_pose', []))
        self.to_pose = array.array('i', kwargs.get('to_pose', []))
        self.cost = kwargs.get('cost', float())
        from ltl_automaton_msgs.msg import TransitionSystemState
        self.current_state = kwargs.get('current_state', TransitionSystemState())
        self.exec_index = kwargs.get('exec_index', int())
        self.type = kwargs.get('type', str())

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
        if self.from_pose != other.from_pose:
            return False
        if self.to_pose != other.to_pose:
            return False
        if self.cost != other.cost:
            return False
        if self.current_state != other.current_state:
            return False
        if self.exec_index != other.exec_index:
            return False
        if self.type != other.type:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def from_pose(self):
        """Message field 'from_pose'."""
        return self._from_pose

    @from_pose.setter
    def from_pose(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'i', \
                "The 'from_pose' array.array() must have the type code of 'i'"
            self._from_pose = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, int) for v in value) and
                 all(val >= -2147483648 and val < 2147483648 for val in value)), \
                "The 'from_pose' field must be a set or sequence and each value of type 'int' and each integer in [-2147483648, 2147483647]"
        self._from_pose = array.array('i', value)

    @builtins.property
    def to_pose(self):
        """Message field 'to_pose'."""
        return self._to_pose

    @to_pose.setter
    def to_pose(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'i', \
                "The 'to_pose' array.array() must have the type code of 'i'"
            self._to_pose = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, int) for v in value) and
                 all(val >= -2147483648 and val < 2147483648 for val in value)), \
                "The 'to_pose' field must be a set or sequence and each value of type 'int' and each integer in [-2147483648, 2147483647]"
        self._to_pose = array.array('i', value)

    @builtins.property
    def cost(self):
        """Message field 'cost'."""
        return self._cost

    @cost.setter
    def cost(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'cost' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'cost' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._cost = value

    @builtins.property
    def current_state(self):
        """Message field 'current_state'."""
        return self._current_state

    @current_state.setter
    def current_state(self, value):
        if __debug__:
            from ltl_automaton_msgs.msg import TransitionSystemState
            assert \
                isinstance(value, TransitionSystemState), \
                "The 'current_state' field must be a sub message of type 'TransitionSystemState'"
        self._current_state = value

    @builtins.property
    def exec_index(self):
        """Message field 'exec_index'."""
        return self._exec_index

    @exec_index.setter
    def exec_index(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'exec_index' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'exec_index' field must be an integer in [-2147483648, 2147483647]"
        self._exec_index = value

    @builtins.property  # noqa: A003
    def type(self):  # noqa: A003
        """Message field 'type'."""
        return self._type

    @type.setter  # noqa: A003
    def type(self, value):  # noqa: A003
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'type' field must be of type 'str'"
        self._type = value
