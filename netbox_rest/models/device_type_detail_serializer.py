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


class DeviceTypeDetailSerializer(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, manufacturer=None, model=None, slug=None, part_number=None, u_height=None, is_full_depth=None, is_console_server=None, is_pdu=None, is_network_device=None, console_port_templates=None, cs_port_templates=None, power_port_templates=None, power_outlet_templates=None, interface_templates=None):
        """
        DeviceTypeDetailSerializer - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'manufacturer': 'ManufacturerNestedSerializer',
            'model': 'str',
            'slug': 'str',
            'part_number': 'str',
            'u_height': 'int',
            'is_full_depth': 'bool',
            'is_console_server': 'bool',
            'is_pdu': 'bool',
            'is_network_device': 'bool',
            'console_port_templates': 'list[ConsolePortTemplateNestedSerializer]',
            'cs_port_templates': 'list[ConsoleServerPortTemplateNestedSerializer]',
            'power_port_templates': 'list[PowerPortTemplateNestedSerializer]',
            'power_outlet_templates': 'list[PowerPortTemplateNestedSerializer]',
            'interface_templates': 'list[InterfaceTemplateNestedSerializer]'
        }

        self.attribute_map = {
            'id': 'id',
            'manufacturer': 'manufacturer',
            'model': 'model',
            'slug': 'slug',
            'part_number': 'part_number',
            'u_height': 'u_height',
            'is_full_depth': 'is_full_depth',
            'is_console_server': 'is_console_server',
            'is_pdu': 'is_pdu',
            'is_network_device': 'is_network_device',
            'console_port_templates': 'console_port_templates',
            'cs_port_templates': 'cs_port_templates',
            'power_port_templates': 'power_port_templates',
            'power_outlet_templates': 'power_outlet_templates',
            'interface_templates': 'interface_templates'
        }

        self._id = id
        self._manufacturer = manufacturer
        self._model = model
        self._slug = slug
        self._part_number = part_number
        self._u_height = u_height
        self._is_full_depth = is_full_depth
        self._is_console_server = is_console_server
        self._is_pdu = is_pdu
        self._is_network_device = is_network_device
        self._console_port_templates = console_port_templates
        self._cs_port_templates = cs_port_templates
        self._power_port_templates = power_port_templates
        self._power_outlet_templates = power_outlet_templates
        self._interface_templates = interface_templates


    @property
    def id(self):
        """
        Gets the id of this DeviceTypeDetailSerializer.


        :return: The id of this DeviceTypeDetailSerializer.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DeviceTypeDetailSerializer.


        :param id: The id of this DeviceTypeDetailSerializer.
        :type: int
        """

        self._id = id

    @property
    def manufacturer(self):
        """
        Gets the manufacturer of this DeviceTypeDetailSerializer.


        :return: The manufacturer of this DeviceTypeDetailSerializer.
        :rtype: ManufacturerNestedSerializer
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        """
        Sets the manufacturer of this DeviceTypeDetailSerializer.


        :param manufacturer: The manufacturer of this DeviceTypeDetailSerializer.
        :type: ManufacturerNestedSerializer
        """

        self._manufacturer = manufacturer

    @property
    def model(self):
        """
        Gets the model of this DeviceTypeDetailSerializer.


        :return: The model of this DeviceTypeDetailSerializer.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this DeviceTypeDetailSerializer.


        :param model: The model of this DeviceTypeDetailSerializer.
        :type: str
        """

        self._model = model

    @property
    def slug(self):
        """
        Gets the slug of this DeviceTypeDetailSerializer.


        :return: The slug of this DeviceTypeDetailSerializer.
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """
        Sets the slug of this DeviceTypeDetailSerializer.


        :param slug: The slug of this DeviceTypeDetailSerializer.
        :type: str
        """

        self._slug = slug

    @property
    def part_number(self):
        """
        Gets the part_number of this DeviceTypeDetailSerializer.
        Discrete part number (optional)

        :return: The part_number of this DeviceTypeDetailSerializer.
        :rtype: str
        """
        return self._part_number

    @part_number.setter
    def part_number(self, part_number):
        """
        Sets the part_number of this DeviceTypeDetailSerializer.
        Discrete part number (optional)

        :param part_number: The part_number of this DeviceTypeDetailSerializer.
        :type: str
        """

        self._part_number = part_number

    @property
    def u_height(self):
        """
        Gets the u_height of this DeviceTypeDetailSerializer.


        :return: The u_height of this DeviceTypeDetailSerializer.
        :rtype: int
        """
        return self._u_height

    @u_height.setter
    def u_height(self, u_height):
        """
        Sets the u_height of this DeviceTypeDetailSerializer.


        :param u_height: The u_height of this DeviceTypeDetailSerializer.
        :type: int
        """

        if not u_height:
            raise ValueError("Invalid value for `u_height`, must not be `None`")
        if u_height > 32767.0:
            raise ValueError("Invalid value for `u_height`, must be a value less than or equal to `32767.0`")
        if u_height < 0.0:
            raise ValueError("Invalid value for `u_height`, must be a value greater than or equal to `0.0`")

        self._u_height = u_height

    @property
    def is_full_depth(self):
        """
        Gets the is_full_depth of this DeviceTypeDetailSerializer.
        Device consumes both front and rear rack faces

        :return: The is_full_depth of this DeviceTypeDetailSerializer.
        :rtype: bool
        """
        return self._is_full_depth

    @is_full_depth.setter
    def is_full_depth(self, is_full_depth):
        """
        Sets the is_full_depth of this DeviceTypeDetailSerializer.
        Device consumes both front and rear rack faces

        :param is_full_depth: The is_full_depth of this DeviceTypeDetailSerializer.
        :type: bool
        """

        self._is_full_depth = is_full_depth

    @property
    def is_console_server(self):
        """
        Gets the is_console_server of this DeviceTypeDetailSerializer.
        This type of device has console server ports

        :return: The is_console_server of this DeviceTypeDetailSerializer.
        :rtype: bool
        """
        return self._is_console_server

    @is_console_server.setter
    def is_console_server(self, is_console_server):
        """
        Sets the is_console_server of this DeviceTypeDetailSerializer.
        This type of device has console server ports

        :param is_console_server: The is_console_server of this DeviceTypeDetailSerializer.
        :type: bool
        """

        self._is_console_server = is_console_server

    @property
    def is_pdu(self):
        """
        Gets the is_pdu of this DeviceTypeDetailSerializer.
        This type of device has power outlets

        :return: The is_pdu of this DeviceTypeDetailSerializer.
        :rtype: bool
        """
        return self._is_pdu

    @is_pdu.setter
    def is_pdu(self, is_pdu):
        """
        Sets the is_pdu of this DeviceTypeDetailSerializer.
        This type of device has power outlets

        :param is_pdu: The is_pdu of this DeviceTypeDetailSerializer.
        :type: bool
        """

        self._is_pdu = is_pdu

    @property
    def is_network_device(self):
        """
        Gets the is_network_device of this DeviceTypeDetailSerializer.
        This type of device has network interfaces

        :return: The is_network_device of this DeviceTypeDetailSerializer.
        :rtype: bool
        """
        return self._is_network_device

    @is_network_device.setter
    def is_network_device(self, is_network_device):
        """
        Sets the is_network_device of this DeviceTypeDetailSerializer.
        This type of device has network interfaces

        :param is_network_device: The is_network_device of this DeviceTypeDetailSerializer.
        :type: bool
        """

        self._is_network_device = is_network_device

    @property
    def console_port_templates(self):
        """
        Gets the console_port_templates of this DeviceTypeDetailSerializer.


        :return: The console_port_templates of this DeviceTypeDetailSerializer.
        :rtype: list[ConsolePortTemplateNestedSerializer]
        """
        return self._console_port_templates

    @console_port_templates.setter
    def console_port_templates(self, console_port_templates):
        """
        Sets the console_port_templates of this DeviceTypeDetailSerializer.


        :param console_port_templates: The console_port_templates of this DeviceTypeDetailSerializer.
        :type: list[ConsolePortTemplateNestedSerializer]
        """

        self._console_port_templates = console_port_templates

    @property
    def cs_port_templates(self):
        """
        Gets the cs_port_templates of this DeviceTypeDetailSerializer.


        :return: The cs_port_templates of this DeviceTypeDetailSerializer.
        :rtype: list[ConsoleServerPortTemplateNestedSerializer]
        """
        return self._cs_port_templates

    @cs_port_templates.setter
    def cs_port_templates(self, cs_port_templates):
        """
        Sets the cs_port_templates of this DeviceTypeDetailSerializer.


        :param cs_port_templates: The cs_port_templates of this DeviceTypeDetailSerializer.
        :type: list[ConsoleServerPortTemplateNestedSerializer]
        """

        self._cs_port_templates = cs_port_templates

    @property
    def power_port_templates(self):
        """
        Gets the power_port_templates of this DeviceTypeDetailSerializer.


        :return: The power_port_templates of this DeviceTypeDetailSerializer.
        :rtype: list[PowerPortTemplateNestedSerializer]
        """
        return self._power_port_templates

    @power_port_templates.setter
    def power_port_templates(self, power_port_templates):
        """
        Sets the power_port_templates of this DeviceTypeDetailSerializer.


        :param power_port_templates: The power_port_templates of this DeviceTypeDetailSerializer.
        :type: list[PowerPortTemplateNestedSerializer]
        """

        self._power_port_templates = power_port_templates

    @property
    def power_outlet_templates(self):
        """
        Gets the power_outlet_templates of this DeviceTypeDetailSerializer.


        :return: The power_outlet_templates of this DeviceTypeDetailSerializer.
        :rtype: list[PowerPortTemplateNestedSerializer]
        """
        return self._power_outlet_templates

    @power_outlet_templates.setter
    def power_outlet_templates(self, power_outlet_templates):
        """
        Sets the power_outlet_templates of this DeviceTypeDetailSerializer.


        :param power_outlet_templates: The power_outlet_templates of this DeviceTypeDetailSerializer.
        :type: list[PowerPortTemplateNestedSerializer]
        """

        self._power_outlet_templates = power_outlet_templates

    @property
    def interface_templates(self):
        """
        Gets the interface_templates of this DeviceTypeDetailSerializer.


        :return: The interface_templates of this DeviceTypeDetailSerializer.
        :rtype: list[InterfaceTemplateNestedSerializer]
        """
        return self._interface_templates

    @interface_templates.setter
    def interface_templates(self, interface_templates):
        """
        Sets the interface_templates of this DeviceTypeDetailSerializer.


        :param interface_templates: The interface_templates of this DeviceTypeDetailSerializer.
        :type: list[InterfaceTemplateNestedSerializer]
        """

        self._interface_templates = interface_templates

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
