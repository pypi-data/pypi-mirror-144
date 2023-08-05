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


class ItemOutputV1(object):
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
        'ancillaries': 'list[ItemAncillaryOutputV1]',
        'cached': 'bool',
        'datasource': 'DatasourcePreviewV1',
        'description': 'str',
        'effective_permissions': 'PermissionsV1',
        'fingerprint': 'str',
        'id': 'str',
        'is_archived': 'bool',
        'is_redacted': 'bool',
        'name': 'str',
        'properties': 'list[PropertyOutputV1]',
        'scoped_to': 'str',
        'status_message': 'str',
        'translation_key': 'str',
        'type': 'str',
        'workbook_id': 'str'
    }

    attribute_map = {
        'ancillaries': 'ancillaries',
        'cached': 'cached',
        'datasource': 'datasource',
        'description': 'description',
        'effective_permissions': 'effectivePermissions',
        'fingerprint': 'fingerprint',
        'id': 'id',
        'is_archived': 'isArchived',
        'is_redacted': 'isRedacted',
        'name': 'name',
        'properties': 'properties',
        'scoped_to': 'scopedTo',
        'status_message': 'statusMessage',
        'translation_key': 'translationKey',
        'type': 'type',
        'workbook_id': 'workbookId'
    }

    def __init__(self, ancillaries=None, cached=False, datasource=None, description=None, effective_permissions=None, fingerprint=None, id=None, is_archived=False, is_redacted=False, name=None, properties=None, scoped_to=None, status_message=None, translation_key=None, type=None, workbook_id=None):
        """
        ItemOutputV1 - a model defined in Swagger
        """

        self._ancillaries = None
        self._cached = None
        self._datasource = None
        self._description = None
        self._effective_permissions = None
        self._fingerprint = None
        self._id = None
        self._is_archived = None
        self._is_redacted = None
        self._name = None
        self._properties = None
        self._scoped_to = None
        self._status_message = None
        self._translation_key = None
        self._type = None
        self._workbook_id = None

        if ancillaries is not None:
          self.ancillaries = ancillaries
        if cached is not None:
          self.cached = cached
        if datasource is not None:
          self.datasource = datasource
        if description is not None:
          self.description = description
        if effective_permissions is not None:
          self.effective_permissions = effective_permissions
        if fingerprint is not None:
          self.fingerprint = fingerprint
        if id is not None:
          self.id = id
        if is_archived is not None:
          self.is_archived = is_archived
        if is_redacted is not None:
          self.is_redacted = is_redacted
        if name is not None:
          self.name = name
        if properties is not None:
          self.properties = properties
        if scoped_to is not None:
          self.scoped_to = scoped_to
        if status_message is not None:
          self.status_message = status_message
        if translation_key is not None:
          self.translation_key = translation_key
        if type is not None:
          self.type = type
        if workbook_id is not None:
          self.workbook_id = workbook_id

    @property
    def ancillaries(self):
        """
        Gets the ancillaries of this ItemOutputV1.
        The list of the item's ancillaries

        :return: The ancillaries of this ItemOutputV1.
        :rtype: list[ItemAncillaryOutputV1]
        """
        return self._ancillaries

    @ancillaries.setter
    def ancillaries(self, ancillaries):
        """
        Sets the ancillaries of this ItemOutputV1.
        The list of the item's ancillaries

        :param ancillaries: The ancillaries of this ItemOutputV1.
        :type: list[ItemAncillaryOutputV1]
        """

        self._ancillaries = ancillaries

    @property
    def cached(self):
        """
        Gets the cached of this ItemOutputV1.
        Indicates whether the item's persistent disk cache is enabled. Only present for items which support caching

        :return: The cached of this ItemOutputV1.
        :rtype: bool
        """
        return self._cached

    @cached.setter
    def cached(self, cached):
        """
        Sets the cached of this ItemOutputV1.
        Indicates whether the item's persistent disk cache is enabled. Only present for items which support caching

        :param cached: The cached of this ItemOutputV1.
        :type: bool
        """

        self._cached = cached

    @property
    def datasource(self):
        """
        Gets the datasource of this ItemOutputV1.
        The datasource for the item

        :return: The datasource of this ItemOutputV1.
        :rtype: DatasourcePreviewV1
        """
        return self._datasource

    @datasource.setter
    def datasource(self, datasource):
        """
        Sets the datasource of this ItemOutputV1.
        The datasource for the item

        :param datasource: The datasource of this ItemOutputV1.
        :type: DatasourcePreviewV1
        """

        self._datasource = datasource

    @property
    def description(self):
        """
        Gets the description of this ItemOutputV1.
        Clarifying information or other plain language description of this item

        :return: The description of this ItemOutputV1.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ItemOutputV1.
        Clarifying information or other plain language description of this item

        :param description: The description of this ItemOutputV1.
        :type: str
        """

        self._description = description

    @property
    def effective_permissions(self):
        """
        Gets the effective_permissions of this ItemOutputV1.
        The permissions the current user has to the item.

        :return: The effective_permissions of this ItemOutputV1.
        :rtype: PermissionsV1
        """
        return self._effective_permissions

    @effective_permissions.setter
    def effective_permissions(self, effective_permissions):
        """
        Sets the effective_permissions of this ItemOutputV1.
        The permissions the current user has to the item.

        :param effective_permissions: The effective_permissions of this ItemOutputV1.
        :type: PermissionsV1
        """

        self._effective_permissions = effective_permissions

    @property
    def fingerprint(self):
        """
        Gets the fingerprint of this ItemOutputV1.
        For stored items, an optional CDC (Change Data Capture) attribute.

        :return: The fingerprint of this ItemOutputV1.
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        """
        Sets the fingerprint of this ItemOutputV1.
        For stored items, an optional CDC (Change Data Capture) attribute.

        :param fingerprint: The fingerprint of this ItemOutputV1.
        :type: str
        """

        self._fingerprint = fingerprint

    @property
    def id(self):
        """
        Gets the id of this ItemOutputV1.
        The ID that can be used to interact with the item

        :return: The id of this ItemOutputV1.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ItemOutputV1.
        The ID that can be used to interact with the item

        :param id: The id of this ItemOutputV1.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def is_archived(self):
        """
        Gets the is_archived of this ItemOutputV1.
        Whether item is archived

        :return: The is_archived of this ItemOutputV1.
        :rtype: bool
        """
        return self._is_archived

    @is_archived.setter
    def is_archived(self, is_archived):
        """
        Sets the is_archived of this ItemOutputV1.
        Whether item is archived

        :param is_archived: The is_archived of this ItemOutputV1.
        :type: bool
        """

        self._is_archived = is_archived

    @property
    def is_redacted(self):
        """
        Gets the is_redacted of this ItemOutputV1.
        Whether item is redacted

        :return: The is_redacted of this ItemOutputV1.
        :rtype: bool
        """
        return self._is_redacted

    @is_redacted.setter
    def is_redacted(self, is_redacted):
        """
        Sets the is_redacted of this ItemOutputV1.
        Whether item is redacted

        :param is_redacted: The is_redacted of this ItemOutputV1.
        :type: bool
        """

        self._is_redacted = is_redacted

    @property
    def name(self):
        """
        Gets the name of this ItemOutputV1.
        The human readable name

        :return: The name of this ItemOutputV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ItemOutputV1.
        The human readable name

        :param name: The name of this ItemOutputV1.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def properties(self):
        """
        Gets the properties of this ItemOutputV1.
        The list of the item's properties

        :return: The properties of this ItemOutputV1.
        :rtype: list[PropertyOutputV1]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this ItemOutputV1.
        The list of the item's properties

        :param properties: The properties of this ItemOutputV1.
        :type: list[PropertyOutputV1]
        """

        self._properties = properties

    @property
    def scoped_to(self):
        """
        Gets the scoped_to of this ItemOutputV1.
        The ID of the workbook to which this item is scoped or null if it is in the global scope.

        :return: The scoped_to of this ItemOutputV1.
        :rtype: str
        """
        return self._scoped_to

    @scoped_to.setter
    def scoped_to(self, scoped_to):
        """
        Sets the scoped_to of this ItemOutputV1.
        The ID of the workbook to which this item is scoped or null if it is in the global scope.

        :param scoped_to: The scoped_to of this ItemOutputV1.
        :type: str
        """

        self._scoped_to = scoped_to

    @property
    def status_message(self):
        """
        Gets the status_message of this ItemOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation

        :return: The status_message of this ItemOutputV1.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """
        Sets the status_message of this ItemOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation

        :param status_message: The status_message of this ItemOutputV1.
        :type: str
        """

        self._status_message = status_message

    @property
    def translation_key(self):
        """
        Gets the translation_key of this ItemOutputV1.
        The item's translation key, if any

        :return: The translation_key of this ItemOutputV1.
        :rtype: str
        """
        return self._translation_key

    @translation_key.setter
    def translation_key(self, translation_key):
        """
        Sets the translation_key of this ItemOutputV1.
        The item's translation key, if any

        :param translation_key: The translation_key of this ItemOutputV1.
        :type: str
        """

        self._translation_key = translation_key

    @property
    def type(self):
        """
        Gets the type of this ItemOutputV1.
        The type of the item

        :return: The type of this ItemOutputV1.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ItemOutputV1.
        The type of the item

        :param type: The type of this ItemOutputV1.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def workbook_id(self):
        """
        Gets the workbook_id of this ItemOutputV1.
        If the item is a worksheet, the ID of its associated workbook

        :return: The workbook_id of this ItemOutputV1.
        :rtype: str
        """
        return self._workbook_id

    @workbook_id.setter
    def workbook_id(self, workbook_id):
        """
        Sets the workbook_id of this ItemOutputV1.
        If the item is a worksheet, the ID of its associated workbook

        :param workbook_id: The workbook_id of this ItemOutputV1.
        :type: str
        """

        self._workbook_id = workbook_id

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
        if not isinstance(other, ItemOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
