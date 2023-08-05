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


class DatasourceOutputV1(object):
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
        'additional_properties': 'list[ScalarPropertyV1]',
        'cache_enabled': 'bool',
        'condition_location': 'str',
        'data_version_check': 'str',
        'datasource_class': 'str',
        'datasource_id': 'str',
        'description': 'str',
        'effective_permissions': 'PermissionsV1',
        'id': 'str',
        'indexing_schedule_supported': 'bool',
        'is_archived': 'bool',
        'is_redacted': 'bool',
        'name': 'str',
        'seeq_internal': 'bool',
        'signal_location': 'str',
        'status_message': 'str',
        'stored_in_seeq': 'bool',
        'translation_key': 'str',
        'type': 'str'
    }

    attribute_map = {
        'additional_properties': 'additionalProperties',
        'cache_enabled': 'cacheEnabled',
        'condition_location': 'conditionLocation',
        'data_version_check': 'dataVersionCheck',
        'datasource_class': 'datasourceClass',
        'datasource_id': 'datasourceId',
        'description': 'description',
        'effective_permissions': 'effectivePermissions',
        'id': 'id',
        'indexing_schedule_supported': 'indexingScheduleSupported',
        'is_archived': 'isArchived',
        'is_redacted': 'isRedacted',
        'name': 'name',
        'seeq_internal': 'seeqInternal',
        'signal_location': 'signalLocation',
        'status_message': 'statusMessage',
        'stored_in_seeq': 'storedInSeeq',
        'translation_key': 'translationKey',
        'type': 'type'
    }

    def __init__(self, additional_properties=None, cache_enabled=False, condition_location=None, data_version_check=None, datasource_class=None, datasource_id=None, description=None, effective_permissions=None, id=None, indexing_schedule_supported=False, is_archived=False, is_redacted=False, name=None, seeq_internal=False, signal_location=None, status_message=None, stored_in_seeq=False, translation_key=None, type=None):
        """
        DatasourceOutputV1 - a model defined in Swagger
        """

        self._additional_properties = None
        self._cache_enabled = None
        self._condition_location = None
        self._data_version_check = None
        self._datasource_class = None
        self._datasource_id = None
        self._description = None
        self._effective_permissions = None
        self._id = None
        self._indexing_schedule_supported = None
        self._is_archived = None
        self._is_redacted = None
        self._name = None
        self._seeq_internal = None
        self._signal_location = None
        self._status_message = None
        self._stored_in_seeq = None
        self._translation_key = None
        self._type = None

        if additional_properties is not None:
          self.additional_properties = additional_properties
        if cache_enabled is not None:
          self.cache_enabled = cache_enabled
        if condition_location is not None:
          self.condition_location = condition_location
        if data_version_check is not None:
          self.data_version_check = data_version_check
        if datasource_class is not None:
          self.datasource_class = datasource_class
        if datasource_id is not None:
          self.datasource_id = datasource_id
        if description is not None:
          self.description = description
        if effective_permissions is not None:
          self.effective_permissions = effective_permissions
        if id is not None:
          self.id = id
        if indexing_schedule_supported is not None:
          self.indexing_schedule_supported = indexing_schedule_supported
        if is_archived is not None:
          self.is_archived = is_archived
        if is_redacted is not None:
          self.is_redacted = is_redacted
        if name is not None:
          self.name = name
        if seeq_internal is not None:
          self.seeq_internal = seeq_internal
        if signal_location is not None:
          self.signal_location = signal_location
        if status_message is not None:
          self.status_message = status_message
        if stored_in_seeq is not None:
          self.stored_in_seeq = stored_in_seeq
        if translation_key is not None:
          self.translation_key = translation_key
        if type is not None:
          self.type = type

    @property
    def additional_properties(self):
        """
        Gets the additional_properties of this DatasourceOutputV1.
        Additional properties of the datasource

        :return: The additional_properties of this DatasourceOutputV1.
        :rtype: list[ScalarPropertyV1]
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """
        Sets the additional_properties of this DatasourceOutputV1.
        Additional properties of the datasource

        :param additional_properties: The additional_properties of this DatasourceOutputV1.
        :type: list[ScalarPropertyV1]
        """

        self._additional_properties = additional_properties

    @property
    def cache_enabled(self):
        """
        Gets the cache_enabled of this DatasourceOutputV1.
        Whether this datasource's signal data will be cached in Seeq.

        :return: The cache_enabled of this DatasourceOutputV1.
        :rtype: bool
        """
        return self._cache_enabled

    @cache_enabled.setter
    def cache_enabled(self, cache_enabled):
        """
        Sets the cache_enabled of this DatasourceOutputV1.
        Whether this datasource's signal data will be cached in Seeq.

        :param cache_enabled: The cache_enabled of this DatasourceOutputV1.
        :type: bool
        """

        self._cache_enabled = cache_enabled

    @property
    def condition_location(self):
        """
        Gets the condition_location of this DatasourceOutputV1.
        Where this datasource's condition data is stored, if this datasource is stored in seeq

        :return: The condition_location of this DatasourceOutputV1.
        :rtype: str
        """
        return self._condition_location

    @condition_location.setter
    def condition_location(self, condition_location):
        """
        Sets the condition_location of this DatasourceOutputV1.
        Where this datasource's condition data is stored, if this datasource is stored in seeq

        :param condition_location: The condition_location of this DatasourceOutputV1.
        :type: str
        """
        allowed_values = ["FILE_SIGNAL_CACHE", "FILE_SIGNAL_STORAGE", "POSTGRES"]
        if condition_location not in allowed_values:
            raise ValueError(
                "Invalid value for `condition_location` ({0}), must be one of {1}"
                .format(condition_location, allowed_values)
            )

        self._condition_location = condition_location

    @property
    def data_version_check(self):
        """
        Gets the data_version_check of this DatasourceOutputV1.
        The datasource's version check, which represents a version of the metadata synced for this datasource. If its data version check is unchanged on subsequent metadata syncs, no update is necessary. A common data version check is a datetime, checksum or last change date.

        :return: The data_version_check of this DatasourceOutputV1.
        :rtype: str
        """
        return self._data_version_check

    @data_version_check.setter
    def data_version_check(self, data_version_check):
        """
        Sets the data_version_check of this DatasourceOutputV1.
        The datasource's version check, which represents a version of the metadata synced for this datasource. If its data version check is unchanged on subsequent metadata syncs, no update is necessary. A common data version check is a datetime, checksum or last change date.

        :param data_version_check: The data_version_check of this DatasourceOutputV1.
        :type: str
        """

        self._data_version_check = data_version_check

    @property
    def datasource_class(self):
        """
        Gets the datasource_class of this DatasourceOutputV1.
        The class of the datasource

        :return: The datasource_class of this DatasourceOutputV1.
        :rtype: str
        """
        return self._datasource_class

    @datasource_class.setter
    def datasource_class(self, datasource_class):
        """
        Sets the datasource_class of this DatasourceOutputV1.
        The class of the datasource

        :param datasource_class: The datasource_class of this DatasourceOutputV1.
        :type: str
        """

        self._datasource_class = datasource_class

    @property
    def datasource_id(self):
        """
        Gets the datasource_id of this DatasourceOutputV1.
        The ID of the datasource

        :return: The datasource_id of this DatasourceOutputV1.
        :rtype: str
        """
        return self._datasource_id

    @datasource_id.setter
    def datasource_id(self, datasource_id):
        """
        Sets the datasource_id of this DatasourceOutputV1.
        The ID of the datasource

        :param datasource_id: The datasource_id of this DatasourceOutputV1.
        :type: str
        """

        self._datasource_id = datasource_id

    @property
    def description(self):
        """
        Gets the description of this DatasourceOutputV1.
        Clarifying information or other plain language description of this item

        :return: The description of this DatasourceOutputV1.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DatasourceOutputV1.
        Clarifying information or other plain language description of this item

        :param description: The description of this DatasourceOutputV1.
        :type: str
        """

        self._description = description

    @property
    def effective_permissions(self):
        """
        Gets the effective_permissions of this DatasourceOutputV1.
        The permissions the current user has to the item.

        :return: The effective_permissions of this DatasourceOutputV1.
        :rtype: PermissionsV1
        """
        return self._effective_permissions

    @effective_permissions.setter
    def effective_permissions(self, effective_permissions):
        """
        Sets the effective_permissions of this DatasourceOutputV1.
        The permissions the current user has to the item.

        :param effective_permissions: The effective_permissions of this DatasourceOutputV1.
        :type: PermissionsV1
        """

        self._effective_permissions = effective_permissions

    @property
    def id(self):
        """
        Gets the id of this DatasourceOutputV1.
        The ID that can be used to interact with the item

        :return: The id of this DatasourceOutputV1.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DatasourceOutputV1.
        The ID that can be used to interact with the item

        :param id: The id of this DatasourceOutputV1.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def indexing_schedule_supported(self):
        """
        Gets the indexing_schedule_supported of this DatasourceOutputV1.
        Whether for this datasource indexing can be scheduled or requested from Datasource Management UI.

        :return: The indexing_schedule_supported of this DatasourceOutputV1.
        :rtype: bool
        """
        return self._indexing_schedule_supported

    @indexing_schedule_supported.setter
    def indexing_schedule_supported(self, indexing_schedule_supported):
        """
        Sets the indexing_schedule_supported of this DatasourceOutputV1.
        Whether for this datasource indexing can be scheduled or requested from Datasource Management UI.

        :param indexing_schedule_supported: The indexing_schedule_supported of this DatasourceOutputV1.
        :type: bool
        """

        self._indexing_schedule_supported = indexing_schedule_supported

    @property
    def is_archived(self):
        """
        Gets the is_archived of this DatasourceOutputV1.
        Whether item is archived

        :return: The is_archived of this DatasourceOutputV1.
        :rtype: bool
        """
        return self._is_archived

    @is_archived.setter
    def is_archived(self, is_archived):
        """
        Sets the is_archived of this DatasourceOutputV1.
        Whether item is archived

        :param is_archived: The is_archived of this DatasourceOutputV1.
        :type: bool
        """

        self._is_archived = is_archived

    @property
    def is_redacted(self):
        """
        Gets the is_redacted of this DatasourceOutputV1.
        Whether item is redacted

        :return: The is_redacted of this DatasourceOutputV1.
        :rtype: bool
        """
        return self._is_redacted

    @is_redacted.setter
    def is_redacted(self, is_redacted):
        """
        Sets the is_redacted of this DatasourceOutputV1.
        Whether item is redacted

        :param is_redacted: The is_redacted of this DatasourceOutputV1.
        :type: bool
        """

        self._is_redacted = is_redacted

    @property
    def name(self):
        """
        Gets the name of this DatasourceOutputV1.
        The human readable name

        :return: The name of this DatasourceOutputV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DatasourceOutputV1.
        The human readable name

        :param name: The name of this DatasourceOutputV1.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def seeq_internal(self):
        """
        Gets the seeq_internal of this DatasourceOutputV1.
        Whether this datasource is internal to Seeq (Local Datasource) or not.

        :return: The seeq_internal of this DatasourceOutputV1.
        :rtype: bool
        """
        return self._seeq_internal

    @seeq_internal.setter
    def seeq_internal(self, seeq_internal):
        """
        Sets the seeq_internal of this DatasourceOutputV1.
        Whether this datasource is internal to Seeq (Local Datasource) or not.

        :param seeq_internal: The seeq_internal of this DatasourceOutputV1.
        :type: bool
        """

        self._seeq_internal = seeq_internal

    @property
    def signal_location(self):
        """
        Gets the signal_location of this DatasourceOutputV1.
        Where this datasource's signal data is stored, if this datasource is stored in seeq

        :return: The signal_location of this DatasourceOutputV1.
        :rtype: str
        """
        return self._signal_location

    @signal_location.setter
    def signal_location(self, signal_location):
        """
        Sets the signal_location of this DatasourceOutputV1.
        Where this datasource's signal data is stored, if this datasource is stored in seeq

        :param signal_location: The signal_location of this DatasourceOutputV1.
        :type: str
        """
        allowed_values = ["FILE_SIGNAL_CACHE", "FILE_SIGNAL_STORAGE", "POSTGRES"]
        if signal_location not in allowed_values:
            raise ValueError(
                "Invalid value for `signal_location` ({0}), must be one of {1}"
                .format(signal_location, allowed_values)
            )

        self._signal_location = signal_location

    @property
    def status_message(self):
        """
        Gets the status_message of this DatasourceOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation

        :return: The status_message of this DatasourceOutputV1.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """
        Sets the status_message of this DatasourceOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation

        :param status_message: The status_message of this DatasourceOutputV1.
        :type: str
        """

        self._status_message = status_message

    @property
    def stored_in_seeq(self):
        """
        Gets the stored_in_seeq of this DatasourceOutputV1.
        Whether this datasource's data is stored in Seeq.

        :return: The stored_in_seeq of this DatasourceOutputV1.
        :rtype: bool
        """
        return self._stored_in_seeq

    @stored_in_seeq.setter
    def stored_in_seeq(self, stored_in_seeq):
        """
        Sets the stored_in_seeq of this DatasourceOutputV1.
        Whether this datasource's data is stored in Seeq.

        :param stored_in_seeq: The stored_in_seeq of this DatasourceOutputV1.
        :type: bool
        """

        self._stored_in_seeq = stored_in_seeq

    @property
    def translation_key(self):
        """
        Gets the translation_key of this DatasourceOutputV1.
        The item's translation key, if any

        :return: The translation_key of this DatasourceOutputV1.
        :rtype: str
        """
        return self._translation_key

    @translation_key.setter
    def translation_key(self, translation_key):
        """
        Sets the translation_key of this DatasourceOutputV1.
        The item's translation key, if any

        :param translation_key: The translation_key of this DatasourceOutputV1.
        :type: str
        """

        self._translation_key = translation_key

    @property
    def type(self):
        """
        Gets the type of this DatasourceOutputV1.
        The type of the item

        :return: The type of this DatasourceOutputV1.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this DatasourceOutputV1.
        The type of the item

        :param type: The type of this DatasourceOutputV1.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

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
        if not isinstance(other, DatasourceOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
