# coding: utf-8

"""
    ecs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class OperationDetailForDeleteKeyPairsOutput(object):
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
        'error': 'ErrorForDeleteKeyPairsOutput',
        'key_pair_name': 'str'
    }

    attribute_map = {
        'error': 'Error',
        'key_pair_name': 'KeyPairName'
    }

    def __init__(self, error=None, key_pair_name=None, _configuration=None):  # noqa: E501
        """OperationDetailForDeleteKeyPairsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._error = None
        self._key_pair_name = None
        self.discriminator = None

        if error is not None:
            self.error = error
        if key_pair_name is not None:
            self.key_pair_name = key_pair_name

    @property
    def error(self):
        """Gets the error of this OperationDetailForDeleteKeyPairsOutput.  # noqa: E501


        :return: The error of this OperationDetailForDeleteKeyPairsOutput.  # noqa: E501
        :rtype: ErrorForDeleteKeyPairsOutput
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this OperationDetailForDeleteKeyPairsOutput.


        :param error: The error of this OperationDetailForDeleteKeyPairsOutput.  # noqa: E501
        :type: ErrorForDeleteKeyPairsOutput
        """

        self._error = error

    @property
    def key_pair_name(self):
        """Gets the key_pair_name of this OperationDetailForDeleteKeyPairsOutput.  # noqa: E501


        :return: The key_pair_name of this OperationDetailForDeleteKeyPairsOutput.  # noqa: E501
        :rtype: str
        """
        return self._key_pair_name

    @key_pair_name.setter
    def key_pair_name(self, key_pair_name):
        """Sets the key_pair_name of this OperationDetailForDeleteKeyPairsOutput.


        :param key_pair_name: The key_pair_name of this OperationDetailForDeleteKeyPairsOutput.  # noqa: E501
        :type: str
        """

        self._key_pair_name = key_pair_name

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
        if issubclass(OperationDetailForDeleteKeyPairsOutput, dict):
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
        if not isinstance(other, OperationDetailForDeleteKeyPairsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OperationDetailForDeleteKeyPairsOutput):
            return True

        return self.to_dict() != other.to_dict()
