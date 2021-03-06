# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class DeviceTypeNestedSerializer(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, manufacturer=None, model=None, slug=None):
        """
        DeviceTypeNestedSerializer - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'manufacturer': 'ManufacturerNestedSerializer',
            'model': 'str',
            'slug': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'manufacturer': 'manufacturer',
            'model': 'model',
            'slug': 'slug'
        }

        self._id = id
        self._manufacturer = manufacturer
        self._model = model
        self._slug = slug


    @property
    def id(self):
        """
        Gets the id of this DeviceTypeNestedSerializer.


        :return: The id of this DeviceTypeNestedSerializer.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DeviceTypeNestedSerializer.


        :param id: The id of this DeviceTypeNestedSerializer.
        :type: int
        """

        self._id = id

    @property
    def manufacturer(self):
        """
        Gets the manufacturer of this DeviceTypeNestedSerializer.


        :return: The manufacturer of this DeviceTypeNestedSerializer.
        :rtype: ManufacturerNestedSerializer
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        """
        Sets the manufacturer of this DeviceTypeNestedSerializer.


        :param manufacturer: The manufacturer of this DeviceTypeNestedSerializer.
        :type: ManufacturerNestedSerializer
        """

        self._manufacturer = manufacturer

    @property
    def model(self):
        """
        Gets the model of this DeviceTypeNestedSerializer.


        :return: The model of this DeviceTypeNestedSerializer.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this DeviceTypeNestedSerializer.


        :param model: The model of this DeviceTypeNestedSerializer.
        :type: str
        """

        self._model = model

    @property
    def slug(self):
        """
        Gets the slug of this DeviceTypeNestedSerializer.


        :return: The slug of this DeviceTypeNestedSerializer.
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """
        Sets the slug of this DeviceTypeNestedSerializer.


        :param slug: The slug of this DeviceTypeNestedSerializer.
        :type: str
        """

        self._slug = slug

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
