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

class TokenResponse(object):
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
        'email': 'str',
        'exchanges': 'list[str]',
        'products': 'list[str]',
        'broker': 'str',
        'user_id': 'str',
        'user_name': 'str',
        'order_types': 'list[str]',
        'user_type': 'str',
        'poa': 'bool',
        'is_active': 'bool',
        'access_token': 'str',
        'extended_token': 'str'
    }

    attribute_map = {
        'email': 'email',
        'exchanges': 'exchanges',
        'products': 'products',
        'broker': 'broker',
        'user_id': 'user_id',
        'user_name': 'user_name',
        'order_types': 'order_types',
        'user_type': 'user_type',
        'poa': 'poa',
        'is_active': 'is_active',
        'access_token': 'access_token',
        'extended_token': 'extended_token'
    }

    def __init__(self, email=None, exchanges=None, products=None, broker=None, user_id=None, user_name=None, order_types=None, user_type=None, poa=None, is_active=None, access_token=None, extended_token=None):  # noqa: E501
        """TokenResponse - a model defined in Swagger"""  # noqa: E501
        self._email = None
        self._exchanges = None
        self._products = None
        self._broker = None
        self._user_id = None
        self._user_name = None
        self._order_types = None
        self._user_type = None
        self._poa = None
        self._is_active = None
        self._access_token = None
        self._extended_token = None
        self.discriminator = None
        if email is not None:
            self.email = email
        if exchanges is not None:
            self.exchanges = exchanges
        if products is not None:
            self.products = products
        if broker is not None:
            self.broker = broker
        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name
        if order_types is not None:
            self.order_types = order_types
        if user_type is not None:
            self.user_type = user_type
        if poa is not None:
            self.poa = poa
        if is_active is not None:
            self.is_active = is_active
        if access_token is not None:
            self.access_token = access_token
        if extended_token is not None:
            self.extended_token = extended_token

    @property
    def email(self):
        """Gets the email of this TokenResponse.  # noqa: E501

        E-mail address of the user  # noqa: E501

        :return: The email of this TokenResponse.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this TokenResponse.

        E-mail address of the user  # noqa: E501

        :param email: The email of this TokenResponse.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def exchanges(self):
        """Gets the exchanges of this TokenResponse.  # noqa: E501

        Lists the exchanges to which the user has access  # noqa: E501

        :return: The exchanges of this TokenResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._exchanges

    @exchanges.setter
    def exchanges(self, exchanges):
        """Sets the exchanges of this TokenResponse.

        Lists the exchanges to which the user has access  # noqa: E501

        :param exchanges: The exchanges of this TokenResponse.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["NSE", "NFO", "CDS", "BSE", "BFO", "BCD", "MCX"]  # noqa: E501
        if not set(exchanges).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `exchanges` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(exchanges) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._exchanges = exchanges

    @property
    def products(self):
        """Gets the products of this TokenResponse.  # noqa: E501

        Lists the products types to which the user has access  # noqa: E501

        :return: The products of this TokenResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._products

    @products.setter
    def products(self, products):
        """Sets the products of this TokenResponse.

        Lists the products types to which the user has access  # noqa: E501

        :param products: The products of this TokenResponse.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["I", "D", "CO", "OCO", "MTF"]  # noqa: E501
        if not set(products).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `products` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(products) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._products = products

    @property
    def broker(self):
        """Gets the broker of this TokenResponse.  # noqa: E501

        The broker ID  # noqa: E501

        :return: The broker of this TokenResponse.  # noqa: E501
        :rtype: str
        """
        return self._broker

    @broker.setter
    def broker(self, broker):
        """Sets the broker of this TokenResponse.

        The broker ID  # noqa: E501

        :param broker: The broker of this TokenResponse.  # noqa: E501
        :type: str
        """

        self._broker = broker

    @property
    def user_id(self):
        """Gets the user_id of this TokenResponse.  # noqa: E501

        Uniquely identifies the user  # noqa: E501

        :return: The user_id of this TokenResponse.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this TokenResponse.

        Uniquely identifies the user  # noqa: E501

        :param user_id: The user_id of this TokenResponse.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def user_name(self):
        """Gets the user_name of this TokenResponse.  # noqa: E501

        Name of the user  # noqa: E501

        :return: The user_name of this TokenResponse.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this TokenResponse.

        Name of the user  # noqa: E501

        :param user_name: The user_name of this TokenResponse.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def order_types(self):
        """Gets the order_types of this TokenResponse.  # noqa: E501

        Order types enabled for the user  # noqa: E501

        :return: The order_types of this TokenResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._order_types

    @order_types.setter
    def order_types(self, order_types):
        """Sets the order_types of this TokenResponse.

        Order types enabled for the user  # noqa: E501

        :param order_types: The order_types of this TokenResponse.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["MARKET", "LIMIT", "SL", "SL-M"]  # noqa: E501
        if not set(order_types).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `order_types` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(order_types) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._order_types = order_types

    @property
    def user_type(self):
        """Gets the user_type of this TokenResponse.  # noqa: E501

          Identifies the user's registered role at the broker. This will be individual for all retail users  # noqa: E501

        :return: The user_type of this TokenResponse.  # noqa: E501
        :rtype: str
        """
        return self._user_type

    @user_type.setter
    def user_type(self, user_type):
        """Sets the user_type of this TokenResponse.

          Identifies the user's registered role at the broker. This will be individual for all retail users  # noqa: E501

        :param user_type: The user_type of this TokenResponse.  # noqa: E501
        :type: str
        """

        self._user_type = user_type

    @property
    def poa(self):
        """Gets the poa of this TokenResponse.  # noqa: E501

          To depict if the user has given power of attorney for transactions  # noqa: E501

        :return: The poa of this TokenResponse.  # noqa: E501
        :rtype: bool
        """
        return self._poa

    @poa.setter
    def poa(self, poa):
        """Sets the poa of this TokenResponse.

          To depict if the user has given power of attorney for transactions  # noqa: E501

        :param poa: The poa of this TokenResponse.  # noqa: E501
        :type: bool
        """

        self._poa = poa

    @property
    def is_active(self):
        """Gets the is_active of this TokenResponse.  # noqa: E501

          Whether the status of account is active or not  # noqa: E501

        :return: The is_active of this TokenResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this TokenResponse.

          Whether the status of account is active or not  # noqa: E501

        :param is_active: The is_active of this TokenResponse.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def access_token(self):
        """Gets the access_token of this TokenResponse.  # noqa: E501

        The authentication token that is to used with every subsequent API requests  # noqa: E501

        :return: The access_token of this TokenResponse.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this TokenResponse.

        The authentication token that is to used with every subsequent API requests  # noqa: E501

        :param access_token: The access_token of this TokenResponse.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def extended_token(self):
        """Gets the extended_token of this TokenResponse.  # noqa: E501

        The authentication token that is to used with every subsequent API requests  # noqa: E501

        :return: The extended_token of this TokenResponse.  # noqa: E501
        :rtype: str
        """
        return self._extended_token

    @extended_token.setter
    def extended_token(self, extended_token):
        """Sets the extended_token of this TokenResponse.

        The authentication token that is to used with every subsequent API requests  # noqa: E501

        :param extended_token: The extended_token of this TokenResponse.  # noqa: E501
        :type: str
        """

        self._extended_token = extended_token

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
        if issubclass(TokenResponse, dict):
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
        if not isinstance(other, TokenResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
