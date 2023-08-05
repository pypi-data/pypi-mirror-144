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


class AssetTreeSingleInputV1(object):
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
        'child_data_id': 'str',
        'parent_data_id': 'str'
    }

    attribute_map = {
        'child_data_id': 'childDataId',
        'parent_data_id': 'parentDataId'
    }

    def __init__(self, child_data_id=None, parent_data_id=None):
        """
        AssetTreeSingleInputV1 - a model defined in Swagger
        """

        self._child_data_id = None
        self._parent_data_id = None

        if child_data_id is not None:
          self.child_data_id = child_data_id
        if parent_data_id is not None:
          self.parent_data_id = parent_data_id

    @property
    def child_data_id(self):
        """
        Gets the child_data_id of this AssetTreeSingleInputV1.
        The unique data ID (non-Seeq) to create/update parent-child relationships with. In the form of Pair<parentDataId, childDataId>.

        :return: The child_data_id of this AssetTreeSingleInputV1.
        :rtype: str
        """
        return self._child_data_id

    @child_data_id.setter
    def child_data_id(self, child_data_id):
        """
        Sets the child_data_id of this AssetTreeSingleInputV1.
        The unique data ID (non-Seeq) to create/update parent-child relationships with. In the form of Pair<parentDataId, childDataId>.

        :param child_data_id: The child_data_id of this AssetTreeSingleInputV1.
        :type: str
        """

        self._child_data_id = child_data_id

    @property
    def parent_data_id(self):
        """
        Gets the parent_data_id of this AssetTreeSingleInputV1.
        The unique data ID (non-Seeq) of the parent to create a relationship with the child.

        :return: The parent_data_id of this AssetTreeSingleInputV1.
        :rtype: str
        """
        return self._parent_data_id

    @parent_data_id.setter
    def parent_data_id(self, parent_data_id):
        """
        Sets the parent_data_id of this AssetTreeSingleInputV1.
        The unique data ID (non-Seeq) of the parent to create a relationship with the child.

        :param parent_data_id: The parent_data_id of this AssetTreeSingleInputV1.
        :type: str
        """

        self._parent_data_id = parent_data_id

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
        if not isinstance(other, AssetTreeSingleInputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
