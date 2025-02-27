# coding: utf-8

"""
    auto_scaling

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ScalingGroupForDescribeScalingGroupsOutput(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'active_scaling_configuration_id': 'str',
        'created_at': 'str',
        'db_instance_ids': 'list[str]',
        'default_cooldown': 'int',
        'desire_instance_number': 'int',
        'instance_terminate_policy': 'str',
        'lifecycle_state': 'str',
        'max_instance_number': 'int',
        'min_instance_number': 'int',
        'multi_az_policy': 'str',
        'scaling_group_id': 'str',
        'scaling_group_name': 'str',
        'server_group_attributes': 'list[ServerGroupAttributeForDescribeScalingGroupsOutput]',
        'subnet_ids': 'list[str]',
        'total_instance_count': 'int',
        'updated_at': 'str',
        'vpc_id': 'str'
    }

    attribute_map = {
        'active_scaling_configuration_id': 'ActiveScalingConfigurationId',
        'created_at': 'CreatedAt',
        'db_instance_ids': 'DBInstanceIds',
        'default_cooldown': 'DefaultCooldown',
        'desire_instance_number': 'DesireInstanceNumber',
        'instance_terminate_policy': 'InstanceTerminatePolicy',
        'lifecycle_state': 'LifecycleState',
        'max_instance_number': 'MaxInstanceNumber',
        'min_instance_number': 'MinInstanceNumber',
        'multi_az_policy': 'MultiAZPolicy',
        'scaling_group_id': 'ScalingGroupId',
        'scaling_group_name': 'ScalingGroupName',
        'server_group_attributes': 'ServerGroupAttributes',
        'subnet_ids': 'SubnetIds',
        'total_instance_count': 'TotalInstanceCount',
        'updated_at': 'UpdatedAt',
        'vpc_id': 'VpcId'
    }

    def __init__(self, active_scaling_configuration_id=None, created_at=None, db_instance_ids=None, default_cooldown=None, desire_instance_number=None, instance_terminate_policy=None, lifecycle_state=None, max_instance_number=None, min_instance_number=None, multi_az_policy=None, scaling_group_id=None, scaling_group_name=None, server_group_attributes=None, subnet_ids=None, total_instance_count=None, updated_at=None, vpc_id=None, _configuration=None):  # noqa: E501
        """ScalingGroupForDescribeScalingGroupsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._active_scaling_configuration_id = None
        self._created_at = None
        self._db_instance_ids = None
        self._default_cooldown = None
        self._desire_instance_number = None
        self._instance_terminate_policy = None
        self._lifecycle_state = None
        self._max_instance_number = None
        self._min_instance_number = None
        self._multi_az_policy = None
        self._scaling_group_id = None
        self._scaling_group_name = None
        self._server_group_attributes = None
        self._subnet_ids = None
        self._total_instance_count = None
        self._updated_at = None
        self._vpc_id = None
        self.discriminator = None

        if active_scaling_configuration_id is not None:
            self.active_scaling_configuration_id = active_scaling_configuration_id
        if created_at is not None:
            self.created_at = created_at
        if db_instance_ids is not None:
            self.db_instance_ids = db_instance_ids
        if default_cooldown is not None:
            self.default_cooldown = default_cooldown
        if desire_instance_number is not None:
            self.desire_instance_number = desire_instance_number
        if instance_terminate_policy is not None:
            self.instance_terminate_policy = instance_terminate_policy
        if lifecycle_state is not None:
            self.lifecycle_state = lifecycle_state
        if max_instance_number is not None:
            self.max_instance_number = max_instance_number
        if min_instance_number is not None:
            self.min_instance_number = min_instance_number
        if multi_az_policy is not None:
            self.multi_az_policy = multi_az_policy
        if scaling_group_id is not None:
            self.scaling_group_id = scaling_group_id
        if scaling_group_name is not None:
            self.scaling_group_name = scaling_group_name
        if server_group_attributes is not None:
            self.server_group_attributes = server_group_attributes
        if subnet_ids is not None:
            self.subnet_ids = subnet_ids
        if total_instance_count is not None:
            self.total_instance_count = total_instance_count
        if updated_at is not None:
            self.updated_at = updated_at
        if vpc_id is not None:
            self.vpc_id = vpc_id

    @property
    def active_scaling_configuration_id(self):
        """Gets the active_scaling_configuration_id of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501


        :return: The active_scaling_configuration_id of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._active_scaling_configuration_id

    @active_scaling_configuration_id.setter
    def active_scaling_configuration_id(self, active_scaling_configuration_id):
        """Sets the active_scaling_configuration_id of this ScalingGroupForDescribeScalingGroupsOutput.


        :param active_scaling_configuration_id: The active_scaling_configuration_id of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501
        :type: str
        """

        self._active_scaling_configuration_id = active_scaling_configuration_id

    @property
    def created_at(self):
        """Gets the created_at of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501


        :return: The created_at of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ScalingGroupForDescribeScalingGroupsOutput.


        :param created_at: The created_at of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def db_instance_ids(self):
        """Gets the db_instance_ids of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501


        :return: The db_instance_ids of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._db_instance_ids

    @db_instance_ids.setter
    def db_instance_ids(self, db_instance_ids):
        """Sets the db_instance_ids of this ScalingGroupForDescribeScalingGroupsOutput.


        :param db_instance_ids: The db_instance_ids of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501
        :type: list[str]
        """

        self._db_instance_ids = db_instance_ids

    @property
    def default_cooldown(self):
        """Gets the default_cooldown of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501


        :return: The default_cooldown of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501
        :rtype: int
        """
        return self._default_cooldown

    @default_cooldown.setter
    def default_cooldown(self, default_cooldown):
        """Sets the default_cooldown of this ScalingGroupForDescribeScalingGroupsOutput.


        :param default_cooldown: The default_cooldown of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501
        :type: int
        """

        self._default_cooldown = default_cooldown

    @property
    def desire_instance_number(self):
        """Gets the desire_instance_number of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501


        :return: The desire_instance_number of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501
        :rtype: int
        """
        return self._desire_instance_number

    @desire_instance_number.setter
    def desire_instance_number(self, desire_instance_number):
        """Sets the desire_instance_number of this ScalingGroupForDescribeScalingGroupsOutput.


        :param desire_instance_number: The desire_instance_number of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501
        :type: int
        """

        self._desire_instance_number = desire_instance_number

    @property
    def instance_terminate_policy(self):
        """Gets the instance_terminate_policy of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501


        :return: The instance_terminate_policy of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_terminate_policy

    @instance_terminate_policy.setter
    def instance_terminate_policy(self, instance_terminate_policy):
        """Sets the instance_terminate_policy of this ScalingGroupForDescribeScalingGroupsOutput.


        :param instance_terminate_policy: The instance_terminate_policy of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501
        :type: str
        """

        self._instance_terminate_policy = instance_terminate_policy

    @property
    def lifecycle_state(self):
        """Gets the lifecycle_state of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501


        :return: The lifecycle_state of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """Sets the lifecycle_state of this ScalingGroupForDescribeScalingGroupsOutput.


        :param lifecycle_state: The lifecycle_state of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501
        :type: str
        """

        self._lifecycle_state = lifecycle_state

    @property
    def max_instance_number(self):
        """Gets the max_instance_number of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501


        :return: The max_instance_number of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501
        :rtype: int
        """
        return self._max_instance_number

    @max_instance_number.setter
    def max_instance_number(self, max_instance_number):
        """Sets the max_instance_number of this ScalingGroupForDescribeScalingGroupsOutput.


        :param max_instance_number: The max_instance_number of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501
        :type: int
        """

        self._max_instance_number = max_instance_number

    @property
    def min_instance_number(self):
        """Gets the min_instance_number of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501


        :return: The min_instance_number of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501
        :rtype: int
        """
        return self._min_instance_number

    @min_instance_number.setter
    def min_instance_number(self, min_instance_number):
        """Sets the min_instance_number of this ScalingGroupForDescribeScalingGroupsOutput.


        :param min_instance_number: The min_instance_number of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501
        :type: int
        """

        self._min_instance_number = min_instance_number

    @property
    def multi_az_policy(self):
        """Gets the multi_az_policy of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501


        :return: The multi_az_policy of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._multi_az_policy

    @multi_az_policy.setter
    def multi_az_policy(self, multi_az_policy):
        """Sets the multi_az_policy of this ScalingGroupForDescribeScalingGroupsOutput.


        :param multi_az_policy: The multi_az_policy of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501
        :type: str
        """

        self._multi_az_policy = multi_az_policy

    @property
    def scaling_group_id(self):
        """Gets the scaling_group_id of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501


        :return: The scaling_group_id of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._scaling_group_id

    @scaling_group_id.setter
    def scaling_group_id(self, scaling_group_id):
        """Sets the scaling_group_id of this ScalingGroupForDescribeScalingGroupsOutput.


        :param scaling_group_id: The scaling_group_id of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501
        :type: str
        """

        self._scaling_group_id = scaling_group_id

    @property
    def scaling_group_name(self):
        """Gets the scaling_group_name of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501


        :return: The scaling_group_name of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._scaling_group_name

    @scaling_group_name.setter
    def scaling_group_name(self, scaling_group_name):
        """Sets the scaling_group_name of this ScalingGroupForDescribeScalingGroupsOutput.


        :param scaling_group_name: The scaling_group_name of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501
        :type: str
        """

        self._scaling_group_name = scaling_group_name

    @property
    def server_group_attributes(self):
        """Gets the server_group_attributes of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501


        :return: The server_group_attributes of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501
        :rtype: list[ServerGroupAttributeForDescribeScalingGroupsOutput]
        """
        return self._server_group_attributes

    @server_group_attributes.setter
    def server_group_attributes(self, server_group_attributes):
        """Sets the server_group_attributes of this ScalingGroupForDescribeScalingGroupsOutput.


        :param server_group_attributes: The server_group_attributes of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501
        :type: list[ServerGroupAttributeForDescribeScalingGroupsOutput]
        """

        self._server_group_attributes = server_group_attributes

    @property
    def subnet_ids(self):
        """Gets the subnet_ids of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501


        :return: The subnet_ids of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._subnet_ids

    @subnet_ids.setter
    def subnet_ids(self, subnet_ids):
        """Sets the subnet_ids of this ScalingGroupForDescribeScalingGroupsOutput.


        :param subnet_ids: The subnet_ids of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501
        :type: list[str]
        """

        self._subnet_ids = subnet_ids

    @property
    def total_instance_count(self):
        """Gets the total_instance_count of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501


        :return: The total_instance_count of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501
        :rtype: int
        """
        return self._total_instance_count

    @total_instance_count.setter
    def total_instance_count(self, total_instance_count):
        """Sets the total_instance_count of this ScalingGroupForDescribeScalingGroupsOutput.


        :param total_instance_count: The total_instance_count of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501
        :type: int
        """

        self._total_instance_count = total_instance_count

    @property
    def updated_at(self):
        """Gets the updated_at of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501


        :return: The updated_at of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ScalingGroupForDescribeScalingGroupsOutput.


        :param updated_at: The updated_at of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501


        :return: The vpc_id of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ScalingGroupForDescribeScalingGroupsOutput.


        :param vpc_id: The vpc_id of this ScalingGroupForDescribeScalingGroupsOutput.  # noqa: E501
        :type: str
        """

        self._vpc_id = vpc_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(ScalingGroupForDescribeScalingGroupsOutput, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ScalingGroupForDescribeScalingGroupsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScalingGroupForDescribeScalingGroupsOutput):
            return True

        return self.to_dict() != other.to_dict()
