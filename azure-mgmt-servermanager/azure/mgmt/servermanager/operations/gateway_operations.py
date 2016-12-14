# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.pipeline import ClientRawResponse
from msrestazure.azure_operation import AzureOperationPoller
import uuid

from .. import models


class GatewayOperations(object):
    """GatewayOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An objec model deserializer.
    """

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config

    def create(
            self, resource_group_name, gateway_name, location=None, tags=None, upgrade_mode=None, custom_headers=None, raw=False, **operation_config):
        """Creates or updates a ManagementService gateway.

        :param resource_group_name: The resource group name uniquely
         identifies the resource group within the user subscriptionId.
        :type resource_group_name: str
        :param gateway_name: The gateway name (256 characters maximum).
        :type gateway_name: str
        :param location: Location of the resource.
        :type location: str
        :param tags: Resource tags.
        :type tags: object
        :param upgrade_mode: The upgradeMode property gives the flexibility to
         gateway to auto upgrade itself. If properties value not specified,
         then we assume upgradeMode = Automatic. Possible values include:
         'Manual', 'Automatic'
        :type upgrade_mode: str or :class:`upgradeMode
         <azure.mgmt.servermanager.models.upgradeMode>`
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :rtype:
         :class:`AzureOperationPoller<msrestazure.azure_operation.AzureOperationPoller>`
         instance that returns :class:`GatewayResource
         <azure.mgmt.servermanager.models.GatewayResource>`
        :rtype: :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
         if raw=true
        :raises:
         :class:`ErrorException<azure.mgmt.servermanager.models.ErrorException>`
        """
        gateway_parameters = models.GatewayParameters(location=location, tags=tags, upgrade_mode=upgrade_mode)

        # Construct URL
        url = '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServerManagement/gateways/{gatewayName}'
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', min_length=3, pattern='[a-zA-Z0-9]+'),
            'gatewayName': self._serialize.url("gateway_name", gateway_name, 'str', max_length=256, min_length=1, pattern='^[a-zA-Z0-9][a-zA-Z0-9_.-]*$')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.config.api_version", self.config.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(gateway_parameters, 'GatewayParameters')

        # Construct and send request
        def long_running_send():

            request = self._client.put(url, query_parameters)
            return self._client.send(
                request, header_parameters, body_content, **operation_config)

        def get_long_running_status(status_link, headers=None):

            request = self._client.get(status_link)
            if headers:
                request.headers.update(headers)
            return self._client.send(
                request, header_parameters, **operation_config)

        def get_long_running_output(response):

            if response.status_code not in [200, 201]:
                raise models.ErrorException(self._deserialize, response)

            deserialized = None

            if response.status_code == 200:
                deserialized = self._deserialize('GatewayResource', response)
            if response.status_code == 201:
                deserialized = self._deserialize('GatewayResource', response)

            if raw:
                client_raw_response = ClientRawResponse(deserialized, response)
                return client_raw_response

            return deserialized

        if raw:
            response = long_running_send()
            return get_long_running_output(response)

        long_running_operation_timeout = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        return AzureOperationPoller(
            long_running_send, get_long_running_output,
            get_long_running_status, long_running_operation_timeout)

    def update(
            self, resource_group_name, gateway_name, location=None, tags=None, upgrade_mode=None, custom_headers=None, raw=False, **operation_config):
        """Updates a gateway belonging to a resource group.

        :param resource_group_name: The resource group name uniquely
         identifies the resource group within the user subscriptionId.
        :type resource_group_name: str
        :param gateway_name: The gateway name (256 characters maximum).
        :type gateway_name: str
        :param location: Location of the resource.
        :type location: str
        :param tags: Resource tags.
        :type tags: object
        :param upgrade_mode: The upgradeMode property gives the flexibility to
         gateway to auto upgrade itself. If properties value not specified,
         then we assume upgradeMode = Automatic. Possible values include:
         'Manual', 'Automatic'
        :type upgrade_mode: str or :class:`upgradeMode
         <azure.mgmt.servermanager.models.upgradeMode>`
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :rtype:
         :class:`AzureOperationPoller<msrestazure.azure_operation.AzureOperationPoller>`
         instance that returns :class:`GatewayResource
         <azure.mgmt.servermanager.models.GatewayResource>`
        :rtype: :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
         if raw=true
        :raises:
         :class:`ErrorException<azure.mgmt.servermanager.models.ErrorException>`
        """
        gateway_parameters = models.GatewayParameters(location=location, tags=tags, upgrade_mode=upgrade_mode)

        # Construct URL
        url = '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServerManagement/gateways/{gatewayName}'
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', min_length=3, pattern='[a-zA-Z0-9]+'),
            'gatewayName': self._serialize.url("gateway_name", gateway_name, 'str', max_length=256, min_length=1, pattern='^[a-zA-Z0-9][a-zA-Z0-9_.-]*$')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.config.api_version", self.config.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(gateway_parameters, 'GatewayParameters')

        # Construct and send request
        def long_running_send():

            request = self._client.patch(url, query_parameters)
            return self._client.send(
                request, header_parameters, body_content, **operation_config)

        def get_long_running_status(status_link, headers=None):

            request = self._client.get(status_link)
            if headers:
                request.headers.update(headers)
            return self._client.send(
                request, header_parameters, **operation_config)

        def get_long_running_output(response):

            if response.status_code not in [200, 202]:
                raise models.ErrorException(self._deserialize, response)

            deserialized = None

            if response.status_code == 200:
                deserialized = self._deserialize('GatewayResource', response)

            if raw:
                client_raw_response = ClientRawResponse(deserialized, response)
                return client_raw_response

            return deserialized

        if raw:
            response = long_running_send()
            return get_long_running_output(response)

        long_running_operation_timeout = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        return AzureOperationPoller(
            long_running_send, get_long_running_output,
            get_long_running_status, long_running_operation_timeout)

    def delete(
            self, resource_group_name, gateway_name, custom_headers=None, raw=False, **operation_config):
        """Deletes a gateway from a resource group.

        :param resource_group_name: The resource group name uniquely
         identifies the resource group within the user subscriptionId.
        :type resource_group_name: str
        :param gateway_name: The gateway name (256 characters maximum).
        :type gateway_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :rtype: None
        :rtype: :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
         if raw=true
        :raises:
         :class:`ErrorException<azure.mgmt.servermanager.models.ErrorException>`
        """
        # Construct URL
        url = '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServerManagement/gateways/{gatewayName}'
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', min_length=3, pattern='[a-zA-Z0-9]+'),
            'gatewayName': self._serialize.url("gateway_name", gateway_name, 'str', max_length=256, min_length=1, pattern='^[a-zA-Z0-9][a-zA-Z0-9_.-]*$')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.config.api_version", self.config.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, **operation_config)

        if response.status_code not in [200, 204]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    def get(
            self, resource_group_name, gateway_name, expand=None, custom_headers=None, raw=False, **operation_config):
        """Gets a gateway.

        :param resource_group_name: The resource group name uniquely
         identifies the resource group within the user subscriptionId.
        :type resource_group_name: str
        :param gateway_name: The gateway name (256 characters maximum)
        :type gateway_name: str
        :param expand: Gets subscription credentials which uniquely identify
         Microsoft Azure subscription. The subscription ID forms part of the
         URI for every service call. Possible values include: 'status',
         'download'
        :type expand: str or :class:`GatewayExpandOption
         <azure.mgmt.servermanager.models.GatewayExpandOption>`
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :rtype: :class:`GatewayResource
         <azure.mgmt.servermanager.models.GatewayResource>`
        :rtype: :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
         if raw=true
        :raises:
         :class:`ErrorException<azure.mgmt.servermanager.models.ErrorException>`
        """
        # Construct URL
        url = '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServerManagement/gateways/{gatewayName}'
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', min_length=3, pattern='[a-zA-Z0-9]+'),
            'gatewayName': self._serialize.url("gateway_name", gateway_name, 'str', max_length=256, min_length=1, pattern='^[a-zA-Z0-9][a-zA-Z0-9_.-]*$')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.config.api_version", self.config.api_version, 'str')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query("expand", expand, 'GatewayExpandOption')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('GatewayResource', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def list(
            self, custom_headers=None, raw=False, **operation_config):
        """Returns gateways in a subscription.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :rtype: :class:`GatewayResourcePaged
         <azure.mgmt.servermanager.models.GatewayResourcePaged>`
        :raises:
         :class:`ErrorException<azure.mgmt.servermanager.models.ErrorException>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = '/subscriptions/{subscriptionId}/providers/Microsoft.ServerManagement/gateways'
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.config.api_version", self.config.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters)
            response = self._client.send(
                request, header_parameters, **operation_config)

            if response.status_code not in [200]:
                raise models.ErrorException(self._deserialize, response)

            return response

        # Deserialize response
        deserialized = models.GatewayResourcePaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.GatewayResourcePaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized

    def list_for_resource_group(
            self, resource_group_name, custom_headers=None, raw=False, **operation_config):
        """Returns gateways in a resource group.

        :param resource_group_name: The resource group name uniquely
         identifies the resource group within the user subscriptionId.
        :type resource_group_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :rtype: :class:`GatewayResourcePaged
         <azure.mgmt.servermanager.models.GatewayResourcePaged>`
        :raises:
         :class:`ErrorException<azure.mgmt.servermanager.models.ErrorException>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServerManagement/gateways'
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', min_length=3, pattern='[a-zA-Z0-9]+')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.config.api_version", self.config.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters)
            response = self._client.send(
                request, header_parameters, **operation_config)

            if response.status_code not in [200]:
                raise models.ErrorException(self._deserialize, response)

            return response

        # Deserialize response
        deserialized = models.GatewayResourcePaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.GatewayResourcePaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized

    def upgrade(
            self, resource_group_name, gateway_name, custom_headers=None, raw=False, **operation_config):
        """Upgrades a gateway.

        :param resource_group_name: The resource group name uniquely
         identifies the resource group within the user subscriptionId.
        :type resource_group_name: str
        :param gateway_name: The gateway name (256 characters maximum).
        :type gateway_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :rtype:
         :class:`AzureOperationPoller<msrestazure.azure_operation.AzureOperationPoller>`
         instance that returns None
        :rtype: :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
         if raw=true
        :raises:
         :class:`ErrorException<azure.mgmt.servermanager.models.ErrorException>`
        """
        # Construct URL
        url = '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServerManagement/gateways/{gatewayName}/upgradetolatest'
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', min_length=3, pattern='[a-zA-Z0-9]+'),
            'gatewayName': self._serialize.url("gateway_name", gateway_name, 'str', max_length=256, min_length=1, pattern='^[a-zA-Z0-9][a-zA-Z0-9_.-]*$')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.config.api_version", self.config.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        def long_running_send():

            request = self._client.post(url, query_parameters)
            return self._client.send(request, header_parameters, **operation_config)

        def get_long_running_status(status_link, headers=None):

            request = self._client.get(status_link)
            if headers:
                request.headers.update(headers)
            return self._client.send(
                request, header_parameters, **operation_config)

        def get_long_running_output(response):

            if response.status_code not in [200, 202]:
                raise models.ErrorException(self._deserialize, response)

            if raw:
                client_raw_response = ClientRawResponse(None, response)
                return client_raw_response

        if raw:
            response = long_running_send()
            return get_long_running_output(response)

        long_running_operation_timeout = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        return AzureOperationPoller(
            long_running_send, get_long_running_output,
            get_long_running_status, long_running_operation_timeout)

    def regenerate_profile(
            self, resource_group_name, gateway_name, custom_headers=None, raw=False, **operation_config):
        """Regenerate a gateway's profile.

        :param resource_group_name: The resource group name uniquely
         identifies the resource group within the user subscriptionId.
        :type resource_group_name: str
        :param gateway_name: The gateway name (256 characters maximum).
        :type gateway_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :rtype:
         :class:`AzureOperationPoller<msrestazure.azure_operation.AzureOperationPoller>`
         instance that returns None
        :rtype: :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
         if raw=true
        :raises:
         :class:`ErrorException<azure.mgmt.servermanager.models.ErrorException>`
        """
        # Construct URL
        url = '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServerManagement/gateways/{gatewayName}/regenerateprofile'
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', min_length=3, pattern='[a-zA-Z0-9]+'),
            'gatewayName': self._serialize.url("gateway_name", gateway_name, 'str', max_length=256, min_length=1, pattern='^[a-zA-Z0-9][a-zA-Z0-9_.-]*$')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.config.api_version", self.config.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        def long_running_send():

            request = self._client.post(url, query_parameters)
            return self._client.send(request, header_parameters, **operation_config)

        def get_long_running_status(status_link, headers=None):

            request = self._client.get(status_link)
            if headers:
                request.headers.update(headers)
            return self._client.send(
                request, header_parameters, **operation_config)

        def get_long_running_output(response):

            if response.status_code not in [200, 202]:
                raise models.ErrorException(self._deserialize, response)

            if raw:
                client_raw_response = ClientRawResponse(None, response)
                return client_raw_response

        if raw:
            response = long_running_send()
            return get_long_running_output(response)

        long_running_operation_timeout = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        return AzureOperationPoller(
            long_running_send, get_long_running_output,
            get_long_running_status, long_running_operation_timeout)

    def get_profile(
            self, resource_group_name, gateway_name, custom_headers=None, raw=False, **operation_config):
        """Gets a gateway profile.

        :param resource_group_name: The resource group name uniquely
         identifies the resource group within the user subscriptionId.
        :type resource_group_name: str
        :param gateway_name: The gateway name (256 characters maximum).
        :type gateway_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :rtype:
         :class:`AzureOperationPoller<msrestazure.azure_operation.AzureOperationPoller>`
         instance that returns :class:`GatewayProfile
         <azure.mgmt.servermanager.models.GatewayProfile>`
        :rtype: :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
         if raw=true
        :raises:
         :class:`ErrorException<azure.mgmt.servermanager.models.ErrorException>`
        """
        # Construct URL
        url = '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServerManagement/gateways/{gatewayName}/profile'
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', min_length=3, pattern='[a-zA-Z0-9]+'),
            'gatewayName': self._serialize.url("gateway_name", gateway_name, 'str', max_length=256, min_length=1, pattern='^[a-zA-Z0-9][a-zA-Z0-9_.-]*$')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.config.api_version", self.config.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        def long_running_send():

            request = self._client.post(url, query_parameters)
            return self._client.send(request, header_parameters, **operation_config)

        def get_long_running_status(status_link, headers=None):

            request = self._client.get(status_link)
            if headers:
                request.headers.update(headers)
            return self._client.send(
                request, header_parameters, **operation_config)

        def get_long_running_output(response):

            if response.status_code not in [200, 202]:
                raise models.ErrorException(self._deserialize, response)

            deserialized = None

            if response.status_code == 200:
                deserialized = self._deserialize('GatewayProfile', response)

            if raw:
                client_raw_response = ClientRawResponse(deserialized, response)
                return client_raw_response

            return deserialized

        if raw:
            response = long_running_send()
            return get_long_running_output(response)

        long_running_operation_timeout = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        return AzureOperationPoller(
            long_running_send, get_long_running_output,
            get_long_running_status, long_running_operation_timeout)