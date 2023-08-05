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
    'GetKubernetesClusterResult',
    'AwaitableGetKubernetesClusterResult',
    'get_kubernetes_cluster',
    'get_kubernetes_cluster_output',
]

@pulumi.output_type
class GetKubernetesClusterResult:
    """
    A collection of values returned by getKubernetesCluster.
    """
    def __init__(__self__, aci_connector_linuxes=None, addon_profiles=None, agent_pool_profiles=None, api_server_authorized_ip_ranges=None, azure_active_directory_role_based_access_controls=None, azure_policy_enabled=None, disk_encryption_set_id=None, dns_prefix=None, fqdn=None, http_application_routing_enabled=None, http_application_routing_zone_name=None, id=None, identities=None, ingress_application_gateways=None, key_vault_secrets_providers=None, kube_admin_config_raw=None, kube_admin_configs=None, kube_config_raw=None, kube_configs=None, kubelet_identities=None, kubernetes_version=None, linux_profiles=None, location=None, name=None, network_profiles=None, node_resource_group=None, oms_agents=None, open_service_mesh_enabled=None, private_cluster_enabled=None, private_fqdn=None, private_link_enabled=None, resource_group_name=None, role_based_access_control_enabled=None, role_based_access_controls=None, service_principals=None, tags=None, windows_profiles=None):
        if aci_connector_linuxes and not isinstance(aci_connector_linuxes, list):
            raise TypeError("Expected argument 'aci_connector_linuxes' to be a list")
        pulumi.set(__self__, "aci_connector_linuxes", aci_connector_linuxes)
        if addon_profiles and not isinstance(addon_profiles, list):
            raise TypeError("Expected argument 'addon_profiles' to be a list")
        if addon_profiles is not None:
            warnings.warn("""`addon_profile` is deprecated in favour of the properties `https_application_routing_enabled`, `azure_policy_enabled`, `open_service_mesh_enabled` and the blocks `oms_agent`, `ingress_application_gateway` and `key_vault_secrets_provider` and will be removed in version 3.0 of the AzureRM Provider""", DeprecationWarning)
            pulumi.log.warn("""addon_profiles is deprecated: `addon_profile` is deprecated in favour of the properties `https_application_routing_enabled`, `azure_policy_enabled`, `open_service_mesh_enabled` and the blocks `oms_agent`, `ingress_application_gateway` and `key_vault_secrets_provider` and will be removed in version 3.0 of the AzureRM Provider""")

        pulumi.set(__self__, "addon_profiles", addon_profiles)
        if agent_pool_profiles and not isinstance(agent_pool_profiles, list):
            raise TypeError("Expected argument 'agent_pool_profiles' to be a list")
        pulumi.set(__self__, "agent_pool_profiles", agent_pool_profiles)
        if api_server_authorized_ip_ranges and not isinstance(api_server_authorized_ip_ranges, list):
            raise TypeError("Expected argument 'api_server_authorized_ip_ranges' to be a list")
        pulumi.set(__self__, "api_server_authorized_ip_ranges", api_server_authorized_ip_ranges)
        if azure_active_directory_role_based_access_controls and not isinstance(azure_active_directory_role_based_access_controls, list):
            raise TypeError("Expected argument 'azure_active_directory_role_based_access_controls' to be a list")
        pulumi.set(__self__, "azure_active_directory_role_based_access_controls", azure_active_directory_role_based_access_controls)
        if azure_policy_enabled and not isinstance(azure_policy_enabled, bool):
            raise TypeError("Expected argument 'azure_policy_enabled' to be a bool")
        pulumi.set(__self__, "azure_policy_enabled", azure_policy_enabled)
        if disk_encryption_set_id and not isinstance(disk_encryption_set_id, str):
            raise TypeError("Expected argument 'disk_encryption_set_id' to be a str")
        pulumi.set(__self__, "disk_encryption_set_id", disk_encryption_set_id)
        if dns_prefix and not isinstance(dns_prefix, str):
            raise TypeError("Expected argument 'dns_prefix' to be a str")
        pulumi.set(__self__, "dns_prefix", dns_prefix)
        if fqdn and not isinstance(fqdn, str):
            raise TypeError("Expected argument 'fqdn' to be a str")
        pulumi.set(__self__, "fqdn", fqdn)
        if http_application_routing_enabled and not isinstance(http_application_routing_enabled, bool):
            raise TypeError("Expected argument 'http_application_routing_enabled' to be a bool")
        pulumi.set(__self__, "http_application_routing_enabled", http_application_routing_enabled)
        if http_application_routing_zone_name and not isinstance(http_application_routing_zone_name, str):
            raise TypeError("Expected argument 'http_application_routing_zone_name' to be a str")
        pulumi.set(__self__, "http_application_routing_zone_name", http_application_routing_zone_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identities and not isinstance(identities, list):
            raise TypeError("Expected argument 'identities' to be a list")
        pulumi.set(__self__, "identities", identities)
        if ingress_application_gateways and not isinstance(ingress_application_gateways, list):
            raise TypeError("Expected argument 'ingress_application_gateways' to be a list")
        pulumi.set(__self__, "ingress_application_gateways", ingress_application_gateways)
        if key_vault_secrets_providers and not isinstance(key_vault_secrets_providers, list):
            raise TypeError("Expected argument 'key_vault_secrets_providers' to be a list")
        pulumi.set(__self__, "key_vault_secrets_providers", key_vault_secrets_providers)
        if kube_admin_config_raw and not isinstance(kube_admin_config_raw, str):
            raise TypeError("Expected argument 'kube_admin_config_raw' to be a str")
        pulumi.set(__self__, "kube_admin_config_raw", kube_admin_config_raw)
        if kube_admin_configs and not isinstance(kube_admin_configs, list):
            raise TypeError("Expected argument 'kube_admin_configs' to be a list")
        pulumi.set(__self__, "kube_admin_configs", kube_admin_configs)
        if kube_config_raw and not isinstance(kube_config_raw, str):
            raise TypeError("Expected argument 'kube_config_raw' to be a str")
        pulumi.set(__self__, "kube_config_raw", kube_config_raw)
        if kube_configs and not isinstance(kube_configs, list):
            raise TypeError("Expected argument 'kube_configs' to be a list")
        pulumi.set(__self__, "kube_configs", kube_configs)
        if kubelet_identities and not isinstance(kubelet_identities, list):
            raise TypeError("Expected argument 'kubelet_identities' to be a list")
        pulumi.set(__self__, "kubelet_identities", kubelet_identities)
        if kubernetes_version and not isinstance(kubernetes_version, str):
            raise TypeError("Expected argument 'kubernetes_version' to be a str")
        pulumi.set(__self__, "kubernetes_version", kubernetes_version)
        if linux_profiles and not isinstance(linux_profiles, list):
            raise TypeError("Expected argument 'linux_profiles' to be a list")
        pulumi.set(__self__, "linux_profiles", linux_profiles)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_profiles and not isinstance(network_profiles, list):
            raise TypeError("Expected argument 'network_profiles' to be a list")
        pulumi.set(__self__, "network_profiles", network_profiles)
        if node_resource_group and not isinstance(node_resource_group, str):
            raise TypeError("Expected argument 'node_resource_group' to be a str")
        pulumi.set(__self__, "node_resource_group", node_resource_group)
        if oms_agents and not isinstance(oms_agents, list):
            raise TypeError("Expected argument 'oms_agents' to be a list")
        pulumi.set(__self__, "oms_agents", oms_agents)
        if open_service_mesh_enabled and not isinstance(open_service_mesh_enabled, bool):
            raise TypeError("Expected argument 'open_service_mesh_enabled' to be a bool")
        pulumi.set(__self__, "open_service_mesh_enabled", open_service_mesh_enabled)
        if private_cluster_enabled and not isinstance(private_cluster_enabled, bool):
            raise TypeError("Expected argument 'private_cluster_enabled' to be a bool")
        pulumi.set(__self__, "private_cluster_enabled", private_cluster_enabled)
        if private_fqdn and not isinstance(private_fqdn, str):
            raise TypeError("Expected argument 'private_fqdn' to be a str")
        pulumi.set(__self__, "private_fqdn", private_fqdn)
        if private_link_enabled and not isinstance(private_link_enabled, bool):
            raise TypeError("Expected argument 'private_link_enabled' to be a bool")
        if private_link_enabled is not None:
            warnings.warn("""`private_link_enabled` is deprecated in favour of `private_cluster_enabled` and will be removed in version 3.0 of the AzureRM Provider""", DeprecationWarning)
            pulumi.log.warn("""private_link_enabled is deprecated: `private_link_enabled` is deprecated in favour of `private_cluster_enabled` and will be removed in version 3.0 of the AzureRM Provider""")

        pulumi.set(__self__, "private_link_enabled", private_link_enabled)
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if role_based_access_control_enabled and not isinstance(role_based_access_control_enabled, bool):
            raise TypeError("Expected argument 'role_based_access_control_enabled' to be a bool")
        pulumi.set(__self__, "role_based_access_control_enabled", role_based_access_control_enabled)
        if role_based_access_controls and not isinstance(role_based_access_controls, list):
            raise TypeError("Expected argument 'role_based_access_controls' to be a list")
        if role_based_access_controls is not None:
            warnings.warn("""`role_based_access_control` is deprecated in favour of the property `role_based_access_control_enabled` and the block `azure_active_directory_role_based_access_control` and will be removed in version 3.0 of the AzureRM Provider.""", DeprecationWarning)
            pulumi.log.warn("""role_based_access_controls is deprecated: `role_based_access_control` is deprecated in favour of the property `role_based_access_control_enabled` and the block `azure_active_directory_role_based_access_control` and will be removed in version 3.0 of the AzureRM Provider.""")

        pulumi.set(__self__, "role_based_access_controls", role_based_access_controls)
        if service_principals and not isinstance(service_principals, list):
            raise TypeError("Expected argument 'service_principals' to be a list")
        pulumi.set(__self__, "service_principals", service_principals)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if windows_profiles and not isinstance(windows_profiles, list):
            raise TypeError("Expected argument 'windows_profiles' to be a list")
        pulumi.set(__self__, "windows_profiles", windows_profiles)

    @property
    @pulumi.getter(name="aciConnectorLinuxes")
    def aci_connector_linuxes(self) -> Sequence['outputs.GetKubernetesClusterAciConnectorLinuxResult']:
        """
        An `aci_connector_linux` block as documented below.
        """
        return pulumi.get(self, "aci_connector_linuxes")

    @property
    @pulumi.getter(name="addonProfiles")
    def addon_profiles(self) -> Sequence['outputs.GetKubernetesClusterAddonProfileResult']:
        return pulumi.get(self, "addon_profiles")

    @property
    @pulumi.getter(name="agentPoolProfiles")
    def agent_pool_profiles(self) -> Sequence['outputs.GetKubernetesClusterAgentPoolProfileResult']:
        """
        An `agent_pool_profile` block as documented below.
        """
        return pulumi.get(self, "agent_pool_profiles")

    @property
    @pulumi.getter(name="apiServerAuthorizedIpRanges")
    def api_server_authorized_ip_ranges(self) -> Sequence[str]:
        """
        The IP ranges to whitelist for incoming traffic to the primaries.
        """
        return pulumi.get(self, "api_server_authorized_ip_ranges")

    @property
    @pulumi.getter(name="azureActiveDirectoryRoleBasedAccessControls")
    def azure_active_directory_role_based_access_controls(self) -> Sequence['outputs.GetKubernetesClusterAzureActiveDirectoryRoleBasedAccessControlResult']:
        """
        An `azure_active_directory_role_based_access_control` block as documented below.
        """
        return pulumi.get(self, "azure_active_directory_role_based_access_controls")

    @property
    @pulumi.getter(name="azurePolicyEnabled")
    def azure_policy_enabled(self) -> bool:
        """
        Is Azure Policy enabled on this managed Kubernetes Cluster?
        """
        return pulumi.get(self, "azure_policy_enabled")

    @property
    @pulumi.getter(name="diskEncryptionSetId")
    def disk_encryption_set_id(self) -> str:
        """
        The ID of the Disk Encryption Set used for the Nodes and Volumes.
        """
        return pulumi.get(self, "disk_encryption_set_id")

    @property
    @pulumi.getter(name="dnsPrefix")
    def dns_prefix(self) -> str:
        """
        The DNS Prefix of the managed Kubernetes cluster.
        """
        return pulumi.get(self, "dns_prefix")

    @property
    @pulumi.getter
    def fqdn(self) -> str:
        """
        The FQDN of the Azure Kubernetes Managed Cluster.
        """
        return pulumi.get(self, "fqdn")

    @property
    @pulumi.getter(name="httpApplicationRoutingEnabled")
    def http_application_routing_enabled(self) -> bool:
        """
        Is HTTP Application Routing enabled for this managed Kubernetes Cluster?
        """
        return pulumi.get(self, "http_application_routing_enabled")

    @property
    @pulumi.getter(name="httpApplicationRoutingZoneName")
    def http_application_routing_zone_name(self) -> str:
        """
        The Zone Name of the HTTP Application Routing.
        """
        return pulumi.get(self, "http_application_routing_zone_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identities(self) -> Sequence['outputs.GetKubernetesClusterIdentityResult']:
        """
        A `identity` block as documented below.
        """
        return pulumi.get(self, "identities")

    @property
    @pulumi.getter(name="ingressApplicationGateways")
    def ingress_application_gateways(self) -> Sequence['outputs.GetKubernetesClusterIngressApplicationGatewayResult']:
        """
        An `ingress_application_gateway` block as documented below.
        """
        return pulumi.get(self, "ingress_application_gateways")

    @property
    @pulumi.getter(name="keyVaultSecretsProviders")
    def key_vault_secrets_providers(self) -> Sequence['outputs.GetKubernetesClusterKeyVaultSecretsProviderResult']:
        """
        A `key_vault_secrets_provider` block as documented below.
        """
        return pulumi.get(self, "key_vault_secrets_providers")

    @property
    @pulumi.getter(name="kubeAdminConfigRaw")
    def kube_admin_config_raw(self) -> str:
        """
        Raw Kubernetes config for the admin account to be used by [kubectl](https://kubernetes.io/docs/reference/kubectl/overview/) and other compatible tools. This is only available when Role Based Access Control with Azure Active Directory is enabled and local accounts are not disabled.
        """
        return pulumi.get(self, "kube_admin_config_raw")

    @property
    @pulumi.getter(name="kubeAdminConfigs")
    def kube_admin_configs(self) -> Sequence['outputs.GetKubernetesClusterKubeAdminConfigResult']:
        """
        A `kube_admin_config` block as defined below. This is only available when Role Based Access Control with Azure Active Directory is enabled and local accounts are not disabled.
        """
        return pulumi.get(self, "kube_admin_configs")

    @property
    @pulumi.getter(name="kubeConfigRaw")
    def kube_config_raw(self) -> str:
        """
        Base64 encoded Kubernetes configuration.
        """
        return pulumi.get(self, "kube_config_raw")

    @property
    @pulumi.getter(name="kubeConfigs")
    def kube_configs(self) -> Sequence['outputs.GetKubernetesClusterKubeConfigResult']:
        """
        A `kube_config` block as defined below.
        """
        return pulumi.get(self, "kube_configs")

    @property
    @pulumi.getter(name="kubeletIdentities")
    def kubelet_identities(self) -> Sequence['outputs.GetKubernetesClusterKubeletIdentityResult']:
        """
        A `kubelet_identity` block as documented below.
        """
        return pulumi.get(self, "kubelet_identities")

    @property
    @pulumi.getter(name="kubernetesVersion")
    def kubernetes_version(self) -> str:
        """
        The version of Kubernetes used on the managed Kubernetes Cluster.
        """
        return pulumi.get(self, "kubernetes_version")

    @property
    @pulumi.getter(name="linuxProfiles")
    def linux_profiles(self) -> Sequence['outputs.GetKubernetesClusterLinuxProfileResult']:
        """
        A `linux_profile` block as documented below.
        """
        return pulumi.get(self, "linux_profiles")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The Azure Region in which the managed Kubernetes Cluster exists.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name assigned to this pool of agents.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkProfiles")
    def network_profiles(self) -> Sequence['outputs.GetKubernetesClusterNetworkProfileResult']:
        """
        A `network_profile` block as documented below.
        """
        return pulumi.get(self, "network_profiles")

    @property
    @pulumi.getter(name="nodeResourceGroup")
    def node_resource_group(self) -> str:
        """
        Auto-generated Resource Group containing AKS Cluster resources.
        """
        return pulumi.get(self, "node_resource_group")

    @property
    @pulumi.getter(name="omsAgents")
    def oms_agents(self) -> Sequence['outputs.GetKubernetesClusterOmsAgentResult']:
        """
        An `oms_agent` block as documented below.
        """
        return pulumi.get(self, "oms_agents")

    @property
    @pulumi.getter(name="openServiceMeshEnabled")
    def open_service_mesh_enabled(self) -> bool:
        """
        Is Open Service Mesh enabled for this managed Kubernetes Cluster?
        """
        return pulumi.get(self, "open_service_mesh_enabled")

    @property
    @pulumi.getter(name="privateClusterEnabled")
    def private_cluster_enabled(self) -> bool:
        """
        If the cluster has the Kubernetes API only exposed on internal IP addresses.
        """
        return pulumi.get(self, "private_cluster_enabled")

    @property
    @pulumi.getter(name="privateFqdn")
    def private_fqdn(self) -> str:
        """
        The FQDN of this Kubernetes Cluster when private link has been enabled. This name is only resolvable inside the Virtual Network where the Azure Kubernetes Service is located
        """
        return pulumi.get(self, "private_fqdn")

    @property
    @pulumi.getter(name="privateLinkEnabled")
    def private_link_enabled(self) -> bool:
        return pulumi.get(self, "private_link_enabled")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> str:
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="roleBasedAccessControlEnabled")
    def role_based_access_control_enabled(self) -> bool:
        """
        Is Role Based Access Control enabled for this managed Kubernetes Cluster.
        """
        return pulumi.get(self, "role_based_access_control_enabled")

    @property
    @pulumi.getter(name="roleBasedAccessControls")
    def role_based_access_controls(self) -> Sequence['outputs.GetKubernetesClusterRoleBasedAccessControlResult']:
        return pulumi.get(self, "role_based_access_controls")

    @property
    @pulumi.getter(name="servicePrincipals")
    def service_principals(self) -> Sequence['outputs.GetKubernetesClusterServicePrincipalResult']:
        """
        A `service_principal` block as documented below.
        """
        return pulumi.get(self, "service_principals")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="windowsProfiles")
    def windows_profiles(self) -> Sequence['outputs.GetKubernetesClusterWindowsProfileResult']:
        """
        A `windows_profile` block as documented below.
        """
        return pulumi.get(self, "windows_profiles")


