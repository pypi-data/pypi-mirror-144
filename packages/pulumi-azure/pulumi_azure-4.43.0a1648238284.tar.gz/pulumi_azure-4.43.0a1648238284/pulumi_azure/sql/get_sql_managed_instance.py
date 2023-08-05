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
    'GetSqlManagedInstanceResult',
    'AwaitableGetSqlManagedInstanceResult',
    'get_sql_managed_instance',
    'get_sql_managed_instance_output',
]

@pulumi.output_type
class GetSqlManagedInstanceResult:
    """
    A collection of values returned by getSqlManagedInstance.
    """
    def __init__(__self__, administrator_login=None, collation=None, dns_zone_partner_id=None, fqdn=None, id=None, identities=None, license_type=None, location=None, minimum_tls_version=None, name=None, proxy_override=None, public_data_endpoint_enabled=None, resource_group_name=None, sku_name=None, storage_account_type=None, storage_size_in_gb=None, subnet_id=None, tags=None, timezone_id=None, vcores=None):
        if administrator_login and not isinstance(administrator_login, str):
            raise TypeError("Expected argument 'administrator_login' to be a str")
        pulumi.set(__self__, "administrator_login", administrator_login)
        if collation and not isinstance(collation, str):
            raise TypeError("Expected argument 'collation' to be a str")
        pulumi.set(__self__, "collation", collation)
        if dns_zone_partner_id and not isinstance(dns_zone_partner_id, str):
            raise TypeError("Expected argument 'dns_zone_partner_id' to be a str")
        pulumi.set(__self__, "dns_zone_partner_id", dns_zone_partner_id)
        if fqdn and not isinstance(fqdn, str):
            raise TypeError("Expected argument 'fqdn' to be a str")
        pulumi.set(__self__, "fqdn", fqdn)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identities and not isinstance(identities, list):
            raise TypeError("Expected argument 'identities' to be a list")
        pulumi.set(__self__, "identities", identities)
        if license_type and not isinstance(license_type, str):
            raise TypeError("Expected argument 'license_type' to be a str")
        pulumi.set(__self__, "license_type", license_type)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if minimum_tls_version and not isinstance(minimum_tls_version, str):
            raise TypeError("Expected argument 'minimum_tls_version' to be a str")
        pulumi.set(__self__, "minimum_tls_version", minimum_tls_version)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if proxy_override and not isinstance(proxy_override, str):
            raise TypeError("Expected argument 'proxy_override' to be a str")
        pulumi.set(__self__, "proxy_override", proxy_override)
        if public_data_endpoint_enabled and not isinstance(public_data_endpoint_enabled, bool):
            raise TypeError("Expected argument 'public_data_endpoint_enabled' to be a bool")
        pulumi.set(__self__, "public_data_endpoint_enabled", public_data_endpoint_enabled)
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if sku_name and not isinstance(sku_name, str):
            raise TypeError("Expected argument 'sku_name' to be a str")
        pulumi.set(__self__, "sku_name", sku_name)
        if storage_account_type and not isinstance(storage_account_type, str):
            raise TypeError("Expected argument 'storage_account_type' to be a str")
        pulumi.set(__self__, "storage_account_type", storage_account_type)
        if storage_size_in_gb and not isinstance(storage_size_in_gb, int):
            raise TypeError("Expected argument 'storage_size_in_gb' to be a int")
        pulumi.set(__self__, "storage_size_in_gb", storage_size_in_gb)
        if subnet_id and not isinstance(subnet_id, str):
            raise TypeError("Expected argument 'subnet_id' to be a str")
        pulumi.set(__self__, "subnet_id", subnet_id)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if timezone_id and not isinstance(timezone_id, str):
            raise TypeError("Expected argument 'timezone_id' to be a str")
        pulumi.set(__self__, "timezone_id", timezone_id)
        if vcores and not isinstance(vcores, int):
            raise TypeError("Expected argument 'vcores' to be a int")
        pulumi.set(__self__, "vcores", vcores)

    @property
    @pulumi.getter(name="administratorLogin")
    def administrator_login(self) -> str:
        return pulumi.get(self, "administrator_login")

    @property
    @pulumi.getter
    def collation(self) -> str:
        return pulumi.get(self, "collation")

    @property
    @pulumi.getter(name="dnsZonePartnerId")
    def dns_zone_partner_id(self) -> str:
        return pulumi.get(self, "dns_zone_partner_id")

    @property
    @pulumi.getter
    def fqdn(self) -> str:
        return pulumi.get(self, "fqdn")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identities(self) -> Sequence['outputs.GetSqlManagedInstanceIdentityResult']:
        return pulumi.get(self, "identities")

    @property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> str:
        return pulumi.get(self, "license_type")

    @property
    @pulumi.getter
    def location(self) -> str:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="minimumTlsVersion")
    def minimum_tls_version(self) -> str:
        return pulumi.get(self, "minimum_tls_version")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="proxyOverride")
    def proxy_override(self) -> str:
        return pulumi.get(self, "proxy_override")

    @property
    @pulumi.getter(name="publicDataEndpointEnabled")
    def public_data_endpoint_enabled(self) -> bool:
        return pulumi.get(self, "public_data_endpoint_enabled")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> str:
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="skuName")
    def sku_name(self) -> str:
        return pulumi.get(self, "sku_name")

    @property
    @pulumi.getter(name="storageAccountType")
    def storage_account_type(self) -> str:
        return pulumi.get(self, "storage_account_type")

    @property
    @pulumi.getter(name="storageSizeInGb")
    def storage_size_in_gb(self) -> int:
        return pulumi.get(self, "storage_size_in_gb")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> str:
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="timezoneId")
    def timezone_id(self) -> str:
        return pulumi.get(self, "timezone_id")

    @property
    @pulumi.getter
    def vcores(self) -> int:
        return pulumi.get(self, "vcores")


