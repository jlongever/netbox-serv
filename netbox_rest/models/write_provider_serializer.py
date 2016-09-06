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


class WriteProviderSerializer(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, slug=None, asn=None, account=None, portal_url=None, noc_contact=None, admin_contact=None, comments=None):
        """
        WriteProviderSerializer - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'slug': 'str',
            'asn': 'int',
            'account': 'str',
            'portal_url': 'str',
            'noc_contact': 'str',
            'admin_contact': 'str',
            'comments': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'slug': 'slug',
            'asn': 'asn',
            'account': 'account',
            'portal_url': 'portal_url',
            'noc_contact': 'noc_contact',
            'admin_contact': 'admin_contact',
            'comments': 'comments'
        }

        self._name = name
        self._slug = slug
        self._asn = asn
        self._account = account
        self._portal_url = portal_url
        self._noc_contact = noc_contact
        self._admin_contact = admin_contact
        self._comments = comments


    @property
    def name(self):
        """
        Gets the name of this WriteProviderSerializer.


        :return: The name of this WriteProviderSerializer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this WriteProviderSerializer.


        :param name: The name of this WriteProviderSerializer.
        :type: str
        """

        self._name = name

    @property
    def slug(self):
        """
        Gets the slug of this WriteProviderSerializer.


        :return: The slug of this WriteProviderSerializer.
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """
        Sets the slug of this WriteProviderSerializer.


        :param slug: The slug of this WriteProviderSerializer.
        :type: str
        """

        self._slug = slug

    @property
    def asn(self):
        """
        Gets the asn of this WriteProviderSerializer.


        :return: The asn of this WriteProviderSerializer.
        :rtype: int
        """
        return self._asn

    @asn.setter
    def asn(self, asn):
        """
        Sets the asn of this WriteProviderSerializer.


        :param asn: The asn of this WriteProviderSerializer.
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
    def account(self):
        """
        Gets the account of this WriteProviderSerializer.


        :return: The account of this WriteProviderSerializer.
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """
        Sets the account of this WriteProviderSerializer.


        :param account: The account of this WriteProviderSerializer.
        :type: str
        """

        self._account = account

    @property
    def portal_url(self):
        """
        Gets the portal_url of this WriteProviderSerializer.


        :return: The portal_url of this WriteProviderSerializer.
        :rtype: str
        """
        return self._portal_url

    @portal_url.setter
    def portal_url(self, portal_url):
        """
        Sets the portal_url of this WriteProviderSerializer.


        :param portal_url: The portal_url of this WriteProviderSerializer.
        :type: str
        """

        self._portal_url = portal_url

    @property
    def noc_contact(self):
        """
        Gets the noc_contact of this WriteProviderSerializer.


        :return: The noc_contact of this WriteProviderSerializer.
        :rtype: str
        """
        return self._noc_contact

    @noc_contact.setter
    def noc_contact(self, noc_contact):
        """
        Sets the noc_contact of this WriteProviderSerializer.


        :param noc_contact: The noc_contact of this WriteProviderSerializer.
        :type: str
        """

        self._noc_contact = noc_contact

    @property
    def admin_contact(self):
        """
        Gets the admin_contact of this WriteProviderSerializer.


        :return: The admin_contact of this WriteProviderSerializer.
        :rtype: str
        """
        return self._admin_contact

    @admin_contact.setter
    def admin_contact(self, admin_contact):
        """
        Sets the admin_contact of this WriteProviderSerializer.


        :param admin_contact: The admin_contact of this WriteProviderSerializer.
        :type: str
        """

        self._admin_contact = admin_contact

    @property
    def comments(self):
        """
        Gets the comments of this WriteProviderSerializer.


        :return: The comments of this WriteProviderSerializer.
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """
        Sets the comments of this WriteProviderSerializer.


        :param comments: The comments of this WriteProviderSerializer.
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