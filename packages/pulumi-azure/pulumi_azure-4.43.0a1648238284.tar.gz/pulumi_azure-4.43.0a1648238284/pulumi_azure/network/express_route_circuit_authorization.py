# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ExpressRouteCircuitAuthorizationArgs', 'ExpressRouteCircuitAuthorization']

@pulumi.input_type
class ExpressRouteCircuitAuthorizationArgs:
    def __init__(__self__, *,
                 express_route_circuit_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ExpressRouteCircuitAuthorization resource.
        :param pulumi.Input[str] express_route_circuit_name: The name of the Express Route Circuit in which to create the Authorization.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to
               create the ExpressRoute circuit. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the ExpressRoute circuit. Changing this forces a
               new resource to be created.
        """
        pulumi.set(__self__, "express_route_circuit_name", express_route_circuit_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="expressRouteCircuitName")
    def express_route_circuit_name(self) -> pulumi.Input[str]:
        """
        The name of the Express Route Circuit in which to create the Authorization.
        """
        return pulumi.get(self, "express_route_circuit_name")

    @express_route_circuit_name.setter
    def express_route_circuit_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "express_route_circuit_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group in which to
        create the ExpressRoute circuit. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the ExpressRoute circuit. Changing this forces a
        new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _ExpressRouteCircuitAuthorizationState:
    def __init__(__self__, *,
                 authorization_key: Optional[pulumi.Input[str]] = None,
                 authorization_use_status: Optional[pulumi.Input[str]] = None,
                 express_route_circuit_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ExpressRouteCircuitAuthorization resources.
        :param pulumi.Input[str] authorization_key: The Authorization Key.
        :param pulumi.Input[str] authorization_use_status: The authorization use status.
        :param pulumi.Input[str] express_route_circuit_name: The name of the Express Route Circuit in which to create the Authorization.
        :param pulumi.Input[str] name: The name of the ExpressRoute circuit. Changing this forces a
               new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to
               create the ExpressRoute circuit. Changing this forces a new resource to be created.
        """
        if authorization_key is not None:
            pulumi.set(__self__, "authorization_key", authorization_key)
        if authorization_use_status is not None:
            pulumi.set(__self__, "authorization_use_status", authorization_use_status)
        if express_route_circuit_name is not None:
            pulumi.set(__self__, "express_route_circuit_name", express_route_circuit_name)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if resource_group_name is not None:
            pulumi.set(__self__, "resource_group_name", resource_group_name)

    @property
    @pulumi.getter(name="authorizationKey")
    def authorization_key(self) -> Optional[pulumi.Input[str]]:
        """
        The Authorization Key.
        """
        return pulumi.get(self, "authorization_key")

    @authorization_key.setter
    def authorization_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authorization_key", value)

    @property
    @pulumi.getter(name="authorizationUseStatus")
    def authorization_use_status(self) -> Optional[pulumi.Input[str]]:
        """
        The authorization use status.
        """
        return pulumi.get(self, "authorization_use_status")

    @authorization_use_status.setter
    def authorization_use_status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authorization_use_status", value)

    @property
    @pulumi.getter(name="expressRouteCircuitName")
    def express_route_circuit_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Express Route Circuit in which to create the Authorization.
        """
        return pulumi.get(self, "express_route_circuit_name")

    @express_route_circuit_name.setter
    def express_route_circuit_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "express_route_circuit_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the ExpressRoute circuit. Changing this forces a
        new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the resource group in which to
        create the ExpressRoute circuit. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)


class ExpressRouteCircuitAuthorization(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 express_route_circuit_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages an ExpressRoute Circuit Authorization.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_express_route_circuit = azure.network.ExpressRouteCircuit("exampleExpressRouteCircuit",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            service_provider_name="Equinix",
            peering_location="Silicon Valley",
            bandwidth_in_mbps=50,
            sku=azure.network.ExpressRouteCircuitSkuArgs(
                tier="Standard",
                family="MeteredData",
            ),
            allow_classic_operations=False,
            tags={
                "environment": "Production",
            })
        example_express_route_circuit_authorization = azure.network.ExpressRouteCircuitAuthorization("exampleExpressRouteCircuitAuthorization",
            express_route_circuit_name=example_express_route_circuit.name,
            resource_group_name=example_resource_group.name)
        ```

        ## Import

        ExpressRoute Circuit Authorizations can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:network/expressRouteCircuitAuthorization:ExpressRouteCircuitAuthorization auth1 /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.Network/expressRouteCircuits/myExpressRoute/authorizations/auth1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] express_route_circuit_name: The name of the Express Route Circuit in which to create the Authorization.
        :param pulumi.Input[str] name: The name of the ExpressRoute circuit. Changing this forces a
               new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to
               create the ExpressRoute circuit. Changing this forces a new resource to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ExpressRouteCircuitAuthorizationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages an ExpressRoute Circuit Authorization.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_express_route_circuit = azure.network.ExpressRouteCircuit("exampleExpressRouteCircuit",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location,
            service_provider_name="Equinix",
            peering_location="Silicon Valley",
            bandwidth_in_mbps=50,
            sku=azure.network.ExpressRouteCircuitSkuArgs(
                tier="Standard",
                family="MeteredData",
            ),
            allow_classic_operations=False,
            tags={
                "environment": "Production",
            })
        example_express_route_circuit_authorization = azure.network.ExpressRouteCircuitAuthorization("exampleExpressRouteCircuitAuthorization",
            express_route_circuit_name=example_express_route_circuit.name,
            resource_group_name=example_resource_group.name)
        ```

        ## Import

        ExpressRoute Circuit Authorizations can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:network/expressRouteCircuitAuthorization:ExpressRouteCircuitAuthorization auth1 /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.Network/expressRouteCircuits/myExpressRoute/authorizations/auth1
        ```

        :param str resource_name: The name of the resource.
        :param ExpressRouteCircuitAuthorizationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ExpressRouteCircuitAuthorizationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 express_route_circuit_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = ExpressRouteCircuitAuthorizationArgs.__new__(ExpressRouteCircuitAuthorizationArgs)

            if express_route_circuit_name is None and not opts.urn:
                raise TypeError("Missing required property 'express_route_circuit_name'")
            __props__.__dict__["express_route_circuit_name"] = express_route_circuit_name
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["authorization_key"] = None
            __props__.__dict__["authorization_use_status"] = None
        super(ExpressRouteCircuitAuthorization, __self__).__init__(
            'azure:network/expressRouteCircuitAuthorization:ExpressRouteCircuitAuthorization',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            authorization_key: Optional[pulumi.Input[str]] = None,
            authorization_use_status: Optional[pulumi.Input[str]] = None,
            express_route_circuit_name: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None) -> 'ExpressRouteCircuitAuthorization':
        """
        Get an existing ExpressRouteCircuitAuthorization resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] authorization_key: The Authorization Key.
        :param pulumi.Input[str] authorization_use_status: The authorization use status.
        :param pulumi.Input[str] express_route_circuit_name: The name of the Express Route Circuit in which to create the Authorization.
        :param pulumi.Input[str] name: The name of the ExpressRoute circuit. Changing this forces a
               new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to
               create the ExpressRoute circuit. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ExpressRouteCircuitAuthorizationState.__new__(_ExpressRouteCircuitAuthorizationState)

        __props__.__dict__["authorization_key"] = authorization_key
        __props__.__dict__["authorization_use_status"] = authorization_use_status
        __props__.__dict__["express_route_circuit_name"] = express_route_circuit_name
        __props__.__dict__["name"] = name
        __props__.__dict__["resource_group_name"] = resource_group_name
        return ExpressRouteCircuitAuthorization(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="authorizationKey")
    def authorization_key(self) -> pulumi.Output[str]:
        """
        The Authorization Key.
        """
        return pulumi.get(self, "authorization_key")

    @property
    @pulumi.getter(name="authorizationUseStatus")
    def authorization_use_status(self) -> pulumi.Output[str]:
        """
        The authorization use status.
        """
        return pulumi.get(self, "authorization_use_status")

    @property
    @pulumi.getter(name="expressRouteCircuitName")
    def express_route_circuit_name(self) -> pulumi.Output[str]:
        """
        The name of the Express Route Circuit in which to create the Authorization.
        """
        return pulumi.get(self, "express_route_circuit_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the ExpressRoute circuit. Changing this forces a
        new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the resource group in which to
        create the ExpressRoute circuit. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "resource_group_name")

