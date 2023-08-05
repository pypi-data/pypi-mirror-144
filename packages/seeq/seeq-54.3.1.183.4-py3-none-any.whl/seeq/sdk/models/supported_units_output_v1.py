# coding: utf-8

"""
    Seeq REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 54.3.1-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class SupportedUnitsOutputV1(object):
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
        'status_message': 'str',
        'units': 'dict(str, list[str])'
    }

    attribute_map = {
        'status_message': 'statusMessage',
        'units': 'units'
    }

    def __init__(self, status_message=None, units=None):
        """
        SupportedUnitsOutputV1 - a model defined in Swagger
        """

        self._status_message = None
        self._units = None

        if status_message is not None:
          self.status_message = status_message
        if units is not None:
          self.units = units

    @property
    def status_message(self):
        """
        Gets the status_message of this SupportedUnitsOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation. Null if the status message has not been set.

        :return: The status_message of this SupportedUnitsOutputV1.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """
        Sets the status_message of this SupportedUnitsOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation. Null if the status message has not been set.

        :param status_message: The status_message of this SupportedUnitsOutputV1.
        :type: str
        """

        self._status_message = status_message

    @property
    def units(self):
        """
        Gets the units of this SupportedUnitsOutputV1.
        A hashmap of unit categories to units

        :return: The units of this SupportedUnitsOutputV1.
        :rtype: dict(str, list[str])
        """
        return self._units

    @units.setter
    def units(self, units):
        """
        Sets the units of this SupportedUnitsOutputV1.
        A hashmap of unit categories to units

        :param units: The units of this SupportedUnitsOutputV1.
        :type: dict(str, list[str])
        """

        self._units = units

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
        if not isinstance(other, SupportedUnitsOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
