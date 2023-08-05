# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['JobArgs', 'Job']

@pulumi.input_type
class JobArgs:
    def __init__(__self__, *,
                 batch_pool_id: pulumi.Input[str],
                 common_environment_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 task_retry_maximum: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a Job resource.
        :param pulumi.Input[str] batch_pool_id: The ID of the Batch Pool. Changing this forces a new Batch Job to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] common_environment_properties: Specifies a map of common environment settings applied to this Batch Job. Changing this forces a new Batch Job to be created.
        :param pulumi.Input[str] display_name: The display name of this Batch Job. Changing this forces a new Batch Job to be created.
        :param pulumi.Input[str] name: The name which should be used for this Batch Job. Changing this forces a new Batch Job to be created.
        :param pulumi.Input[int] priority: The priority of this Batch Job, possible values can range from -1000 (lowest) to 1000 (highest). Defaults to `0`.
        :param pulumi.Input[int] task_retry_maximum: The number of retries to each Batch Task belongs to this Batch Job. If this is set to `0`, the Batch service does not retry Tasks. If this is set to `-1`, the Batch service retries Batch Tasks without limit. Default value is `0`.
        """
        pulumi.set(__self__, "batch_pool_id", batch_pool_id)
        if common_environment_properties is not None:
            pulumi.set(__self__, "common_environment_properties", common_environment_properties)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if task_retry_maximum is not None:
            pulumi.set(__self__, "task_retry_maximum", task_retry_maximum)

    @property
    @pulumi.getter(name="batchPoolId")
    def batch_pool_id(self) -> pulumi.Input[str]:
        """
        The ID of the Batch Pool. Changing this forces a new Batch Job to be created.
        """
        return pulumi.get(self, "batch_pool_id")

    @batch_pool_id.setter
    def batch_pool_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "batch_pool_id", value)

    @property
    @pulumi.getter(name="commonEnvironmentProperties")
    def common_environment_properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Specifies a map of common environment settings applied to this Batch Job. Changing this forces a new Batch Job to be created.
        """
        return pulumi.get(self, "common_environment_properties")

    @common_environment_properties.setter
    def common_environment_properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "common_environment_properties", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The display name of this Batch Job. Changing this forces a new Batch Job to be created.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Batch Job. Changing this forces a new Batch Job to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        """
        The priority of this Batch Job, possible values can range from -1000 (lowest) to 1000 (highest). Defaults to `0`.
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter(name="taskRetryMaximum")
    def task_retry_maximum(self) -> Optional[pulumi.Input[int]]:
        """
        The number of retries to each Batch Task belongs to this Batch Job. If this is set to `0`, the Batch service does not retry Tasks. If this is set to `-1`, the Batch service retries Batch Tasks without limit. Default value is `0`.
        """
        return pulumi.get(self, "task_retry_maximum")

    @task_retry_maximum.setter
    def task_retry_maximum(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "task_retry_maximum", value)


@pulumi.input_type
class _JobState:
    def __init__(__self__, *,
                 batch_pool_id: Optional[pulumi.Input[str]] = None,
                 common_environment_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 task_retry_maximum: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering Job resources.
        :param pulumi.Input[str] batch_pool_id: The ID of the Batch Pool. Changing this forces a new Batch Job to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] common_environment_properties: Specifies a map of common environment settings applied to this Batch Job. Changing this forces a new Batch Job to be created.
        :param pulumi.Input[str] display_name: The display name of this Batch Job. Changing this forces a new Batch Job to be created.
        :param pulumi.Input[str] name: The name which should be used for this Batch Job. Changing this forces a new Batch Job to be created.
        :param pulumi.Input[int] priority: The priority of this Batch Job, possible values can range from -1000 (lowest) to 1000 (highest). Defaults to `0`.
        :param pulumi.Input[int] task_retry_maximum: The number of retries to each Batch Task belongs to this Batch Job. If this is set to `0`, the Batch service does not retry Tasks. If this is set to `-1`, the Batch service retries Batch Tasks without limit. Default value is `0`.
        """
        if batch_pool_id is not None:
            pulumi.set(__self__, "batch_pool_id", batch_pool_id)
        if common_environment_properties is not None:
            pulumi.set(__self__, "common_environment_properties", common_environment_properties)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if task_retry_maximum is not None:
            pulumi.set(__self__, "task_retry_maximum", task_retry_maximum)

    @property
    @pulumi.getter(name="batchPoolId")
    def batch_pool_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Batch Pool. Changing this forces a new Batch Job to be created.
        """
        return pulumi.get(self, "batch_pool_id")

    @batch_pool_id.setter
    def batch_pool_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "batch_pool_id", value)

    @property
    @pulumi.getter(name="commonEnvironmentProperties")
    def common_environment_properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Specifies a map of common environment settings applied to this Batch Job. Changing this forces a new Batch Job to be created.
        """
        return pulumi.get(self, "common_environment_properties")

    @common_environment_properties.setter
    def common_environment_properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "common_environment_properties", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The display name of this Batch Job. Changing this forces a new Batch Job to be created.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Batch Job. Changing this forces a new Batch Job to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        """
        The priority of this Batch Job, possible values can range from -1000 (lowest) to 1000 (highest). Defaults to `0`.
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter(name="taskRetryMaximum")
    def task_retry_maximum(self) -> Optional[pulumi.Input[int]]:
        """
        The number of retries to each Batch Task belongs to this Batch Job. If this is set to `0`, the Batch service does not retry Tasks. If this is set to `-1`, the Batch service retries Batch Tasks without limit. Default value is `0`.
        """
        return pulumi.get(self, "task_retry_maximum")

    @task_retry_maximum.setter
    def task_retry_maximum(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "task_retry_maximum", value)


class Job(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 batch_pool_id: Optional[pulumi.Input[str]] = None,
                 common_environment_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 task_retry_maximum: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Manages a Batch Job.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="west europe")
        example_account = azure.batch.Account("exampleAccount",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location)
        example_pool = azure.batch.Pool("examplePool",
            resource_group_name=example_resource_group.name,
            account_name=example_account.name,
            node_agent_sku_id="batch.node.ubuntu 16.04",
            vm_size="Standard_A1",
            fixed_scale=azure.batch.PoolFixedScaleArgs(
                target_dedicated_nodes=1,
            ),
            storage_image_reference=azure.batch.PoolStorageImageReferenceArgs(
                publisher="Canonical",
                offer="UbuntuServer",
                sku="16.04.0-LTS",
                version="latest",
            ))
        example_job = azure.batch.Job("exampleJob", batch_pool_id=example_pool.id)
        ```

        ## Import

        Batch Jobs can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:batch/job:Job example /subscriptions/12345678-1234-9876-4563-123456789012/resourceGroups/resGroup1/providers/Microsoft.Batch/batchAccounts/account1/pools/pool1/jobs/job1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] batch_pool_id: The ID of the Batch Pool. Changing this forces a new Batch Job to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] common_environment_properties: Specifies a map of common environment settings applied to this Batch Job. Changing this forces a new Batch Job to be created.
        :param pulumi.Input[str] display_name: The display name of this Batch Job. Changing this forces a new Batch Job to be created.
        :param pulumi.Input[str] name: The name which should be used for this Batch Job. Changing this forces a new Batch Job to be created.
        :param pulumi.Input[int] priority: The priority of this Batch Job, possible values can range from -1000 (lowest) to 1000 (highest). Defaults to `0`.
        :param pulumi.Input[int] task_retry_maximum: The number of retries to each Batch Task belongs to this Batch Job. If this is set to `0`, the Batch service does not retry Tasks. If this is set to `-1`, the Batch service retries Batch Tasks without limit. Default value is `0`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: JobArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Batch Job.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="west europe")
        example_account = azure.batch.Account("exampleAccount",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location)
        example_pool = azure.batch.Pool("examplePool",
            resource_group_name=example_resource_group.name,
            account_name=example_account.name,
            node_agent_sku_id="batch.node.ubuntu 16.04",
            vm_size="Standard_A1",
            fixed_scale=azure.batch.PoolFixedScaleArgs(
                target_dedicated_nodes=1,
            ),
            storage_image_reference=azure.batch.PoolStorageImageReferenceArgs(
                publisher="Canonical",
                offer="UbuntuServer",
                sku="16.04.0-LTS",
                version="latest",
            ))
        example_job = azure.batch.Job("exampleJob", batch_pool_id=example_pool.id)
        ```

        ## Import

        Batch Jobs can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:batch/job:Job example /subscriptions/12345678-1234-9876-4563-123456789012/resourceGroups/resGroup1/providers/Microsoft.Batch/batchAccounts/account1/pools/pool1/jobs/job1
        ```

        :param str resource_name: The name of the resource.
        :param JobArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(JobArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 batch_pool_id: Optional[pulumi.Input[str]] = None,
                 common_environment_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 task_retry_maximum: Optional[pulumi.Input[int]] = None,
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
            __props__ = JobArgs.__new__(JobArgs)

            if batch_pool_id is None and not opts.urn:
                raise TypeError("Missing required property 'batch_pool_id'")
            __props__.__dict__["batch_pool_id"] = batch_pool_id
            __props__.__dict__["common_environment_properties"] = common_environment_properties
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["name"] = name
            __props__.__dict__["priority"] = priority
            __props__.__dict__["task_retry_maximum"] = task_retry_maximum
        super(Job, __self__).__init__(
            'azure:batch/job:Job',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            batch_pool_id: Optional[pulumi.Input[str]] = None,
            common_environment_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            priority: Optional[pulumi.Input[int]] = None,
            task_retry_maximum: Optional[pulumi.Input[int]] = None) -> 'Job':
        """
        Get an existing Job resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] batch_pool_id: The ID of the Batch Pool. Changing this forces a new Batch Job to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] common_environment_properties: Specifies a map of common environment settings applied to this Batch Job. Changing this forces a new Batch Job to be created.
        :param pulumi.Input[str] display_name: The display name of this Batch Job. Changing this forces a new Batch Job to be created.
        :param pulumi.Input[str] name: The name which should be used for this Batch Job. Changing this forces a new Batch Job to be created.
        :param pulumi.Input[int] priority: The priority of this Batch Job, possible values can range from -1000 (lowest) to 1000 (highest). Defaults to `0`.
        :param pulumi.Input[int] task_retry_maximum: The number of retries to each Batch Task belongs to this Batch Job. If this is set to `0`, the Batch service does not retry Tasks. If this is set to `-1`, the Batch service retries Batch Tasks without limit. Default value is `0`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _JobState.__new__(_JobState)

        __props__.__dict__["batch_pool_id"] = batch_pool_id
        __props__.__dict__["common_environment_properties"] = common_environment_properties
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["name"] = name
        __props__.__dict__["priority"] = priority
        __props__.__dict__["task_retry_maximum"] = task_retry_maximum
        return Job(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="batchPoolId")
    def batch_pool_id(self) -> pulumi.Output[str]:
        """
        The ID of the Batch Pool. Changing this forces a new Batch Job to be created.
        """
        return pulumi.get(self, "batch_pool_id")

    @property
    @pulumi.getter(name="commonEnvironmentProperties")
    def common_environment_properties(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Specifies a map of common environment settings applied to this Batch Job. Changing this forces a new Batch Job to be created.
        """
        return pulumi.get(self, "common_environment_properties")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        The display name of this Batch Job. Changing this forces a new Batch Job to be created.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name which should be used for this Batch Job. Changing this forces a new Batch Job to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[Optional[int]]:
        """
        The priority of this Batch Job, possible values can range from -1000 (lowest) to 1000 (highest). Defaults to `0`.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="taskRetryMaximum")
    def task_retry_maximum(self) -> pulumi.Output[Optional[int]]:
        """
        The number of retries to each Batch Task belongs to this Batch Job. If this is set to `0`, the Batch service does not retry Tasks. If this is set to `-1`, the Batch service retries Batch Tasks without limit. Default value is `0`.
        """
        return pulumi.get(self, "task_retry_maximum")