class AwaitableGetKubernetesClusterResult(GetKubernetesClusterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetKubernetesClusterResult(
            aci_connector_linuxes=self.aci_connector_linuxes,
            addon_profiles=self.addon_profiles,
            agent_pool_profiles=self.agent_pool_profiles,
            api_server_authorized_ip_ranges=self.api_server_authorized_ip_ranges,
            azure_active_directory_role_based_access_controls=self.azure_active_directory_role_based_access_controls,
            azure_policy_enabled=self.azure_policy_enabled,
            disk_encryption_set_id=self.disk_encryption_set_id,
            dns_prefix=self.dns_prefix,
            fqdn=self.fqdn,
            http_application_routing_enabled=self.http_application_routing_enabled,
            http_application_routing_zone_name=self.http_application_routing_zone_name,
            id=self.id,
            identities=self.identities,
            ingress_application_gateways=self.ingress_application_gateways,
            key_vault_secrets_providers=self.key_vault_secrets_providers,
            kube_admin_config_raw=self.kube_admin_config_raw,
            kube_admin_configs=self.kube_admin_configs,
            kube_config_raw=self.kube_config_raw,
            kube_configs=self.kube_configs,
            kubelet_identities=self.kubelet_identities,
            kubernetes_version=self.kubernetes_version,
            linux_profiles=self.linux_profiles,
            location=self.location,
            name=self.name,
            network_profiles=self.network_profiles,
            node_resource_group=self.node_resource_group,
            oms_agents=self.oms_agents,
            open_service_mesh_enabled=self.open_service_mesh_enabled,
            private_cluster_enabled=self.private_cluster_enabled,
            private_fqdn=self.private_fqdn,
            private_link_enabled=self.private_link_enabled,
            resource_group_name=self.resource_group_name,
            role_based_access_control_enabled=self.role_based_access_control_enabled,
            role_based_access_controls=self.role_based_access_controls,
            service_principals=self.service_principals,
            tags=self.tags,
            windows_profiles=self.windows_profiles)


def get_kubernetes_cluster(name: Optional[str] = None,
                           resource_group_name: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetKubernetesClusterResult:
    """
    Use this data source to access information about an existing Managed Kubernetes Cluster (AKS).

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.containerservice.get_kubernetes_cluster(name="myakscluster",
        resource_group_name="my-example-resource-group")
    ```


    :param str name: The name of the managed Kubernetes Cluster.
    :param str resource_group_name: The name of the Resource Group in which the managed Kubernetes Cluster exists.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure:containerservice/getKubernetesCluster:getKubernetesCluster', __args__, opts=opts, typ=GetKubernetesClusterResult).value

    return AwaitableGetKubernetesClusterResult(
        aci_connector_linuxes=__ret__.aci_connector_linuxes,
        addon_profiles=__ret__.addon_profiles,
        agent_pool_profiles=__ret__.agent_pool_profiles,
        api_server_authorized_ip_ranges=__ret__.api_server_authorized_ip_ranges,
        azure_active_directory_role_based_access_controls=__ret__.azure_active_directory_role_based_access_controls,
        azure_policy_enabled=__ret__.azure_policy_enabled,
        disk_encryption_set_id=__ret__.disk_encryption_set_id,
        dns_prefix=__ret__.dns_prefix,
        fqdn=__ret__.fqdn,
        http_application_routing_enabled=__ret__.http_application_routing_enabled,
        http_application_routing_zone_name=__ret__.http_application_routing_zone_name,
        id=__ret__.id,
        identities=__ret__.identities,
        ingress_application_gateways=__ret__.ingress_application_gateways,
        key_vault_secrets_providers=__ret__.key_vault_secrets_providers,
        kube_admin_config_raw=__ret__.kube_admin_config_raw,
        kube_admin_configs=__ret__.kube_admin_configs,
        kube_config_raw=__ret__.kube_config_raw,
        kube_configs=__ret__.kube_configs,
        kubelet_identities=__ret__.kubelet_identities,
        kubernetes_version=__ret__.kubernetes_version,
        linux_profiles=__ret__.linux_profiles,
        location=__ret__.location,
        name=__ret__.name,
        network_profiles=__ret__.network_profiles,
        node_resource_group=__ret__.node_resource_group,
        oms_agents=__ret__.oms_agents,
        open_service_mesh_enabled=__ret__.open_service_mesh_enabled,
        private_cluster_enabled=__ret__.private_cluster_enabled,
        private_fqdn=__ret__.private_fqdn,
        private_link_enabled=__ret__.private_link_enabled,
        resource_group_name=__ret__.resource_group_name,
        role_based_access_control_enabled=__ret__.role_based_access_control_enabled,
        role_based_access_controls=__ret__.role_based_access_controls,
        service_principals=__ret__.service_principals,
        tags=__ret__.tags,
        windows_profiles=__ret__.windows_profiles)


@_utilities.lift_output_func(get_kubernetes_cluster)
def get_kubernetes_cluster_output(name: Optional[pulumi.Input[str]] = None,
                                  resource_group_name: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetKubernetesClusterResult]:
    """
    Use this data source to access information about an existing Managed Kubernetes Cluster (AKS).

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azure as azure

    example = azure.containerservice.get_kubernetes_cluster(name="myakscluster",
        resource_group_name="my-example-resource-group")
    ```


    :param str name: The name of the managed Kubernetes Cluster.
    :param str resource_group_name: The name of the Resource Group in which the managed Kubernetes Cluster exists.
    """
    ...
