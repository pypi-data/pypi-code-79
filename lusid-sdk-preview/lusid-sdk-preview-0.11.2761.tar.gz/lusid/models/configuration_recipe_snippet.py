# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2761
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class ConfigurationRecipeSnippet(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'scope': 'str',
        'code': 'str',
        'aggregation_options': 'AggregationOptions',
        'model_rules': 'list[VendorModelRule]',
        'pricing_options': 'PricingOptions',
        'market_rules': 'list[MarketDataKeyRule]',
        'market_options': 'MarketOptions',
        'recipe': 'ConfigurationRecipe'
    }

    attribute_map = {
        'scope': 'scope',
        'code': 'code',
        'aggregation_options': 'aggregationOptions',
        'model_rules': 'modelRules',
        'pricing_options': 'pricingOptions',
        'market_rules': 'marketRules',
        'market_options': 'marketOptions',
        'recipe': 'recipe'
    }

    required_map = {
        'scope': 'required',
        'code': 'required',
        'aggregation_options': 'optional',
        'model_rules': 'optional',
        'pricing_options': 'optional',
        'market_rules': 'optional',
        'market_options': 'optional',
        'recipe': 'optional'
    }

    def __init__(self, scope=None, code=None, aggregation_options=None, model_rules=None, pricing_options=None, market_rules=None, market_options=None, recipe=None):  # noqa: E501
        """
        ConfigurationRecipeSnippet - a model defined in OpenAPI

        :param scope:  The scope used when updating or inserting the Configuration Recipe snippet (required)
        :type scope: str
        :param code:  User given string name (code) to identify the recipe. (required)
        :type code: str
        :param aggregation_options: 
        :type aggregation_options: lusid.AggregationOptions
        :param model_rules:  The set of model rules that are available. There may be multiple rules for Vendors, but only one per model-instrument pair.  Which of these preference sets is used depends upon the model choice selection if specified, or failing that the global default model specification  in the options.
        :type model_rules: list[lusid.VendorModelRule]
        :param pricing_options: 
        :type pricing_options: lusid.PricingOptions
        :param market_rules:  The set of rules that define how to resolve particular use cases. These can be relatively general or specific in nature.  Nominally any number are possible and will be processed in order where applicable. However, there is evidently a potential  for increased computational cost where many rules must be applied to resolve data. Ensuring that portfolios are structured in  such a way as to reduce the number of rules required is therefore sensible.
        :type market_rules: list[lusid.MarketDataKeyRule]
        :param market_options: 
        :type market_options: lusid.MarketOptions
        :param recipe: 
        :type recipe: lusid.ConfigurationRecipe

        """  # noqa: E501

        self._scope = None
        self._code = None
        self._aggregation_options = None
        self._model_rules = None
        self._pricing_options = None
        self._market_rules = None
        self._market_options = None
        self._recipe = None
        self.discriminator = None

        self.scope = scope
        self.code = code
        if aggregation_options is not None:
            self.aggregation_options = aggregation_options
        self.model_rules = model_rules
        if pricing_options is not None:
            self.pricing_options = pricing_options
        self.market_rules = market_rules
        if market_options is not None:
            self.market_options = market_options
        if recipe is not None:
            self.recipe = recipe

    @property
    def scope(self):
        """Gets the scope of this ConfigurationRecipeSnippet.  # noqa: E501

        The scope used when updating or inserting the Configuration Recipe snippet  # noqa: E501

        :return: The scope of this ConfigurationRecipeSnippet.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this ConfigurationRecipeSnippet.

        The scope used when updating or inserting the Configuration Recipe snippet  # noqa: E501

        :param scope: The scope of this ConfigurationRecipeSnippet.  # noqa: E501
        :type: str
        """
        if scope is None:
            raise ValueError("Invalid value for `scope`, must not be `None`")  # noqa: E501
        if scope is not None and len(scope) > 64:
            raise ValueError("Invalid value for `scope`, length must be less than or equal to `64`")  # noqa: E501
        if scope is not None and len(scope) < 1:
            raise ValueError("Invalid value for `scope`, length must be greater than or equal to `1`")  # noqa: E501
        if (scope is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', scope)):  # noqa: E501
            raise ValueError(r"Invalid value for `scope`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._scope = scope

    @property
    def code(self):
        """Gets the code of this ConfigurationRecipeSnippet.  # noqa: E501

        User given string name (code) to identify the recipe.  # noqa: E501

        :return: The code of this ConfigurationRecipeSnippet.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ConfigurationRecipeSnippet.

        User given string name (code) to identify the recipe.  # noqa: E501

        :param code: The code of this ConfigurationRecipeSnippet.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501
        if code is not None and len(code) > 64:
            raise ValueError("Invalid value for `code`, length must be less than or equal to `64`")  # noqa: E501
        if code is not None and len(code) < 1:
            raise ValueError("Invalid value for `code`, length must be greater than or equal to `1`")  # noqa: E501
        if (code is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', code)):  # noqa: E501
            raise ValueError(r"Invalid value for `code`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._code = code

    @property
    def aggregation_options(self):
        """Gets the aggregation_options of this ConfigurationRecipeSnippet.  # noqa: E501


        :return: The aggregation_options of this ConfigurationRecipeSnippet.  # noqa: E501
        :rtype: AggregationOptions
        """
        return self._aggregation_options

    @aggregation_options.setter
    def aggregation_options(self, aggregation_options):
        """Sets the aggregation_options of this ConfigurationRecipeSnippet.


        :param aggregation_options: The aggregation_options of this ConfigurationRecipeSnippet.  # noqa: E501
        :type: AggregationOptions
        """

        self._aggregation_options = aggregation_options

    @property
    def model_rules(self):
        """Gets the model_rules of this ConfigurationRecipeSnippet.  # noqa: E501

        The set of model rules that are available. There may be multiple rules for Vendors, but only one per model-instrument pair.  Which of these preference sets is used depends upon the model choice selection if specified, or failing that the global default model specification  in the options.  # noqa: E501

        :return: The model_rules of this ConfigurationRecipeSnippet.  # noqa: E501
        :rtype: list[VendorModelRule]
        """
        return self._model_rules

    @model_rules.setter
    def model_rules(self, model_rules):
        """Sets the model_rules of this ConfigurationRecipeSnippet.

        The set of model rules that are available. There may be multiple rules for Vendors, but only one per model-instrument pair.  Which of these preference sets is used depends upon the model choice selection if specified, or failing that the global default model specification  in the options.  # noqa: E501

        :param model_rules: The model_rules of this ConfigurationRecipeSnippet.  # noqa: E501
        :type: list[VendorModelRule]
        """

        self._model_rules = model_rules

    @property
    def pricing_options(self):
        """Gets the pricing_options of this ConfigurationRecipeSnippet.  # noqa: E501


        :return: The pricing_options of this ConfigurationRecipeSnippet.  # noqa: E501
        :rtype: PricingOptions
        """
        return self._pricing_options

    @pricing_options.setter
    def pricing_options(self, pricing_options):
        """Sets the pricing_options of this ConfigurationRecipeSnippet.


        :param pricing_options: The pricing_options of this ConfigurationRecipeSnippet.  # noqa: E501
        :type: PricingOptions
        """

        self._pricing_options = pricing_options

    @property
    def market_rules(self):
        """Gets the market_rules of this ConfigurationRecipeSnippet.  # noqa: E501

        The set of rules that define how to resolve particular use cases. These can be relatively general or specific in nature.  Nominally any number are possible and will be processed in order where applicable. However, there is evidently a potential  for increased computational cost where many rules must be applied to resolve data. Ensuring that portfolios are structured in  such a way as to reduce the number of rules required is therefore sensible.  # noqa: E501

        :return: The market_rules of this ConfigurationRecipeSnippet.  # noqa: E501
        :rtype: list[MarketDataKeyRule]
        """
        return self._market_rules

    @market_rules.setter
    def market_rules(self, market_rules):
        """Sets the market_rules of this ConfigurationRecipeSnippet.

        The set of rules that define how to resolve particular use cases. These can be relatively general or specific in nature.  Nominally any number are possible and will be processed in order where applicable. However, there is evidently a potential  for increased computational cost where many rules must be applied to resolve data. Ensuring that portfolios are structured in  such a way as to reduce the number of rules required is therefore sensible.  # noqa: E501

        :param market_rules: The market_rules of this ConfigurationRecipeSnippet.  # noqa: E501
        :type: list[MarketDataKeyRule]
        """

        self._market_rules = market_rules

    @property
    def market_options(self):
        """Gets the market_options of this ConfigurationRecipeSnippet.  # noqa: E501


        :return: The market_options of this ConfigurationRecipeSnippet.  # noqa: E501
        :rtype: MarketOptions
        """
        return self._market_options

    @market_options.setter
    def market_options(self, market_options):
        """Sets the market_options of this ConfigurationRecipeSnippet.


        :param market_options: The market_options of this ConfigurationRecipeSnippet.  # noqa: E501
        :type: MarketOptions
        """

        self._market_options = market_options

    @property
    def recipe(self):
        """Gets the recipe of this ConfigurationRecipeSnippet.  # noqa: E501


        :return: The recipe of this ConfigurationRecipeSnippet.  # noqa: E501
        :rtype: ConfigurationRecipe
        """
        return self._recipe

    @recipe.setter
    def recipe(self, recipe):
        """Sets the recipe of this ConfigurationRecipeSnippet.


        :param recipe: The recipe of this ConfigurationRecipeSnippet.  # noqa: E501
        :type: ConfigurationRecipe
        """

        self._recipe = recipe

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ConfigurationRecipeSnippet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
