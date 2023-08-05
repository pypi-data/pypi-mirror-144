# coding: utf-8

"""
    Seeq REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 55.2.1-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ServerSpecOutputV1(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'component_name': 'str',
        'error': 'bool',
        'message': 'str',
        'system_spec_value': 'str',
        'warning': 'bool'
    }

    attribute_map = {
        'component_name': 'componentName',
        'error': 'error',
        'message': 'message',
        'system_spec_value': 'systemSpecValue',
        'warning': 'warning'
    }

    def __init__(self, component_name=None, error=False, message=None, system_spec_value=None, warning=False):
        """
        ServerSpecOutputV1 - a model defined in Swagger
        """

        self._component_name = None
        self._error = None
        self._message = None
        self._system_spec_value = None
        self._warning = None

        if component_name is not None:
          self.component_name = component_name
        if error is not None:
          self.error = error
        if message is not None:
          self.message = message
        if system_spec_value is not None:
          self.system_spec_value = system_spec_value
        if warning is not None:
          self.warning = warning

    @property
    def component_name(self):
        """
        Gets the component_name of this ServerSpecOutputV1.
        The name of the component. E.G. CPU, Memory...

        :return: The component_name of this ServerSpecOutputV1.
        :rtype: str
        """
        return self._component_name

    @component_name.setter
    def component_name(self, component_name):
        """
        Sets the component_name of this ServerSpecOutputV1.
        The name of the component. E.G. CPU, Memory...

        :param component_name: The component_name of this ServerSpecOutputV1.
        :type: str
        """

        self._component_name = component_name

    @property
    def error(self):
        """
        Gets the error of this ServerSpecOutputV1.
        True if this value is far lower than recommended

        :return: The error of this ServerSpecOutputV1.
        :rtype: bool
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this ServerSpecOutputV1.
        True if this value is far lower than recommended

        :param error: The error of this ServerSpecOutputV1.
        :type: bool
        """

        self._error = error

    @property
    def message(self):
        """
        Gets the message of this ServerSpecOutputV1.
        An optional message about the spec

        :return: The message of this ServerSpecOutputV1.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this ServerSpecOutputV1.
        An optional message about the spec

        :param message: The message of this ServerSpecOutputV1.
        :type: str
        """

        self._message = message

    @property
    def system_spec_value(self):
        """
        Gets the system_spec_value of this ServerSpecOutputV1.
        The value of the component

        :return: The system_spec_value of this ServerSpecOutputV1.
        :rtype: str
        """
        return self._system_spec_value

    @system_spec_value.setter
    def system_spec_value(self, system_spec_value):
        """
        Sets the system_spec_value of this ServerSpecOutputV1.
        The value of the component

        :param system_spec_value: The system_spec_value of this ServerSpecOutputV1.
        :type: str
        """

        self._system_spec_value = system_spec_value

    @property
    def warning(self):
        """
        Gets the warning of this ServerSpecOutputV1.
        True if this value is lower than recommended, but not a critical failure

        :return: The warning of this ServerSpecOutputV1.
        :rtype: bool
        """
        return self._warning

    @warning.setter
    def warning(self, warning):
        """
        Sets the warning of this ServerSpecOutputV1.
        True if this value is lower than recommended, but not a critical failure

        :param warning: The warning of this ServerSpecOutputV1.
        :type: bool
        """

        self._warning = warning

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ServerSpecOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
