# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ConnectionArgs', 'Connection']

@pulumi.input_type
class ConnectionArgs:
    def __init__(__self__, *,
                 default_payload: pulumi.Input[str],
                 type: pulumi.Input[str],
                 url: pulumi.Input[str],
                 connection_subtype: Optional[pulumi.Input[str]] = None,
                 custom_headers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 headers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 webhook_type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Connection resource.
        :param pulumi.Input[str] default_payload: Default payload of the webhook.
        :param pulumi.Input[str] type: Type of connection. Only `WebhookConnection` is implemented right now.
        :param pulumi.Input[str] url: URL for the webhook connection.
        :param pulumi.Input[str] connection_subtype: The subtype of the connection. Valid values are `Incident` and `Event`. NOTE: This is only used for the `ServiceNow` webhook type.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] custom_headers: Map of custom webhook headers
        :param pulumi.Input[str] description: Description of the connection.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] headers: Map of access authorization headers.
        :param pulumi.Input[str] name: Name of connection. Name should be a valid alphanumeric value.
        :param pulumi.Input[str] webhook_type: Type of webhook. Valid values are `AWSLambda`, `Azure`, `Datadog`, `HipChat`, `PagerDuty`, `Slack`, `Webhook`, `NewRelic`, `MicrosoftTeams`, and `ServiceNow`. Default: `Webhook`
        """
        pulumi.set(__self__, "default_payload", default_payload)
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "url", url)
        if connection_subtype is not None:
            pulumi.set(__self__, "connection_subtype", connection_subtype)
        if custom_headers is not None:
            pulumi.set(__self__, "custom_headers", custom_headers)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if headers is not None:
            pulumi.set(__self__, "headers", headers)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if webhook_type is not None:
            pulumi.set(__self__, "webhook_type", webhook_type)

    @property
    @pulumi.getter(name="defaultPayload")
    def default_payload(self) -> pulumi.Input[str]:
        """
        Default payload of the webhook.
        """
        return pulumi.get(self, "default_payload")

    @default_payload.setter
    def default_payload(self, value: pulumi.Input[str]):
        pulumi.set(self, "default_payload", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        Type of connection. Only `WebhookConnection` is implemented right now.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def url(self) -> pulumi.Input[str]:
        """
        URL for the webhook connection.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: pulumi.Input[str]):
        pulumi.set(self, "url", value)

    @property
    @pulumi.getter(name="connectionSubtype")
    def connection_subtype(self) -> Optional[pulumi.Input[str]]:
        """
        The subtype of the connection. Valid values are `Incident` and `Event`. NOTE: This is only used for the `ServiceNow` webhook type.
        """
        return pulumi.get(self, "connection_subtype")

    @connection_subtype.setter
    def connection_subtype(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connection_subtype", value)

    @property
    @pulumi.getter(name="customHeaders")
    def custom_headers(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Map of custom webhook headers
        """
        return pulumi.get(self, "custom_headers")

    @custom_headers.setter
    def custom_headers(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "custom_headers", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the connection.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def headers(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Map of access authorization headers.
        """
        return pulumi.get(self, "headers")

    @headers.setter
    def headers(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "headers", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of connection. Name should be a valid alphanumeric value.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="webhookType")
    def webhook_type(self) -> Optional[pulumi.Input[str]]:
        """
        Type of webhook. Valid values are `AWSLambda`, `Azure`, `Datadog`, `HipChat`, `PagerDuty`, `Slack`, `Webhook`, `NewRelic`, `MicrosoftTeams`, and `ServiceNow`. Default: `Webhook`
        """
        return pulumi.get(self, "webhook_type")

    @webhook_type.setter
    def webhook_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "webhook_type", value)


@pulumi.input_type
class _ConnectionState:
    def __init__(__self__, *,
                 connection_subtype: Optional[pulumi.Input[str]] = None,
                 custom_headers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 default_payload: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 headers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 webhook_type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Connection resources.
        :param pulumi.Input[str] connection_subtype: The subtype of the connection. Valid values are `Incident` and `Event`. NOTE: This is only used for the `ServiceNow` webhook type.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] custom_headers: Map of custom webhook headers
        :param pulumi.Input[str] default_payload: Default payload of the webhook.
        :param pulumi.Input[str] description: Description of the connection.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] headers: Map of access authorization headers.
        :param pulumi.Input[str] name: Name of connection. Name should be a valid alphanumeric value.
        :param pulumi.Input[str] type: Type of connection. Only `WebhookConnection` is implemented right now.
        :param pulumi.Input[str] url: URL for the webhook connection.
        :param pulumi.Input[str] webhook_type: Type of webhook. Valid values are `AWSLambda`, `Azure`, `Datadog`, `HipChat`, `PagerDuty`, `Slack`, `Webhook`, `NewRelic`, `MicrosoftTeams`, and `ServiceNow`. Default: `Webhook`
        """
        if connection_subtype is not None:
            pulumi.set(__self__, "connection_subtype", connection_subtype)
        if custom_headers is not None:
            pulumi.set(__self__, "custom_headers", custom_headers)
        if default_payload is not None:
            pulumi.set(__self__, "default_payload", default_payload)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if headers is not None:
            pulumi.set(__self__, "headers", headers)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if url is not None:
            pulumi.set(__self__, "url", url)
        if webhook_type is not None:
            pulumi.set(__self__, "webhook_type", webhook_type)

    @property
    @pulumi.getter(name="connectionSubtype")
    def connection_subtype(self) -> Optional[pulumi.Input[str]]:
        """
        The subtype of the connection. Valid values are `Incident` and `Event`. NOTE: This is only used for the `ServiceNow` webhook type.
        """
        return pulumi.get(self, "connection_subtype")

    @connection_subtype.setter
    def connection_subtype(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connection_subtype", value)

    @property
    @pulumi.getter(name="customHeaders")
    def custom_headers(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Map of custom webhook headers
        """
        return pulumi.get(self, "custom_headers")

    @custom_headers.setter
    def custom_headers(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "custom_headers", value)

    @property
    @pulumi.getter(name="defaultPayload")
    def default_payload(self) -> Optional[pulumi.Input[str]]:
        """
        Default payload of the webhook.
        """
        return pulumi.get(self, "default_payload")

    @default_payload.setter
    def default_payload(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_payload", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the connection.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def headers(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Map of access authorization headers.
        """
        return pulumi.get(self, "headers")

    @headers.setter
    def headers(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "headers", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of connection. Name should be a valid alphanumeric value.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        Type of connection. Only `WebhookConnection` is implemented right now.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        """
        URL for the webhook connection.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)

    @property
    @pulumi.getter(name="webhookType")
    def webhook_type(self) -> Optional[pulumi.Input[str]]:
        """
        Type of webhook. Valid values are `AWSLambda`, `Azure`, `Datadog`, `HipChat`, `PagerDuty`, `Slack`, `Webhook`, `NewRelic`, `MicrosoftTeams`, and `ServiceNow`. Default: `Webhook`
        """
        return pulumi.get(self, "webhook_type")

    @webhook_type.setter
    def webhook_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "webhook_type", value)


