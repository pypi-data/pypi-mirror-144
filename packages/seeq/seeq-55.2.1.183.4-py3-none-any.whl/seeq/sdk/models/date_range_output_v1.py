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


class DateRangeOutputV1(object):
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
        'archived': 'bool',
        'background': 'bool',
        'condition': 'ItemPreviewV1',
        'content': 'list[ItemPreviewV1]',
        'cron_schedule': 'list[str]',
        'date_range': 'CapsuleV1',
        'description': 'str',
        'effective_permissions': 'PermissionsV1',
        'enabled': 'bool',
        'formula': 'str',
        'id': 'str',
        'is_archived': 'bool',
        'is_redacted': 'bool',
        'name': 'str',
        'report': 'ItemPreviewV1',
        'status_message': 'str',
        'translation_key': 'str',
        'type': 'str'
    }

    attribute_map = {
        'archived': 'archived',
        'background': 'background',
        'condition': 'condition',
        'content': 'content',
        'cron_schedule': 'cronSchedule',
        'date_range': 'dateRange',
        'description': 'description',
        'effective_permissions': 'effectivePermissions',
        'enabled': 'enabled',
        'formula': 'formula',
        'id': 'id',
        'is_archived': 'isArchived',
        'is_redacted': 'isRedacted',
        'name': 'name',
        'report': 'report',
        'status_message': 'statusMessage',
        'translation_key': 'translationKey',
        'type': 'type'
    }

    def __init__(self, archived=False, background=False, condition=None, content=None, cron_schedule=None, date_range=None, description=None, effective_permissions=None, enabled=False, formula=None, id=None, is_archived=False, is_redacted=False, name=None, report=None, status_message=None, translation_key=None, type=None):
        """
        DateRangeOutputV1 - a model defined in Swagger
        """

        self._archived = None
        self._background = None
        self._condition = None
        self._content = None
        self._cron_schedule = None
        self._date_range = None
        self._description = None
        self._effective_permissions = None
        self._enabled = None
        self._formula = None
        self._id = None
        self._is_archived = None
        self._is_redacted = None
        self._name = None
        self._report = None
        self._status_message = None
        self._translation_key = None
        self._type = None

        if archived is not None:
          self.archived = archived
        if background is not None:
          self.background = background
        if condition is not None:
          self.condition = condition
        if content is not None:
          self.content = content
        if cron_schedule is not None:
          self.cron_schedule = cron_schedule
        if date_range is not None:
          self.date_range = date_range
        if description is not None:
          self.description = description
        if effective_permissions is not None:
          self.effective_permissions = effective_permissions
        if enabled is not None:
          self.enabled = enabled
        if formula is not None:
          self.formula = formula
        if id is not None:
          self.id = id
        if is_archived is not None:
          self.is_archived = is_archived
        if is_redacted is not None:
          self.is_redacted = is_redacted
        if name is not None:
          self.name = name
        if report is not None:
          self.report = report
        if status_message is not None:
          self.status_message = status_message
        if translation_key is not None:
          self.translation_key = translation_key
        if type is not None:
          self.type = type

    @property
    def archived(self):
        """
        Gets the archived of this DateRangeOutputV1.
        Whether this date range is archived

        :return: The archived of this DateRangeOutputV1.
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """
        Sets the archived of this DateRangeOutputV1.
        Whether this date range is archived

        :param archived: The archived of this DateRangeOutputV1.
        :type: bool
        """

        self._archived = archived

    @property
    def background(self):
        """
        Gets the background of this DateRangeOutputV1.
        Whether the date range, if scheduled, should continue to update if there are no subscribers (i.e. in the background)

        :return: The background of this DateRangeOutputV1.
        :rtype: bool
        """
        return self._background

    @background.setter
    def background(self, background):
        """
        Sets the background of this DateRangeOutputV1.
        Whether the date range, if scheduled, should continue to update if there are no subscribers (i.e. in the background)

        :param background: The background of this DateRangeOutputV1.
        :type: bool
        """

        self._background = background

    @property
    def condition(self):
        """
        Gets the condition of this DateRangeOutputV1.
        Condition for the formula, if present

        :return: The condition of this DateRangeOutputV1.
        :rtype: ItemPreviewV1
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """
        Sets the condition of this DateRangeOutputV1.
        Condition for the formula, if present

        :param condition: The condition of this DateRangeOutputV1.
        :type: ItemPreviewV1
        """

        self._condition = condition

    @property
    def content(self):
        """
        Gets the content of this DateRangeOutputV1.
        Content using this date range

        :return: The content of this DateRangeOutputV1.
        :rtype: list[ItemPreviewV1]
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this DateRangeOutputV1.
        Content using this date range

        :param content: The content of this DateRangeOutputV1.
        :type: list[ItemPreviewV1]
        """

        self._content = content

    @property
    def cron_schedule(self):
        """
        Gets the cron_schedule of this DateRangeOutputV1.
        Date range update period

        :return: The cron_schedule of this DateRangeOutputV1.
        :rtype: list[str]
        """
        return self._cron_schedule

    @cron_schedule.setter
    def cron_schedule(self, cron_schedule):
        """
        Sets the cron_schedule of this DateRangeOutputV1.
        Date range update period

        :param cron_schedule: The cron_schedule of this DateRangeOutputV1.
        :type: list[str]
        """

        self._cron_schedule = cron_schedule

    @property
    def date_range(self):
        """
        Gets the date_range of this DateRangeOutputV1.
        Currently evaluated date range

        :return: The date_range of this DateRangeOutputV1.
        :rtype: CapsuleV1
        """
        return self._date_range

    @date_range.setter
    def date_range(self, date_range):
        """
        Sets the date_range of this DateRangeOutputV1.
        Currently evaluated date range

        :param date_range: The date_range of this DateRangeOutputV1.
        :type: CapsuleV1
        """

        self._date_range = date_range

    @property
    def description(self):
        """
        Gets the description of this DateRangeOutputV1.
        Clarifying information or other plain language description of this item

        :return: The description of this DateRangeOutputV1.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DateRangeOutputV1.
        Clarifying information or other plain language description of this item

        :param description: The description of this DateRangeOutputV1.
        :type: str
        """

        self._description = description

    @property
    def effective_permissions(self):
        """
        Gets the effective_permissions of this DateRangeOutputV1.
        The permissions the current user has to the item.

        :return: The effective_permissions of this DateRangeOutputV1.
        :rtype: PermissionsV1
        """
        return self._effective_permissions

    @effective_permissions.setter
    def effective_permissions(self, effective_permissions):
        """
        Sets the effective_permissions of this DateRangeOutputV1.
        The permissions the current user has to the item.

        :param effective_permissions: The effective_permissions of this DateRangeOutputV1.
        :type: PermissionsV1
        """

        self._effective_permissions = effective_permissions

    @property
    def enabled(self):
        """
        Gets the enabled of this DateRangeOutputV1.
        Whether this date range is enabled to run jobs

        :return: The enabled of this DateRangeOutputV1.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this DateRangeOutputV1.
        Whether this date range is enabled to run jobs

        :param enabled: The enabled of this DateRangeOutputV1.
        :type: bool
        """

        self._enabled = enabled

    @property
    def formula(self):
        """
        Gets the formula of this DateRangeOutputV1.
        Date range formula

        :return: The formula of this DateRangeOutputV1.
        :rtype: str
        """
        return self._formula

    @formula.setter
    def formula(self, formula):
        """
        Sets the formula of this DateRangeOutputV1.
        Date range formula

        :param formula: The formula of this DateRangeOutputV1.
        :type: str
        """

        self._formula = formula

    @property
    def id(self):
        """
        Gets the id of this DateRangeOutputV1.
        The ID that can be used to interact with the item

        :return: The id of this DateRangeOutputV1.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DateRangeOutputV1.
        The ID that can be used to interact with the item

        :param id: The id of this DateRangeOutputV1.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def is_archived(self):
        """
        Gets the is_archived of this DateRangeOutputV1.
        Whether item is archived

        :return: The is_archived of this DateRangeOutputV1.
        :rtype: bool
        """
        return self._is_archived

    @is_archived.setter
    def is_archived(self, is_archived):
        """
        Sets the is_archived of this DateRangeOutputV1.
        Whether item is archived

        :param is_archived: The is_archived of this DateRangeOutputV1.
        :type: bool
        """

        self._is_archived = is_archived

    @property
    def is_redacted(self):
        """
        Gets the is_redacted of this DateRangeOutputV1.
        Whether item is redacted

        :return: The is_redacted of this DateRangeOutputV1.
        :rtype: bool
        """
        return self._is_redacted

    @is_redacted.setter
    def is_redacted(self, is_redacted):
        """
        Sets the is_redacted of this DateRangeOutputV1.
        Whether item is redacted

        :param is_redacted: The is_redacted of this DateRangeOutputV1.
        :type: bool
        """

        self._is_redacted = is_redacted

    @property
    def name(self):
        """
        Gets the name of this DateRangeOutputV1.
        The human readable name

        :return: The name of this DateRangeOutputV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DateRangeOutputV1.
        The human readable name

        :param name: The name of this DateRangeOutputV1.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def report(self):
        """
        Gets the report of this DateRangeOutputV1.
        Report, if date range is in a report

        :return: The report of this DateRangeOutputV1.
        :rtype: ItemPreviewV1
        """
        return self._report

    @report.setter
    def report(self, report):
        """
        Sets the report of this DateRangeOutputV1.
        Report, if date range is in a report

        :param report: The report of this DateRangeOutputV1.
        :type: ItemPreviewV1
        """

        self._report = report

    @property
    def status_message(self):
        """
        Gets the status_message of this DateRangeOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation

        :return: The status_message of this DateRangeOutputV1.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """
        Sets the status_message of this DateRangeOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation

        :param status_message: The status_message of this DateRangeOutputV1.
        :type: str
        """

        self._status_message = status_message

    @property
    def translation_key(self):
        """
        Gets the translation_key of this DateRangeOutputV1.
        The item's translation key, if any

        :return: The translation_key of this DateRangeOutputV1.
        :rtype: str
        """
        return self._translation_key

    @translation_key.setter
    def translation_key(self, translation_key):
        """
        Sets the translation_key of this DateRangeOutputV1.
        The item's translation key, if any

        :param translation_key: The translation_key of this DateRangeOutputV1.
        :type: str
        """

        self._translation_key = translation_key

    @property
    def type(self):
        """
        Gets the type of this DateRangeOutputV1.
        The type of the item

        :return: The type of this DateRangeOutputV1.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this DateRangeOutputV1.
        The type of the item

        :param type: The type of this DateRangeOutputV1.
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
        if not isinstance(other, DateRangeOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
