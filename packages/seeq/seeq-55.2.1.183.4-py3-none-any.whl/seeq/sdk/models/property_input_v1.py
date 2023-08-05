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


class PropertyInputV1(object):
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
        'unit_of_measure': 'str',
        'value': 'object'
    }

    attribute_map = {
        'unit_of_measure': 'unitOfMeasure',
        'value': 'value'
    }

    def __init__(self, unit_of_measure=None, value=None):
        """
        PropertyInputV1 - a model defined in Swagger
        """

        self._unit_of_measure = None
        self._value = None

        if unit_of_measure is not None:
          self.unit_of_measure = unit_of_measure
        if value is not None:
          self.value = value

    @property
    def unit_of_measure(self):
        """
        Gets the unit_of_measure of this PropertyInputV1.
        The unit of measure to apply to this property's value. If no unit of measure is set, the value is assumed to be unitless. If specified, a value must also be supplied. (If specifying a calculation rather than a value, do not specify the unit of measure as it will be determined from the calculation.)

        :return: The unit_of_measure of this PropertyInputV1.
        :rtype: str
        """
        return self._unit_of_measure

    @unit_of_measure.setter
    def unit_of_measure(self, unit_of_measure):
        """
        Sets the unit_of_measure of this PropertyInputV1.
        The unit of measure to apply to this property's value. If no unit of measure is set, the value is assumed to be unitless. If specified, a value must also be supplied. (If specifying a calculation rather than a value, do not specify the unit of measure as it will be determined from the calculation.)

        :param unit_of_measure: The unit_of_measure of this PropertyInputV1.
        :type: str
        """

        self._unit_of_measure = unit_of_measure

    @property
    def value(self):
        """
        Gets the value of this PropertyInputV1.
        The value to assign to this property. 

        :return: The value of this PropertyInputV1.
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this PropertyInputV1.
        The value to assign to this property. 

        :param value: The value of this PropertyInputV1.
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
        if not isinstance(other, PropertyInputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
