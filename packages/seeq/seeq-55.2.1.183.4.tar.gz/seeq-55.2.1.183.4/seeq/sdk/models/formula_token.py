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


class FormulaToken(object):
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
        'column': 'int',
        'line': 'int',
        'text': 'str'
    }

    attribute_map = {
        'column': 'column',
        'line': 'line',
        'text': 'text'
    }

    def __init__(self, column=None, line=None, text=None):
        """
        FormulaToken - a model defined in Swagger
        """

        self._column = None
        self._line = None
        self._text = None

        if column is not None:
          self.column = column
        if line is not None:
          self.line = line
        if text is not None:
          self.text = text

    @property
    def column(self):
        """
        Gets the column of this FormulaToken.

        :return: The column of this FormulaToken.
        :rtype: int
        """
        return self._column

    @column.setter
    def column(self, column):
        """
        Sets the column of this FormulaToken.

        :param column: The column of this FormulaToken.
        :type: int
        """

        self._column = column

    @property
    def line(self):
        """
        Gets the line of this FormulaToken.

        :return: The line of this FormulaToken.
        :rtype: int
        """
        return self._line

    @line.setter
    def line(self, line):
        """
        Sets the line of this FormulaToken.

        :param line: The line of this FormulaToken.
        :type: int
        """

        self._line = line

    @property
    def text(self):
        """
        Gets the text of this FormulaToken.

        :return: The text of this FormulaToken.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this FormulaToken.

        :param text: The text of this FormulaToken.
        :type: str
        """

        self._text = text

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
        if not isinstance(other, FormulaToken):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
