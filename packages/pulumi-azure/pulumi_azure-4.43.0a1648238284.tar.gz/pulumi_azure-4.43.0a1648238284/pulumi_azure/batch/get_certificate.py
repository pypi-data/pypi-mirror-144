# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetCertificateResult',
    'AwaitableGetCertificateResult',
    'get_certificate',
    'get_certificate_output',
]

@pulumi.output_type
class GetCertificateResult:
    """
    A collection of values returned by getCertificate.
    """
    def __init__(__self__, account_name=None, format=None, id=None, name=None, public_data=None, resource_group_name=None, thumbprint=None, thumbprint_algorithm=None):
        if account_name and not isinstance(account_name, str):
            raise TypeError("Expected argument 'account_name' to be a str")
        pulumi.set(__self__, "account_name", account_name)
        if format and not isinstance(format, str):
            raise TypeError("Expected argument 'format' to be a str")
        pulumi.set(__self__, "format", format)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if public_data and not isinstance(public_data, str):
            raise TypeError("Expected argument 'public_data' to be a str")
        pulumi.set(__self__, "public_data", public_data)
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if thumbprint and not isinstance(thumbprint, str):
            raise TypeError("Expected argument 'thumbprint' to be a str")
        pulumi.set(__self__, "thumbprint", thumbprint)
        if thumbprint_algorithm and not isinstance(thumbprint_algorithm, str):
            raise TypeError("Expected argument 'thumbprint_algorithm' to be a str")
        pulumi.set(__self__, "thumbprint_algorithm", thumbprint_algorithm)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> str:
        return pulumi.get(self, "account_name")

    @property
    @pulumi.getter
    def format(self) -> str:
        """
        The format of the certificate, such as `Cer` or `Pfx`.
        """
        return pulumi.get(self, "format")

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
    @pulumi.getter(name="publicData")
    def public_data(self) -> str:
        """
        The public key of the certificate.
        """
        return pulumi.get(self, "public_data")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> str:
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter
    def thumbprint(self) -> str:
        """
        The thumbprint of the certificate.
        """
        return pulumi.get(self, "thumbprint")

    @property
    @pulumi.getter(name="thumbprintAlgorithm")
    def thumbprint_algorithm(self) -> str:
        """
        The algorithm of the certificate thumbprint.
        """
        return pulumi.get(self, "thumbprint_algorithm")


class AwaitableGetCertificateResult(GetCertificateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCertificateResult(
            account_name=self.account_name,
            format=self.format,
            id=self.id,
            name=self.name,
            public_data=self.public_data,
            resource_group_name=self.resource_group_name,
            thumbprint=self.thumbprint,
            thumbprint_algorithm=self.thumbprint_algorithm)


def get_certificate(account_name: Optional[str] = None,
                    name: Optional[str] = None,
                    resource_group_name: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCertificateResult:
    """
    Use this data source to access information about an existing certificate in a Batch Account.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.batch.get_certificate(name="SHA1-42C107874FD0E4A9583292A2F1098E8FE4B2EDDA",
        account_name="examplebatchaccount",
        resource_group_name="example")
    pulumi.export("thumbprint", example.thumbprint)
    ```


    :param str account_name: The name of the Batch account.
    :param str name: The name of the Batch certificate.
    :param str resource_group_name: The Name of the Resource Group where this Batch account exists.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure:batch/getCertificate:getCertificate', __args__, opts=opts, typ=GetCertificateResult).value

    return AwaitableGetCertificateResult(
        account_name=__ret__.account_name,
        format=__ret__.format,
        id=__ret__.id,
        name=__ret__.name,
        public_data=__ret__.public_data,
        resource_group_name=__ret__.resource_group_name,
        thumbprint=__ret__.thumbprint,
        thumbprint_algorithm=__ret__.thumbprint_algorithm)


@_utilities.lift_output_func(get_certificate)
def get_certificate_output(account_name: Optional[pulumi.Input[str]] = None,
                           name: Optional[pulumi.Input[str]] = None,
                           resource_group_name: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCertificateResult]:
    """
    Use this data source to access information about an existing certificate in a Batch Account.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.batch.get_certificate(name="SHA1-42C107874FD0E4A9583292A2F1098E8FE4B2EDDA",
        account_name="examplebatchaccount",
        resource_group_name="example")
    pulumi.export("thumbprint", example.thumbprint)
    ```


    :param str account_name: The name of the Batch account.
    :param str name: The name of the Batch certificate.
    :param str resource_group_name: The Name of the Resource Group where this Batch account exists.
    """
    ...
