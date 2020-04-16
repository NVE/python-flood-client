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


class County(object):
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
        'id': 'str',
        'name': 'str',
        'municipality_list': 'list[Municipality]',
        'highest_activity_level': 'str'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'municipality_list': 'MunicipalityList',
        'highest_activity_level': 'HighestActivityLevel'
    }

    def __init__(self, id=None, name=None, municipality_list=None, highest_activity_level=None):  # noqa: E501
        """County - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._municipality_list = None
        self._highest_activity_level = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if municipality_list is not None:
            self.municipality_list = municipality_list
        if highest_activity_level is not None:
            self.highest_activity_level = highest_activity_level

    @property
    def id(self):
        """Gets the id of this County.  # noqa: E501


        :return: The id of this County.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this County.


        :param id: The id of this County.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this County.  # noqa: E501


        :return: The name of this County.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this County.


        :param name: The name of this County.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def municipality_list(self):
        """Gets the municipality_list of this County.  # noqa: E501


        :return: The municipality_list of this County.  # noqa: E501
        :rtype: list[Municipality]
        """
        return self._municipality_list

    @municipality_list.setter
    def municipality_list(self, municipality_list):
        """Sets the municipality_list of this County.


        :param municipality_list: The municipality_list of this County.  # noqa: E501
        :type: list[Municipality]
        """

        self._municipality_list = municipality_list

    @property
    def highest_activity_level(self):
        """Gets the highest_activity_level of this County.  # noqa: E501


        :return: The highest_activity_level of this County.  # noqa: E501
        :rtype: str
        """
        return self._highest_activity_level

    @highest_activity_level.setter
    def highest_activity_level(self, highest_activity_level):
        """Sets the highest_activity_level of this County.


        :param highest_activity_level: The highest_activity_level of this County.  # noqa: E501
        :type: str
        """

        self._highest_activity_level = highest_activity_level

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
        if issubclass(County, dict):
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
        if not isinstance(other, County):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
