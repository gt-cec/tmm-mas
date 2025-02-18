# generated from rosidl_generator_py/resource/_idl.py.em
# with input from ltl_automaton_msgs:srv/TaskReplanningDelete.idl
# generated code does not contain a copyright notice


# Import statements for member types

# Member 'delete_from'
# Member 'delete_to'
import array  # noqa: E402, I100

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_TaskReplanningDelete_Request(type):
    """Metaclass of message 'TaskReplanningDelete_Request'."""

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
                'ltl_automaton_msgs.srv.TaskReplanningDelete_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__task_replanning_delete__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__task_replanning_delete__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__task_replanning_delete__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__task_replanning_delete__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__task_replanning_delete__request

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


class TaskReplanningDelete_Request(metaclass=Metaclass_TaskReplanningDelete_Request):
    """Message class 'TaskReplanningDelete_Request'."""

    __slots__ = [
        '_delete_from',
        '_delete_to',
        '_current_state',
        '_exec_index',
    ]

    _fields_and_field_types = {
        'delete_from': 'sequence<int32>',
        'delete_to': 'sequence<int32>',
        'current_state': 'ltl_automaton_msgs/TransitionSystemState',
        'exec_index': 'int32',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('int32')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('int32')),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['ltl_automaton_msgs', 'msg'], 'TransitionSystemState'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.delete_from = array.array('i', kwargs.get('delete_from', []))
        self.delete_to = array.array('i', kwargs.get('delete_to', []))
        from ltl_automaton_msgs.msg import TransitionSystemState
        self.current_state = kwargs.get('current_state', TransitionSystemState())
        self.exec_index = kwargs.get('exec_index', int())

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
        if self.delete_from != other.delete_from:
            return False
        if self.delete_to != other.delete_to:
            return False
        if self.current_state != other.current_state:
            return False
        if self.exec_index != other.exec_index:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def delete_from(self):
        """Message field 'delete_from'."""
        return self._delete_from

    @delete_from.setter
    def delete_from(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'i', \
                "The 'delete_from' array.array() must have the type code of 'i'"
            self._delete_from = value
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
                "The 'delete_from' field must be a set or sequence and each value of type 'int' and each integer in [-2147483648, 2147483647]"
        self._delete_from = array.array('i', value)

    @builtins.property
    def delete_to(self):
        """Message field 'delete_to'."""
        return self._delete_to

    @delete_to.setter
    def delete_to(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'i', \
                "The 'delete_to' array.array() must have the type code of 'i'"
            self._delete_to = value
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
                "The 'delete_to' field must be a set or sequence and each value of type 'int' and each integer in [-2147483648, 2147483647]"
        self._delete_to = array.array('i', value)

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


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_TaskReplanningDelete_Response(type):
    """Metaclass of message 'TaskReplanningDelete_Response'."""

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
                'ltl_automaton_msgs.srv.TaskReplanningDelete_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__task_replanning_delete__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__task_replanning_delete__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__task_replanning_delete__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__task_replanning_delete__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__task_replanning_delete__response

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


class TaskReplanningDelete_Response(metaclass=Metaclass_TaskReplanningDelete_Response):
    """Message class 'TaskReplanningDelete_Response'."""

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


class Metaclass_TaskReplanningDelete(type):
    """Metaclass of service 'TaskReplanningDelete'."""

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
                'ltl_automaton_msgs.srv.TaskReplanningDelete')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__task_replanning_delete

            from ltl_automaton_msgs.srv import _task_replanning_delete
            if _task_replanning_delete.Metaclass_TaskReplanningDelete_Request._TYPE_SUPPORT is None:
                _task_replanning_delete.Metaclass_TaskReplanningDelete_Request.__import_type_support__()
            if _task_replanning_delete.Metaclass_TaskReplanningDelete_Response._TYPE_SUPPORT is None:
                _task_replanning_delete.Metaclass_TaskReplanningDelete_Response.__import_type_support__()


class TaskReplanningDelete(metaclass=Metaclass_TaskReplanningDelete):
    from ltl_automaton_msgs.srv._task_replanning_delete import TaskReplanningDelete_Request as Request
    from ltl_automaton_msgs.srv._task_replanning_delete import TaskReplanningDelete_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
