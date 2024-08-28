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

class MarketQuoteOHLC(object):
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
        'ohlc': 'Ohlc',
        'last_price': 'float',
        'instrument_token': 'str'
    }

    attribute_map = {
        'ohlc': 'ohlc',
        'last_price': 'last_price',
        'instrument_token': 'instrument_token'
    }

    def __init__(self, ohlc=None, last_price=None, instrument_token=None):  # noqa: E501
        """MarketQuoteOHLC - a model defined in Swagger"""  # noqa: E501
        self._ohlc = None
        self._last_price = None
        self._instrument_token = None
        self.discriminator = None
        if ohlc is not None:
            self.ohlc = ohlc
        if last_price is not None:
            self.last_price = last_price
        if instrument_token is not None:
            self.instrument_token = instrument_token

    @property
    def ohlc(self):
        """Gets the ohlc of this MarketQuoteOHLC.  # noqa: E501


        :return: The ohlc of this MarketQuoteOHLC.  # noqa: E501
        :rtype: Ohlc
        """
        return self._ohlc

    @ohlc.setter
    def ohlc(self, ohlc):
        """Sets the ohlc of this MarketQuoteOHLC.


        :param ohlc: The ohlc of this MarketQuoteOHLC.  # noqa: E501
        :type: Ohlc
        """

        self._ohlc = ohlc

    @property
    def last_price(self):
        """Gets the last_price of this MarketQuoteOHLC.  # noqa: E501

        The last traded price of symbol  # noqa: E501

        :return: The last_price of this MarketQuoteOHLC.  # noqa: E501
        :rtype: float
        """
        return self._last_price

    @last_price.setter
    def last_price(self, last_price):
        """Sets the last_price of this MarketQuoteOHLC.

        The last traded price of symbol  # noqa: E501

        :param last_price: The last_price of this MarketQuoteOHLC.  # noqa: E501
        :type: float
        """

        self._last_price = last_price

    @property
    def instrument_token(self):
        """Gets the instrument_token of this MarketQuoteOHLC.  # noqa: E501


        :return: The instrument_token of this MarketQuoteOHLC.  # noqa: E501
        :rtype: str
        """
        return self._instrument_token

    @instrument_token.setter
    def instrument_token(self, instrument_token):
        """Sets the instrument_token of this MarketQuoteOHLC.


        :param instrument_token: The instrument_token of this MarketQuoteOHLC.  # noqa: E501
        :type: str
        """

        self._instrument_token = instrument_token

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
        if issubclass(MarketQuoteOHLC, dict):
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
        if not isinstance(other, MarketQuoteOHLC):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
