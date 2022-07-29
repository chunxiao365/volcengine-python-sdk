# coding: utf-8

"""
    vpc

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class CreateSubnetRequest(object):
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
        'cidr_block': 'str',
        'client_token': 'str',
        'description': 'str',
        'subnet_name': 'str',
        'vpc_id': 'str',
        'zone_id': 'str'
    }

    attribute_map = {
        'cidr_block': 'CidrBlock',
        'client_token': 'ClientToken',
        'description': 'Description',
        'subnet_name': 'SubnetName',
        'vpc_id': 'VpcId',
        'zone_id': 'ZoneId'
    }

    def __init__(self, cidr_block=None, client_token=None, description=None, subnet_name=None, vpc_id=None, zone_id=None, _configuration=None):  # noqa: E501
        """CreateSubnetRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cidr_block = None
        self._client_token = None
        self._description = None
        self._subnet_name = None
        self._vpc_id = None
        self._zone_id = None
        self.discriminator = None

        self.cidr_block = cidr_block
        if client_token is not None:
            self.client_token = client_token
        if description is not None:
            self.description = description
        if subnet_name is not None:
            self.subnet_name = subnet_name
        self.vpc_id = vpc_id
        self.zone_id = zone_id

    @property
    def cidr_block(self):
        """Gets the cidr_block of this CreateSubnetRequest.  # noqa: E501


        :return: The cidr_block of this CreateSubnetRequest.  # noqa: E501
        :rtype: str
        """
        return self._cidr_block

    @cidr_block.setter
    def cidr_block(self, cidr_block):
        """Sets the cidr_block of this CreateSubnetRequest.


        :param cidr_block: The cidr_block of this CreateSubnetRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and cidr_block is None:
            raise ValueError("Invalid value for `cidr_block`, must not be `None`")  # noqa: E501

        self._cidr_block = cidr_block

    @property
    def client_token(self):
        """Gets the client_token of this CreateSubnetRequest.  # noqa: E501


        :return: The client_token of this CreateSubnetRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_token

    @client_token.setter
    def client_token(self, client_token):
        """Sets the client_token of this CreateSubnetRequest.


        :param client_token: The client_token of this CreateSubnetRequest.  # noqa: E501
        :type: str
        """

        self._client_token = client_token

    @property
    def description(self):
        """Gets the description of this CreateSubnetRequest.  # noqa: E501


        :return: The description of this CreateSubnetRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateSubnetRequest.


        :param description: The description of this CreateSubnetRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                description is not None and len(description) > 255):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                description is not None and len(description) < 1):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501

        self._description = description

    @property
    def subnet_name(self):
        """Gets the subnet_name of this CreateSubnetRequest.  # noqa: E501


        :return: The subnet_name of this CreateSubnetRequest.  # noqa: E501
        :rtype: str
        """
        return self._subnet_name

    @subnet_name.setter
    def subnet_name(self, subnet_name):
        """Sets the subnet_name of this CreateSubnetRequest.


        :param subnet_name: The subnet_name of this CreateSubnetRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                subnet_name is not None and len(subnet_name) > 128):
            raise ValueError("Invalid value for `subnet_name`, length must be less than or equal to `128`")  # noqa: E501
        if (self._configuration.client_side_validation and
                subnet_name is not None and len(subnet_name) < 1):
            raise ValueError("Invalid value for `subnet_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._subnet_name = subnet_name

    @property
    def vpc_id(self):
        """Gets the vpc_id of this CreateSubnetRequest.  # noqa: E501


        :return: The vpc_id of this CreateSubnetRequest.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this CreateSubnetRequest.


        :param vpc_id: The vpc_id of this CreateSubnetRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and vpc_id is None:
            raise ValueError("Invalid value for `vpc_id`, must not be `None`")  # noqa: E501

        self._vpc_id = vpc_id

    @property
    def zone_id(self):
        """Gets the zone_id of this CreateSubnetRequest.  # noqa: E501


        :return: The zone_id of this CreateSubnetRequest.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this CreateSubnetRequest.


        :param zone_id: The zone_id of this CreateSubnetRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and zone_id is None:
            raise ValueError("Invalid value for `zone_id`, must not be `None`")  # noqa: E501

        self._zone_id = zone_id

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
        if issubclass(CreateSubnetRequest, dict):
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
        if not isinstance(other, CreateSubnetRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateSubnetRequest):
            return True

        return self.to_dict() != other.to_dict()
