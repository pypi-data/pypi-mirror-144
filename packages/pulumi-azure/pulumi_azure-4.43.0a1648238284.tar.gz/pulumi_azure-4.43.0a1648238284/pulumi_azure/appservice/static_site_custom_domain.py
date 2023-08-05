# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['StaticSiteCustomDomainArgs', 'StaticSiteCustomDomain']

@pulumi.input_type
class StaticSiteCustomDomainArgs:
    def __init__(__self__, *,
                 domain_name: pulumi.Input[str],
                 static_site_id: pulumi.Input[str],
                 validation_type: pulumi.Input[str]):
        """
        The set of arguments for constructing a StaticSiteCustomDomain resource.
        :param pulumi.Input[str] domain_name: The Domain Name which should be associated with this Static Site. Changing this forces a new Static Site Custom Domain to be created.
        :param pulumi.Input[str] static_site_id: The ID of the Static Site. Changing this forces a new Static Site Custom Domain to be created.
        :param pulumi.Input[str] validation_type: One of `cname-delegation` or `dns-txt-token`. Changing this forces a new Static Site Custom Domain to be created.
        """
        pulumi.set(__self__, "domain_name", domain_name)
        pulumi.set(__self__, "static_site_id", static_site_id)
        pulumi.set(__self__, "validation_type", validation_type)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[str]:
        """
        The Domain Name which should be associated with this Static Site. Changing this forces a new Static Site Custom Domain to be created.
        """
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain_name", value)

    @property
    @pulumi.getter(name="staticSiteId")
    def static_site_id(self) -> pulumi.Input[str]:
        """
        The ID of the Static Site. Changing this forces a new Static Site Custom Domain to be created.
        """
        return pulumi.get(self, "static_site_id")

    @static_site_id.setter
    def static_site_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "static_site_id", value)

    @property
    @pulumi.getter(name="validationType")
    def validation_type(self) -> pulumi.Input[str]:
        """
        One of `cname-delegation` or `dns-txt-token`. Changing this forces a new Static Site Custom Domain to be created.
        """
        return pulumi.get(self, "validation_type")

    @validation_type.setter
    def validation_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "validation_type", value)


@pulumi.input_type
class _StaticSiteCustomDomainState:
    def __init__(__self__, *,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 static_site_id: Optional[pulumi.Input[str]] = None,
                 validation_token: Optional[pulumi.Input[str]] = None,
                 validation_type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering StaticSiteCustomDomain resources.
        :param pulumi.Input[str] domain_name: The Domain Name which should be associated with this Static Site. Changing this forces a new Static Site Custom Domain to be created.
        :param pulumi.Input[str] static_site_id: The ID of the Static Site. Changing this forces a new Static Site Custom Domain to be created.
        :param pulumi.Input[str] validation_token: Token to be used with `dns-txt-token` validation.
        :param pulumi.Input[str] validation_type: One of `cname-delegation` or `dns-txt-token`. Changing this forces a new Static Site Custom Domain to be created.
        """
        if domain_name is not None:
            pulumi.set(__self__, "domain_name", domain_name)
        if static_site_id is not None:
            pulumi.set(__self__, "static_site_id", static_site_id)
        if validation_token is not None:
            pulumi.set(__self__, "validation_token", validation_token)
        if validation_type is not None:
            pulumi.set(__self__, "validation_type", validation_type)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[str]]:
        """
        The Domain Name which should be associated with this Static Site. Changing this forces a new Static Site Custom Domain to be created.
        """
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain_name", value)

    @property
    @pulumi.getter(name="staticSiteId")
    def static_site_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Static Site. Changing this forces a new Static Site Custom Domain to be created.
        """
        return pulumi.get(self, "static_site_id")

    @static_site_id.setter
    def static_site_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "static_site_id", value)

    @property
    @pulumi.getter(name="validationToken")
    def validation_token(self) -> Optional[pulumi.Input[str]]:
        """
        Token to be used with `dns-txt-token` validation.
        """
        return pulumi.get(self, "validation_token")

    @validation_token.setter
    def validation_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "validation_token", value)

    @property
    @pulumi.getter(name="validationType")
    def validation_type(self) -> Optional[pulumi.Input[str]]:
        """
        One of `cname-delegation` or `dns-txt-token`. Changing this forces a new Static Site Custom Domain to be created.
        """
        return pulumi.get(self, "validation_type")

    @validation_type.setter
    def validation_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "validation_type", value)


