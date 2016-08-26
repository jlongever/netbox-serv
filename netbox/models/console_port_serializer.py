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


class ConsolePortSerializer(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, device=None, name=None, cs_port=None, connection_status=None):
        """
        ConsolePortSerializer - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'device': 'DeviceNestedSerializer',
            'name': 'str',
            'cs_port': 'ConsoleServerPortNestedSerializer',
            'connection_status': 'bool'
        }

        self.attribute_map = {
            'id': 'id',
            'device': 'device',
            'name': 'name',
            'cs_port': 'cs_port',
            'connection_status': 'connection_status'
        }

        self._id = id
        self._device = device
        self._name = name
        self._cs_port = cs_port
        self._connection_status = connection_status


    @property
    def id(self):
        """
        Gets the id of this ConsolePortSerializer.


        :return: The id of this ConsolePortSerializer.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ConsolePortSerializer.


        :param id: The id of this ConsolePortSerializer.
        :type: int
        """

        self._id = id

    @property
    def device(self):
        """
        Gets the device of this ConsolePortSerializer.


        :return: The device of this ConsolePortSerializer.
        :rtype: DeviceNestedSerializer
        """
        return self._device

    @device.setter
    def device(self, device):
        """
        Sets the device of this ConsolePortSerializer.


        :param device: The device of this ConsolePortSerializer.
        :type: DeviceNestedSerializer
        """

        self._device = device

    @property
    def name(self):
        """
        Gets the name of this ConsolePortSerializer.


        :return: The name of this ConsolePortSerializer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ConsolePortSerializer.


        :param name: The name of this ConsolePortSerializer.
        :type: str
        """

        self._name = name

    @property
    def cs_port(self):
        """
        Gets the cs_port of this ConsolePortSerializer.


        :return: The cs_port of this ConsolePortSerializer.
        :rtype: ConsoleServerPortNestedSerializer
        """
        return self._cs_port

    @cs_port.setter
    def cs_port(self, cs_port):
        """
        Sets the cs_port of this ConsolePortSerializer.


        :param cs_port: The cs_port of this ConsolePortSerializer.
        :type: ConsoleServerPortNestedSerializer
        """

        self._cs_port = cs_port

    @property
    def connection_status(self):
        """
        Gets the connection_status of this ConsolePortSerializer.


        :return: The connection_status of this ConsolePortSerializer.
        :rtype: bool
        """
        return self._connection_status

    @connection_status.setter
    def connection_status(self, connection_status):
        """
        Sets the connection_status of this ConsolePortSerializer.


        :param connection_status: The connection_status of this ConsolePortSerializer.
        :type: bool
        """

        self._connection_status = connection_status

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
