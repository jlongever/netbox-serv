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


class SiteSerializer(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, name=None, slug=None, tenant=None, facility=None, asn=None, physical_address=None, shipping_address=None, comments=None, count_prefixes=None, count_vlans=None, count_racks=None, count_devices=None, count_circuits=None):
        """
        SiteSerializer - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'name': 'str',
            'slug': 'str',
            'tenant': 'TenantNestedSerializer',
            'facility': 'str',
            'asn': 'int',
            'physical_address': 'str',
            'shipping_address': 'str',
            'comments': 'str',
            'count_prefixes': 'str',
            'count_vlans': 'str',
            'count_racks': 'str',
            'count_devices': 'str',
            'count_circuits': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'slug': 'slug',
            'tenant': 'tenant',
            'facility': 'facility',
            'asn': 'asn',
            'physical_address': 'physical_address',
            'shipping_address': 'shipping_address',
            'comments': 'comments',
            'count_prefixes': 'count_prefixes',
            'count_vlans': 'count_vlans',
            'count_racks': 'count_racks',
            'count_devices': 'count_devices',
            'count_circuits': 'count_circuits'
        }

        self._id = id
        self._name = name
        self._slug = slug
        self._tenant = tenant
        self._facility = facility
        self._asn = asn
        self._physical_address = physical_address
        self._shipping_address = shipping_address
        self._comments = comments
        self._count_prefixes = count_prefixes
        self._count_vlans = count_vlans
        self._count_racks = count_racks
        self._count_devices = count_devices
        self._count_circuits = count_circuits


    @property
    def id(self):
        """
        Gets the id of this SiteSerializer.


        :return: The id of this SiteSerializer.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SiteSerializer.


        :param id: The id of this SiteSerializer.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this SiteSerializer.


        :return: The name of this SiteSerializer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SiteSerializer.


        :param name: The name of this SiteSerializer.
        :type: str
        """

        self._name = name

    @property
    def slug(self):
        """
        Gets the slug of this SiteSerializer.


        :return: The slug of this SiteSerializer.
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """
        Sets the slug of this SiteSerializer.


        :param slug: The slug of this SiteSerializer.
        :type: str
        """

        self._slug = slug

    @property
    def tenant(self):
        """
        Gets the tenant of this SiteSerializer.


        :return: The tenant of this SiteSerializer.
        :rtype: TenantNestedSerializer
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """
        Sets the tenant of this SiteSerializer.


        :param tenant: The tenant of this SiteSerializer.
        :type: TenantNestedSerializer
        """

        self._tenant = tenant

    @property
    def facility(self):
        """
        Gets the facility of this SiteSerializer.


        :return: The facility of this SiteSerializer.
        :rtype: str
        """
        return self._facility

    @facility.setter
    def facility(self, facility):
        """
        Sets the facility of this SiteSerializer.


        :param facility: The facility of this SiteSerializer.
        :type: str
        """

        self._facility = facility

    @property
    def asn(self):
        """
        Gets the asn of this SiteSerializer.


        :return: The asn of this SiteSerializer.
        :rtype: int
        """
        return self._asn

    @asn.setter
    def asn(self, asn):
        """
        Sets the asn of this SiteSerializer.


        :param asn: The asn of this SiteSerializer.
        :type: int
        """

        if not asn:
            raise ValueError("Invalid value for `asn`, must not be `None`")
        if asn > 4.294967295E9:
            raise ValueError("Invalid value for `asn`, must be a value less than or equal to `4.294967295E9`")
        if asn < 1.0:
            raise ValueError("Invalid value for `asn`, must be a value greater than or equal to `1.0`")

        self._asn = asn

    @property
    def physical_address(self):
        """
        Gets the physical_address of this SiteSerializer.


        :return: The physical_address of this SiteSerializer.
        :rtype: str
        """
        return self._physical_address

    @physical_address.setter
    def physical_address(self, physical_address):
        """
        Sets the physical_address of this SiteSerializer.


        :param physical_address: The physical_address of this SiteSerializer.
        :type: str
        """

        self._physical_address = physical_address

    @property
    def shipping_address(self):
        """
        Gets the shipping_address of this SiteSerializer.


        :return: The shipping_address of this SiteSerializer.
        :rtype: str
        """
        return self._shipping_address

    @shipping_address.setter
    def shipping_address(self, shipping_address):
        """
        Sets the shipping_address of this SiteSerializer.


        :param shipping_address: The shipping_address of this SiteSerializer.
        :type: str
        """

        self._shipping_address = shipping_address

    @property
    def comments(self):
        """
        Gets the comments of this SiteSerializer.


        :return: The comments of this SiteSerializer.
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """
        Sets the comments of this SiteSerializer.


        :param comments: The comments of this SiteSerializer.
        :type: str
        """

        self._comments = comments

    @property
    def count_prefixes(self):
        """
        Gets the count_prefixes of this SiteSerializer.


        :return: The count_prefixes of this SiteSerializer.
        :rtype: str
        """
        return self._count_prefixes

    @count_prefixes.setter
    def count_prefixes(self, count_prefixes):
        """
        Sets the count_prefixes of this SiteSerializer.


        :param count_prefixes: The count_prefixes of this SiteSerializer.
        :type: str
        """

        self._count_prefixes = count_prefixes

    @property
    def count_vlans(self):
        """
        Gets the count_vlans of this SiteSerializer.


        :return: The count_vlans of this SiteSerializer.
        :rtype: str
        """
        return self._count_vlans

    @count_vlans.setter
    def count_vlans(self, count_vlans):
        """
        Sets the count_vlans of this SiteSerializer.


        :param count_vlans: The count_vlans of this SiteSerializer.
        :type: str
        """

        self._count_vlans = count_vlans

    @property
    def count_racks(self):
        """
        Gets the count_racks of this SiteSerializer.


        :return: The count_racks of this SiteSerializer.
        :rtype: str
        """
        return self._count_racks

    @count_racks.setter
    def count_racks(self, count_racks):
        """
        Sets the count_racks of this SiteSerializer.


        :param count_racks: The count_racks of this SiteSerializer.
        :type: str
        """

        self._count_racks = count_racks

    @property
    def count_devices(self):
        """
        Gets the count_devices of this SiteSerializer.


        :return: The count_devices of this SiteSerializer.
        :rtype: str
        """
        return self._count_devices

    @count_devices.setter
    def count_devices(self, count_devices):
        """
        Sets the count_devices of this SiteSerializer.


        :param count_devices: The count_devices of this SiteSerializer.
        :type: str
        """

        self._count_devices = count_devices

    @property
    def count_circuits(self):
        """
        Gets the count_circuits of this SiteSerializer.


        :return: The count_circuits of this SiteSerializer.
        :rtype: str
        """
        return self._count_circuits

    @count_circuits.setter
    def count_circuits(self, count_circuits):
        """
        Sets the count_circuits of this SiteSerializer.


        :param count_circuits: The count_circuits of this SiteSerializer.
        :type: str
        """

        self._count_circuits = count_circuits

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
