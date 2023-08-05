# coding: utf-8

"""
    Seeq REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 56.0.1-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ExportItemsOutputV1(object):
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
        'autoupdate_time_range': 'bool',
        'capsule_time': 'bool',
        'chain_view': 'bool',
        'created_at': 'str',
        'export_capsules': 'bool',
        'export_name': 'str',
        'grid_enabled': 'bool',
        'grid_size': 'str',
        'id': 'str',
        'is_archived': 'bool',
        'items': 'list[ExportItemV1]',
        'name': 'str',
        'original_timestamps_enabled': 'bool',
        'scoped_to': 'str',
        'status_message': 'str',
        'swap_in': 'str',
        'swap_out': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'autoupdate_time_range': 'autoupdateTimeRange',
        'capsule_time': 'capsuleTime',
        'chain_view': 'chainView',
        'created_at': 'createdAt',
        'export_capsules': 'exportCapsules',
        'export_name': 'exportName',
        'grid_enabled': 'gridEnabled',
        'grid_size': 'gridSize',
        'id': 'id',
        'is_archived': 'isArchived',
        'items': 'items',
        'name': 'name',
        'original_timestamps_enabled': 'originalTimestampsEnabled',
        'scoped_to': 'scopedTo',
        'status_message': 'statusMessage',
        'swap_in': 'swapIn',
        'swap_out': 'swapOut',
        'updated_at': 'updatedAt'
    }

    def __init__(self, autoupdate_time_range=False, capsule_time=False, chain_view=False, created_at=None, export_capsules=False, export_name=None, grid_enabled=False, grid_size=None, id=None, is_archived=False, items=None, name=None, original_timestamps_enabled=False, scoped_to=None, status_message=None, swap_in=None, swap_out=None, updated_at=None):
        """
        ExportItemsOutputV1 - a model defined in Swagger
        """

        self._autoupdate_time_range = None
        self._capsule_time = None
        self._chain_view = None
        self._created_at = None
        self._export_capsules = None
        self._export_name = None
        self._grid_enabled = None
        self._grid_size = None
        self._id = None
        self._is_archived = None
        self._items = None
        self._name = None
        self._original_timestamps_enabled = None
        self._scoped_to = None
        self._status_message = None
        self._swap_in = None
        self._swap_out = None
        self._updated_at = None

        if autoupdate_time_range is not None:
          self.autoupdate_time_range = autoupdate_time_range
        if capsule_time is not None:
          self.capsule_time = capsule_time
        if chain_view is not None:
          self.chain_view = chain_view
        if created_at is not None:
          self.created_at = created_at
        if export_capsules is not None:
          self.export_capsules = export_capsules
        if export_name is not None:
          self.export_name = export_name
        if grid_enabled is not None:
          self.grid_enabled = grid_enabled
        if grid_size is not None:
          self.grid_size = grid_size
        if id is not None:
          self.id = id
        if is_archived is not None:
          self.is_archived = is_archived
        if items is not None:
          self.items = items
        if name is not None:
          self.name = name
        if original_timestamps_enabled is not None:
          self.original_timestamps_enabled = original_timestamps_enabled
        if scoped_to is not None:
          self.scoped_to = scoped_to
        if status_message is not None:
          self.status_message = status_message
        if swap_in is not None:
          self.swap_in = swap_in
        if swap_out is not None:
          self.swap_out = swap_out
        if updated_at is not None:
          self.updated_at = updated_at

    @property
    def autoupdate_time_range(self):
        """
        Gets the autoupdate_time_range of this ExportItemsOutputV1.
        Boolean indicating if the time range for export will be updated to 'now' when the export is started.

        :return: The autoupdate_time_range of this ExportItemsOutputV1.
        :rtype: bool
        """
        return self._autoupdate_time_range

    @autoupdate_time_range.setter
    def autoupdate_time_range(self, autoupdate_time_range):
        """
        Sets the autoupdate_time_range of this ExportItemsOutputV1.
        Boolean indicating if the time range for export will be updated to 'now' when the export is started.

        :param autoupdate_time_range: The autoupdate_time_range of this ExportItemsOutputV1.
        :type: bool
        """

        self._autoupdate_time_range = autoupdate_time_range

    @property
    def capsule_time(self):
        """
        Gets the capsule_time of this ExportItemsOutputV1.
        True if capsule time is displayed, false otherwise.

        :return: The capsule_time of this ExportItemsOutputV1.
        :rtype: bool
        """
        return self._capsule_time

    @capsule_time.setter
    def capsule_time(self, capsule_time):
        """
        Sets the capsule_time of this ExportItemsOutputV1.
        True if capsule time is displayed, false otherwise.

        :param capsule_time: The capsule_time of this ExportItemsOutputV1.
        :type: bool
        """

        self._capsule_time = capsule_time

    @property
    def chain_view(self):
        """
        Gets the chain_view of this ExportItemsOutputV1.
        True if chain view time is displayed, false otherwise.

        :return: The chain_view of this ExportItemsOutputV1.
        :rtype: bool
        """
        return self._chain_view

    @chain_view.setter
    def chain_view(self, chain_view):
        """
        Sets the chain_view of this ExportItemsOutputV1.
        True if chain view time is displayed, false otherwise.

        :param chain_view: The chain_view of this ExportItemsOutputV1.
        :type: bool
        """

        self._chain_view = chain_view

    @property
    def created_at(self):
        """
        Gets the created_at of this ExportItemsOutputV1.
        The ISO 8601 date and time of when the export was created (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm)

        :return: The created_at of this ExportItemsOutputV1.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this ExportItemsOutputV1.
        The ISO 8601 date and time of when the export was created (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm)

        :param created_at: The created_at of this ExportItemsOutputV1.
        :type: str
        """

        self._created_at = created_at

    @property
    def export_capsules(self):
        """
        Gets the export_capsules of this ExportItemsOutputV1.
        True if the capsule table should be exported, false otherwise.

        :return: The export_capsules of this ExportItemsOutputV1.
        :rtype: bool
        """
        return self._export_capsules

    @export_capsules.setter
    def export_capsules(self, export_capsules):
        """
        Sets the export_capsules of this ExportItemsOutputV1.
        True if the capsule table should be exported, false otherwise.

        :param export_capsules: The export_capsules of this ExportItemsOutputV1.
        :type: bool
        """

        self._export_capsules = export_capsules

    @property
    def export_name(self):
        """
        Gets the export_name of this ExportItemsOutputV1.
        The desired name for the export. This name is used to create an OData endpoint for accessing the data being exported.

        :return: The export_name of this ExportItemsOutputV1.
        :rtype: str
        """
        return self._export_name

    @export_name.setter
    def export_name(self, export_name):
        """
        Sets the export_name of this ExportItemsOutputV1.
        The desired name for the export. This name is used to create an OData endpoint for accessing the data being exported.

        :param export_name: The export_name of this ExportItemsOutputV1.
        :type: str
        """

        self._export_name = export_name

    @property
    def grid_enabled(self):
        """
        Gets the grid_enabled of this ExportItemsOutputV1.
        Boolean indicating whether the data grid should be included.

        :return: The grid_enabled of this ExportItemsOutputV1.
        :rtype: bool
        """
        return self._grid_enabled

    @grid_enabled.setter
    def grid_enabled(self, grid_enabled):
        """
        Sets the grid_enabled of this ExportItemsOutputV1.
        Boolean indicating whether the data grid should be included.

        :param grid_enabled: The grid_enabled of this ExportItemsOutputV1.
        :type: bool
        """

        self._grid_enabled = grid_enabled

    @property
    def grid_size(self):
        """
        Gets the grid_size of this ExportItemsOutputV1.
        The desired sample period for the export. An automatic grid size is used when gridSize is set to 'false'.

        :return: The grid_size of this ExportItemsOutputV1.
        :rtype: str
        """
        return self._grid_size

    @grid_size.setter
    def grid_size(self, grid_size):
        """
        Sets the grid_size of this ExportItemsOutputV1.
        The desired sample period for the export. An automatic grid size is used when gridSize is set to 'false'.

        :param grid_size: The grid_size of this ExportItemsOutputV1.
        :type: str
        """

        self._grid_size = grid_size

    @property
    def id(self):
        """
        Gets the id of this ExportItemsOutputV1.
        The ID that can be used to interact with the item

        :return: The id of this ExportItemsOutputV1.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ExportItemsOutputV1.
        The ID that can be used to interact with the item

        :param id: The id of this ExportItemsOutputV1.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def is_archived(self):
        """
        Gets the is_archived of this ExportItemsOutputV1.
        Whether the item is archived.

        :return: The is_archived of this ExportItemsOutputV1.
        :rtype: bool
        """
        return self._is_archived

    @is_archived.setter
    def is_archived(self, is_archived):
        """
        Sets the is_archived of this ExportItemsOutputV1.
        Whether the item is archived.

        :param is_archived: The is_archived of this ExportItemsOutputV1.
        :type: bool
        """

        self._is_archived = is_archived

    @property
    def items(self):
        """
        Gets the items of this ExportItemsOutputV1.
        A list of items to be exported

        :return: The items of this ExportItemsOutputV1.
        :rtype: list[ExportItemV1]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this ExportItemsOutputV1.
        A list of items to be exported

        :param items: The items of this ExportItemsOutputV1.
        :type: list[ExportItemV1]
        """
        if items is None:
            raise ValueError("Invalid value for `items`, must not be `None`")

        self._items = items

    @property
    def name(self):
        """
        Gets the name of this ExportItemsOutputV1.
        The actual name for this export.

        :return: The name of this ExportItemsOutputV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ExportItemsOutputV1.
        The actual name for this export.

        :param name: The name of this ExportItemsOutputV1.
        :type: str
        """

        self._name = name

    @property
    def original_timestamps_enabled(self):
        """
        Gets the original_timestamps_enabled of this ExportItemsOutputV1.
        True if the original sample period should be used. A manual or automatic grid size may be used when false.

        :return: The original_timestamps_enabled of this ExportItemsOutputV1.
        :rtype: bool
        """
        return self._original_timestamps_enabled

    @original_timestamps_enabled.setter
    def original_timestamps_enabled(self, original_timestamps_enabled):
        """
        Sets the original_timestamps_enabled of this ExportItemsOutputV1.
        True if the original sample period should be used. A manual or automatic grid size may be used when false.

        :param original_timestamps_enabled: The original_timestamps_enabled of this ExportItemsOutputV1.
        :type: bool
        """

        self._original_timestamps_enabled = original_timestamps_enabled

    @property
    def scoped_to(self):
        """
        Gets the scoped_to of this ExportItemsOutputV1.
        The ID of the workbook to which this item is scoped. If null, the export is globally-scoped.

        :return: The scoped_to of this ExportItemsOutputV1.
        :rtype: str
        """
        return self._scoped_to

    @scoped_to.setter
    def scoped_to(self, scoped_to):
        """
        Sets the scoped_to of this ExportItemsOutputV1.
        The ID of the workbook to which this item is scoped. If null, the export is globally-scoped.

        :param scoped_to: The scoped_to of this ExportItemsOutputV1.
        :type: str
        """

        self._scoped_to = scoped_to

    @property
    def status_message(self):
        """
        Gets the status_message of this ExportItemsOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation

        :return: The status_message of this ExportItemsOutputV1.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """
        Sets the status_message of this ExportItemsOutputV1.
        A plain language status message with information about any issues that may have been encountered during an operation

        :param status_message: The status_message of this ExportItemsOutputV1.
        :type: str
        """

        self._status_message = status_message

    @property
    def swap_in(self):
        """
        Gets the swap_in of this ExportItemsOutputV1.
        The ID of an asset to swap in. Any parameters in the formula that are named the same in both the swapIn and swapOut assets will be swapped.

        :return: The swap_in of this ExportItemsOutputV1.
        :rtype: str
        """
        return self._swap_in

    @swap_in.setter
    def swap_in(self, swap_in):
        """
        Sets the swap_in of this ExportItemsOutputV1.
        The ID of an asset to swap in. Any parameters in the formula that are named the same in both the swapIn and swapOut assets will be swapped.

        :param swap_in: The swap_in of this ExportItemsOutputV1.
        :type: str
        """

        self._swap_in = swap_in

    @property
    def swap_out(self):
        """
        Gets the swap_out of this ExportItemsOutputV1.
        The ID of an asset to swap out. Any parameters in the formula that are named the same in both the swapIn and swapOut assets will be swapped.

        :return: The swap_out of this ExportItemsOutputV1.
        :rtype: str
        """
        return self._swap_out

    @swap_out.setter
    def swap_out(self, swap_out):
        """
        Sets the swap_out of this ExportItemsOutputV1.
        The ID of an asset to swap out. Any parameters in the formula that are named the same in both the swapIn and swapOut assets will be swapped.

        :param swap_out: The swap_out of this ExportItemsOutputV1.
        :type: str
        """

        self._swap_out = swap_out

    @property
    def updated_at(self):
        """
        Gets the updated_at of this ExportItemsOutputV1.
        The ISO 8601 date and time of when the export was updated/run (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm)

        :return: The updated_at of this ExportItemsOutputV1.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this ExportItemsOutputV1.
        The ISO 8601 date and time of when the export was updated/run (YYYY-MM-DDThh:mm:ss.sssssssss±hh:mm)

        :param updated_at: The updated_at of this ExportItemsOutputV1.
        :type: str
        """

        self._updated_at = updated_at

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
        if not isinstance(other, ExportItemsOutputV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
