# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['WebhookArgs', 'Webhook']

@pulumi.input_type
class WebhookArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 url: pulumi.Input[str],
                 custom_headers: Optional[pulumi.Input[str]] = None,
                 encode_as: Optional[pulumi.Input[str]] = None,
                 payload: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Webhook resource.
        :param pulumi.Input[str] name: The name of the webhook. It corresponds with `<WEBHOOK_NAME>`.
        :param pulumi.Input[str] url: The URL of the webhook.
        :param pulumi.Input[str] custom_headers: The headers attached to the webhook.
        :param pulumi.Input[str] encode_as: Encoding type. Valid values are `json`, `form`.
        :param pulumi.Input[str] payload: The payload of the webhook.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "url", url)
        if custom_headers is not None:
            pulumi.set(__self__, "custom_headers", custom_headers)
        if encode_as is not None:
            pulumi.set(__self__, "encode_as", encode_as)
        if payload is not None:
            pulumi.set(__self__, "payload", payload)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the webhook. It corresponds with `<WEBHOOK_NAME>`.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def url(self) -> pulumi.Input[str]:
        """
        The URL of the webhook.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: pulumi.Input[str]):
        pulumi.set(self, "url", value)

    @property
    @pulumi.getter(name="customHeaders")
    def custom_headers(self) -> Optional[pulumi.Input[str]]:
        """
        The headers attached to the webhook.
        """
        return pulumi.get(self, "custom_headers")

    @custom_headers.setter
    def custom_headers(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_headers", value)

    @property
    @pulumi.getter(name="encodeAs")
    def encode_as(self) -> Optional[pulumi.Input[str]]:
        """
        Encoding type. Valid values are `json`, `form`.
        """
        return pulumi.get(self, "encode_as")

    @encode_as.setter
    def encode_as(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "encode_as", value)

    @property
    @pulumi.getter
    def payload(self) -> Optional[pulumi.Input[str]]:
        """
        The payload of the webhook.
        """
        return pulumi.get(self, "payload")

    @payload.setter
    def payload(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "payload", value)


@pulumi.input_type
class _WebhookState:
    def __init__(__self__, *,
                 custom_headers: Optional[pulumi.Input[str]] = None,
                 encode_as: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 payload: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Webhook resources.
        :param pulumi.Input[str] custom_headers: The headers attached to the webhook.
        :param pulumi.Input[str] encode_as: Encoding type. Valid values are `json`, `form`.
        :param pulumi.Input[str] name: The name of the webhook. It corresponds with `<WEBHOOK_NAME>`.
        :param pulumi.Input[str] payload: The payload of the webhook.
        :param pulumi.Input[str] url: The URL of the webhook.
        """
        if custom_headers is not None:
            pulumi.set(__self__, "custom_headers", custom_headers)
        if encode_as is not None:
            pulumi.set(__self__, "encode_as", encode_as)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if payload is not None:
            pulumi.set(__self__, "payload", payload)
        if url is not None:
            pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter(name="customHeaders")
    def custom_headers(self) -> Optional[pulumi.Input[str]]:
        """
        The headers attached to the webhook.
        """
        return pulumi.get(self, "custom_headers")

    @custom_headers.setter
    def custom_headers(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_headers", value)

    @property
    @pulumi.getter(name="encodeAs")
    def encode_as(self) -> Optional[pulumi.Input[str]]:
        """
        Encoding type. Valid values are `json`, `form`.
        """
        return pulumi.get(self, "encode_as")

    @encode_as.setter
    def encode_as(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "encode_as", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the webhook. It corresponds with `<WEBHOOK_NAME>`.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def payload(self) -> Optional[pulumi.Input[str]]:
        """
        The payload of the webhook.
        """
        return pulumi.get(self, "payload")

    @payload.setter
    def payload(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "payload", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        """
        The URL of the webhook.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)


class Webhook(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 custom_headers: Optional[pulumi.Input[str]] = None,
                 encode_as: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 payload: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Datadog webhook resource. This can be used to create and manage Datadog webhooks.

        ## Example Usage

        ```python
        import pulumi
        import json
        import pulumi_datadog as datadog

        # Create a new Datadog webhook
        foo = datadog.Webhook("foo",
            name="test-webhook",
            url="example.com",
            encode_as="json",
            custom_headers=json.dumps({
                "custom": "header",
            }),
            payload=json.dumps({
                "custom": "payload",
            }))
        ```

        ## Import

        ```sh
         $ pulumi import datadog:index/webhook:Webhook foo example-webhook
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] custom_headers: The headers attached to the webhook.
        :param pulumi.Input[str] encode_as: Encoding type. Valid values are `json`, `form`.
        :param pulumi.Input[str] name: The name of the webhook. It corresponds with `<WEBHOOK_NAME>`.
        :param pulumi.Input[str] payload: The payload of the webhook.
        :param pulumi.Input[str] url: The URL of the webhook.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WebhookArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Datadog webhook resource. This can be used to create and manage Datadog webhooks.

        ## Example Usage

        ```python
        import pulumi
        import json
        import pulumi_datadog as datadog

        # Create a new Datadog webhook
        foo = datadog.Webhook("foo",
            name="test-webhook",
            url="example.com",
            encode_as="json",
            custom_headers=json.dumps({
                "custom": "header",
            }),
            payload=json.dumps({
                "custom": "payload",
            }))
        ```

        ## Import

        ```sh
         $ pulumi import datadog:index/webhook:Webhook foo example-webhook
        ```

        :param str resource_name: The name of the resource.
        :param WebhookArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WebhookArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 custom_headers: Optional[pulumi.Input[str]] = None,
                 encode_as: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 payload: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None,
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
            __props__ = WebhookArgs.__new__(WebhookArgs)

            __props__.__dict__["custom_headers"] = custom_headers
            __props__.__dict__["encode_as"] = encode_as
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            __props__.__dict__["payload"] = payload
            if url is None and not opts.urn:
                raise TypeError("Missing required property 'url'")
            __props__.__dict__["url"] = url
        super(Webhook, __self__).__init__(
            'datadog:index/webhook:Webhook',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            custom_headers: Optional[pulumi.Input[str]] = None,
            encode_as: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            payload: Optional[pulumi.Input[str]] = None,
            url: Optional[pulumi.Input[str]] = None) -> 'Webhook':
        """
        Get an existing Webhook resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] custom_headers: The headers attached to the webhook.
        :param pulumi.Input[str] encode_as: Encoding type. Valid values are `json`, `form`.
        :param pulumi.Input[str] name: The name of the webhook. It corresponds with `<WEBHOOK_NAME>`.
        :param pulumi.Input[str] payload: The payload of the webhook.
        :param pulumi.Input[str] url: The URL of the webhook.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _WebhookState.__new__(_WebhookState)

        __props__.__dict__["custom_headers"] = custom_headers
        __props__.__dict__["encode_as"] = encode_as
        __props__.__dict__["name"] = name
        __props__.__dict__["payload"] = payload
        __props__.__dict__["url"] = url
        return Webhook(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="customHeaders")
    def custom_headers(self) -> pulumi.Output[Optional[str]]:
        """
        The headers attached to the webhook.
        """
        return pulumi.get(self, "custom_headers")

    @property
    @pulumi.getter(name="encodeAs")
    def encode_as(self) -> pulumi.Output[str]:
        """
        Encoding type. Valid values are `json`, `form`.
        """
        return pulumi.get(self, "encode_as")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the webhook. It corresponds with `<WEBHOOK_NAME>`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def payload(self) -> pulumi.Output[str]:
        """
        The payload of the webhook.
        """
        return pulumi.get(self, "payload")

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[str]:
        """
        The URL of the webhook.
        """
        return pulumi.get(self, "url")