class AwaitableGetSqlManagedInstanceResult(GetSqlManagedInstanceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSqlManagedInstanceResult(
            administrator_login=self.administrator_login,
            collation=self.collation,
            dns_zone_partner_id=self.dns_zone_partner_id,
            fqdn=self.fqdn,
            id=self.id,
            identities=self.identities,
            license_type=self.license_type,
            location=self.location,
            minimum_tls_version=self.minimum_tls_version,
            name=self.name,
            proxy_override=self.proxy_override,
            public_data_endpoint_enabled=self.public_data_endpoint_enabled,
            resource_group_name=self.resource_group_name,
            sku_name=self.sku_name,
            storage_account_type=self.storage_account_type,
            storage_size_in_gb=self.storage_size_in_gb,
            subnet_id=self.subnet_id,
            tags=self.tags,
            timezone_id=self.timezone_id,
            vcores=self.vcores)


def get_sql_managed_instance(name: Optional[str] = None,
                             resource_group_name: Optional[str] = None,
                             tags: Optional[Mapping[str, str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSqlManagedInstanceResult:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.sql.get_sql_managed_instance(name="example_mi",
        resource_group_name="example-resources")
    pulumi.export("sqlInstanceId", example.id)
    ```
    ## Attribues Reference

    * `id` - The SQL Managed Instance ID.

    * `fqdn` - The fully qualified domain name of the Azure Managed SQL Instance.

    * `location` - Location where the resource exists.

    * `sku_name` - SKU Name for the SQL Managed Instance.

    * `vcores` - Number of cores assigned to your instance.

    * `storage_size_in_gb` - Maximum storage space for your instance.

    * `license_type` - Type of license the Managed Instance uses.

    * `administrator_login` - The administrator login name for the new server.

    * `subnet_id` - The subnet resource id that the SQL Managed Instance is associated with.

    * `collation` - Specifies how the SQL Managed Instance is collated.

    * `public_data_endpoint_enabled` - Is the public data endpoint enabled?

    * `minimum_tls_version` - The Minimum TLS Version.

    * `proxy_override` - How the SQL Managed Instance is accessed.

    * `timezone_id` - The TimeZone ID that the SQL Managed Instance is operating in.

    * `dns_zone_partner_id` - The ID of the Managed Instance which is sharing the DNS zone.

    * `identity` - An `identity` block as defined below.

    * `storage_account_type` - Storage account type used to store backups for this SQL Managed Instance.

    * `tags` - A mapping of tags assigned to the resource.

    ***

    The `identity` block exports the following:

    * `principal_id` - The Principal ID for the Service Principal associated with the Identity of this SQL Managed Instance.

    * `tenant_id` - The Tenant ID for the Service Principal associated with the Identity of this SQL Managed Instance.


    :param str name: The name of the SQL Managed Instance.
    :param str resource_group_name: The name of the Resource Group in which the SQL Managed Instance exists.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    __args__['tags'] = tags
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure:sql/getSqlManagedInstance:getSqlManagedInstance', __args__, opts=opts, typ=GetSqlManagedInstanceResult).value

    return AwaitableGetSqlManagedInstanceResult(
        administrator_login=__ret__.administrator_login,
        collation=__ret__.collation,
        dns_zone_partner_id=__ret__.dns_zone_partner_id,
        fqdn=__ret__.fqdn,
        id=__ret__.id,
        identities=__ret__.identities,
        license_type=__ret__.license_type,
        location=__ret__.location,
        minimum_tls_version=__ret__.minimum_tls_version,
        name=__ret__.name,
        proxy_override=__ret__.proxy_override,
        public_data_endpoint_enabled=__ret__.public_data_endpoint_enabled,
        resource_group_name=__ret__.resource_group_name,
        sku_name=__ret__.sku_name,
        storage_account_type=__ret__.storage_account_type,
        storage_size_in_gb=__ret__.storage_size_in_gb,
        subnet_id=__ret__.subnet_id,
        tags=__ret__.tags,
        timezone_id=__ret__.timezone_id,
        vcores=__ret__.vcores)


@_utilities.lift_output_func(get_sql_managed_instance)
def get_sql_managed_instance_output(name: Optional[pulumi.Input[str]] = None,
                                    resource_group_name: Optional[pulumi.Input[str]] = None,
                                    tags: Optional[pulumi.Input[Optional[Mapping[str, str]]]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSqlManagedInstanceResult]:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.sql.get_sql_managed_instance(name="example_mi",
        resource_group_name="example-resources")
    pulumi.export("sqlInstanceId", example.id)
    ```
    ## Attribues Reference

    * `id` - The SQL Managed Instance ID.

    * `fqdn` - The fully qualified domain name of the Azure Managed SQL Instance.

    * `location` - Location where the resource exists.

    * `sku_name` - SKU Name for the SQL Managed Instance.

    * `vcores` - Number of cores assigned to your instance.

    * `storage_size_in_gb` - Maximum storage space for your instance.

    * `license_type` - Type of license the Managed Instance uses.

    * `administrator_login` - The administrator login name for the new server.

    * `subnet_id` - The subnet resource id that the SQL Managed Instance is associated with.

    * `collation` - Specifies how the SQL Managed Instance is collated.

    * `public_data_endpoint_enabled` - Is the public data endpoint enabled?

    * `minimum_tls_version` - The Minimum TLS Version.

    * `proxy_override` - How the SQL Managed Instance is accessed.

    * `timezone_id` - The TimeZone ID that the SQL Managed Instance is operating in.

    * `dns_zone_partner_id` - The ID of the Managed Instance which is sharing the DNS zone.

    * `identity` - An `identity` block as defined below.

    * `storage_account_type` - Storage account type used to store backups for this SQL Managed Instance.

    * `tags` - A mapping of tags assigned to the resource.

    ***

    The `identity` block exports the following:

    * `principal_id` - The Principal ID for the Service Principal associated with the Identity of this SQL Managed Instance.

    * `tenant_id` - The Tenant ID for the Service Principal associated with the Identity of this SQL Managed Instance.


    :param str name: The name of the SQL Managed Instance.
    :param str resource_group_name: The name of the Resource Group in which the SQL Managed Instance exists.
    """
    ...
