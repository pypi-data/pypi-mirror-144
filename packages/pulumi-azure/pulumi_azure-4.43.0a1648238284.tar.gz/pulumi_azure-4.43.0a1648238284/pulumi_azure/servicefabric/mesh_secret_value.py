# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['MeshSecretValueArgs', 'MeshSecretValue']

@pulumi.input_type
class MeshSecretValueArgs:
    def __init__(__self__, *,
                 service_fabric_mesh_secret_id: pulumi.Input[str],
                 value: pulumi.Input[str],
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a MeshSecretValue resource.
        :param pulumi.Input[str] service_fabric_mesh_secret_id: The id of the Service Fabric Mesh Secret in which the value will be applied to. Changing this forces a new resource to be created.
        :param pulumi.Input[str] value: Specifies the value that will be applied to the Service Fabric Mesh Secret. Changing this forces a new resource to be created.
        :param pulumi.Input[str] location: Specifies the Azure Region where the Service Fabric Mesh Secret Value should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the Service Fabric Mesh Secret Value. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        """
        pulumi.set(__self__, "service_fabric_mesh_secret_id", service_fabric_mesh_secret_id)
        pulumi.set(__self__, "value", value)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="serviceFabricMeshSecretId")
    def service_fabric_mesh_secret_id(self) -> pulumi.Input[str]:
        """
        The id of the Service Fabric Mesh Secret in which the value will be applied to. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "service_fabric_mesh_secret_id")

    @service_fabric_mesh_secret_id.setter
    def service_fabric_mesh_secret_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_fabric_mesh_secret_id", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        Specifies the value that will be applied to the Service Fabric Mesh Secret. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the Azure Region where the Service Fabric Mesh Secret Value should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Service Fabric Mesh Secret Value. Changing this forces a new resource to be created.
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
class _MeshSecretValueState:
    def __init__(__self__, *,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 service_fabric_mesh_secret_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering MeshSecretValue resources.
        :param pulumi.Input[str] location: Specifies the Azure Region where the Service Fabric Mesh Secret Value should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the Service Fabric Mesh Secret Value. Changing this forces a new resource to be created.
        :param pulumi.Input[str] service_fabric_mesh_secret_id: The id of the Service Fabric Mesh Secret in which the value will be applied to. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] value: Specifies the value that will be applied to the Service Fabric Mesh Secret. Changing this forces a new resource to be created.
        """
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if service_fabric_mesh_secret_id is not None:
            pulumi.set(__self__, "service_fabric_mesh_secret_id", service_fabric_mesh_secret_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the Azure Region where the Service Fabric Mesh Secret Value should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Service Fabric Mesh Secret Value. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="serviceFabricMeshSecretId")
    def service_fabric_mesh_secret_id(self) -> Optional[pulumi.Input[str]]:
        """
        The id of the Service Fabric Mesh Secret in which the value will be applied to. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "service_fabric_mesh_secret_id")

    @service_fabric_mesh_secret_id.setter
    def service_fabric_mesh_secret_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_fabric_mesh_secret_id", value)

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
    def value(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the value that will be applied to the Service Fabric Mesh Secret. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


class MeshSecretValue(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 service_fabric_mesh_secret_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_mesh_secret = azure.servicefabric.MeshSecret("exampleMeshSecret",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location)
        example_mesh_secret_value = azure.servicefabric.MeshSecretValue("exampleMeshSecretValue",
            service_fabric_mesh_secret_id=azurerm_service_fabric_mesh_secret_inline["test"]["id"],
            location=azurerm_resource_group["test"]["location"],
            value="testValue")
        ```

        ## Import

        Service Fabric Mesh Secret Value can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:servicefabric/meshSecretValue:MeshSecretValue value1 /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.ServiceFabricMesh/secrets/secret1/values/value1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] location: Specifies the Azure Region where the Service Fabric Mesh Secret Value should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the Service Fabric Mesh Secret Value. Changing this forces a new resource to be created.
        :param pulumi.Input[str] service_fabric_mesh_secret_id: The id of the Service Fabric Mesh Secret in which the value will be applied to. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] value: Specifies the value that will be applied to the Service Fabric Mesh Secret. Changing this forces a new resource to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MeshSecretValueArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_mesh_secret = azure.servicefabric.MeshSecret("exampleMeshSecret",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location)
        example_mesh_secret_value = azure.servicefabric.MeshSecretValue("exampleMeshSecretValue",
            service_fabric_mesh_secret_id=azurerm_service_fabric_mesh_secret_inline["test"]["id"],
            location=azurerm_resource_group["test"]["location"],
            value="testValue")
        ```

        ## Import

        Service Fabric Mesh Secret Value can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:servicefabric/meshSecretValue:MeshSecretValue value1 /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/mygroup1/providers/Microsoft.ServiceFabricMesh/secrets/secret1/values/value1
        ```

        :param str resource_name: The name of the resource.
        :param MeshSecretValueArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MeshSecretValueArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 service_fabric_mesh_secret_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 value: Optional[pulumi.Input[str]] = None,
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
            __props__ = MeshSecretValueArgs.__new__(MeshSecretValueArgs)

            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            if service_fabric_mesh_secret_id is None and not opts.urn:
                raise TypeError("Missing required property 'service_fabric_mesh_secret_id'")
            __props__.__dict__["service_fabric_mesh_secret_id"] = service_fabric_mesh_secret_id
            __props__.__dict__["tags"] = tags
            if value is None and not opts.urn:
                raise TypeError("Missing required property 'value'")
            __props__.__dict__["value"] = value
        super(MeshSecretValue, __self__).__init__(
            'azure:servicefabric/meshSecretValue:MeshSecretValue',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            service_fabric_mesh_secret_id: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            value: Optional[pulumi.Input[str]] = None) -> 'MeshSecretValue':
        """
        Get an existing MeshSecretValue resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] location: Specifies the Azure Region where the Service Fabric Mesh Secret Value should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: The name of the Service Fabric Mesh Secret Value. Changing this forces a new resource to be created.
        :param pulumi.Input[str] service_fabric_mesh_secret_id: The id of the Service Fabric Mesh Secret in which the value will be applied to. Changing this forces a new resource to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] value: Specifies the value that will be applied to the Service Fabric Mesh Secret. Changing this forces a new resource to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _MeshSecretValueState.__new__(_MeshSecretValueState)

        __props__.__dict__["location"] = location
        __props__.__dict__["name"] = name
        __props__.__dict__["service_fabric_mesh_secret_id"] = service_fabric_mesh_secret_id
        __props__.__dict__["tags"] = tags
        __props__.__dict__["value"] = value
        return MeshSecretValue(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Specifies the Azure Region where the Service Fabric Mesh Secret Value should exist. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Service Fabric Mesh Secret Value. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="serviceFabricMeshSecretId")
    def service_fabric_mesh_secret_id(self) -> pulumi.Output[str]:
        """
        The id of the Service Fabric Mesh Secret in which the value will be applied to. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "service_fabric_mesh_secret_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def value(self) -> pulumi.Output[str]:
        """
        Specifies the value that will be applied to the Service Fabric Mesh Secret. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "value")

