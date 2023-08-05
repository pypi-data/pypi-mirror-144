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


class ReportAdminListOutputV1(object):
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
        'graph_limit': 'int',
        'limit': 'int',
        'next': 'str',
        'offset': 'int',
        'prev': 'str',
        'reports': 'list[ReportAdminOutputV1]',
        'status_message': 'str',
        'total_count': 'int'
    }

    attribute_map = {
        'graph_limit': 'graphLimit',
        'limit': 'limit',
        'next': 'next',
        'offset': 'offset',
        'prev': 'prev',
        'reports': 'reports',
        'status_message': 'statusMessage',
        'total_count': 'totalCount'
    }

    def __init__(self, graph_limit=None, limit=None, next=None, offset=None, prev=None, reports=None, status_message=None, total_count=None):
        """
        ReportAdminListOutputV1 - a model defined in Swagger
        """

        self._graph_limit = None
        self._limit = None
        self._next = None
        self._offset = None
        self._prev = None
        self._reports = None
        self._status_message = None
        self._total_count = None

        if graph_limit is not None:
          self.graph_limit = graph_limit
        if limit is not None:
          self.limit = limit
        if next is not None:
          self.next = next
        if offset is not None:
          self.offset = offset
        if prev is not None:
          self.prev = prev
        if reports is not None:
          self.reports = reports
        if status_message is not None:
          self.status_message = status_message
        if total_count is not None:
          self.total_count = total_count

    @property
    def graph_limit(self):
        """
        Gets the graph_limit of this ReportAdminListOutputV1.

        :return: The graph_limit of this ReportAdminListOutputV1.
        :rtype: int
        """
        return self._graph_limit

    @graph_limit.setter
    def graph_limit(self, graph_limit):
        """
        Sets the graph_limit of this ReportAdminListOutputV1.

        :param graph_limit: The graph_limit of this ReportAdminListOutputV1.
        :type: int
        """

        self._graph_limit = graph_limit

    @property
    def limit(self):
        """
        Gets the limit of this ReportAdminListOutputV1.
        The pagination limit, the total number of collection items that will be returned in this page of results

        :return: The limit of this ReportAdminListOutputV1.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this ReportAdminListOutputV1.
        The pagination limit, the total number of collection items that will be returned in this page of results

        :param limit: The limit of this ReportAdminListOutputV1.
        :type: int
        """

        self._limit = limit

    @property
    def next(self):
        """
        Gets the next of this ReportAdminListOutputV1.
        The href of the next set of paginated results

        :return: The next of this ReportAdminListOutputV1.
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """
        Sets the next of this ReportAdminListOutputV1.
        The href of the next set of paginated results

        :param next: The next of this ReportAdminListOutputV1.
        :type: str
        """

        self._next = next

    @property
    def offset(self):
        """
        Gets the offset of this ReportAdminListOutputV1.
        The pagination offset, the index of the first collection item that will be returned in this page of results

        :return: The offset of this ReportAdminListOutputV1.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """
        Sets the offset of this ReportAdminListOutputV1.
        The pagination offset, the index of the first collection item that will be returned in this page of results

        :param offset: The offset of this ReportAdminListOutputV1.
        :type: int
        """

        self._offset = offset

    @property
    def prev(self):
        """
        Gets the prev of this ReportAdminListOutputV1.
        The href of the previous set of paginated results

        :return: The prev of this ReportAdminListOutputV1.
        :rtype: str
        """
        return self._prev

    @prev.setter
    def prev(self, prev):
        """
        Sets the prev of this ReportAdminListOutputV1.
        The href of the previous set of paginated results

        :param prev: The prev of this ReportAdminListOutputV1.
        :type: str
        """

        self._prev = prev

    @property
    def reports(self):
        """
        Gets the reports of this ReportAdminListOutputV1.
        A list of reports with statistical information added

        :return: The reports of this ReportAdminListOutputV1.
        :rtype: list[ReportAdminOutputV1]
        """
        return self._reports

    @reports.setter
    def reports(self, reports):
        """
        Sets the reports of this ReportAdminListOutputV1.
        A list of reports with statistical information added

        :param reports: The reports of this ReportAdminListOutputV1.
        :type: list[ReportAdminOutputV1]
        """

        self._reports = reports

    @property
    def status_message(self):
        """
        Gets the status_message of this ReportAdminListOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation. Null if the status message has not been set.

        :return: The status_message of this ReportAdminListOutputV1.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """
        Sets the status_message of this ReportAdminListOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation. Null if the status message has not been set.

        :param status_message: The status_message of this ReportAdminListOutputV1.
        :type: str
        """

        self._status_message = status_message

    @property
    def total_count(self):
        """
        Gets the total_count of this ReportAdminListOutputV1.
        The total count of reports

        :return: The total_count of this ReportAdminListOutputV1.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """
        Sets the total_count of this ReportAdminListOutputV1.
        The total count of reports

        :param total_count: The total_count of this ReportAdminListOutputV1.
        :type: int
        """

        self._total_count = total_count

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
        if not isinstance(other, ReportAdminListOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
