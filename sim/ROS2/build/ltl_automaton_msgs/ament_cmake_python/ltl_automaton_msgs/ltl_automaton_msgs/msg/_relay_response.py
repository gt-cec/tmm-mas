# generated from rosidl_generator_py/resource/_idl.py.em
# with input from ltl_automaton_msgs:msg/RelayResponse.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_RelayResponse(type):
    """Metaclass of message 'RelayResponse'."""

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
                'ltl_automaton_msgs.msg.RelayResponse')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__relay_response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__relay_response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__relay_response
            cls._TYPE_SUPPORT = module.type_support_msg__msg__relay_response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__relay_response

            from ltl_automaton_msgs.msg import LTLPlan
            if LTLPlan.__class__._TYPE_SUPPORT is None:
                LTLPlan.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class RelayResponse(metaclass=Metaclass_RelayResponse):
    """Message class 'RelayResponse'."""

    __slots__ = [
        '_success',
        '_new_plan_prefix',
        '_new_plan_suffix',
    ]

    _fields_and_field_types = {
        'success': 'boolean',
        'new_plan_prefix': 'ltl_automaton_msgs/LTLPlan',
        'new_plan_suffix': 'ltl_automaton_msgs/LTLPlan',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['ltl_automaton_msgs', 'msg'], 'LTLPlan'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['ltl_automaton_msgs', 'msg'], 'LTLPlan'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.success = kwargs.get('success', bool())
        from ltl_automaton_msgs.msg import LTLPlan
        self.new_plan_prefix = kwargs.get('new_plan_prefix', LTLPlan())
        from ltl_automaton_msgs.msg import LTLPlan
        self.new_plan_suffix = kwargs.get('new_plan_suffix', LTLPlan())

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
        if self.success != other.success:
            return False
        if self.new_plan_prefix != other.new_plan_prefix:
            return False
        if self.new_plan_suffix != other.new_plan_suffix:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def success(self):
        """Message field 'success'."""
        return self._success

    @success.setter
    def success(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'success' field must be of type 'bool'"
        self._success = value

    @builtins.property
    def new_plan_prefix(self):
        """Message field 'new_plan_prefix'."""
        return self._new_plan_prefix

    @new_plan_prefix.setter
    def new_plan_prefix(self, value):
        if __debug__:
            from ltl_automaton_msgs.msg import LTLPlan
            assert \
                isinstance(value, LTLPlan), \
                "The 'new_plan_prefix' field must be a sub message of type 'LTLPlan'"
        self._new_plan_prefix = value

    @builtins.property
    def new_plan_suffix(self):
        """Message field 'new_plan_suffix'."""
        return self._new_plan_suffix

    @new_plan_suffix.setter
    def new_plan_suffix(self, value):
        if __debug__:
            from ltl_automaton_msgs.msg import LTLPlan
            assert \
                isinstance(value, LTLPlan), \
                "The 'new_plan_suffix' field must be a sub message of type 'LTLPlan'"
        self._new_plan_suffix = value
