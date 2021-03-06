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


class CircuitSerializer(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, cid=None, provider=None, type=None, tenant=None, site=None, interface=None, install_date=None, port_speed=None, upstream_speed=None, commit_rate=None, xconnect_id=None, comments=None):
        """
        CircuitSerializer - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'cid': 'str',
            'provider': 'ProviderNestedSerializer',
            'type': 'CircuitTypeNestedSerializer',
            'tenant': 'TenantNestedSerializer',
            'site': 'SiteNestedSerializer',
            'interface': 'InterfaceNestedSerializer',
            'install_date': 'date',
            'port_speed': 'int',
            'upstream_speed': 'int',
            'commit_rate': 'int',
            'xconnect_id': 'str',
            'comments': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'cid': 'cid',
            'provider': 'provider',
            'type': 'type',
            'tenant': 'tenant',
            'site': 'site',
            'interface': 'interface',
            'install_date': 'install_date',
            'port_speed': 'port_speed',
            'upstream_speed': 'upstream_speed',
            'commit_rate': 'commit_rate',
            'xconnect_id': 'xconnect_id',
            'comments': 'comments'
        }

        self._id = id
        self._cid = cid
        self._provider = provider
        self._type = type
        self._tenant = tenant
        self._site = site
        self._interface = interface
        self._install_date = install_date
        self._port_speed = port_speed
        self._upstream_speed = upstream_speed
        self._commit_rate = commit_rate
        self._xconnect_id = xconnect_id
        self._comments = comments


    @property
    def id(self):
        """
        Gets the id of this CircuitSerializer.


        :return: The id of this CircuitSerializer.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CircuitSerializer.


        :param id: The id of this CircuitSerializer.
        :type: int
        """

        self._id = id

    @property
    def cid(self):
        """
        Gets the cid of this CircuitSerializer.


        :return: The cid of this CircuitSerializer.
        :rtype: str
        """
        return self._cid

    @cid.setter
    def cid(self, cid):
        """
        Sets the cid of this CircuitSerializer.


        :param cid: The cid of this CircuitSerializer.
        :type: str
        """

        self._cid = cid

    @property
    def provider(self):
        """
        Gets the provider of this CircuitSerializer.


        :return: The provider of this CircuitSerializer.
        :rtype: ProviderNestedSerializer
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """
        Sets the provider of this CircuitSerializer.


        :param provider: The provider of this CircuitSerializer.
        :type: ProviderNestedSerializer
        """

        self._provider = provider

    @property
    def type(self):
        """
        Gets the type of this CircuitSerializer.


        :return: The type of this CircuitSerializer.
        :rtype: CircuitTypeNestedSerializer
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CircuitSerializer.


        :param type: The type of this CircuitSerializer.
        :type: CircuitTypeNestedSerializer
        """

        self._type = type

    @property
    def tenant(self):
        """
        Gets the tenant of this CircuitSerializer.


        :return: The tenant of this CircuitSerializer.
        :rtype: TenantNestedSerializer
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """
        Sets the tenant of this CircuitSerializer.


        :param tenant: The tenant of this CircuitSerializer.
        :type: TenantNestedSerializer
        """

        self._tenant = tenant

    @property
    def site(self):
        """
        Gets the site of this CircuitSerializer.


        :return: The site of this CircuitSerializer.
        :rtype: SiteNestedSerializer
        """
        return self._site

    @site.setter
    def site(self, site):
        """
        Sets the site of this CircuitSerializer.


        :param site: The site of this CircuitSerializer.
        :type: SiteNestedSerializer
        """

        self._site = site

    @property
    def interface(self):
        """
        Gets the interface of this CircuitSerializer.


        :return: The interface of this CircuitSerializer.
        :rtype: InterfaceNestedSerializer
        """
        return self._interface

    @interface.setter
    def interface(self, interface):
        """
        Sets the interface of this CircuitSerializer.


        :param interface: The interface of this CircuitSerializer.
        :type: InterfaceNestedSerializer
        """

        self._interface = interface

    @property
    def install_date(self):
        """
        Gets the install_date of this CircuitSerializer.


        :return: The install_date of this CircuitSerializer.
        :rtype: date
        """
        return self._install_date

    @install_date.setter
    def install_date(self, install_date):
        """
        Sets the install_date of this CircuitSerializer.


        :param install_date: The install_date of this CircuitSerializer.
        :type: date
        """

        self._install_date = install_date

    @property
    def port_speed(self):
        """
        Gets the port_speed of this CircuitSerializer.


        :return: The port_speed of this CircuitSerializer.
        :rtype: int
        """
        return self._port_speed

    @port_speed.setter
    def port_speed(self, port_speed):
        """
        Sets the port_speed of this CircuitSerializer.


        :param port_speed: The port_speed of this CircuitSerializer.
        :type: int
        """

        if not port_speed:
            raise ValueError("Invalid value for `port_speed`, must not be `None`")
        if port_speed > 2.147483647E9:
            raise ValueError("Invalid value for `port_speed`, must be a value less than or equal to `2.147483647E9`")
        if port_speed < 0.0:
            raise ValueError("Invalid value for `port_speed`, must be a value greater than or equal to `0.0`")

        self._port_speed = port_speed

    @property
    def upstream_speed(self):
        """
        Gets the upstream_speed of this CircuitSerializer.
        Upstream speed, if different from port speed

        :return: The upstream_speed of this CircuitSerializer.
        :rtype: int
        """
        return self._upstream_speed

    @upstream_speed.setter
    def upstream_speed(self, upstream_speed):
        """
        Sets the upstream_speed of this CircuitSerializer.
        Upstream speed, if different from port speed

        :param upstream_speed: The upstream_speed of this CircuitSerializer.
        :type: int
        """

        if not upstream_speed:
            raise ValueError("Invalid value for `upstream_speed`, must not be `None`")
        if upstream_speed > 2.147483647E9:
            raise ValueError("Invalid value for `upstream_speed`, must be a value less than or equal to `2.147483647E9`")
        if upstream_speed < 0.0:
            raise ValueError("Invalid value for `upstream_speed`, must be a value greater than or equal to `0.0`")

        self._upstream_speed = upstream_speed

    @property
    def commit_rate(self):
        """
        Gets the commit_rate of this CircuitSerializer.


        :return: The commit_rate of this CircuitSerializer.
        :rtype: int
        """
        return self._commit_rate

    @commit_rate.setter
    def commit_rate(self, commit_rate):
        """
        Sets the commit_rate of this CircuitSerializer.


        :param commit_rate: The commit_rate of this CircuitSerializer.
        :type: int
        """

        if not commit_rate:
            raise ValueError("Invalid value for `commit_rate`, must not be `None`")
        if commit_rate > 2.147483647E9:
            raise ValueError("Invalid value for `commit_rate`, must be a value less than or equal to `2.147483647E9`")
        if commit_rate < 0.0:
            raise ValueError("Invalid value for `commit_rate`, must be a value greater than or equal to `0.0`")

        self._commit_rate = commit_rate

    @property
    def xconnect_id(self):
        """
        Gets the xconnect_id of this CircuitSerializer.


        :return: The xconnect_id of this CircuitSerializer.
        :rtype: str
        """
        return self._xconnect_id

    @xconnect_id.setter
    def xconnect_id(self, xconnect_id):
        """
        Sets the xconnect_id of this CircuitSerializer.


        :param xconnect_id: The xconnect_id of this CircuitSerializer.
        :type: str
        """

        self._xconnect_id = xconnect_id

    @property
    def comments(self):
        """
        Gets the comments of this CircuitSerializer.


        :return: The comments of this CircuitSerializer.
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """
        Sets the comments of this CircuitSerializer.


        :param comments: The comments of this CircuitSerializer.
        :type: str
        """

        self._comments = comments

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
