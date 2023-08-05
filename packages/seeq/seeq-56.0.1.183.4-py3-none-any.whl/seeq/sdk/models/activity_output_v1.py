# coding: utf-8

"""
    Seeq REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 56.0.1-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ActivityOutputV1(object):
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
        'category': 'str',
        'description': 'str',
        'id': 'str',
        'properties': 'dict(str, str)'
    }

    attribute_map = {
        'category': 'category',
        'description': 'description',
        'id': 'id',
        'properties': 'properties'
    }

    def __init__(self, category=None, description=None, id=None, properties=None):
        """
        ActivityOutputV1 - a model defined in Swagger
        """

        self._category = None
        self._description = None
        self._id = None
        self._properties = None

        if category is not None:
          self.category = category
        if description is not None:
          self.description = description
        if id is not None:
          self.id = id
        if properties is not None:
          self.properties = properties

    @property
    def category(self):
        """
        Gets the category of this ActivityOutputV1.
        The kind of activity this represents, irrespective of specific instance parameters. Use this to do things like coloring activities of the same kind.

        :return: The category of this ActivityOutputV1.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this ActivityOutputV1.
        The kind of activity this represents, irrespective of specific instance parameters. Use this to do things like coloring activities of the same kind.

        :param category: The category of this ActivityOutputV1.
        :type: str
        """
        if category is None:
            raise ValueError("Invalid value for `category`, must not be `None`")

        self._category = category

    @property
    def description(self):
        """
        Gets the description of this ActivityOutputV1.
        An admin-readable description of the operation being performed

        :return: The description of this ActivityOutputV1.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ActivityOutputV1.
        An admin-readable description of the operation being performed

        :param description: The description of this ActivityOutputV1.
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")

        self._description = description

    @property
    def id(self):
        """
        Gets the id of this ActivityOutputV1.
        The (ephemeral) ID of the Activity.Only valid within the context of a particular snapshot, for example for correlating activities shared amongst multiple requests.

        :return: The id of this ActivityOutputV1.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ActivityOutputV1.
        The (ephemeral) ID of the Activity.Only valid within the context of a particular snapshot, for example for correlating activities shared amongst multiple requests.

        :param id: The id of this ActivityOutputV1.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def properties(self):
        """
        Gets the properties of this ActivityOutputV1.
        Additional details, such as the time interval, names, or identifiers

        :return: The properties of this ActivityOutputV1.
        :rtype: dict(str, str)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this ActivityOutputV1.
        Additional details, such as the time interval, names, or identifiers

        :param properties: The properties of this ActivityOutputV1.
        :type: dict(str, str)
        """
        if properties is None:
            raise ValueError("Invalid value for `properties`, must not be `None`")

        self._properties = properties

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
        if not isinstance(other, ActivityOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
