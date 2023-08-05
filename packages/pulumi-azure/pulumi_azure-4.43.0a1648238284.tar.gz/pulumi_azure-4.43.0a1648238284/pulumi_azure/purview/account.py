# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['AccountArgs', 'Account']

@pulumi.input_type
class AccountArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 location: Optional[pulumi.Input[str]] = None,
                 managed_resource_group_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 public_network_enabled: Optional[pulumi.Input[bool]] = None,
                 sku_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Account resource.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Purview Account should exist. Changing this forces a new Purview Account to be created.
        :param pulumi.Input[str] location: The Azure Region where the Purview Account should exist. Changing this forces a new Purview Account to be created.
        :param pulumi.Input[str] managed_resource_group_name: The name which should be used for the new Resource Group where Purview Account creates the managed resources. Changing this forces a new Purview Account to be created.
        :param pulumi.Input[str] name: The name which should be used for this Purview Account. Changing this forces a new Purview Account to be created.
        :param pulumi.Input[bool] public_network_enabled: Should the Purview Account be visible to the public network? Defaults to `true`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags which should be assigned to the Purview Account.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if managed_resource_group_name is not None:
            pulumi.set(__self__, "managed_resource_group_name", managed_resource_group_name)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if public_network_enabled is not None:
            pulumi.set(__self__, "public_network_enabled", public_network_enabled)
        if sku_name is not None:
            warnings.warn("""This property can no longer be specified on create/update, it can only be updated by creating a support ticket at Azure""", DeprecationWarning)
            pulumi.log.warn("""sku_name is deprecated: This property can no longer be specified on create/update, it can only be updated by creating a support ticket at Azure""")
        if sku_name is not None:
            pulumi.set(__self__, "sku_name", sku_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the Resource Group where the Purview Account should exist. Changing this forces a new Purview Account to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The Azure Region where the Purview Account should exist. Changing this forces a new Purview Account to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="managedResourceGroupName")
    def managed_resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for the new Resource Group where Purview Account creates the managed resources. Changing this forces a new Purview Account to be created.
        """
        return pulumi.get(self, "managed_resource_group_name")

    @managed_resource_group_name.setter
    def managed_resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "managed_resource_group_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Purview Account. Changing this forces a new Purview Account to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="publicNetworkEnabled")
    def public_network_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Should the Purview Account be visible to the public network? Defaults to `true`.
        """
        return pulumi.get(self, "public_network_enabled")

    @public_network_enabled.setter
    def public_network_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "public_network_enabled", value)

    @property
    @pulumi.getter(name="skuName")
    def sku_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "sku_name")

    @sku_name.setter
    def sku_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sku_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of tags which should be assigned to the Purview Account.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _AccountState:
    def __init__(__self__, *,
                 atlas_kafka_endpoint_primary_connection_string: Optional[pulumi.Input[str]] = None,
                 atlas_kafka_endpoint_secondary_connection_string: Optional[pulumi.Input[str]] = None,
                 catalog_endpoint: Optional[pulumi.Input[str]] = None,
                 guardian_endpoint: Optional[pulumi.Input[str]] = None,
                 identities: Optional[pulumi.Input[Sequence[pulumi.Input['AccountIdentityArgs']]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 managed_resource_group_name: Optional[pulumi.Input[str]] = None,
                 managed_resources: Optional[pulumi.Input[Sequence[pulumi.Input['AccountManagedResourceArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 public_network_enabled: Optional[pulumi.Input[bool]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scan_endpoint: Optional[pulumi.Input[str]] = None,
                 sku_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering Account resources.
        :param pulumi.Input[str] atlas_kafka_endpoint_primary_connection_string: Atlas Kafka endpoint primary connection string.
        :param pulumi.Input[str] atlas_kafka_endpoint_secondary_connection_string: Atlas Kafka endpoint secondary connection string.
        :param pulumi.Input[str] catalog_endpoint: Catalog endpoint.
        :param pulumi.Input[str] guardian_endpoint: Guardian endpoint.
        :param pulumi.Input[Sequence[pulumi.Input['AccountIdentityArgs']]] identities: A `identity` block as defined below.
        :param pulumi.Input[str] location: The Azure Region where the Purview Account should exist. Changing this forces a new Purview Account to be created.
        :param pulumi.Input[str] managed_resource_group_name: The name which should be used for the new Resource Group where Purview Account creates the managed resources. Changing this forces a new Purview Account to be created.
        :param pulumi.Input[Sequence[pulumi.Input['AccountManagedResourceArgs']]] managed_resources: A `managed_resources` block as defined below.
        :param pulumi.Input[str] name: The name which should be used for this Purview Account. Changing this forces a new Purview Account to be created.
        :param pulumi.Input[bool] public_network_enabled: Should the Purview Account be visible to the public network? Defaults to `true`.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Purview Account should exist. Changing this forces a new Purview Account to be created.
        :param pulumi.Input[str] scan_endpoint: Scan endpoint.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags which should be assigned to the Purview Account.
        """
        if atlas_kafka_endpoint_primary_connection_string is not None:
            pulumi.set(__self__, "atlas_kafka_endpoint_primary_connection_string", atlas_kafka_endpoint_primary_connection_string)
        if atlas_kafka_endpoint_secondary_connection_string is not None:
            pulumi.set(__self__, "atlas_kafka_endpoint_secondary_connection_string", atlas_kafka_endpoint_secondary_connection_string)
        if catalog_endpoint is not None:
            pulumi.set(__self__, "catalog_endpoint", catalog_endpoint)
        if guardian_endpoint is not None:
            pulumi.set(__self__, "guardian_endpoint", guardian_endpoint)
        if identities is not None:
            pulumi.set(__self__, "identities", identities)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if managed_resource_group_name is not None:
            pulumi.set(__self__, "managed_resource_group_name", managed_resource_group_name)
        if managed_resources is not None:
            pulumi.set(__self__, "managed_resources", managed_resources)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if public_network_enabled is not None:
            pulumi.set(__self__, "public_network_enabled", public_network_enabled)
        if resource_group_name is not None:
            pulumi.set(__self__, "resource_group_name", resource_group_name)
        if scan_endpoint is not None:
            pulumi.set(__self__, "scan_endpoint", scan_endpoint)
        if sku_name is not None:
            warnings.warn("""This property can no longer be specified on create/update, it can only be updated by creating a support ticket at Azure""", DeprecationWarning)
            pulumi.log.warn("""sku_name is deprecated: This property can no longer be specified on create/update, it can only be updated by creating a support ticket at Azure""")
        if sku_name is not None:
            pulumi.set(__self__, "sku_name", sku_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="atlasKafkaEndpointPrimaryConnectionString")
    def atlas_kafka_endpoint_primary_connection_string(self) -> Optional[pulumi.Input[str]]:
        """
        Atlas Kafka endpoint primary connection string.
        """
        return pulumi.get(self, "atlas_kafka_endpoint_primary_connection_string")

    @atlas_kafka_endpoint_primary_connection_string.setter
    def atlas_kafka_endpoint_primary_connection_string(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "atlas_kafka_endpoint_primary_connection_string", value)

    @property
    @pulumi.getter(name="atlasKafkaEndpointSecondaryConnectionString")
    def atlas_kafka_endpoint_secondary_connection_string(self) -> Optional[pulumi.Input[str]]:
        """
        Atlas Kafka endpoint secondary connection string.
        """
        return pulumi.get(self, "atlas_kafka_endpoint_secondary_connection_string")

    @atlas_kafka_endpoint_secondary_connection_string.setter
    def atlas_kafka_endpoint_secondary_connection_string(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "atlas_kafka_endpoint_secondary_connection_string", value)

    @property
    @pulumi.getter(name="catalogEndpoint")
    def catalog_endpoint(self) -> Optional[pulumi.Input[str]]:
        """
        Catalog endpoint.
        """
        return pulumi.get(self, "catalog_endpoint")

    @catalog_endpoint.setter
    def catalog_endpoint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "catalog_endpoint", value)

    @property
    @pulumi.getter(name="guardianEndpoint")
    def guardian_endpoint(self) -> Optional[pulumi.Input[str]]:
        """
        Guardian endpoint.
        """
        return pulumi.get(self, "guardian_endpoint")

    @guardian_endpoint.setter
    def guardian_endpoint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "guardian_endpoint", value)

    @property
    @pulumi.getter
    def identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AccountIdentityArgs']]]]:
        """
        A `identity` block as defined below.
        """
        return pulumi.get(self, "identities")

    @identities.setter
    def identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AccountIdentityArgs']]]]):
        pulumi.set(self, "identities", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The Azure Region where the Purview Account should exist. Changing this forces a new Purview Account to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="managedResourceGroupName")
    def managed_resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for the new Resource Group where Purview Account creates the managed resources. Changing this forces a new Purview Account to be created.
        """
        return pulumi.get(self, "managed_resource_group_name")

    @managed_resource_group_name.setter
    def managed_resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "managed_resource_group_name", value)

    @property
    @pulumi.getter(name="managedResources")
    def managed_resources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AccountManagedResourceArgs']]]]:
        """
        A `managed_resources` block as defined below.
        """
        return pulumi.get(self, "managed_resources")

    @managed_resources.setter
    def managed_resources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AccountManagedResourceArgs']]]]):
        pulumi.set(self, "managed_resources", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Purview Account. Changing this forces a new Purview Account to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="publicNetworkEnabled")
    def public_network_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Should the Purview Account be visible to the public network? Defaults to `true`.
        """
        return pulumi.get(self, "public_network_enabled")

    @public_network_enabled.setter
    def public_network_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "public_network_enabled", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Resource Group where the Purview Account should exist. Changing this forces a new Purview Account to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="scanEndpoint")
    def scan_endpoint(self) -> Optional[pulumi.Input[str]]:
        """
        Scan endpoint.
        """
        return pulumi.get(self, "scan_endpoint")

    @scan_endpoint.setter
    def scan_endpoint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scan_endpoint", value)

    @property
    @pulumi.getter(name="skuName")
    def sku_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "sku_name")

    @sku_name.setter
    def sku_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sku_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of tags which should be assigned to the Purview Account.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class Account(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 managed_resource_group_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 public_network_enabled: Optional[pulumi.Input[bool]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Manages a Purview Account.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_account = azure.purview.Account("exampleAccount",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location)
        ```

        ## Import

        Purview Accounts can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:purview/account:Account example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Purview/accounts/account1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] location: The Azure Region where the Purview Account should exist. Changing this forces a new Purview Account to be created.
        :param pulumi.Input[str] managed_resource_group_name: The name which should be used for the new Resource Group where Purview Account creates the managed resources. Changing this forces a new Purview Account to be created.
        :param pulumi.Input[str] name: The name which should be used for this Purview Account. Changing this forces a new Purview Account to be created.
        :param pulumi.Input[bool] public_network_enabled: Should the Purview Account be visible to the public network? Defaults to `true`.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Purview Account should exist. Changing this forces a new Purview Account to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags which should be assigned to the Purview Account.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AccountArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Purview Account.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_account = azure.purview.Account("exampleAccount",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location)
        ```

        ## Import

        Purview Accounts can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:purview/account:Account example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Purview/accounts/account1
        ```

        :param str resource_name: The name of the resource.
        :param AccountArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AccountArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 managed_resource_group_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 public_network_enabled: Optional[pulumi.Input[bool]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
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
            __props__ = AccountArgs.__new__(AccountArgs)

            __props__.__dict__["location"] = location
            __props__.__dict__["managed_resource_group_name"] = managed_resource_group_name
            __props__.__dict__["name"] = name
            __props__.__dict__["public_network_enabled"] = public_network_enabled
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if sku_name is not None and not opts.urn:
                warnings.warn("""This property can no longer be specified on create/update, it can only be updated by creating a support ticket at Azure""", DeprecationWarning)
                pulumi.log.warn("""sku_name is deprecated: This property can no longer be specified on create/update, it can only be updated by creating a support ticket at Azure""")
            __props__.__dict__["sku_name"] = sku_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["atlas_kafka_endpoint_primary_connection_string"] = None
            __props__.__dict__["atlas_kafka_endpoint_secondary_connection_string"] = None
            __props__.__dict__["catalog_endpoint"] = None
            __props__.__dict__["guardian_endpoint"] = None
            __props__.__dict__["identities"] = None
            __props__.__dict__["managed_resources"] = None
            __props__.__dict__["scan_endpoint"] = None
        super(Account, __self__).__init__(
            'azure:purview/account:Account',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            atlas_kafka_endpoint_primary_connection_string: Optional[pulumi.Input[str]] = None,
            atlas_kafka_endpoint_secondary_connection_string: Optional[pulumi.Input[str]] = None,
            catalog_endpoint: Optional[pulumi.Input[str]] = None,
            guardian_endpoint: Optional[pulumi.Input[str]] = None,
            identities: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AccountIdentityArgs']]]]] = None,
            location: Optional[pulumi.Input[str]] = None,
            managed_resource_group_name: Optional[pulumi.Input[str]] = None,
            managed_resources: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AccountManagedResourceArgs']]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            public_network_enabled: Optional[pulumi.Input[bool]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            scan_endpoint: Optional[pulumi.Input[str]] = None,
            sku_name: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'Account':
        """
        Get an existing Account resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] atlas_kafka_endpoint_primary_connection_string: Atlas Kafka endpoint primary connection string.
        :param pulumi.Input[str] atlas_kafka_endpoint_secondary_connection_string: Atlas Kafka endpoint secondary connection string.
        :param pulumi.Input[str] catalog_endpoint: Catalog endpoint.
        :param pulumi.Input[str] guardian_endpoint: Guardian endpoint.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AccountIdentityArgs']]]] identities: A `identity` block as defined below.
        :param pulumi.Input[str] location: The Azure Region where the Purview Account should exist. Changing this forces a new Purview Account to be created.
        :param pulumi.Input[str] managed_resource_group_name: The name which should be used for the new Resource Group where Purview Account creates the managed resources. Changing this forces a new Purview Account to be created.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AccountManagedResourceArgs']]]] managed_resources: A `managed_resources` block as defined below.
        :param pulumi.Input[str] name: The name which should be used for this Purview Account. Changing this forces a new Purview Account to be created.
        :param pulumi.Input[bool] public_network_enabled: Should the Purview Account be visible to the public network? Defaults to `true`.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Purview Account should exist. Changing this forces a new Purview Account to be created.
        :param pulumi.Input[str] scan_endpoint: Scan endpoint.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags which should be assigned to the Purview Account.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AccountState.__new__(_AccountState)

        __props__.__dict__["atlas_kafka_endpoint_primary_connection_string"] = atlas_kafka_endpoint_primary_connection_string
        __props__.__dict__["atlas_kafka_endpoint_secondary_connection_string"] = atlas_kafka_endpoint_secondary_connection_string
        __props__.__dict__["catalog_endpoint"] = catalog_endpoint
        __props__.__dict__["guardian_endpoint"] = guardian_endpoint
        __props__.__dict__["identities"] = identities
        __props__.__dict__["location"] = location
        __props__.__dict__["managed_resource_group_name"] = managed_resource_group_name
        __props__.__dict__["managed_resources"] = managed_resources
        __props__.__dict__["name"] = name
        __props__.__dict__["public_network_enabled"] = public_network_enabled
        __props__.__dict__["resource_group_name"] = resource_group_name
        __props__.__dict__["scan_endpoint"] = scan_endpoint
        __props__.__dict__["sku_name"] = sku_name
        __props__.__dict__["tags"] = tags
        return Account(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="atlasKafkaEndpointPrimaryConnectionString")
    def atlas_kafka_endpoint_primary_connection_string(self) -> pulumi.Output[str]:
        """
        Atlas Kafka endpoint primary connection string.
        """
        return pulumi.get(self, "atlas_kafka_endpoint_primary_connection_string")

    @property
    @pulumi.getter(name="atlasKafkaEndpointSecondaryConnectionString")
    def atlas_kafka_endpoint_secondary_connection_string(self) -> pulumi.Output[str]:
        """
        Atlas Kafka endpoint secondary connection string.
        """
        return pulumi.get(self, "atlas_kafka_endpoint_secondary_connection_string")

    @property
    @pulumi.getter(name="catalogEndpoint")
    def catalog_endpoint(self) -> pulumi.Output[str]:
        """
        Catalog endpoint.
        """
        return pulumi.get(self, "catalog_endpoint")

    @property
    @pulumi.getter(name="guardianEndpoint")
    def guardian_endpoint(self) -> pulumi.Output[str]:
        """
        Guardian endpoint.
        """
        return pulumi.get(self, "guardian_endpoint")

    @property
    @pulumi.getter
    def identities(self) -> pulumi.Output[Sequence['outputs.AccountIdentity']]:
        """
        A `identity` block as defined below.
        """
        return pulumi.get(self, "identities")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The Azure Region where the Purview Account should exist. Changing this forces a new Purview Account to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="managedResourceGroupName")
    def managed_resource_group_name(self) -> pulumi.Output[str]:
        """
        The name which should be used for the new Resource Group where Purview Account creates the managed resources. Changing this forces a new Purview Account to be created.
        """
        return pulumi.get(self, "managed_resource_group_name")

    @property
    @pulumi.getter(name="managedResources")
    def managed_resources(self) -> pulumi.Output[Sequence['outputs.AccountManagedResource']]:
        """
        A `managed_resources` block as defined below.
        """
        return pulumi.get(self, "managed_resources")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name which should be used for this Purview Account. Changing this forces a new Purview Account to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="publicNetworkEnabled")
    def public_network_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Should the Purview Account be visible to the public network? Defaults to `true`.
        """
        return pulumi.get(self, "public_network_enabled")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the Resource Group where the Purview Account should exist. Changing this forces a new Purview Account to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="scanEndpoint")
    def scan_endpoint(self) -> pulumi.Output[str]:
        """
        Scan endpoint.
        """
        return pulumi.get(self, "scan_endpoint")

    @property
    @pulumi.getter(name="skuName")
    def sku_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "sku_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags which should be assigned to the Purview Account.
        """
        return pulumi.get(self, "tags")