class Connection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connection_subtype: Optional[pulumi.Input[str]] = None,
                 custom_headers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 default_payload: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 headers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 webhook_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides the ability to create, read, delete, update connections.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sumologic as sumologic

        connection = sumologic.Connection("connection",
            type="WebhookConnection",
            description="My description",
            url="https://connection-endpoint.com",
            headers={
                "X-Header": "my-header",
            },
            custom_headers={
                "X-custom": "my-custom-header",
            },
            default_payload=\"\"\"{
          "client" : "Sumo Logic",
          "eventType" : "{{Name}}",
          "description" : "{{Description}}",
          "search_url" : "{{QueryUrl}}",
          "num_records" : "{{NumRawResults}}",
          "search_results" : "{{AggregateResultsJson}}"
        }
        \"\"\",
            webhook_type="Webhook")
        ```

        ## Import

        Connections can be imported using the connection id, e.g.hcl

        ```sh
         $ pulumi import sumologic:index/connection:Connection test 1234567890
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] connection_subtype: The subtype of the connection. Valid values are `Incident` and `Event`. NOTE: This is only used for the `ServiceNow` webhook type.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] custom_headers: Map of custom webhook headers
        :param pulumi.Input[str] default_payload: Default payload of the webhook.
        :param pulumi.Input[str] description: Description of the connection.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] headers: Map of access authorization headers.
        :param pulumi.Input[str] name: Name of connection. Name should be a valid alphanumeric value.
        :param pulumi.Input[str] type: Type of connection. Only `WebhookConnection` is implemented right now.
        :param pulumi.Input[str] url: URL for the webhook connection.
        :param pulumi.Input[str] webhook_type: Type of webhook. Valid values are `AWSLambda`, `Azure`, `Datadog`, `HipChat`, `PagerDuty`, `Slack`, `Webhook`, `NewRelic`, `MicrosoftTeams`, and `ServiceNow`. Default: `Webhook`
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConnectionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides the ability to create, read, delete, update connections.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sumologic as sumologic

        connection = sumologic.Connection("connection",
            type="WebhookConnection",
            description="My description",
            url="https://connection-endpoint.com",
            headers={
                "X-Header": "my-header",
            },
            custom_headers={
                "X-custom": "my-custom-header",
            },
            default_payload=\"\"\"{
          "client" : "Sumo Logic",
          "eventType" : "{{Name}}",
          "description" : "{{Description}}",
          "search_url" : "{{QueryUrl}}",
          "num_records" : "{{NumRawResults}}",
          "search_results" : "{{AggregateResultsJson}}"
        }
        \"\"\",
            webhook_type="Webhook")
        ```

        ## Import

        Connections can be imported using the connection id, e.g.hcl

        ```sh
         $ pulumi import sumologic:index/connection:Connection test 1234567890
        ```

        :param str resource_name: The name of the resource.
        :param ConnectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConnectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connection_subtype: Optional[pulumi.Input[str]] = None,
                 custom_headers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 default_payload: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 headers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 webhook_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConnectionArgs.__new__(ConnectionArgs)

            __props__.__dict__["connection_subtype"] = connection_subtype
            __props__.__dict__["custom_headers"] = custom_headers
            if default_payload is None and not opts.urn:
                raise TypeError("Missing required property 'default_payload'")
            __props__.__dict__["default_payload"] = default_payload
            __props__.__dict__["description"] = description
            __props__.__dict__["headers"] = headers
            __props__.__dict__["name"] = name
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            if url is None and not opts.urn:
                raise TypeError("Missing required property 'url'")
            __props__.__dict__["url"] = url
            __props__.__dict__["webhook_type"] = webhook_type
        super(Connection, __self__).__init__(
            'sumologic:index/connection:Connection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            connection_subtype: Optional[pulumi.Input[str]] = None,
            custom_headers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            default_payload: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            headers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None,
            url: Optional[pulumi.Input[str]] = None,
            webhook_type: Optional[pulumi.Input[str]] = None) -> 'Connection':
        """
        Get an existing Connection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] connection_subtype: The subtype of the connection. Valid values are `Incident` and `Event`. NOTE: This is only used for the `ServiceNow` webhook type.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] custom_headers: Map of custom webhook headers
        :param pulumi.Input[str] default_payload: Default payload of the webhook.
        :param pulumi.Input[str] description: Description of the connection.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] headers: Map of access authorization headers.
        :param pulumi.Input[str] name: Name of connection. Name should be a valid alphanumeric value.
        :param pulumi.Input[str] type: Type of connection. Only `WebhookConnection` is implemented right now.
        :param pulumi.Input[str] url: URL for the webhook connection.
        :param pulumi.Input[str] webhook_type: Type of webhook. Valid values are `AWSLambda`, `Azure`, `Datadog`, `HipChat`, `PagerDuty`, `Slack`, `Webhook`, `NewRelic`, `MicrosoftTeams`, and `ServiceNow`. Default: `Webhook`
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ConnectionState.__new__(_ConnectionState)

        __props__.__dict__["connection_subtype"] = connection_subtype
        __props__.__dict__["custom_headers"] = custom_headers
        __props__.__dict__["default_payload"] = default_payload
        __props__.__dict__["description"] = description
        __props__.__dict__["headers"] = headers
        __props__.__dict__["name"] = name
        __props__.__dict__["type"] = type
        __props__.__dict__["url"] = url
        __props__.__dict__["webhook_type"] = webhook_type
        return Connection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="connectionSubtype")
    def connection_subtype(self) -> pulumi.Output[Optional[str]]:
        """
        The subtype of the connection. Valid values are `Incident` and `Event`. NOTE: This is only used for the `ServiceNow` webhook type.
        """
        return pulumi.get(self, "connection_subtype")

    @property
    @pulumi.getter(name="customHeaders")
    def custom_headers(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Map of custom webhook headers
        """
        return pulumi.get(self, "custom_headers")

    @property
    @pulumi.getter(name="defaultPayload")
    def default_payload(self) -> pulumi.Output[str]:
        """
        Default payload of the webhook.
        """
        return pulumi.get(self, "default_payload")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the connection.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def headers(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Map of access authorization headers.
        """
        return pulumi.get(self, "headers")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of connection. Name should be a valid alphanumeric value.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of connection. Only `WebhookConnection` is implemented right now.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[str]:
        """
        URL for the webhook connection.
        """
        return pulumi.get(self, "url")

    @property
    @pulumi.getter(name="webhookType")
    def webhook_type(self) -> pulumi.Output[Optional[str]]:
        """
        Type of webhook. Valid values are `AWSLambda`, `Azure`, `Datadog`, `HipChat`, `PagerDuty`, `Slack`, `Webhook`, `NewRelic`, `MicrosoftTeams`, and `ServiceNow`. Default: `Webhook`
        """
        return pulumi.get(self, "webhook_type")

