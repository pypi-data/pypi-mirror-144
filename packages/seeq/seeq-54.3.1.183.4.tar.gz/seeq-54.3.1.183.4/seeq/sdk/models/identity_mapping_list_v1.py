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


class IdentityMappingListV1(object):
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
        'mapped_identities': 'list[IdentityMappingV1]'
    }

    attribute_map = {
        'mapped_identities': 'mappedIdentities'
    }

    def __init__(self, mapped_identities=None):
        """
        IdentityMappingListV1 - a model defined in Swagger
        """

        self._mapped_identities = None

        if mapped_identities is not None:
          self.mapped_identities = mapped_identities

    @property
    def mapped_identities(self):
        """
        Gets the mapped_identities of this IdentityMappingListV1.
        The list of members that are contained within a synced UserGroup, identified by their Remote Item ID.

        :return: The mapped_identities of this IdentityMappingListV1.
        :rtype: list[IdentityMappingV1]
        """
        return self._mapped_identities

    @mapped_identities.setter
    def mapped_identities(self, mapped_identities):
        """
        Sets the mapped_identities of this IdentityMappingListV1.
        The list of members that are contained within a synced UserGroup, identified by their Remote Item ID.

        :param mapped_identities: The mapped_identities of this IdentityMappingListV1.
        :type: list[IdentityMappingV1]
        """

        self._mapped_identities = mapped_identities

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
        if not isinstance(other, IdentityMappingListV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
