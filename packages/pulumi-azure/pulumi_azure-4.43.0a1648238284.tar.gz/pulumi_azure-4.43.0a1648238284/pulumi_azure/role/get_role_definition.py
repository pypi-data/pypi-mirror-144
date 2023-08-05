# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetRoleDefinitionResult',
    'AwaitableGetRoleDefinitionResult',
    'get_role_definition',
    'get_role_definition_output',
]

warnings.warn("""azure.role.getRoleDefinition has been deprecated in favor of azure.authorization.getRoleDefinition""", DeprecationWarning)

@pulumi.output_type
class GetRoleDefinitionResult:
    """
    A collection of values returned by getRoleDefinition.
    """
    def __init__(__self__, assignable_scopes=None, description=None, id=None, name=None, permissions=None, role_definition_id=None, scope=None, type=None):
        if assignable_scopes and not isinstance(assignable_scopes, list):
            raise TypeError("Expected argument 'assignable_scopes' to be a list")
        pulumi.set(__self__, "assignable_scopes", assignable_scopes)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if permissions and not isinstance(permissions, list):
            raise TypeError("Expected argument 'permissions' to be a list")
        pulumi.set(__self__, "permissions", permissions)
        if role_definition_id and not isinstance(role_definition_id, str):
            raise TypeError("Expected argument 'role_definition_id' to be a str")
        pulumi.set(__self__, "role_definition_id", role_definition_id)
        if scope and not isinstance(scope, str):
            raise TypeError("Expected argument 'scope' to be a str")
        pulumi.set(__self__, "scope", scope)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="assignableScopes")
    def assignable_scopes(self) -> Sequence[str]:
        """
        One or more assignable scopes for this Role Definition, such as `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333`, `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup`, or `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM`.
        """
        return pulumi.get(self, "assignable_scopes")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        the Description of the built-in Role.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def permissions(self) -> Sequence['outputs.GetRoleDefinitionPermissionResult']:
        """
        a `permissions` block as documented below.
        """
        return pulumi.get(self, "permissions")

    @property
    @pulumi.getter(name="roleDefinitionId")
    def role_definition_id(self) -> str:
        return pulumi.get(self, "role_definition_id")

    @property
    @pulumi.getter
    def scope(self) -> Optional[str]:
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        the Type of the Role.
        """
        return pulumi.get(self, "type")


class AwaitableGetRoleDefinitionResult(GetRoleDefinitionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRoleDefinitionResult(
            assignable_scopes=self.assignable_scopes,
            description=self.description,
            id=self.id,
            name=self.name,
            permissions=self.permissions,
            role_definition_id=self.role_definition_id,
            scope=self.scope,
            type=self.type)


def get_role_definition(name: Optional[str] = None,
                        role_definition_id: Optional[str] = None,
                        scope: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRoleDefinitionResult:
    """
    Use this data source to access information about an existing Role Definition.


    :param str name: Specifies the Name of either a built-in or custom Role Definition.
    :param str role_definition_id: Specifies the ID of the Role Definition as a UUID/GUID.
    :param str scope: Specifies the Scope at which the Custom Role Definition exists.
    """
    pulumi.log.warn("""get_role_definition is deprecated: azure.role.getRoleDefinition has been deprecated in favor of azure.authorization.getRoleDefinition""")
    __args__ = dict()
    __args__['name'] = name
    __args__['roleDefinitionId'] = role_definition_id
    __args__['scope'] = scope
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure:role/getRoleDefinition:getRoleDefinition', __args__, opts=opts, typ=GetRoleDefinitionResult).value

    return AwaitableGetRoleDefinitionResult(
        assignable_scopes=__ret__.assignable_scopes,
        description=__ret__.description,
        id=__ret__.id,
        name=__ret__.name,
        permissions=__ret__.permissions,
        role_definition_id=__ret__.role_definition_id,
        scope=__ret__.scope,
        type=__ret__.type)


@_utilities.lift_output_func(get_role_definition)
def get_role_definition_output(name: Optional[pulumi.Input[Optional[str]]] = None,
                               role_definition_id: Optional[pulumi.Input[Optional[str]]] = None,
                               scope: Optional[pulumi.Input[Optional[str]]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRoleDefinitionResult]:
    """
    Use this data source to access information about an existing Role Definition.


    :param str name: Specifies the Name of either a built-in or custom Role Definition.
    :param str role_definition_id: Specifies the ID of the Role Definition as a UUID/GUID.
    :param str scope: Specifies the Scope at which the Custom Role Definition exists.
    """
    pulumi.log.warn("""get_role_definition is deprecated: azure.role.getRoleDefinition has been deprecated in favor of azure.authorization.getRoleDefinition""")
    ...
