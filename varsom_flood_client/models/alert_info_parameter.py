# coding: utf-8

"""
    Flomvarsel API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1.0.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class AlertInfoParameter(object):
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
        'value_name_field': 'str',
        'value_field': 'str'
    }

    attribute_map = {
        'value_name_field': 'valueNameField',
        'value_field': 'valueField'
    }

    def __init__(self, value_name_field=None, value_field=None):  # noqa: E501
        """AlertInfoParameter - a model defined in Swagger"""  # noqa: E501
        self._value_name_field = None
        self._value_field = None
        self.discriminator = None
        if value_name_field is not None:
            self.value_name_field = value_name_field
        if value_field is not None:
            self.value_field = value_field

    @property
    def value_name_field(self):
        """Gets the value_name_field of this AlertInfoParameter.  # noqa: E501


        :return: The value_name_field of this AlertInfoParameter.  # noqa: E501
        :rtype: str
        """
        return self._value_name_field

    @value_name_field.setter
    def value_name_field(self, value_name_field):
        """Sets the value_name_field of this AlertInfoParameter.


        :param value_name_field: The value_name_field of this AlertInfoParameter.  # noqa: E501
        :type: str
        """

        self._value_name_field = value_name_field

    @property
    def value_field(self):
        """Gets the value_field of this AlertInfoParameter.  # noqa: E501


        :return: The value_field of this AlertInfoParameter.  # noqa: E501
        :rtype: str
        """
        return self._value_field

    @value_field.setter
    def value_field(self, value_field):
        """Sets the value_field of this AlertInfoParameter.


        :param value_field: The value_field of this AlertInfoParameter.  # noqa: E501
        :type: str
        """

        self._value_field = value_field

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
        if issubclass(AlertInfoParameter, dict):
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
        if not isinstance(other, AlertInfoParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
