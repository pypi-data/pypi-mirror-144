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

__all__ = ['VpnGatewayArgs', 'VpnGateway']

@pulumi.input_type
class VpnGatewayArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 virtual_hub_id: pulumi.Input[str],
                 bgp_settings: Optional[pulumi.Input['VpnGatewayBgpSettingsArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 routing_preference: Optional[pulumi.Input[str]] = None,
                 scale_unit: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a VpnGateway resource.
        :param pulumi.Input[str] resource_group_name: The Name of the Resource Group in which this VPN Gateway should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] virtual_hub_id: The ID of the Virtual Hub within which this VPN Gateway should be created. Changing this forces a new resource to be created.
        :param pulumi.Input['VpnGatewayBgpSettingsArgs'] bgp_settings: A `bgp_settings` block as defined below.
        :param pulumi.Input[str] location: The Azure location where this VPN Gateway should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The Name which should be used for this VPN Gateway. Changing this forces a new resource to be created.
        :param pulumi.Input[str] routing_preference: Azure routing preference lets you to choose how your traffic routes between Azure and the internet. You can choose to route traffic either via the Microsoft network (default value, `Microsoft Network`), or via the ISP network (public internet, set to `Internet`). More context of the configuration can be found in the
               [Microsoft Docs](https://docs.microsoft.com/en-us/azure/virtual-wan/virtual-wan-site-to-site-portal#gateway) to create a VPN Gateway. Changing this forces a new resource to be created.
        :param pulumi.Input[int] scale_unit: The Scale Unit for this VPN Gateway. Defaults to `1`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the VPN Gateway.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "virtual_hub_id", virtual_hub_id)
        if bgp_settings is not None:
            pulumi.set(__self__, "bgp_settings", bgp_settings)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if routing_preference is not None:
            pulumi.set(__self__, "routing_preference", routing_preference)
        if scale_unit is not None:
            pulumi.set(__self__, "scale_unit", scale_unit)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The Name of the Resource Group in which this VPN Gateway should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="virtualHubId")
    def virtual_hub_id(self) -> pulumi.Input[str]:
        """
        The ID of the Virtual Hub within which this VPN Gateway should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "virtual_hub_id")

    @virtual_hub_id.setter
    def virtual_hub_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "virtual_hub_id", value)

    @property
    @pulumi.getter(name="bgpSettings")
    def bgp_settings(self) -> Optional[pulumi.Input['VpnGatewayBgpSettingsArgs']]:
        """
        A `bgp_settings` block as defined below.
        """
        return pulumi.get(self, "bgp_settings")

    @bgp_settings.setter
    def bgp_settings(self, value: Optional[pulumi.Input['VpnGatewayBgpSettingsArgs']]):
        pulumi.set(self, "bgp_settings", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The Azure location where this VPN Gateway should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The Name which should be used for this VPN Gateway. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="routingPreference")
    def routing_preference(self) -> Optional[pulumi.Input[str]]:
        """
        Azure routing preference lets you to choose how your traffic routes between Azure and the internet. You can choose to route traffic either via the Microsoft network (default value, `Microsoft Network`), or via the ISP network (public internet, set to `Internet`). More context of the configuration can be found in the
        [Microsoft Docs](https://docs.microsoft.com/en-us/azure/virtual-wan/virtual-wan-site-to-site-portal#gateway) to create a VPN Gateway. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "routing_preference")

    @routing_preference.setter
    def routing_preference(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "routing_preference", value)

    @property
    @pulumi.getter(name="scaleUnit")
    def scale_unit(self) -> Optional[pulumi.Input[int]]:
        """
        The Scale Unit for this VPN Gateway. Defaults to `1`.
        """
        return pulumi.get(self, "scale_unit")

    @scale_unit.setter
    def scale_unit(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "scale_unit", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of tags to assign to the VPN Gateway.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _VpnGatewayState:
    def __init__(__self__, *,
                 bgp_settings: Optional[pulumi.Input['VpnGatewayBgpSettingsArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 routing_preference: Optional[pulumi.Input[str]] = None,
                 scale_unit: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_hub_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering VpnGateway resources.
        :param pulumi.Input['VpnGatewayBgpSettingsArgs'] bgp_settings: A `bgp_settings` block as defined below.
        :param pulumi.Input[str] location: The Azure location where this VPN Gateway should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The Name which should be used for this VPN Gateway. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The Name of the Resource Group in which this VPN Gateway should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] routing_preference: Azure routing preference lets you to choose how your traffic routes between Azure and the internet. You can choose to route traffic either via the Microsoft network (default value, `Microsoft Network`), or via the ISP network (public internet, set to `Internet`). More context of the configuration can be found in the
               [Microsoft Docs](https://docs.microsoft.com/en-us/azure/virtual-wan/virtual-wan-site-to-site-portal#gateway) to create a VPN Gateway. Changing this forces a new resource to be created.
        :param pulumi.Input[int] scale_unit: The Scale Unit for this VPN Gateway. Defaults to `1`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the VPN Gateway.
        :param pulumi.Input[str] virtual_hub_id: The ID of the Virtual Hub within which this VPN Gateway should be created. Changing this forces a new resource to be created.
        """
        if bgp_settings is not None:
            pulumi.set(__self__, "bgp_settings", bgp_settings)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if resource_group_name is not None:
            pulumi.set(__self__, "resource_group_name", resource_group_name)
        if routing_preference is not None:
            pulumi.set(__self__, "routing_preference", routing_preference)
        if scale_unit is not None:
            pulumi.set(__self__, "scale_unit", scale_unit)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if virtual_hub_id is not None:
            pulumi.set(__self__, "virtual_hub_id", virtual_hub_id)

    @property
    @pulumi.getter(name="bgpSettings")
    def bgp_settings(self) -> Optional[pulumi.Input['VpnGatewayBgpSettingsArgs']]:
        """
        A `bgp_settings` block as defined below.
        """
        return pulumi.get(self, "bgp_settings")

    @bgp_settings.setter
    def bgp_settings(self, value: Optional[pulumi.Input['VpnGatewayBgpSettingsArgs']]):
        pulumi.set(self, "bgp_settings", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The Azure location where this VPN Gateway should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The Name which should be used for this VPN Gateway. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The Name of the Resource Group in which this VPN Gateway should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="routingPreference")
    def routing_preference(self) -> Optional[pulumi.Input[str]]:
        """
        Azure routing preference lets you to choose how your traffic routes between Azure and the internet. You can choose to route traffic either via the Microsoft network (default value, `Microsoft Network`), or via the ISP network (public internet, set to `Internet`). More context of the configuration can be found in the
        [Microsoft Docs](https://docs.microsoft.com/en-us/azure/virtual-wan/virtual-wan-site-to-site-portal#gateway) to create a VPN Gateway. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "routing_preference")

    @routing_preference.setter
    def routing_preference(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "routing_preference", value)

    @property
    @pulumi.getter(name="scaleUnit")
    def scale_unit(self) -> Optional[pulumi.Input[int]]:
        """
        The Scale Unit for this VPN Gateway. Defaults to `1`.
        """
        return pulumi.get(self, "scale_unit")

    @scale_unit.setter
    def scale_unit(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "scale_unit", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of tags to assign to the VPN Gateway.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="virtualHubId")
    def virtual_hub_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Virtual Hub within which this VPN Gateway should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "virtual_hub_id")

    @virtual_hub_id.setter
    def virtual_hub_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "virtual_hub_id", value)


class VpnGateway(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bgp_settings: Optional[pulumi.Input[pulumi.InputType['VpnGatewayBgpSettingsArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 routing_preference: Optional[pulumi.Input[str]] = None,
                 scale_unit: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_hub_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a VPN Gateway within a Virtual Hub, which enables Site-to-Site communication.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_virtual_network = azure.network.VirtualNetwork("exampleVirtualNetwork",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            address_spaces=["10.0.0.0/16"])
        example_virtual_wan = azure.network.VirtualWan("exampleVirtualWan",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location)
        example_virtual_hub = azure.network.VirtualHub("exampleVirtualHub",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            virtual_wan_id=example_virtual_wan.id,
            address_prefix="10.0.1.0/24")
        example_vpn_gateway = azure.network.VpnGateway("exampleVpnGateway",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            virtual_hub_id=example_virtual_hub.id)
        ```

        ## Import

        VPN Gateways can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:network/vpnGateway:VpnGateway gateway1 /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Network/vpnGateways/gateway1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['VpnGatewayBgpSettingsArgs']] bgp_settings: A `bgp_settings` block as defined below.
        :param pulumi.Input[str] location: The Azure location where this VPN Gateway should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The Name which should be used for this VPN Gateway. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The Name of the Resource Group in which this VPN Gateway should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] routing_preference: Azure routing preference lets you to choose how your traffic routes between Azure and the internet. You can choose to route traffic either via the Microsoft network (default value, `Microsoft Network`), or via the ISP network (public internet, set to `Internet`). More context of the configuration can be found in the
               [Microsoft Docs](https://docs.microsoft.com/en-us/azure/virtual-wan/virtual-wan-site-to-site-portal#gateway) to create a VPN Gateway. Changing this forces a new resource to be created.
        :param pulumi.Input[int] scale_unit: The Scale Unit for this VPN Gateway. Defaults to `1`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the VPN Gateway.
        :param pulumi.Input[str] virtual_hub_id: The ID of the Virtual Hub within which this VPN Gateway should be created. Changing this forces a new resource to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VpnGatewayArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a VPN Gateway within a Virtual Hub, which enables Site-to-Site communication.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_virtual_network = azure.network.VirtualNetwork("exampleVirtualNetwork",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            address_spaces=["10.0.0.0/16"])
        example_virtual_wan = azure.network.VirtualWan("exampleVirtualWan",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location)
        example_virtual_hub = azure.network.VirtualHub("exampleVirtualHub",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            virtual_wan_id=example_virtual_wan.id,
            address_prefix="10.0.1.0/24")
        example_vpn_gateway = azure.network.VpnGateway("exampleVpnGateway",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            virtual_hub_id=example_virtual_hub.id)
        ```

        ## Import

        VPN Gateways can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:network/vpnGateway:VpnGateway gateway1 /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.Network/vpnGateways/gateway1
        ```

        :param str resource_name: The name of the resource.
        :param VpnGatewayArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VpnGatewayArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bgp_settings: Optional[pulumi.Input[pulumi.InputType['VpnGatewayBgpSettingsArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 routing_preference: Optional[pulumi.Input[str]] = None,
                 scale_unit: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_hub_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = VpnGatewayArgs.__new__(VpnGatewayArgs)

            __props__.__dict__["bgp_settings"] = bgp_settings
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["routing_preference"] = routing_preference
            __props__.__dict__["scale_unit"] = scale_unit
            __props__.__dict__["tags"] = tags
            if virtual_hub_id is None and not opts.urn:
                raise TypeError("Missing required property 'virtual_hub_id'")
            __props__.__dict__["virtual_hub_id"] = virtual_hub_id
        super(VpnGateway, __self__).__init__(
            'azure:network/vpnGateway:VpnGateway',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            bgp_settings: Optional[pulumi.Input[pulumi.InputType['VpnGatewayBgpSettingsArgs']]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            routing_preference: Optional[pulumi.Input[str]] = None,
            scale_unit: Optional[pulumi.Input[int]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            virtual_hub_id: Optional[pulumi.Input[str]] = None) -> 'VpnGateway':
        """
        Get an existing VpnGateway resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['VpnGatewayBgpSettingsArgs']] bgp_settings: A `bgp_settings` block as defined below.
        :param pulumi.Input[str] location: The Azure location where this VPN Gateway should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The Name which should be used for this VPN Gateway. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The Name of the Resource Group in which this VPN Gateway should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] routing_preference: Azure routing preference lets you to choose how your traffic routes between Azure and the internet. You can choose to route traffic either via the Microsoft network (default value, `Microsoft Network`), or via the ISP network (public internet, set to `Internet`). More context of the configuration can be found in the
               [Microsoft Docs](https://docs.microsoft.com/en-us/azure/virtual-wan/virtual-wan-site-to-site-portal#gateway) to create a VPN Gateway. Changing this forces a new resource to be created.
        :param pulumi.Input[int] scale_unit: The Scale Unit for this VPN Gateway. Defaults to `1`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the VPN Gateway.
        :param pulumi.Input[str] virtual_hub_id: The ID of the Virtual Hub within which this VPN Gateway should be created. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _VpnGatewayState.__new__(_VpnGatewayState)

        __props__.__dict__["bgp_settings"] = bgp_settings
        __props__.__dict__["location"] = location
        __props__.__dict__["name"] = name
        __props__.__dict__["resource_group_name"] = resource_group_name
        __props__.__dict__["routing_preference"] = routing_preference
        __props__.__dict__["scale_unit"] = scale_unit
        __props__.__dict__["tags"] = tags
        __props__.__dict__["virtual_hub_id"] = virtual_hub_id
        return VpnGateway(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="bgpSettings")
    def bgp_settings(self) -> pulumi.Output['outputs.VpnGatewayBgpSettings']:
        """
        A `bgp_settings` block as defined below.
        """
        return pulumi.get(self, "bgp_settings")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The Azure location where this VPN Gateway should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The Name which should be used for this VPN Gateway. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The Name of the Resource Group in which this VPN Gateway should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="routingPreference")
    def routing_preference(self) -> pulumi.Output[str]:
        """
        Azure routing preference lets you to choose how your traffic routes between Azure and the internet. You can choose to route traffic either via the Microsoft network (default value, `Microsoft Network`), or via the ISP network (public internet, set to `Internet`). More context of the configuration can be found in the
        [Microsoft Docs](https://docs.microsoft.com/en-us/azure/virtual-wan/virtual-wan-site-to-site-portal#gateway) to create a VPN Gateway. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "routing_preference")

    @property
    @pulumi.getter(name="scaleUnit")
    def scale_unit(self) -> pulumi.Output[Optional[int]]:
        """
        The Scale Unit for this VPN Gateway. Defaults to `1`.
        """
        return pulumi.get(self, "scale_unit")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags to assign to the VPN Gateway.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="virtualHubId")
    def virtual_hub_id(self) -> pulumi.Output[str]:
        """
        The ID of the Virtual Hub within which this VPN Gateway should be created. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "virtual_hub_id")

