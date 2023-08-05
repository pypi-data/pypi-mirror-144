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


class DatasourceInputV1(object):
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
        'indexing_schedule_supported': 'bool',
        'name': 'str',
        'signal_location': 'str',
        'stored_in_seeq': 'bool'
    }

    attribute_map = {
        'additional_properties': 'additionalProperties',
        'cache_enabled': 'cacheEnabled',
        'condition_location': 'conditionLocation',
        'data_version_check': 'dataVersionCheck',
        'datasource_class': 'datasourceClass',
        'datasource_id': 'datasourceId',
        'description': 'description',
        'indexing_schedule_supported': 'indexingScheduleSupported',
        'name': 'name',
        'signal_location': 'signalLocation',
        'stored_in_seeq': 'storedInSeeq'
    }

    def __init__(self, additional_properties=None, cache_enabled=False, condition_location=None, data_version_check=None, datasource_class=None, datasource_id=None, description=None, indexing_schedule_supported=False, name=None, signal_location=None, stored_in_seeq=False):
        """
        DatasourceInputV1 - a model defined in Swagger
        """

        self._additional_properties = None
        self._cache_enabled = None
        self._condition_location = None
        self._data_version_check = None
        self._datasource_class = None
        self._datasource_id = None
        self._description = None
        self._indexing_schedule_supported = None
        self._name = None
        self._signal_location = None
        self._stored_in_seeq = None

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
        if indexing_schedule_supported is not None:
          self.indexing_schedule_supported = indexing_schedule_supported
        if name is not None:
          self.name = name
        if signal_location is not None:
          self.signal_location = signal_location
        if stored_in_seeq is not None:
          self.stored_in_seeq = stored_in_seeq

    @property
    def additional_properties(self):
        """
        Gets the additional_properties of this DatasourceInputV1.
        Additional properties to set on the datasource

        :return: The additional_properties of this DatasourceInputV1.
        :rtype: list[ScalarPropertyV1]
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """
        Sets the additional_properties of this DatasourceInputV1.
        Additional properties to set on the datasource

        :param additional_properties: The additional_properties of this DatasourceInputV1.
        :type: list[ScalarPropertyV1]
        """

        self._additional_properties = additional_properties

    @property
    def cache_enabled(self):
        """
        Gets the cache_enabled of this DatasourceInputV1.
        True if this datasource's signal data should be cached in Seeq; false otherwise

        :return: The cache_enabled of this DatasourceInputV1.
        :rtype: bool
        """
        return self._cache_enabled

    @cache_enabled.setter
    def cache_enabled(self, cache_enabled):
        """
        Sets the cache_enabled of this DatasourceInputV1.
        True if this datasource's signal data should be cached in Seeq; false otherwise

        :param cache_enabled: The cache_enabled of this DatasourceInputV1.
        :type: bool
        """

        self._cache_enabled = cache_enabled

    @property
    def condition_location(self):
        """
        Gets the condition_location of this DatasourceInputV1.
        If StoredInSeeq is set to true, then this is where conditions under this datasource will be stored. Valid values: POSTGRES.

        :return: The condition_location of this DatasourceInputV1.
        :rtype: str
        """
        return self._condition_location

    @condition_location.setter
    def condition_location(self, condition_location):
        """
        Sets the condition_location of this DatasourceInputV1.
        If StoredInSeeq is set to true, then this is where conditions under this datasource will be stored. Valid values: POSTGRES.

        :param condition_location: The condition_location of this DatasourceInputV1.
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
        Gets the data_version_check of this DatasourceInputV1.
        The datasource's version check, which represents a version of the metadata synced for this datasource. If its data version check is unchanged on subsequent metadata syncs, no update is necessary. A common data version check is a datetime, checksum or last change date.

        :return: The data_version_check of this DatasourceInputV1.
        :rtype: str
        """
        return self._data_version_check

    @data_version_check.setter
    def data_version_check(self, data_version_check):
        """
        Sets the data_version_check of this DatasourceInputV1.
        The datasource's version check, which represents a version of the metadata synced for this datasource. If its data version check is unchanged on subsequent metadata syncs, no update is necessary. A common data version check is a datetime, checksum or last change date.

        :param data_version_check: The data_version_check of this DatasourceInputV1.
        :type: str
        """

        self._data_version_check = data_version_check

    @property
    def datasource_class(self):
        """
        Gets the datasource_class of this DatasourceInputV1.
        The class of the datasource

        :return: The datasource_class of this DatasourceInputV1.
        :rtype: str
        """
        return self._datasource_class

    @datasource_class.setter
    def datasource_class(self, datasource_class):
        """
        Sets the datasource_class of this DatasourceInputV1.
        The class of the datasource

        :param datasource_class: The datasource_class of this DatasourceInputV1.
        :type: str
        """
        if datasource_class is None:
            raise ValueError("Invalid value for `datasource_class`, must not be `None`")

        self._datasource_class = datasource_class

    @property
    def datasource_id(self):
        """
        Gets the datasource_id of this DatasourceInputV1.
        The ID of the datasource

        :return: The datasource_id of this DatasourceInputV1.
        :rtype: str
        """
        return self._datasource_id

    @datasource_id.setter
    def datasource_id(self, datasource_id):
        """
        Sets the datasource_id of this DatasourceInputV1.
        The ID of the datasource

        :param datasource_id: The datasource_id of this DatasourceInputV1.
        :type: str
        """
        if datasource_id is None:
            raise ValueError("Invalid value for `datasource_id`, must not be `None`")

        self._datasource_id = datasource_id

    @property
    def description(self):
        """
        Gets the description of this DatasourceInputV1.
        Clarifying information or other plain language description of this item. An input of just whitespace is equivalent to a null input.

        :return: The description of this DatasourceInputV1.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DatasourceInputV1.
        Clarifying information or other plain language description of this item. An input of just whitespace is equivalent to a null input.

        :param description: The description of this DatasourceInputV1.
        :type: str
        """

        self._description = description

    @property
    def indexing_schedule_supported(self):
        """
        Gets the indexing_schedule_supported of this DatasourceInputV1.
        True if for this datasource indexing can be scheduled or requested from Datasource Management UI.

        :return: The indexing_schedule_supported of this DatasourceInputV1.
        :rtype: bool
        """
        return self._indexing_schedule_supported

    @indexing_schedule_supported.setter
    def indexing_schedule_supported(self, indexing_schedule_supported):
        """
        Sets the indexing_schedule_supported of this DatasourceInputV1.
        True if for this datasource indexing can be scheduled or requested from Datasource Management UI.

        :param indexing_schedule_supported: The indexing_schedule_supported of this DatasourceInputV1.
        :type: bool
        """

        self._indexing_schedule_supported = indexing_schedule_supported

    @property
    def name(self):
        """
        Gets the name of this DatasourceInputV1.
        Human readable name. Required during creation. An input of just whitespaces is equivalent to a null input.

        :return: The name of this DatasourceInputV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DatasourceInputV1.
        Human readable name. Required during creation. An input of just whitespaces is equivalent to a null input.

        :param name: The name of this DatasourceInputV1.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def signal_location(self):
        """
        Gets the signal_location of this DatasourceInputV1.
        If StoredInSeeq is set to true, then this is where signals under this datasource will be stored. Valid values: FILE_SIGNAL_STORAGE.

        :return: The signal_location of this DatasourceInputV1.
        :rtype: str
        """
        return self._signal_location

    @signal_location.setter
    def signal_location(self, signal_location):
        """
        Sets the signal_location of this DatasourceInputV1.
        If StoredInSeeq is set to true, then this is where signals under this datasource will be stored. Valid values: FILE_SIGNAL_STORAGE.

        :param signal_location: The signal_location of this DatasourceInputV1.
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
    def stored_in_seeq(self):
        """
        Gets the stored_in_seeq of this DatasourceInputV1.
        True if this datasource's data is stored in Seeq; false otherwise (e.g. a remote datasource like PI).

        :return: The stored_in_seeq of this DatasourceInputV1.
        :rtype: bool
        """
        return self._stored_in_seeq

    @stored_in_seeq.setter
    def stored_in_seeq(self, stored_in_seeq):
        """
        Sets the stored_in_seeq of this DatasourceInputV1.
        True if this datasource's data is stored in Seeq; false otherwise (e.g. a remote datasource like PI).

        :param stored_in_seeq: The stored_in_seeq of this DatasourceInputV1.
        :type: bool
        """

        self._stored_in_seeq = stored_in_seeq

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
        if not isinstance(other, DatasourceInputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
