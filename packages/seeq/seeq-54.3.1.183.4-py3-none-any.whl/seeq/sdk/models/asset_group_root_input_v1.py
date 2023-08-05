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


class AssetGroupRootInputV1(object):
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
        'data_id': 'str',
        'description': 'str',
        'host_id': 'str',
        'id': 'str',
        'manually_added': 'str',
        'name': 'str',
        'properties': 'list[ScalarPropertyV1]',
        'scoped_to': 'str',
        'security_string': 'str',
        'source_security_string': 'str',
        'sync_token': 'str'
    }

    attribute_map = {
        'data_id': 'dataId',
        'description': 'description',
        'host_id': 'hostId',
        'id': 'id',
        'manually_added': 'manuallyAdded',
        'name': 'name',
        'properties': 'properties',
        'scoped_to': 'scopedTo',
        'security_string': 'securityString',
        'source_security_string': 'sourceSecurityString',
        'sync_token': 'syncToken'
    }

    def __init__(self, data_id=None, description=None, host_id=None, id=None, manually_added=None, name=None, properties=None, scoped_to=None, security_string=None, source_security_string=None, sync_token=None):
        """
        AssetGroupRootInputV1 - a model defined in Swagger
        """

        self._data_id = None
        self._description = None
        self._host_id = None
        self._id = None
        self._manually_added = None
        self._name = None
        self._properties = None
        self._scoped_to = None
        self._security_string = None
        self._source_security_string = None
        self._sync_token = None

        if data_id is not None:
          self.data_id = data_id
        if description is not None:
          self.description = description
        if host_id is not None:
          self.host_id = host_id
        if id is not None:
          self.id = id
        if manually_added is not None:
          self.manually_added = manually_added
        if name is not None:
          self.name = name
        if properties is not None:
          self.properties = properties
        if scoped_to is not None:
          self.scoped_to = scoped_to
        if security_string is not None:
          self.security_string = security_string
        if source_security_string is not None:
          self.source_security_string = source_security_string
        if sync_token is not None:
          self.sync_token = sync_token

    @property
    def data_id(self):
        """
        Gets the data_id of this AssetGroupRootInputV1.
        The data ID of this item. Note: This is not the Seeq ID, but the unique identifier that the remote datasource uses.

        :return: The data_id of this AssetGroupRootInputV1.
        :rtype: str
        """
        return self._data_id

    @data_id.setter
    def data_id(self, data_id):
        """
        Sets the data_id of this AssetGroupRootInputV1.
        The data ID of this item. Note: This is not the Seeq ID, but the unique identifier that the remote datasource uses.

        :param data_id: The data_id of this AssetGroupRootInputV1.
        :type: str
        """

        self._data_id = data_id

    @property
    def description(self):
        """
        Gets the description of this AssetGroupRootInputV1.
        Clarifying information or other plain language description of this item. An input of just whitespaces is equivalent to a null input.

        :return: The description of this AssetGroupRootInputV1.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this AssetGroupRootInputV1.
        Clarifying information or other plain language description of this item. An input of just whitespaces is equivalent to a null input.

        :param description: The description of this AssetGroupRootInputV1.
        :type: str
        """

        self._description = description

    @property
    def host_id(self):
        """
        Gets the host_id of this AssetGroupRootInputV1.
        The ID of the datasource hosting this item. Note that this is a Seeq-generated ID, not the way that the datasource identifies itself.

        :return: The host_id of this AssetGroupRootInputV1.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """
        Sets the host_id of this AssetGroupRootInputV1.
        The ID of the datasource hosting this item. Note that this is a Seeq-generated ID, not the way that the datasource identifies itself.

        :param host_id: The host_id of this AssetGroupRootInputV1.
        :type: str
        """

        self._host_id = host_id

    @property
    def id(self):
        """
        Gets the id of this AssetGroupRootInputV1.
        The Seeq ID of the item to be updated.  If this is present it means the item needs to be updated

        :return: The id of this AssetGroupRootInputV1.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AssetGroupRootInputV1.
        The Seeq ID of the item to be updated.  If this is present it means the item needs to be updated

        :param id: The id of this AssetGroupRootInputV1.
        :type: str
        """

        self._id = id

    @property
    def manually_added(self):
        """
        Gets the manually_added of this AssetGroupRootInputV1.
        UUID of the user who created the asset group

        :return: The manually_added of this AssetGroupRootInputV1.
        :rtype: str
        """
        return self._manually_added

    @manually_added.setter
    def manually_added(self, manually_added):
        """
        Sets the manually_added of this AssetGroupRootInputV1.
        UUID of the user who created the asset group

        :param manually_added: The manually_added of this AssetGroupRootInputV1.
        :type: str
        """

        self._manually_added = manually_added

    @property
    def name(self):
        """
        Gets the name of this AssetGroupRootInputV1.
        Human readable name. Required during creation. An input of just whitespaces is equivalent to a null input.

        :return: The name of this AssetGroupRootInputV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AssetGroupRootInputV1.
        Human readable name. Required during creation. An input of just whitespaces is equivalent to a null input.

        :param name: The name of this AssetGroupRootInputV1.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def properties(self):
        """
        Gets the properties of this AssetGroupRootInputV1.

        :return: The properties of this AssetGroupRootInputV1.
        :rtype: list[ScalarPropertyV1]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this AssetGroupRootInputV1.

        :param properties: The properties of this AssetGroupRootInputV1.
        :type: list[ScalarPropertyV1]
        """

        self._properties = properties

    @property
    def scoped_to(self):
        """
        Gets the scoped_to of this AssetGroupRootInputV1.
        The ID of the workbook to which this item will be scoped.

        :return: The scoped_to of this AssetGroupRootInputV1.
        :rtype: str
        """
        return self._scoped_to

    @scoped_to.setter
    def scoped_to(self, scoped_to):
        """
        Sets the scoped_to of this AssetGroupRootInputV1.
        The ID of the workbook to which this item will be scoped.

        :param scoped_to: The scoped_to of this AssetGroupRootInputV1.
        :type: str
        """

        self._scoped_to = scoped_to

    @property
    def security_string(self):
        """
        Gets the security_string of this AssetGroupRootInputV1.
        Security string containing all identities and their permissions for the item. If set, permissions can only be managed by the connector and not in Seeq.

        :return: The security_string of this AssetGroupRootInputV1.
        :rtype: str
        """
        return self._security_string

    @security_string.setter
    def security_string(self, security_string):
        """
        Sets the security_string of this AssetGroupRootInputV1.
        Security string containing all identities and their permissions for the item. If set, permissions can only be managed by the connector and not in Seeq.

        :param security_string: The security_string of this AssetGroupRootInputV1.
        :type: str
        """

        self._security_string = security_string

    @property
    def source_security_string(self):
        """
        Gets the source_security_string of this AssetGroupRootInputV1.
        The security string as it was originally found on the source (for debugging ACLs only)

        :return: The source_security_string of this AssetGroupRootInputV1.
        :rtype: str
        """
        return self._source_security_string

    @source_security_string.setter
    def source_security_string(self, source_security_string):
        """
        Sets the source_security_string of this AssetGroupRootInputV1.
        The security string as it was originally found on the source (for debugging ACLs only)

        :param source_security_string: The source_security_string of this AssetGroupRootInputV1.
        :type: str
        """

        self._source_security_string = source_security_string

    @property
    def sync_token(self):
        """
        Gets the sync_token of this AssetGroupRootInputV1.
        An arbitrary token (often a date or random ID) that is used during metadata syncs. At the end of a full sync, items with mismatching sync tokens are identified as stale and may be archived using the Datasources clean-up API.

        :return: The sync_token of this AssetGroupRootInputV1.
        :rtype: str
        """
        return self._sync_token

    @sync_token.setter
    def sync_token(self, sync_token):
        """
        Sets the sync_token of this AssetGroupRootInputV1.
        An arbitrary token (often a date or random ID) that is used during metadata syncs. At the end of a full sync, items with mismatching sync tokens are identified as stale and may be archived using the Datasources clean-up API.

        :param sync_token: The sync_token of this AssetGroupRootInputV1.
        :type: str
        """

        self._sync_token = sync_token

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
        if not isinstance(other, AssetGroupRootInputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
