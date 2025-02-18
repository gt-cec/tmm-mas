# generated from rosidl_generator_py/resource/_idl.py.em
# with input from ltl_automaton_msgs:msg/LTLState.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_LTLState(type):
    """Metaclass of message 'LTLState'."""

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
                'ltl_automaton_msgs.msg.LTLState')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__ltl_state
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__ltl_state
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__ltl_state
            cls._TYPE_SUPPORT = module.type_support_msg__msg__ltl_state
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__ltl_state

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


class LTLState(metaclass=Metaclass_LTLState):
    """Message class 'LTLState'."""

    __slots__ = [
        '_ts_state',
        '_buchi_state',
    ]

    _fields_and_field_types = {
        'ts_state': 'ltl_automaton_msgs/TransitionSystemState',
        'buchi_state': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['ltl_automaton_msgs', 'msg'], 'TransitionSystemState'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from ltl_automaton_msgs.msg import TransitionSystemState
        self.ts_state = kwargs.get('ts_state', TransitionSystemState())
        self.buchi_state = kwargs.get('buchi_state', str())

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
        if self.buchi_state != other.buchi_state:
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

    @builtins.property
    def buchi_state(self):
        """Message field 'buchi_state'."""
        return self._buchi_state

    @buchi_state.setter
    def buchi_state(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'buchi_state' field must be of type 'str'"
        self._buchi_state = value
