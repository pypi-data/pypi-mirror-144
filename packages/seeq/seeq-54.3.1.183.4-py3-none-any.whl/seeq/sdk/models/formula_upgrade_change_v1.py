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


class FormulaUpgradeChangeV1(object):
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
        'change': 'str',
        'more_details_url': 'str'
    }

    attribute_map = {
        'change': 'change',
        'more_details_url': 'moreDetailsUrl'
    }

    def __init__(self, change=None, more_details_url=None):
        """
        FormulaUpgradeChangeV1 - a model defined in Swagger
        """

        self._change = None
        self._more_details_url = None

        if change is not None:
          self.change = change
        if more_details_url is not None:
          self.more_details_url = more_details_url

    @property
    def change(self):
        """
        Gets the change of this FormulaUpgradeChangeV1.
        Description of the change

        :return: The change of this FormulaUpgradeChangeV1.
        :rtype: str
        """
        return self._change

    @change.setter
    def change(self, change):
        """
        Sets the change of this FormulaUpgradeChangeV1.
        Description of the change

        :param change: The change of this FormulaUpgradeChangeV1.
        :type: str
        """

        self._change = change

    @property
    def more_details_url(self):
        """
        Gets the more_details_url of this FormulaUpgradeChangeV1.
        A link to the Knowledge Base for more explanation of why this was applied

        :return: The more_details_url of this FormulaUpgradeChangeV1.
        :rtype: str
        """
        return self._more_details_url

    @more_details_url.setter
    def more_details_url(self, more_details_url):
        """
        Sets the more_details_url of this FormulaUpgradeChangeV1.
        A link to the Knowledge Base for more explanation of why this was applied

        :param more_details_url: The more_details_url of this FormulaUpgradeChangeV1.
        :type: str
        """

        self._more_details_url = more_details_url

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
        if not isinstance(other, FormulaUpgradeChangeV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
