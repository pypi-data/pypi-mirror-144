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


class FormulaDocSummariesOutputV1(object):
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
        'functions': 'list[FormulaDocSummaryOutputV1]'
    }

    attribute_map = {
        'functions': 'functions'
    }

    def __init__(self, functions=None):
        """
        FormulaDocSummariesOutputV1 - a model defined in Swagger
        """

        self._functions = None

        if functions is not None:
          self.functions = functions

    @property
    def functions(self):
        """
        Gets the functions of this FormulaDocSummariesOutputV1.

        :return: The functions of this FormulaDocSummariesOutputV1.
        :rtype: list[FormulaDocSummaryOutputV1]
        """
        return self._functions

    @functions.setter
    def functions(self, functions):
        """
        Sets the functions of this FormulaDocSummariesOutputV1.

        :param functions: The functions of this FormulaDocSummariesOutputV1.
        :type: list[FormulaDocSummaryOutputV1]
        """

        self._functions = functions

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
        if not isinstance(other, FormulaDocSummariesOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
