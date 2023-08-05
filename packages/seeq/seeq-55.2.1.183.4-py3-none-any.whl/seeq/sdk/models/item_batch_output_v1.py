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


class ItemBatchOutputV1(object):
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
        'item_updates': 'list[ItemUpdateOutputV1]',
        'status_message': 'str'
    }

    attribute_map = {
        'item_updates': 'itemUpdates',
        'status_message': 'statusMessage'
    }

    def __init__(self, item_updates=None, status_message=None):
        """
        ItemBatchOutputV1 - a model defined in Swagger
        """

        self._item_updates = None
        self._status_message = None

        if item_updates is not None:
          self.item_updates = item_updates
        if status_message is not None:
          self.status_message = status_message

    @property
    def item_updates(self):
        """
        Gets the item_updates of this ItemBatchOutputV1.
        The list of results from item updates. The Nth output corresponds to the Nth input.

        :return: The item_updates of this ItemBatchOutputV1.
        :rtype: list[ItemUpdateOutputV1]
        """
        return self._item_updates

    @item_updates.setter
    def item_updates(self, item_updates):
        """
        Sets the item_updates of this ItemBatchOutputV1.
        The list of results from item updates. The Nth output corresponds to the Nth input.

        :param item_updates: The item_updates of this ItemBatchOutputV1.
        :type: list[ItemUpdateOutputV1]
        """

        self._item_updates = item_updates

    @property
    def status_message(self):
        """
        Gets the status_message of this ItemBatchOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation. Null if the status message has not been set.

        :return: The status_message of this ItemBatchOutputV1.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """
        Sets the status_message of this ItemBatchOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation. Null if the status message has not been set.

        :param status_message: The status_message of this ItemBatchOutputV1.
        :type: str
        """

        self._status_message = status_message

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
        if not isinstance(other, ItemBatchOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
