# coding: utf-8

# flake8: noqa

"""
    Properties

    All HubSpot objects store data in default and custom properties. These endpoints provide access to read and modify object properties in HubSpot.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.0"

# import apis into sdk package
from hubspot.crm.properties.api.batch_api import BatchApi
from hubspot.crm.properties.api.core_api import CoreApi
from hubspot.crm.properties.api.groups_api import GroupsApi

# import ApiClient
from hubspot.crm.properties.api_client import ApiClient
from hubspot.crm.properties.configuration import Configuration
from hubspot.crm.properties.exceptions import OpenApiException
from hubspot.crm.properties.exceptions import ApiTypeError
from hubspot.crm.properties.exceptions import ApiValueError
from hubspot.crm.properties.exceptions import ApiKeyError
from hubspot.crm.properties.exceptions import ApiException

# import models into sdk package
from hubspot.crm.properties.models.batch_input_property_create import (
    BatchInputPropertyCreate,
)
from hubspot.crm.properties.models.batch_input_property_name import (
    BatchInputPropertyName,
)
from hubspot.crm.properties.models.batch_read_input_property_name import (
    BatchReadInputPropertyName,
)
from hubspot.crm.properties.models.batch_response_property import BatchResponseProperty
from hubspot.crm.properties.models.collection_response_property import (
    CollectionResponseProperty,
)
from hubspot.crm.properties.models.collection_response_property_group import (
    CollectionResponsePropertyGroup,
)
from hubspot.crm.properties.models.error import Error
from hubspot.crm.properties.models.error_category import ErrorCategory
from hubspot.crm.properties.models.error_detail import ErrorDetail
from hubspot.crm.properties.models.model_property import ModelProperty
from hubspot.crm.properties.models.next_page import NextPage
from hubspot.crm.properties.models.option import Option
from hubspot.crm.properties.models.option_input import OptionInput
from hubspot.crm.properties.models.paging import Paging
from hubspot.crm.properties.models.property_create import PropertyCreate
from hubspot.crm.properties.models.property_group import PropertyGroup
from hubspot.crm.properties.models.property_group_create import PropertyGroupCreate
from hubspot.crm.properties.models.property_group_update import PropertyGroupUpdate
from hubspot.crm.properties.models.property_modification_metadata import (
    PropertyModificationMetadata,
)
from hubspot.crm.properties.models.property_name import PropertyName
from hubspot.crm.properties.models.property_update import PropertyUpdate
from hubspot.crm.properties.models.standard_error import StandardError
