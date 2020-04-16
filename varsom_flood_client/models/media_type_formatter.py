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


class MediaTypeFormatter(object):
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
        'supported_media_types': 'list[MediaTypeHeaderValue]',
        'supported_encodings': 'list[Encoding]',
        'media_type_mappings': 'list[MediaTypeMapping]',
        'required_member_selector': 'IRequiredMemberSelector'
    }

    attribute_map = {
        'supported_media_types': 'SupportedMediaTypes',
        'supported_encodings': 'SupportedEncodings',
        'media_type_mappings': 'MediaTypeMappings',
        'required_member_selector': 'RequiredMemberSelector'
    }

    def __init__(self, supported_media_types=None, supported_encodings=None, media_type_mappings=None, required_member_selector=None):  # noqa: E501
        """MediaTypeFormatter - a model defined in Swagger"""  # noqa: E501
        self._supported_media_types = None
        self._supported_encodings = None
        self._media_type_mappings = None
        self._required_member_selector = None
        self.discriminator = None
        if supported_media_types is not None:
            self.supported_media_types = supported_media_types
        if supported_encodings is not None:
            self.supported_encodings = supported_encodings
        if media_type_mappings is not None:
            self.media_type_mappings = media_type_mappings
        if required_member_selector is not None:
            self.required_member_selector = required_member_selector

    @property
    def supported_media_types(self):
        """Gets the supported_media_types of this MediaTypeFormatter.  # noqa: E501


        :return: The supported_media_types of this MediaTypeFormatter.  # noqa: E501
        :rtype: list[MediaTypeHeaderValue]
        """
        return self._supported_media_types

    @supported_media_types.setter
    def supported_media_types(self, supported_media_types):
        """Sets the supported_media_types of this MediaTypeFormatter.


        :param supported_media_types: The supported_media_types of this MediaTypeFormatter.  # noqa: E501
        :type: list[MediaTypeHeaderValue]
        """

        self._supported_media_types = supported_media_types

    @property
    def supported_encodings(self):
        """Gets the supported_encodings of this MediaTypeFormatter.  # noqa: E501


        :return: The supported_encodings of this MediaTypeFormatter.  # noqa: E501
        :rtype: list[Encoding]
        """
        return self._supported_encodings

    @supported_encodings.setter
    def supported_encodings(self, supported_encodings):
        """Sets the supported_encodings of this MediaTypeFormatter.


        :param supported_encodings: The supported_encodings of this MediaTypeFormatter.  # noqa: E501
        :type: list[Encoding]
        """

        self._supported_encodings = supported_encodings

    @property
    def media_type_mappings(self):
        """Gets the media_type_mappings of this MediaTypeFormatter.  # noqa: E501


        :return: The media_type_mappings of this MediaTypeFormatter.  # noqa: E501
        :rtype: list[MediaTypeMapping]
        """
        return self._media_type_mappings

    @media_type_mappings.setter
    def media_type_mappings(self, media_type_mappings):
        """Sets the media_type_mappings of this MediaTypeFormatter.


        :param media_type_mappings: The media_type_mappings of this MediaTypeFormatter.  # noqa: E501
        :type: list[MediaTypeMapping]
        """

        self._media_type_mappings = media_type_mappings

    @property
    def required_member_selector(self):
        """Gets the required_member_selector of this MediaTypeFormatter.  # noqa: E501


        :return: The required_member_selector of this MediaTypeFormatter.  # noqa: E501
        :rtype: IRequiredMemberSelector
        """
        return self._required_member_selector

    @required_member_selector.setter
    def required_member_selector(self, required_member_selector):
        """Sets the required_member_selector of this MediaTypeFormatter.


        :param required_member_selector: The required_member_selector of this MediaTypeFormatter.  # noqa: E501
        :type: IRequiredMemberSelector
        """

        self._required_member_selector = required_member_selector

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
        if issubclass(MediaTypeFormatter, dict):
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
        if not isinstance(other, MediaTypeFormatter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other