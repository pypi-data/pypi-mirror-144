# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['AAAARecordArgs', 'AAAARecord']

@pulumi.input_type
class AAAARecordArgs:
    def __init__(__self__, *,
                 records: pulumi.Input[Sequence[pulumi.Input[str]]],
                 resource_group_name: pulumi.Input[str],
                 ttl: pulumi.Input[int],
                 zone_name: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a AAAARecord resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] records: A list of IPv6 Addresses.
        :param pulumi.Input[str] resource_group_name: Specifies the resource group where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] zone_name: Specifies the Private DNS Zone where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the DNS A Record.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        """
        pulumi.set(__self__, "records", records)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "ttl", ttl)
        pulumi.set(__self__, "zone_name", zone_name)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def records(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        A list of IPv6 Addresses.
        """
        return pulumi.get(self, "records")

    @records.setter
    def records(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "records", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Specifies the resource group where the resource exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def ttl(self) -> pulumi.Input[int]:
        return pulumi.get(self, "ttl")

    @ttl.setter
    def ttl(self, value: pulumi.Input[int]):
        pulumi.set(self, "ttl", value)

    @property
    @pulumi.getter(name="zoneName")
    def zone_name(self) -> pulumi.Input[str]:
        """
        Specifies the Private DNS Zone where the resource exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "zone_name")

    @zone_name.setter
    def zone_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "zone_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the DNS A Record.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _AAAARecordState:
    def __init__(__self__, *,
                 fqdn: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 records: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 ttl: Optional[pulumi.Input[int]] = None,
                 zone_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AAAARecord resources.
        :param pulumi.Input[str] fqdn: The FQDN of the DNS AAAA Record.
        :param pulumi.Input[str] name: The name of the DNS A Record.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] records: A list of IPv6 Addresses.
        :param pulumi.Input[str] resource_group_name: Specifies the resource group where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] zone_name: Specifies the Private DNS Zone where the resource exists. Changing this forces a new resource to be created.
        """
        if fqdn is not None:
            pulumi.set(__self__, "fqdn", fqdn)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if records is not None:
            pulumi.set(__self__, "records", records)
        if resource_group_name is not None:
            pulumi.set(__self__, "resource_group_name", resource_group_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if ttl is not None:
            pulumi.set(__self__, "ttl", ttl)
        if zone_name is not None:
            pulumi.set(__self__, "zone_name", zone_name)

    @property
    @pulumi.getter
    def fqdn(self) -> Optional[pulumi.Input[str]]:
        """
        The FQDN of the DNS AAAA Record.
        """
        return pulumi.get(self, "fqdn")

    @fqdn.setter
    def fqdn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "fqdn", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the DNS A Record.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def records(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of IPv6 Addresses.
        """
        return pulumi.get(self, "records")

    @records.setter
    def records(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "records", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the resource group where the resource exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def ttl(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "ttl")

    @ttl.setter
    def ttl(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ttl", value)

    @property
    @pulumi.getter(name="zoneName")
    def zone_name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the Private DNS Zone where the resource exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "zone_name")

    @zone_name.setter
    def zone_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone_name", value)


class AAAARecord(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 records: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 ttl: Optional[pulumi.Input[int]] = None,
                 zone_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Enables you to manage DNS AAAA Records within Azure Private DNS.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        test_resource_group = azure.core.ResourceGroup("testResourceGroup", location="West Europe")
        test_zone = azure.privatedns.Zone("testZone", resource_group_name=test_resource_group.name)
        test_aaaa_record = azure.privatedns.AAAARecord("testAAAARecord",
            zone_name=test_zone.name,
            resource_group_name=test_resource_group.name,
            ttl=300,
            records=[
                "fd5d:70bc:930e:d008:0000:0000:0000:7334",
                "fd5d:70bc:930e:d008::7335",
            ])
        ```

        ## Import

        Private DNS AAAA Records can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:privatedns/aAAARecord:AAAARecord test /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.Network/privateDnsZones/zone1/AAAA/myrecord1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name of the DNS A Record.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] records: A list of IPv6 Addresses.
        :param pulumi.Input[str] resource_group_name: Specifies the resource group where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] zone_name: Specifies the Private DNS Zone where the resource exists. Changing this forces a new resource to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AAAARecordArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Enables you to manage DNS AAAA Records within Azure Private DNS.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        test_resource_group = azure.core.ResourceGroup("testResourceGroup", location="West Europe")
        test_zone = azure.privatedns.Zone("testZone", resource_group_name=test_resource_group.name)
        test_aaaa_record = azure.privatedns.AAAARecord("testAAAARecord",
            zone_name=test_zone.name,
            resource_group_name=test_resource_group.name,
            ttl=300,
            records=[
                "fd5d:70bc:930e:d008:0000:0000:0000:7334",
                "fd5d:70bc:930e:d008::7335",
            ])
        ```

        ## Import

        Private DNS AAAA Records can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:privatedns/aAAARecord:AAAARecord test /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.Network/privateDnsZones/zone1/AAAA/myrecord1
        ```

        :param str resource_name: The name of the resource.
        :param AAAARecordArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AAAARecordArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 records: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 ttl: Optional[pulumi.Input[int]] = None,
                 zone_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = AAAARecordArgs.__new__(AAAARecordArgs)

            __props__.__dict__["name"] = name
            if records is None and not opts.urn:
                raise TypeError("Missing required property 'records'")
            __props__.__dict__["records"] = records
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            if ttl is None and not opts.urn:
                raise TypeError("Missing required property 'ttl'")
            __props__.__dict__["ttl"] = ttl
            if zone_name is None and not opts.urn:
                raise TypeError("Missing required property 'zone_name'")
            __props__.__dict__["zone_name"] = zone_name
            __props__.__dict__["fqdn"] = None
        super(AAAARecord, __self__).__init__(
            'azure:privatedns/aAAARecord:AAAARecord',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            fqdn: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            records: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            ttl: Optional[pulumi.Input[int]] = None,
            zone_name: Optional[pulumi.Input[str]] = None) -> 'AAAARecord':
        """
        Get an existing AAAARecord resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] fqdn: The FQDN of the DNS AAAA Record.
        :param pulumi.Input[str] name: The name of the DNS A Record.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] records: A list of IPv6 Addresses.
        :param pulumi.Input[str] resource_group_name: Specifies the resource group where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] zone_name: Specifies the Private DNS Zone where the resource exists. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AAAARecordState.__new__(_AAAARecordState)

        __props__.__dict__["fqdn"] = fqdn
        __props__.__dict__["name"] = name
        __props__.__dict__["records"] = records
        __props__.__dict__["resource_group_name"] = resource_group_name
        __props__.__dict__["tags"] = tags
        __props__.__dict__["ttl"] = ttl
        __props__.__dict__["zone_name"] = zone_name
        return AAAARecord(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def fqdn(self) -> pulumi.Output[str]:
        """
        The FQDN of the DNS AAAA Record.
        """
        return pulumi.get(self, "fqdn")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the DNS A Record.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def records(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of IPv6 Addresses.
        """
        return pulumi.get(self, "records")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        Specifies the resource group where the resource exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def ttl(self) -> pulumi.Output[int]:
        return pulumi.get(self, "ttl")

    @property
    @pulumi.getter(name="zoneName")
    def zone_name(self) -> pulumi.Output[str]:
        """
        Specifies the Private DNS Zone where the resource exists. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "zone_name")

