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


class ConnectorInputV1(object):
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
        'backup_name': 'str',
        'json': 'str',
        'propagate_to_agent': 'bool'
    }

    attribute_map = {
        'backup_name': 'backupName',
        'json': 'json',
        'propagate_to_agent': 'propagateToAgent'
    }

    def __init__(self, backup_name=None, json=None, propagate_to_agent=True):
        """
        ConnectorInputV1 - a model defined in Swagger
        """

        self._backup_name = None
        self._json = None
        self._propagate_to_agent = None

        if backup_name is not None:
          self.backup_name = backup_name
        if json is not None:
          self.json = json
        if propagate_to_agent is not None:
          self.propagate_to_agent = propagate_to_agent

    @property
    def backup_name(self):
        """
        Gets the backup_name of this ConnectorInputV1.
        The name of a connector backup to restore, when updating a connector.

        :return: The backup_name of this ConnectorInputV1.
        :rtype: str
        """
        return self._backup_name

    @backup_name.setter
    def backup_name(self, backup_name):
        """
        Sets the backup_name of this ConnectorInputV1.
        The name of a connector backup to restore, when updating a connector.

        :param backup_name: The backup_name of this ConnectorInputV1.
        :type: str
        """

        self._backup_name = backup_name

    @property
    def json(self):
        """
        Gets the json of this ConnectorInputV1.
        The connector’s json configuration.

        :return: The json of this ConnectorInputV1.
        :rtype: str
        """
        return self._json

    @json.setter
    def json(self, json):
        """
        Sets the json of this ConnectorInputV1.
        The connector’s json configuration.

        :param json: The json of this ConnectorInputV1.
        :type: str
        """

        self._json = json

    @property
    def propagate_to_agent(self):
        """
        Gets the propagate_to_agent of this ConnectorInputV1.
        Whether the connector's json update event should propagate to the remote agent.

        :return: The propagate_to_agent of this ConnectorInputV1.
        :rtype: bool
        """
        return self._propagate_to_agent

    @propagate_to_agent.setter
    def propagate_to_agent(self, propagate_to_agent):
        """
        Sets the propagate_to_agent of this ConnectorInputV1.
        Whether the connector's json update event should propagate to the remote agent.

        :param propagate_to_agent: The propagate_to_agent of this ConnectorInputV1.
        :type: bool
        """

        self._propagate_to_agent = propagate_to_agent

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
        if not isinstance(other, ConnectorInputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
