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


class ModuleSerializer(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, device=None, parent=None, name=None, manufacturer=None, part_id=None, serial=None, discovered=None):
        """
        ModuleSerializer - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'device': 'DeviceNestedSerializer',
            'parent': 'str',
            'name': 'str',
            'manufacturer': 'ManufacturerNestedSerializer',
            'part_id': 'str',
            'serial': 'str',
            'discovered': 'bool'
        }

        self.attribute_map = {
            'id': 'id',
            'device': 'device',
            'parent': 'parent',
            'name': 'name',
            'manufacturer': 'manufacturer',
            'part_id': 'part_id',
            'serial': 'serial',
            'discovered': 'discovered'
        }

        self._id = id
        self._device = device
        self._parent = parent
        self._name = name
        self._manufacturer = manufacturer
        self._part_id = part_id
        self._serial = serial
        self._discovered = discovered


    @property
    def id(self):
        """
        Gets the id of this ModuleSerializer.


        :return: The id of this ModuleSerializer.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ModuleSerializer.


        :param id: The id of this ModuleSerializer.
        :type: int
        """

        self._id = id

    @property
    def device(self):
        """
        Gets the device of this ModuleSerializer.


        :return: The device of this ModuleSerializer.
        :rtype: DeviceNestedSerializer
        """
        return self._device

    @device.setter
    def device(self, device):
        """
        Sets the device of this ModuleSerializer.


        :param device: The device of this ModuleSerializer.
        :type: DeviceNestedSerializer
        """

        self._device = device

    @property
    def parent(self):
        """
        Gets the parent of this ModuleSerializer.


        :return: The parent of this ModuleSerializer.
        :rtype: str
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this ModuleSerializer.


        :param parent: The parent of this ModuleSerializer.
        :type: str
        """

        self._parent = parent

    @property
    def name(self):
        """
        Gets the name of this ModuleSerializer.


        :return: The name of this ModuleSerializer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ModuleSerializer.


        :param name: The name of this ModuleSerializer.
        :type: str
        """

        self._name = name

    @property
    def manufacturer(self):
        """
        Gets the manufacturer of this ModuleSerializer.


        :return: The manufacturer of this ModuleSerializer.
        :rtype: ManufacturerNestedSerializer
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        """
        Sets the manufacturer of this ModuleSerializer.


        :param manufacturer: The manufacturer of this ModuleSerializer.
        :type: ManufacturerNestedSerializer
        """

        self._manufacturer = manufacturer

    @property
    def part_id(self):
        """
        Gets the part_id of this ModuleSerializer.


        :return: The part_id of this ModuleSerializer.
        :rtype: str
        """
        return self._part_id

    @part_id.setter
    def part_id(self, part_id):
        """
        Sets the part_id of this ModuleSerializer.


        :param part_id: The part_id of this ModuleSerializer.
        :type: str
        """

        self._part_id = part_id

    @property
    def serial(self):
        """
        Gets the serial of this ModuleSerializer.


        :return: The serial of this ModuleSerializer.
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """
        Sets the serial of this ModuleSerializer.


        :param serial: The serial of this ModuleSerializer.
        :type: str
        """

        self._serial = serial

    @property
    def discovered(self):
        """
        Gets the discovered of this ModuleSerializer.


        :return: The discovered of this ModuleSerializer.
        :rtype: bool
        """
        return self._discovered

    @discovered.setter
    def discovered(self, discovered):
        """
        Sets the discovered of this ModuleSerializer.


        :param discovered: The discovered of this ModuleSerializer.
        :type: bool
        """

        self._discovered = discovered

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
