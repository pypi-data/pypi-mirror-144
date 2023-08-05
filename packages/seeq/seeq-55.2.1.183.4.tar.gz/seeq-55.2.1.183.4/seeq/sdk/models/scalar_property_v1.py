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


class ScalarPropertyV1(object):
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
        'name': 'str',
        'unit_of_measure': 'str',
        'value': 'object'
    }

    attribute_map = {
        'name': 'name',
        'unit_of_measure': 'unitOfMeasure',
        'value': 'value'
    }

    def __init__(self, name=None, unit_of_measure=None, value=None):
        """
        ScalarPropertyV1 - a model defined in Swagger
        """

        self._name = None
        self._unit_of_measure = None
        self._value = None

        if name is not None:
          self.name = name
        if unit_of_measure is not None:
          self.unit_of_measure = unit_of_measure
        if value is not None:
          self.value = value

    @property
    def name(self):
        """
        Gets the name of this ScalarPropertyV1.
        Human readable name.  Null or whitespace names are not permitted

        :return: The name of this ScalarPropertyV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ScalarPropertyV1.
        Human readable name.  Null or whitespace names are not permitted

        :param name: The name of this ScalarPropertyV1.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def unit_of_measure(self):
        """
        Gets the unit_of_measure of this ScalarPropertyV1.
        The unit of measure to apply to this property's value. If no unit of measure is set and the value is numeric, it is assumed to be unitless

        :return: The unit_of_measure of this ScalarPropertyV1.
        :rtype: str
        """
        return self._unit_of_measure

    @unit_of_measure.setter
    def unit_of_measure(self, unit_of_measure):
        """
        Sets the unit_of_measure of this ScalarPropertyV1.
        The unit of measure to apply to this property's value. If no unit of measure is set and the value is numeric, it is assumed to be unitless

        :param unit_of_measure: The unit_of_measure of this ScalarPropertyV1.
        :type: str
        """

        self._unit_of_measure = unit_of_measure

    @property
    def value(self):
        """
        Gets the value of this ScalarPropertyV1.
        The value to assign to this property. If the value is surrounded by quotes, it is interpreted as a string and no units are set

        :return: The value of this ScalarPropertyV1.
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this ScalarPropertyV1.
        The value to assign to this property. If the value is surrounded by quotes, it is interpreted as a string and no units are set

        :param value: The value of this ScalarPropertyV1.
        :type: object
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")

        self._value = value

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
        if not isinstance(other, ScalarPropertyV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
