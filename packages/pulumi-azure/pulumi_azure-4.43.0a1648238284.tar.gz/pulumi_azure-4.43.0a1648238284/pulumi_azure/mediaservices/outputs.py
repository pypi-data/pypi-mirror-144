# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'AccountIdentity',
    'AccountKeyDeliveryAccessControl',
    'AccountStorageAccount',
]

@pulumi.output_type
class AccountIdentity(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "principalId":
            suggest = "principal_id"
        elif key == "tenantId":
            suggest = "tenant_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AccountIdentity. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AccountIdentity.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AccountIdentity.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 type: str,
                 principal_id: Optional[str] = None,
                 tenant_id: Optional[str] = None):
        """
        :param str type: Specifies the type of Managed Service Identity that should be configured on this Media Services Account. Possible value is  `SystemAssigned`.
        :param str principal_id: The Principal ID associated with this Managed Service Identity.
        :param str tenant_id: The Tenant ID associated with this Managed Service Identity.
        """
        pulumi.set(__self__, "type", type)
        if principal_id is not None:
            pulumi.set(__self__, "principal_id", principal_id)
        if tenant_id is not None:
            pulumi.set(__self__, "tenant_id", tenant_id)

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Specifies the type of Managed Service Identity that should be configured on this Media Services Account. Possible value is  `SystemAssigned`.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[str]:
        """
        The Principal ID associated with this Managed Service Identity.
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[str]:
        """
        The Tenant ID associated with this Managed Service Identity.
        """
        return pulumi.get(self, "tenant_id")


@pulumi.output_type
class AccountKeyDeliveryAccessControl(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "defaultAction":
            suggest = "default_action"
        elif key == "ipAllowLists":
            suggest = "ip_allow_lists"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AccountKeyDeliveryAccessControl. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AccountKeyDeliveryAccessControl.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AccountKeyDeliveryAccessControl.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 default_action: Optional[str] = None,
                 ip_allow_lists: Optional[Sequence[str]] = None):
        """
        :param str default_action: The Default Action to use when no rules match from `ip_allow_list`. Possible values are `Allow` and `Deny`.
        :param Sequence[str] ip_allow_lists: One or more IP Addresses, or CIDR Blocks which should be able to access the Key Delivery.
        """
        if default_action is not None:
            pulumi.set(__self__, "default_action", default_action)
        if ip_allow_lists is not None:
            pulumi.set(__self__, "ip_allow_lists", ip_allow_lists)

    @property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> Optional[str]:
        """
        The Default Action to use when no rules match from `ip_allow_list`. Possible values are `Allow` and `Deny`.
        """
        return pulumi.get(self, "default_action")

    @property
    @pulumi.getter(name="ipAllowLists")
    def ip_allow_lists(self) -> Optional[Sequence[str]]:
        """
        One or more IP Addresses, or CIDR Blocks which should be able to access the Key Delivery.
        """
        return pulumi.get(self, "ip_allow_lists")


@pulumi.output_type
class AccountStorageAccount(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "isPrimary":
            suggest = "is_primary"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AccountStorageAccount. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AccountStorageAccount.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AccountStorageAccount.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 id: str,
                 is_primary: Optional[bool] = None):
        """
        :param str id: Specifies the ID of the Storage Account that will be associated with the Media Services instance.
        :param bool is_primary: Specifies whether the storage account should be the primary account or not. Defaults to `false`.
        """
        pulumi.set(__self__, "id", id)
        if is_primary is not None:
            pulumi.set(__self__, "is_primary", is_primary)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Specifies the ID of the Storage Account that will be associated with the Media Services instance.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isPrimary")
    def is_primary(self) -> Optional[bool]:
        """
        Specifies whether the storage account should be the primary account or not. Defaults to `false`.
        """
        return pulumi.get(self, "is_primary")