class StaticSiteCustomDomain(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 static_site_id: Optional[pulumi.Input[str]] = None,
                 validation_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage
        ### CNAME validation

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_static_site = azure.appservice.StaticSite("exampleStaticSite",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location)
        example_c_name_record = azure.dns.CNameRecord("exampleCNameRecord",
            zone_name="contoso.com",
            resource_group_name=example_resource_group.name,
            ttl=300,
            record=example_static_site.default_host_name)
        example_static_site_custom_domain = azure.appservice.StaticSiteCustomDomain("exampleStaticSiteCustomDomain",
            static_site_id=example_static_site.id,
            domain_name=pulumi.Output.all(example_c_name_record.name, example_c_name_record.zone_name).apply(lambda name, zone_name: f"{name}.{zone_name}"),
            validation_type="cname-delegation")
        ```
        ### TXT validation

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_static_site = azure.appservice.StaticSite("exampleStaticSite",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location)
        example_static_site_custom_domain = azure.appservice.StaticSiteCustomDomain("exampleStaticSiteCustomDomain",
            static_site_id=example_static_site.id,
            domain_name=f"my-domain.{azurerm_dns_cname_record['example']['zone_name']}",
            validation_type="dns-txt-token")
        example_txt_record = azure.dns.TxtRecord("exampleTxtRecord",
            zone_name="contoso.com",
            resource_group_name=example_resource_group.name,
            ttl=300,
            records=[azure.dns.TxtRecordRecordArgs(
                value=example_static_site_custom_domain.validation_token,
            )])
        ```

        ## Import

        Static Site Custom Domains can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:appservice/staticSiteCustomDomain:StaticSiteCustomDomain example /subscriptions/12345678-1234-9876-4563-123456789012/resourceGroups/group1/providers/Microsoft.Web/staticSites/my-static-site1/customDomains/name.contoso.com
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] domain_name: The Domain Name which should be associated with this Static Site. Changing this forces a new Static Site Custom Domain to be created.
        :param pulumi.Input[str] static_site_id: The ID of the Static Site. Changing this forces a new Static Site Custom Domain to be created.
        :param pulumi.Input[str] validation_type: One of `cname-delegation` or `dns-txt-token`. Changing this forces a new Static Site Custom Domain to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: StaticSiteCustomDomainArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage
        ### CNAME validation

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_static_site = azure.appservice.StaticSite("exampleStaticSite",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location)
        example_c_name_record = azure.dns.CNameRecord("exampleCNameRecord",
            zone_name="contoso.com",
            resource_group_name=example_resource_group.name,
            ttl=300,
            record=example_static_site.default_host_name)
        example_static_site_custom_domain = azure.appservice.StaticSiteCustomDomain("exampleStaticSiteCustomDomain",
            static_site_id=example_static_site.id,
            domain_name=pulumi.Output.all(example_c_name_record.name, example_c_name_record.zone_name).apply(lambda name, zone_name: f"{name}.{zone_name}"),
            validation_type="cname-delegation")
        ```
        ### TXT validation

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_static_site = azure.appservice.StaticSite("exampleStaticSite",
            resource_group_name=example_resource_group.name,
            location=example_resource_group.location)
        example_static_site_custom_domain = azure.appservice.StaticSiteCustomDomain("exampleStaticSiteCustomDomain",
            static_site_id=example_static_site.id,
            domain_name=f"my-domain.{azurerm_dns_cname_record['example']['zone_name']}",
            validation_type="dns-txt-token")
        example_txt_record = azure.dns.TxtRecord("exampleTxtRecord",
            zone_name="contoso.com",
            resource_group_name=example_resource_group.name,
            ttl=300,
            records=[azure.dns.TxtRecordRecordArgs(
                value=example_static_site_custom_domain.validation_token,
            )])
        ```

        ## Import

        Static Site Custom Domains can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:appservice/staticSiteCustomDomain:StaticSiteCustomDomain example /subscriptions/12345678-1234-9876-4563-123456789012/resourceGroups/group1/providers/Microsoft.Web/staticSites/my-static-site1/customDomains/name.contoso.com
        ```

        :param str resource_name: The name of the resource.
        :param StaticSiteCustomDomainArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(StaticSiteCustomDomainArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 static_site_id: Optional[pulumi.Input[str]] = None,
                 validation_type: Optional[pulumi.Input[str]] = None,
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
            __props__ = StaticSiteCustomDomainArgs.__new__(StaticSiteCustomDomainArgs)

            if domain_name is None and not opts.urn:
                raise TypeError("Missing required property 'domain_name'")
            __props__.__dict__["domain_name"] = domain_name
            if static_site_id is None and not opts.urn:
                raise TypeError("Missing required property 'static_site_id'")
            __props__.__dict__["static_site_id"] = static_site_id
            if validation_type is None and not opts.urn:
                raise TypeError("Missing required property 'validation_type'")
            __props__.__dict__["validation_type"] = validation_type
            __props__.__dict__["validation_token"] = None
        super(StaticSiteCustomDomain, __self__).__init__(
            'azure:appservice/staticSiteCustomDomain:StaticSiteCustomDomain',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            domain_name: Optional[pulumi.Input[str]] = None,
            static_site_id: Optional[pulumi.Input[str]] = None,
            validation_token: Optional[pulumi.Input[str]] = None,
            validation_type: Optional[pulumi.Input[str]] = None) -> 'StaticSiteCustomDomain':
        """
        Get an existing StaticSiteCustomDomain resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] domain_name: The Domain Name which should be associated with this Static Site. Changing this forces a new Static Site Custom Domain to be created.
        :param pulumi.Input[str] static_site_id: The ID of the Static Site. Changing this forces a new Static Site Custom Domain to be created.
        :param pulumi.Input[str] validation_token: Token to be used with `dns-txt-token` validation.
        :param pulumi.Input[str] validation_type: One of `cname-delegation` or `dns-txt-token`. Changing this forces a new Static Site Custom Domain to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _StaticSiteCustomDomainState.__new__(_StaticSiteCustomDomainState)

        __props__.__dict__["domain_name"] = domain_name
        __props__.__dict__["static_site_id"] = static_site_id
        __props__.__dict__["validation_token"] = validation_token
        __props__.__dict__["validation_type"] = validation_type
        return StaticSiteCustomDomain(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[str]:
        """
        The Domain Name which should be associated with this Static Site. Changing this forces a new Static Site Custom Domain to be created.
        """
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter(name="staticSiteId")
    def static_site_id(self) -> pulumi.Output[str]:
        """
        The ID of the Static Site. Changing this forces a new Static Site Custom Domain to be created.
        """
        return pulumi.get(self, "static_site_id")

    @property
    @pulumi.getter(name="validationToken")
    def validation_token(self) -> pulumi.Output[str]:
        """
        Token to be used with `dns-txt-token` validation.
        """
        return pulumi.get(self, "validation_token")

    @property
    @pulumi.getter(name="validationType")
    def validation_type(self) -> pulumi.Output[str]:
        """
        One of `cname-delegation` or `dns-txt-token`. Changing this forces a new Static Site Custom Domain to be created.
        """
        return pulumi.get(self, "validation_type")

