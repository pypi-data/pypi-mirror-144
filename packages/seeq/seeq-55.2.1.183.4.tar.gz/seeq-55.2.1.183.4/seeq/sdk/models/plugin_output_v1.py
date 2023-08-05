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


class PluginOutputV1(object):
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
        'effective_permissions': 'PermissionsV1',
        'entry_point': 'str',
        'host': 'object',
        'icon': 'str',
        'id': 'str',
        'identifier': 'str',
        'is_archived': 'bool',
        'is_redacted': 'bool',
        'name': 'str',
        'options': 'object',
        'status_message': 'str',
        'translation_key': 'str',
        'type': 'str',
        'version': 'str'
    }

    attribute_map = {
        'category': 'category',
        'description': 'description',
        'effective_permissions': 'effectivePermissions',
        'entry_point': 'entryPoint',
        'host': 'host',
        'icon': 'icon',
        'id': 'id',
        'identifier': 'identifier',
        'is_archived': 'isArchived',
        'is_redacted': 'isRedacted',
        'name': 'name',
        'options': 'options',
        'status_message': 'statusMessage',
        'translation_key': 'translationKey',
        'type': 'type',
        'version': 'version'
    }

    def __init__(self, category=None, description=None, effective_permissions=None, entry_point=None, host=None, icon=None, id=None, identifier=None, is_archived=False, is_redacted=False, name=None, options=None, status_message=None, translation_key=None, type=None, version=None):
        """
        PluginOutputV1 - a model defined in Swagger
        """

        self._category = None
        self._description = None
        self._effective_permissions = None
        self._entry_point = None
        self._host = None
        self._icon = None
        self._id = None
        self._identifier = None
        self._is_archived = None
        self._is_redacted = None
        self._name = None
        self._options = None
        self._status_message = None
        self._translation_key = None
        self._type = None
        self._version = None

        if category is not None:
          self.category = category
        if description is not None:
          self.description = description
        if effective_permissions is not None:
          self.effective_permissions = effective_permissions
        if entry_point is not None:
          self.entry_point = entry_point
        if host is not None:
          self.host = host
        if icon is not None:
          self.icon = icon
        if id is not None:
          self.id = id
        if identifier is not None:
          self.identifier = identifier
        if is_archived is not None:
          self.is_archived = is_archived
        if is_redacted is not None:
          self.is_redacted = is_redacted
        if name is not None:
          self.name = name
        if options is not None:
          self.options = options
        if status_message is not None:
          self.status_message = status_message
        if translation_key is not None:
          self.translation_key = translation_key
        if type is not None:
          self.type = type
        if version is not None:
          self.version = version

    @property
    def category(self):
        """
        Gets the category of this PluginOutputV1.
        The plugin category (e.g. \"DisplayPane\")

        :return: The category of this PluginOutputV1.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this PluginOutputV1.
        The plugin category (e.g. \"DisplayPane\")

        :param category: The category of this PluginOutputV1.
        :type: str
        """

        self._category = category

    @property
    def description(self):
        """
        Gets the description of this PluginOutputV1.
        Clarifying information or other plain language description of this item

        :return: The description of this PluginOutputV1.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this PluginOutputV1.
        Clarifying information or other plain language description of this item

        :param description: The description of this PluginOutputV1.
        :type: str
        """

        self._description = description

    @property
    def effective_permissions(self):
        """
        Gets the effective_permissions of this PluginOutputV1.
        The permissions the current user has to the item.

        :return: The effective_permissions of this PluginOutputV1.
        :rtype: PermissionsV1
        """
        return self._effective_permissions

    @effective_permissions.setter
    def effective_permissions(self, effective_permissions):
        """
        Sets the effective_permissions of this PluginOutputV1.
        The permissions the current user has to the item.

        :param effective_permissions: The effective_permissions of this PluginOutputV1.
        :type: PermissionsV1
        """

        self._effective_permissions = effective_permissions

    @property
    def entry_point(self):
        """
        Gets the entry_point of this PluginOutputV1.
        The relative path to the plugin entry point (e.g. \"myfolder/index.html \")

        :return: The entry_point of this PluginOutputV1.
        :rtype: str
        """
        return self._entry_point

    @entry_point.setter
    def entry_point(self, entry_point):
        """
        Sets the entry_point of this PluginOutputV1.
        The relative path to the plugin entry point (e.g. \"myfolder/index.html \")

        :param entry_point: The entry_point of this PluginOutputV1.
        :type: str
        """

        self._entry_point = entry_point

    @property
    def host(self):
        """
        Gets the host of this PluginOutputV1.
        Plugin host configuration settings

        :return: The host of this PluginOutputV1.
        :rtype: object
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this PluginOutputV1.
        Plugin host configuration settings

        :param host: The host of this PluginOutputV1.
        :type: object
        """

        self._host = host

    @property
    def icon(self):
        """
        Gets the icon of this PluginOutputV1.
        The plugin icon (e.g. \"fa fa-wrench\")

        :return: The icon of this PluginOutputV1.
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """
        Sets the icon of this PluginOutputV1.
        The plugin icon (e.g. \"fa fa-wrench\")

        :param icon: The icon of this PluginOutputV1.
        :type: str
        """

        self._icon = icon

    @property
    def id(self):
        """
        Gets the id of this PluginOutputV1.
        The ID that can be used to interact with the item

        :return: The id of this PluginOutputV1.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PluginOutputV1.
        The ID that can be used to interact with the item

        :param id: The id of this PluginOutputV1.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def identifier(self):
        """
        Gets the identifier of this PluginOutputV1.
        The plugin identifier (e.g. \"com.seeq.samplePlugin\")

        :return: The identifier of this PluginOutputV1.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this PluginOutputV1.
        The plugin identifier (e.g. \"com.seeq.samplePlugin\")

        :param identifier: The identifier of this PluginOutputV1.
        :type: str
        """

        self._identifier = identifier

    @property
    def is_archived(self):
        """
        Gets the is_archived of this PluginOutputV1.
        Whether item is archived

        :return: The is_archived of this PluginOutputV1.
        :rtype: bool
        """
        return self._is_archived

    @is_archived.setter
    def is_archived(self, is_archived):
        """
        Sets the is_archived of this PluginOutputV1.
        Whether item is archived

        :param is_archived: The is_archived of this PluginOutputV1.
        :type: bool
        """

        self._is_archived = is_archived

    @property
    def is_redacted(self):
        """
        Gets the is_redacted of this PluginOutputV1.
        Whether item is redacted

        :return: The is_redacted of this PluginOutputV1.
        :rtype: bool
        """
        return self._is_redacted

    @is_redacted.setter
    def is_redacted(self, is_redacted):
        """
        Sets the is_redacted of this PluginOutputV1.
        Whether item is redacted

        :param is_redacted: The is_redacted of this PluginOutputV1.
        :type: bool
        """

        self._is_redacted = is_redacted

    @property
    def name(self):
        """
        Gets the name of this PluginOutputV1.
        The human readable name

        :return: The name of this PluginOutputV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PluginOutputV1.
        The human readable name

        :param name: The name of this PluginOutputV1.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def options(self):
        """
        Gets the options of this PluginOutputV1.
        Plugin-specific configuration settings

        :return: The options of this PluginOutputV1.
        :rtype: object
        """
        return self._options

    @options.setter
    def options(self, options):
        """
        Sets the options of this PluginOutputV1.
        Plugin-specific configuration settings

        :param options: The options of this PluginOutputV1.
        :type: object
        """

        self._options = options

    @property
    def status_message(self):
        """
        Gets the status_message of this PluginOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation

        :return: The status_message of this PluginOutputV1.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """
        Sets the status_message of this PluginOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation

        :param status_message: The status_message of this PluginOutputV1.
        :type: str
        """

        self._status_message = status_message

    @property
    def translation_key(self):
        """
        Gets the translation_key of this PluginOutputV1.
        The item's translation key, if any

        :return: The translation_key of this PluginOutputV1.
        :rtype: str
        """
        return self._translation_key

    @translation_key.setter
    def translation_key(self, translation_key):
        """
        Sets the translation_key of this PluginOutputV1.
        The item's translation key, if any

        :param translation_key: The translation_key of this PluginOutputV1.
        :type: str
        """

        self._translation_key = translation_key

    @property
    def type(self):
        """
        Gets the type of this PluginOutputV1.
        The type of the item

        :return: The type of this PluginOutputV1.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this PluginOutputV1.
        The type of the item

        :param type: The type of this PluginOutputV1.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def version(self):
        """
        Gets the version of this PluginOutputV1.
        The plugin version (e.g. \"1.0.0\")

        :return: The version of this PluginOutputV1.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this PluginOutputV1.
        The plugin version (e.g. \"1.0.0\")

        :param version: The version of this PluginOutputV1.
        :type: str
        """

        self._version = version

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
        if not isinstance(other, PluginOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
