# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetPolicyDefintionResult',
    'AwaitableGetPolicyDefintionResult',
    'get_policy_defintion',
    'get_policy_defintion_output',
]

@pulumi.output_type
class GetPolicyDefintionResult:
    """
    A collection of values returned by getPolicyDefintion.
    """
    def __init__(__self__, description=None, display_name=None, id=None, management_group_id=None, management_group_name=None, metadata=None, name=None, parameters=None, policy_rule=None, policy_type=None, type=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if management_group_id and not isinstance(management_group_id, str):
            raise TypeError("Expected argument 'management_group_id' to be a str")
        if management_group_id is not None:
            warnings.warn("""Deprecated in favour of `management_group_name`""", DeprecationWarning)
            pulumi.log.warn("""management_group_id is deprecated: Deprecated in favour of `management_group_name`""")

        pulumi.set(__self__, "management_group_id", management_group_id)
        if management_group_name and not isinstance(management_group_name, str):
            raise TypeError("Expected argument 'management_group_name' to be a str")
        pulumi.set(__self__, "management_group_name", management_group_name)
        if metadata and not isinstance(metadata, str):
            raise TypeError("Expected argument 'metadata' to be a str")
        pulumi.set(__self__, "metadata", metadata)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if parameters and not isinstance(parameters, str):
            raise TypeError("Expected argument 'parameters' to be a str")
        pulumi.set(__self__, "parameters", parameters)
        if policy_rule and not isinstance(policy_rule, str):
            raise TypeError("Expected argument 'policy_rule' to be a str")
        pulumi.set(__self__, "policy_rule", policy_rule)
        if policy_type and not isinstance(policy_type, str):
            raise TypeError("Expected argument 'policy_type' to be a str")
        pulumi.set(__self__, "policy_type", policy_type)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The Description of the Policy.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="managementGroupId")
    def management_group_id(self) -> Optional[str]:
        return pulumi.get(self, "management_group_id")

    @property
    @pulumi.getter(name="managementGroupName")
    def management_group_name(self) -> Optional[str]:
        return pulumi.get(self, "management_group_name")

    @property
    @pulumi.getter
    def metadata(self) -> str:
        """
        Any Metadata defined in the Policy.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parameters(self) -> str:
        """
        Any Parameters defined in the Policy.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="policyRule")
    def policy_rule(self) -> str:
        """
        The Rule as defined (in JSON) in the Policy.
        """
        return pulumi.get(self, "policy_rule")

    @property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> str:
        """
        The Type of the Policy. Possible values are "BuiltIn", "Custom" and "NotSpecified".
        """
        return pulumi.get(self, "policy_type")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The Type of Policy.
        """
        return pulumi.get(self, "type")


class AwaitableGetPolicyDefintionResult(GetPolicyDefintionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPolicyDefintionResult(
            description=self.description,
            display_name=self.display_name,
            id=self.id,
            management_group_id=self.management_group_id,
            management_group_name=self.management_group_name,
            metadata=self.metadata,
            name=self.name,
            parameters=self.parameters,
            policy_rule=self.policy_rule,
            policy_type=self.policy_type,
            type=self.type)


def get_policy_defintion(display_name: Optional[str] = None,
                         management_group_id: Optional[str] = None,
                         management_group_name: Optional[str] = None,
                         name: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPolicyDefintionResult:
    """
    Use this data source to access information about a Policy Definition, both custom and built in. Retrieves Policy Definitions from your current subscription by default.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.policy.get_policy_defintion(display_name="Allowed resource types")
    pulumi.export("id", example.id)
    ```


    :param str display_name: Specifies the display name of the Policy Definition. Conflicts with `name`.
    :param str management_group_name: Only retrieve Policy Definitions from this Management Group.
    :param str name: Specifies the name of the Policy Definition. Conflicts with `display_name`.
    """
    __args__ = dict()
    __args__['displayName'] = display_name
    __args__['managementGroupId'] = management_group_id
    __args__['managementGroupName'] = management_group_name
    __args__['name'] = name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure:policy/getPolicyDefintion:getPolicyDefintion', __args__, opts=opts, typ=GetPolicyDefintionResult).value

    return AwaitableGetPolicyDefintionResult(
        description=__ret__.description,
        display_name=__ret__.display_name,
        id=__ret__.id,
        management_group_id=__ret__.management_group_id,
        management_group_name=__ret__.management_group_name,
        metadata=__ret__.metadata,
        name=__ret__.name,
        parameters=__ret__.parameters,
        policy_rule=__ret__.policy_rule,
        policy_type=__ret__.policy_type,
        type=__ret__.type)


@_utilities.lift_output_func(get_policy_defintion)
def get_policy_defintion_output(display_name: Optional[pulumi.Input[Optional[str]]] = None,
                                management_group_id: Optional[pulumi.Input[Optional[str]]] = None,
                                management_group_name: Optional[pulumi.Input[Optional[str]]] = None,
                                name: Optional[pulumi.Input[Optional[str]]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPolicyDefintionResult]:
    """
    Use this data source to access information about a Policy Definition, both custom and built in. Retrieves Policy Definitions from your current subscription by default.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.policy.get_policy_defintion(display_name="Allowed resource types")
    pulumi.export("id", example.id)
    ```


    :param str display_name: Specifies the display name of the Policy Definition. Conflicts with `name`.
    :param str management_group_name: Only retrieve Policy Definitions from this Management Group.
    :param str name: Specifies the name of the Policy Definition. Conflicts with `display_name`.
    """
    ...
