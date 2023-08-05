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


class ThresholdOutputV1(object):
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
        'is_generated': 'bool',
        'item': 'ItemPreviewV1',
        'priority': 'PriorityV1',
        'value': 'ScalarValueOutputV1'
    }

    attribute_map = {
        'is_generated': 'isGenerated',
        'item': 'item',
        'priority': 'priority',
        'value': 'value'
    }

    def __init__(self, is_generated=False, item=None, priority=None, value=None):
        """
        ThresholdOutputV1 - a model defined in Swagger
        """

        self._is_generated = None
        self._item = None
        self._priority = None
        self._value = None

        if is_generated is not None:
          self.is_generated = is_generated
        if item is not None:
          self.item = item
        if priority is not None:
          self.priority = priority
        if value is not None:
          self.value = value

    @property
    def is_generated(self):
        """
        Gets the is_generated of this ThresholdOutputV1.

        :return: The is_generated of this ThresholdOutputV1.
        :rtype: bool
        """
        return self._is_generated

    @is_generated.setter
    def is_generated(self, is_generated):
        """
        Sets the is_generated of this ThresholdOutputV1.

        :param is_generated: The is_generated of this ThresholdOutputV1.
        :type: bool
        """

        self._is_generated = is_generated

    @property
    def item(self):
        """
        Gets the item of this ThresholdOutputV1.
        The threshold item

        :return: The item of this ThresholdOutputV1.
        :rtype: ItemPreviewV1
        """
        return self._item

    @item.setter
    def item(self, item):
        """
        Sets the item of this ThresholdOutputV1.
        The threshold item

        :param item: The item of this ThresholdOutputV1.
        :type: ItemPreviewV1
        """

        self._item = item

    @property
    def priority(self):
        """
        Gets the priority of this ThresholdOutputV1.
        The priority associated with the threshold. If a custom color has been specified for this threshold it will be set as the color

        :return: The priority of this ThresholdOutputV1.
        :rtype: PriorityV1
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this ThresholdOutputV1.
        The priority associated with the threshold. If a custom color has been specified for this threshold it will be set as the color

        :param priority: The priority of this ThresholdOutputV1.
        :type: PriorityV1
        """

        self._priority = priority

    @property
    def value(self):
        """
        Gets the value of this ThresholdOutputV1.
        The scalar value, only if the item is a scalar

        :return: The value of this ThresholdOutputV1.
        :rtype: ScalarValueOutputV1
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this ThresholdOutputV1.
        The scalar value, only if the item is a scalar

        :param value: The value of this ThresholdOutputV1.
        :type: ScalarValueOutputV1
        """

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
        if not isinstance(other, ThresholdOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
