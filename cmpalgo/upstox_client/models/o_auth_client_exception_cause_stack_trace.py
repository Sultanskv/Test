# coding: utf-8

"""
    Upstox Developer API

    Build your App on the Upstox platform  ![Banner](https://api-v2.upstox.com/api-docs/images/banner.jpg \"banner\")  # Introduction  Upstox API is a set of rest APIs that provide data required to build a complete investment and trading platform. Execute orders in real time, manage user portfolio, stream live market data (using Websocket), and more, with the easy to understand API collection.  All requests are over HTTPS and the requests are sent with the content-type ‘application/json’. Developers have the option of choosing the response type as JSON or CSV for a few API calls.  To be able to use these APIs you need to create an App in the Developer Console and generate your **apiKey** and **apiSecret**. You can use a redirect URL which will be called after the login flow.  If you are a **trader**, you can directly create apps from Upstox mobile app or the desktop platform itself from **Apps** sections inside the **Account** Tab. Head over to <a href=\"http://account.upstox.com/developer/apps\" target=\"_blank\">account.upstox.com/developer/apps</a>.</br> If you are a **business** looking to integrate Upstox APIs, reach out to us and we will get a custom app created for you in no time.  It is highly recommended that you do not embed the **apiSecret** in your frontend app. Create a remote backend which does the handshake on behalf of the frontend app. Marking the apiSecret in the frontend app will make your app vulnerable to threats and potential issues.   # noqa: E501

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class OAuthClientExceptionCauseStackTrace(object):
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
        'class_loader_name': 'str',
        'module_name': 'str',
        'module_version': 'str',
        'method_name': 'str',
        'file_name': 'str',
        'line_number': 'int',
        'class_name': 'str',
        'native_method': 'bool'
    }

    attribute_map = {
        'class_loader_name': 'classLoaderName',
        'module_name': 'moduleName',
        'module_version': 'moduleVersion',
        'method_name': 'methodName',
        'file_name': 'fileName',
        'line_number': 'lineNumber',
        'class_name': 'className',
        'native_method': 'nativeMethod'
    }

    def __init__(self, class_loader_name=None, module_name=None, module_version=None, method_name=None, file_name=None, line_number=None, class_name=None, native_method=None):  # noqa: E501
        """OAuthClientExceptionCauseStackTrace - a model defined in Swagger"""  # noqa: E501
        self._class_loader_name = None
        self._module_name = None
        self._module_version = None
        self._method_name = None
        self._file_name = None
        self._line_number = None
        self._class_name = None
        self._native_method = None
        self.discriminator = None
        if class_loader_name is not None:
            self.class_loader_name = class_loader_name
        if module_name is not None:
            self.module_name = module_name
        if module_version is not None:
            self.module_version = module_version
        if method_name is not None:
            self.method_name = method_name
        if file_name is not None:
            self.file_name = file_name
        if line_number is not None:
            self.line_number = line_number
        if class_name is not None:
            self.class_name = class_name
        if native_method is not None:
            self.native_method = native_method

    @property
    def class_loader_name(self):
        """Gets the class_loader_name of this OAuthClientExceptionCauseStackTrace.  # noqa: E501


        :return: The class_loader_name of this OAuthClientExceptionCauseStackTrace.  # noqa: E501
        :rtype: str
        """
        return self._class_loader_name

    @class_loader_name.setter
    def class_loader_name(self, class_loader_name):
        """Sets the class_loader_name of this OAuthClientExceptionCauseStackTrace.


        :param class_loader_name: The class_loader_name of this OAuthClientExceptionCauseStackTrace.  # noqa: E501
        :type: str
        """

        self._class_loader_name = class_loader_name

    @property
    def module_name(self):
        """Gets the module_name of this OAuthClientExceptionCauseStackTrace.  # noqa: E501


        :return: The module_name of this OAuthClientExceptionCauseStackTrace.  # noqa: E501
        :rtype: str
        """
        return self._module_name

    @module_name.setter
    def module_name(self, module_name):
        """Sets the module_name of this OAuthClientExceptionCauseStackTrace.


        :param module_name: The module_name of this OAuthClientExceptionCauseStackTrace.  # noqa: E501
        :type: str
        """

        self._module_name = module_name

    @property
    def module_version(self):
        """Gets the module_version of this OAuthClientExceptionCauseStackTrace.  # noqa: E501


        :return: The module_version of this OAuthClientExceptionCauseStackTrace.  # noqa: E501
        :rtype: str
        """
        return self._module_version

    @module_version.setter
    def module_version(self, module_version):
        """Sets the module_version of this OAuthClientExceptionCauseStackTrace.


        :param module_version: The module_version of this OAuthClientExceptionCauseStackTrace.  # noqa: E501
        :type: str
        """

        self._module_version = module_version

    @property
    def method_name(self):
        """Gets the method_name of this OAuthClientExceptionCauseStackTrace.  # noqa: E501


        :return: The method_name of this OAuthClientExceptionCauseStackTrace.  # noqa: E501
        :rtype: str
        """
        return self._method_name

    @method_name.setter
    def method_name(self, method_name):
        """Sets the method_name of this OAuthClientExceptionCauseStackTrace.


        :param method_name: The method_name of this OAuthClientExceptionCauseStackTrace.  # noqa: E501
        :type: str
        """

        self._method_name = method_name

    @property
    def file_name(self):
        """Gets the file_name of this OAuthClientExceptionCauseStackTrace.  # noqa: E501


        :return: The file_name of this OAuthClientExceptionCauseStackTrace.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this OAuthClientExceptionCauseStackTrace.


        :param file_name: The file_name of this OAuthClientExceptionCauseStackTrace.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def line_number(self):
        """Gets the line_number of this OAuthClientExceptionCauseStackTrace.  # noqa: E501


        :return: The line_number of this OAuthClientExceptionCauseStackTrace.  # noqa: E501
        :rtype: int
        """
        return self._line_number

    @line_number.setter
    def line_number(self, line_number):
        """Sets the line_number of this OAuthClientExceptionCauseStackTrace.


        :param line_number: The line_number of this OAuthClientExceptionCauseStackTrace.  # noqa: E501
        :type: int
        """

        self._line_number = line_number

    @property
    def class_name(self):
        """Gets the class_name of this OAuthClientExceptionCauseStackTrace.  # noqa: E501


        :return: The class_name of this OAuthClientExceptionCauseStackTrace.  # noqa: E501
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        """Sets the class_name of this OAuthClientExceptionCauseStackTrace.


        :param class_name: The class_name of this OAuthClientExceptionCauseStackTrace.  # noqa: E501
        :type: str
        """

        self._class_name = class_name

    @property
    def native_method(self):
        """Gets the native_method of this OAuthClientExceptionCauseStackTrace.  # noqa: E501


        :return: The native_method of this OAuthClientExceptionCauseStackTrace.  # noqa: E501
        :rtype: bool
        """
        return self._native_method

    @native_method.setter
    def native_method(self, native_method):
        """Sets the native_method of this OAuthClientExceptionCauseStackTrace.


        :param native_method: The native_method of this OAuthClientExceptionCauseStackTrace.  # noqa: E501
        :type: bool
        """

        self._native_method = native_method

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
        if issubclass(OAuthClientExceptionCauseStackTrace, dict):
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
        if not isinstance(other, OAuthClientExceptionCauseStackTrace):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
