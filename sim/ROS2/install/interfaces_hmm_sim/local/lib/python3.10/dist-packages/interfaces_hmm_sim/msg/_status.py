# generated from rosidl_generator_py/resource/_idl.py.em
# with input from interfaces_hmm_sim:msg/Status.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Status(type):
    """Metaclass of message 'Status'."""

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
            module = import_type_support('interfaces_hmm_sim')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'interfaces_hmm_sim.msg.Status')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__status
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__status
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__status
            cls._TYPE_SUPPORT = module.type_support_msg__msg__status
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__status

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Status(metaclass=Metaclass_Status):
    """Message class 'Status'."""

    __slots__ = [
        '_agent',
        '_start',
        '_arrived',
        '_replan_received',
    ]

    _fields_and_field_types = {
        'agent': 'string',
        'start': 'boolean',
        'arrived': 'boolean',
        'replan_received': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.agent = kwargs.get('agent', str())
        self.start = kwargs.get('start', bool())
        self.arrived = kwargs.get('arrived', bool())
        self.replan_received = kwargs.get('replan_received', bool())

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
        if self.agent != other.agent:
            return False
        if self.start != other.start:
            return False
        if self.arrived != other.arrived:
            return False
        if self.replan_received != other.replan_received:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def agent(self):
        """Message field 'agent'."""
        return self._agent

    @agent.setter
    def agent(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'agent' field must be of type 'str'"
        self._agent = value

    @builtins.property
    def start(self):
        """Message field 'start'."""
        return self._start

    @start.setter
    def start(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'start' field must be of type 'bool'"
        self._start = value

    @builtins.property
    def arrived(self):
        """Message field 'arrived'."""
        return self._arrived

    @arrived.setter
    def arrived(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'arrived' field must be of type 'bool'"
        self._arrived = value

    @builtins.property
    def replan_received(self):
        """Message field 'replan_received'."""
        return self._replan_received

    @replan_received.setter
    def replan_received(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'replan_received' field must be of type 'bool'"
        self._replan_received = value
