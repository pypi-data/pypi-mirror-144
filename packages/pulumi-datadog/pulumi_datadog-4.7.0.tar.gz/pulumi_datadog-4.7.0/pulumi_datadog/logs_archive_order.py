# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['LogsArchiveOrderArgs', 'LogsArchiveOrder']

@pulumi.input_type
class LogsArchiveOrderArgs:
    def __init__(__self__, *,
                 archive_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a LogsArchiveOrder resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] archive_ids: The archive IDs list. The order of archive IDs in this attribute defines the overall archive order for logs. If `archive_ids` is empty or not specified, it will import the actual archive order, and create the resource. Otherwise, it will try to update the order.
        """
        if archive_ids is not None:
            pulumi.set(__self__, "archive_ids", archive_ids)

    @property
    @pulumi.getter(name="archiveIds")
    def archive_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The archive IDs list. The order of archive IDs in this attribute defines the overall archive order for logs. If `archive_ids` is empty or not specified, it will import the actual archive order, and create the resource. Otherwise, it will try to update the order.
        """
        return pulumi.get(self, "archive_ids")

    @archive_ids.setter
    def archive_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "archive_ids", value)


@pulumi.input_type
class _LogsArchiveOrderState:
    def __init__(__self__, *,
                 archive_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering LogsArchiveOrder resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] archive_ids: The archive IDs list. The order of archive IDs in this attribute defines the overall archive order for logs. If `archive_ids` is empty or not specified, it will import the actual archive order, and create the resource. Otherwise, it will try to update the order.
        """
        if archive_ids is not None:
            pulumi.set(__self__, "archive_ids", archive_ids)

    @property
    @pulumi.getter(name="archiveIds")
    def archive_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The archive IDs list. The order of archive IDs in this attribute defines the overall archive order for logs. If `archive_ids` is empty or not specified, it will import the actual archive order, and create the resource. Otherwise, it will try to update the order.
        """
        return pulumi.get(self, "archive_ids")

    @archive_ids.setter
    def archive_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "archive_ids", value)


class LogsArchiveOrder(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 archive_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Provides a Datadog [Logs Archive API](https://docs.datadoghq.com/api/v2/logs-archives/) resource, which is used to manage Datadog log archives order.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_datadog as datadog

        sample_archive_order = datadog.LogsArchiveOrder("sampleArchiveOrder", archive_ids=[
            datadog_logs_archive["sample_archive_1"]["id"],
            datadog_logs_archive["sample_archive_2"]["id"],
        ])
        ```

        ## Import

        # There must be at most one datadog_logs_archive_order resource. You can import the datadog_logs_archive_order or create an archive order.

        ```sh
         $ pulumi import datadog:index/logsArchiveOrder:LogsArchiveOrder name> archiveOrderID
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] archive_ids: The archive IDs list. The order of archive IDs in this attribute defines the overall archive order for logs. If `archive_ids` is empty or not specified, it will import the actual archive order, and create the resource. Otherwise, it will try to update the order.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[LogsArchiveOrderArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Datadog [Logs Archive API](https://docs.datadoghq.com/api/v2/logs-archives/) resource, which is used to manage Datadog log archives order.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_datadog as datadog

        sample_archive_order = datadog.LogsArchiveOrder("sampleArchiveOrder", archive_ids=[
            datadog_logs_archive["sample_archive_1"]["id"],
            datadog_logs_archive["sample_archive_2"]["id"],
        ])
        ```

        ## Import

        # There must be at most one datadog_logs_archive_order resource. You can import the datadog_logs_archive_order or create an archive order.

        ```sh
         $ pulumi import datadog:index/logsArchiveOrder:LogsArchiveOrder name> archiveOrderID
        ```

        :param str resource_name: The name of the resource.
        :param LogsArchiveOrderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LogsArchiveOrderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 archive_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
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
            __props__ = LogsArchiveOrderArgs.__new__(LogsArchiveOrderArgs)

            __props__.__dict__["archive_ids"] = archive_ids
        super(LogsArchiveOrder, __self__).__init__(
            'datadog:index/logsArchiveOrder:LogsArchiveOrder',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            archive_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'LogsArchiveOrder':
        """
        Get an existing LogsArchiveOrder resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] archive_ids: The archive IDs list. The order of archive IDs in this attribute defines the overall archive order for logs. If `archive_ids` is empty or not specified, it will import the actual archive order, and create the resource. Otherwise, it will try to update the order.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _LogsArchiveOrderState.__new__(_LogsArchiveOrderState)

        __props__.__dict__["archive_ids"] = archive_ids
        return LogsArchiveOrder(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="archiveIds")
    def archive_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        The archive IDs list. The order of archive IDs in this attribute defines the overall archive order for logs. If `archive_ids` is empty or not specified, it will import the actual archive order, and create the resource. Otherwise, it will try to update the order.
        """
        return pulumi.get(self, "archive_ids")

