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


class PrefixSerializer(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, family=None, prefix=None, site=None, vrf=None, tenant=None, vlan=None, status=None, role=None, description=None):
        """
        PrefixSerializer - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'family': 'int',
            'prefix': 'str',
            'site': 'SiteNestedSerializer',
            'vrf': 'VRFTenantSerializer',
            'tenant': 'TenantNestedSerializer',
            'vlan': 'VLANNestedSerializer',
            'status': 'int',
            'role': 'RoleNestedSerializer',
            'description': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'family': 'family',
            'prefix': 'prefix',
            'site': 'site',
            'vrf': 'vrf',
            'tenant': 'tenant',
            'vlan': 'vlan',
            'status': 'status',
            'role': 'role',
            'description': 'description'
        }

        self._id = id
        self._family = family
        self._prefix = prefix
        self._site = site
        self._vrf = vrf
        self._tenant = tenant
        self._vlan = vlan
        self._status = status
        self._role = role
        self._description = description


    @property
    def id(self):
        """
        Gets the id of this PrefixSerializer.


        :return: The id of this PrefixSerializer.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PrefixSerializer.


        :param id: The id of this PrefixSerializer.
        :type: int
        """

        self._id = id

    @property
    def family(self):
        """
        Gets the family of this PrefixSerializer.


        :return: The family of this PrefixSerializer.
        :rtype: int
        """
        return self._family

    @family.setter
    def family(self, family):
        """
        Sets the family of this PrefixSerializer.


        :param family: The family of this PrefixSerializer.
        :type: int
        """

        self._family = family

    @property
    def prefix(self):
        """
        Gets the prefix of this PrefixSerializer.


        :return: The prefix of this PrefixSerializer.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """
        Sets the prefix of this PrefixSerializer.


        :param prefix: The prefix of this PrefixSerializer.
        :type: str
        """

        self._prefix = prefix

    @property
    def site(self):
        """
        Gets the site of this PrefixSerializer.


        :return: The site of this PrefixSerializer.
        :rtype: SiteNestedSerializer
        """
        return self._site

    @site.setter
    def site(self, site):
        """
        Sets the site of this PrefixSerializer.


        :param site: The site of this PrefixSerializer.
        :type: SiteNestedSerializer
        """

        self._site = site

    @property
    def vrf(self):
        """
        Gets the vrf of this PrefixSerializer.


        :return: The vrf of this PrefixSerializer.
        :rtype: VRFTenantSerializer
        """
        return self._vrf

    @vrf.setter
    def vrf(self, vrf):
        """
        Sets the vrf of this PrefixSerializer.


        :param vrf: The vrf of this PrefixSerializer.
        :type: VRFTenantSerializer
        """

        self._vrf = vrf

    @property
    def tenant(self):
        """
        Gets the tenant of this PrefixSerializer.


        :return: The tenant of this PrefixSerializer.
        :rtype: TenantNestedSerializer
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """
        Sets the tenant of this PrefixSerializer.


        :param tenant: The tenant of this PrefixSerializer.
        :type: TenantNestedSerializer
        """

        self._tenant = tenant

    @property
    def vlan(self):
        """
        Gets the vlan of this PrefixSerializer.


        :return: The vlan of this PrefixSerializer.
        :rtype: VLANNestedSerializer
        """
        return self._vlan

    @vlan.setter
    def vlan(self, vlan):
        """
        Sets the vlan of this PrefixSerializer.


        :param vlan: The vlan of this PrefixSerializer.
        :type: VLANNestedSerializer
        """

        self._vlan = vlan

    @property
    def status(self):
        """
        Gets the status of this PrefixSerializer.


        :return: The status of this PrefixSerializer.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this PrefixSerializer.


        :param status: The status of this PrefixSerializer.
        :type: int
        """
        allowed_values = ["0", "1", "2", "3"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def role(self):
        """
        Gets the role of this PrefixSerializer.


        :return: The role of this PrefixSerializer.
        :rtype: RoleNestedSerializer
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this PrefixSerializer.


        :param role: The role of this PrefixSerializer.
        :type: RoleNestedSerializer
        """

        self._role = role

    @property
    def description(self):
        """
        Gets the description of this PrefixSerializer.


        :return: The description of this PrefixSerializer.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this PrefixSerializer.


        :param description: The description of this PrefixSerializer.
        :type: str
        """

        self._description = description

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