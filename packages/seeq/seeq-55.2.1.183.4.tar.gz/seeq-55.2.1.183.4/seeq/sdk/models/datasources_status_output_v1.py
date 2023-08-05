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


class DatasourcesStatusOutputV1(object):
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
        'agents': 'list[AgentStatusOutputV1]',
        'connected_connections_count': 'int',
        'connected_datasources_count': 'int',
        'datasources': 'list[DatasourceSummaryStatusOutputV1]',
        'total_connections_count': 'int',
        'total_datasources_count': 'int'
    }

    attribute_map = {
        'agents': 'agents',
        'connected_connections_count': 'connectedConnectionsCount',
        'connected_datasources_count': 'connectedDatasourcesCount',
        'datasources': 'datasources',
        'total_connections_count': 'totalConnectionsCount',
        'total_datasources_count': 'totalDatasourcesCount'
    }

    def __init__(self, agents=None, connected_connections_count=None, connected_datasources_count=None, datasources=None, total_connections_count=None, total_datasources_count=None):
        """
        DatasourcesStatusOutputV1 - a model defined in Swagger
        """

        self._agents = None
        self._connected_connections_count = None
        self._connected_datasources_count = None
        self._datasources = None
        self._total_connections_count = None
        self._total_datasources_count = None

        if agents is not None:
          self.agents = agents
        if connected_connections_count is not None:
          self.connected_connections_count = connected_connections_count
        if connected_datasources_count is not None:
          self.connected_datasources_count = connected_datasources_count
        if datasources is not None:
          self.datasources = datasources
        if total_connections_count is not None:
          self.total_connections_count = total_connections_count
        if total_datasources_count is not None:
          self.total_datasources_count = total_datasources_count

    @property
    def agents(self):
        """
        Gets the agents of this DatasourcesStatusOutputV1.
        The status for all agents accessible by the user. Provided only when the required level of detail is 'Complete'

        :return: The agents of this DatasourcesStatusOutputV1.
        :rtype: list[AgentStatusOutputV1]
        """
        return self._agents

    @agents.setter
    def agents(self, agents):
        """
        Sets the agents of this DatasourcesStatusOutputV1.
        The status for all agents accessible by the user. Provided only when the required level of detail is 'Complete'

        :param agents: The agents of this DatasourcesStatusOutputV1.
        :type: list[AgentStatusOutputV1]
        """

        self._agents = agents

    @property
    def connected_connections_count(self):
        """
        Gets the connected_connections_count of this DatasourcesStatusOutputV1.
        The number of connections in status 'Connected'. Provided regardless of the level of detail requested

        :return: The connected_connections_count of this DatasourcesStatusOutputV1.
        :rtype: int
        """
        return self._connected_connections_count

    @connected_connections_count.setter
    def connected_connections_count(self, connected_connections_count):
        """
        Sets the connected_connections_count of this DatasourcesStatusOutputV1.
        The number of connections in status 'Connected'. Provided regardless of the level of detail requested

        :param connected_connections_count: The connected_connections_count of this DatasourcesStatusOutputV1.
        :type: int
        """
        if connected_connections_count is None:
            raise ValueError("Invalid value for `connected_connections_count`, must not be `None`")

        self._connected_connections_count = connected_connections_count

    @property
    def connected_datasources_count(self):
        """
        Gets the connected_datasources_count of this DatasourcesStatusOutputV1.
        The number of connected datasources. Provided regardless of the level of detail requested

        :return: The connected_datasources_count of this DatasourcesStatusOutputV1.
        :rtype: int
        """
        return self._connected_datasources_count

    @connected_datasources_count.setter
    def connected_datasources_count(self, connected_datasources_count):
        """
        Sets the connected_datasources_count of this DatasourcesStatusOutputV1.
        The number of connected datasources. Provided regardless of the level of detail requested

        :param connected_datasources_count: The connected_datasources_count of this DatasourcesStatusOutputV1.
        :type: int
        """
        if connected_datasources_count is None:
            raise ValueError("Invalid value for `connected_datasources_count`, must not be `None`")

        self._connected_datasources_count = connected_datasources_count

    @property
    def datasources(self):
        """
        Gets the datasources of this DatasourcesStatusOutputV1.
        The status for all datasources accessible by the user. Available only when the required level of detail is 'Complete' or 'Summary'

        :return: The datasources of this DatasourcesStatusOutputV1.
        :rtype: list[DatasourceSummaryStatusOutputV1]
        """
        return self._datasources

    @datasources.setter
    def datasources(self, datasources):
        """
        Sets the datasources of this DatasourcesStatusOutputV1.
        The status for all datasources accessible by the user. Available only when the required level of detail is 'Complete' or 'Summary'

        :param datasources: The datasources of this DatasourcesStatusOutputV1.
        :type: list[DatasourceSummaryStatusOutputV1]
        """

        self._datasources = datasources

    @property
    def total_connections_count(self):
        """
        Gets the total_connections_count of this DatasourcesStatusOutputV1.
        The total number of connections expected to be in  the status 'Connected'. Provided regardless of the level of detail requested

        :return: The total_connections_count of this DatasourcesStatusOutputV1.
        :rtype: int
        """
        return self._total_connections_count

    @total_connections_count.setter
    def total_connections_count(self, total_connections_count):
        """
        Sets the total_connections_count of this DatasourcesStatusOutputV1.
        The total number of connections expected to be in  the status 'Connected'. Provided regardless of the level of detail requested

        :param total_connections_count: The total_connections_count of this DatasourcesStatusOutputV1.
        :type: int
        """
        if total_connections_count is None:
            raise ValueError("Invalid value for `total_connections_count`, must not be `None`")

        self._total_connections_count = total_connections_count

    @property
    def total_datasources_count(self):
        """
        Gets the total_datasources_count of this DatasourcesStatusOutputV1.
        The total number of datasources expected to be connected. Provided regardless of the level of detail requested

        :return: The total_datasources_count of this DatasourcesStatusOutputV1.
        :rtype: int
        """
        return self._total_datasources_count

    @total_datasources_count.setter
    def total_datasources_count(self, total_datasources_count):
        """
        Sets the total_datasources_count of this DatasourcesStatusOutputV1.
        The total number of datasources expected to be connected. Provided regardless of the level of detail requested

        :param total_datasources_count: The total_datasources_count of this DatasourcesStatusOutputV1.
        :type: int
        """
        if total_datasources_count is None:
            raise ValueError("Invalid value for `total_datasources_count`, must not be `None`")

        self._total_datasources_count = total_datasources_count

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
        if not isinstance(other, DatasourcesStatusOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
