# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['DatasetKustoClusterArgs', 'DatasetKustoCluster']

@pulumi.input_type
class DatasetKustoClusterArgs:
    def __init__(__self__, *,
                 kusto_cluster_id: pulumi.Input[str],
                 share_id: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DatasetKustoCluster resource.
        :param pulumi.Input[str] kusto_cluster_id: The resource ID of the Kusto Cluster to be shared with the receiver. Changing this forces a new Data Share Kusto Cluster Dataset to be created.
        :param pulumi.Input[str] share_id: The resource ID of the Data Share where this Data Share Kusto Cluster Dataset should be created. Changing this forces a new Data Share Kusto Cluster Dataset to be created.
        :param pulumi.Input[str] name: The name which should be used for this Data Share Kusto Cluster Dataset. Changing this forces a new Data Share Kusto Cluster Dataset to be created.
        """
        pulumi.set(__self__, "kusto_cluster_id", kusto_cluster_id)
        pulumi.set(__self__, "share_id", share_id)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="kustoClusterId")
    def kusto_cluster_id(self) -> pulumi.Input[str]:
        """
        The resource ID of the Kusto Cluster to be shared with the receiver. Changing this forces a new Data Share Kusto Cluster Dataset to be created.
        """
        return pulumi.get(self, "kusto_cluster_id")

    @kusto_cluster_id.setter
    def kusto_cluster_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "kusto_cluster_id", value)

    @property
    @pulumi.getter(name="shareId")
    def share_id(self) -> pulumi.Input[str]:
        """
        The resource ID of the Data Share where this Data Share Kusto Cluster Dataset should be created. Changing this forces a new Data Share Kusto Cluster Dataset to be created.
        """
        return pulumi.get(self, "share_id")

    @share_id.setter
    def share_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "share_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Data Share Kusto Cluster Dataset. Changing this forces a new Data Share Kusto Cluster Dataset to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _DatasetKustoClusterState:
    def __init__(__self__, *,
                 display_name: Optional[pulumi.Input[str]] = None,
                 kusto_cluster_id: Optional[pulumi.Input[str]] = None,
                 kusto_cluster_location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 share_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering DatasetKustoCluster resources.
        :param pulumi.Input[str] display_name: The name of the Data Share Dataset.
        :param pulumi.Input[str] kusto_cluster_id: The resource ID of the Kusto Cluster to be shared with the receiver. Changing this forces a new Data Share Kusto Cluster Dataset to be created.
        :param pulumi.Input[str] kusto_cluster_location: The location of the Kusto Cluster.
        :param pulumi.Input[str] name: The name which should be used for this Data Share Kusto Cluster Dataset. Changing this forces a new Data Share Kusto Cluster Dataset to be created.
        :param pulumi.Input[str] share_id: The resource ID of the Data Share where this Data Share Kusto Cluster Dataset should be created. Changing this forces a new Data Share Kusto Cluster Dataset to be created.
        """
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if kusto_cluster_id is not None:
            pulumi.set(__self__, "kusto_cluster_id", kusto_cluster_id)
        if kusto_cluster_location is not None:
            pulumi.set(__self__, "kusto_cluster_location", kusto_cluster_location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if share_id is not None:
            pulumi.set(__self__, "share_id", share_id)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Data Share Dataset.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="kustoClusterId")
    def kusto_cluster_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource ID of the Kusto Cluster to be shared with the receiver. Changing this forces a new Data Share Kusto Cluster Dataset to be created.
        """
        return pulumi.get(self, "kusto_cluster_id")

    @kusto_cluster_id.setter
    def kusto_cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kusto_cluster_id", value)

    @property
    @pulumi.getter(name="kustoClusterLocation")
    def kusto_cluster_location(self) -> Optional[pulumi.Input[str]]:
        """
        The location of the Kusto Cluster.
        """
        return pulumi.get(self, "kusto_cluster_location")

    @kusto_cluster_location.setter
    def kusto_cluster_location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kusto_cluster_location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Data Share Kusto Cluster Dataset. Changing this forces a new Data Share Kusto Cluster Dataset to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="shareId")
    def share_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource ID of the Data Share where this Data Share Kusto Cluster Dataset should be created. Changing this forces a new Data Share Kusto Cluster Dataset to be created.
        """
        return pulumi.get(self, "share_id")

    @share_id.setter
    def share_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "share_id", value)


class DatasetKustoCluster(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 kusto_cluster_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 share_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Data Share Kusto Cluster Dataset.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_account = azure.datashare.Account("exampleAccount",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            identity=azure.datashare.AccountIdentityArgs(
                type="SystemAssigned",
            ))
        example_share = azure.datashare.Share("exampleShare",
            account_id=example_account.id,
            kind="InPlace")
        example_cluster = azure.kusto.Cluster("exampleCluster",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku=azure.kusto.ClusterSkuArgs(
                name="Dev(No SLA)_Standard_D11_v2",
                capacity=1,
            ))
        example_assignment = azure.authorization.Assignment("exampleAssignment",
            scope=example_cluster.id,
            role_definition_name="Contributor",
            principal_id=example_account.identity.principal_id)
        example_dataset_kusto_cluster = azure.datashare.DatasetKustoCluster("exampleDatasetKustoCluster",
            share_id=example_share.id,
            kusto_cluster_id=example_cluster.id,
            opts=pulumi.ResourceOptions(depends_on=[example_assignment]))
        ```

        ## Import

        Data Share Kusto Cluster Datasets can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:datashare/datasetKustoCluster:DatasetKustoCluster example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.DataShare/accounts/account1/shares/share1/dataSets/dataSet1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] kusto_cluster_id: The resource ID of the Kusto Cluster to be shared with the receiver. Changing this forces a new Data Share Kusto Cluster Dataset to be created.
        :param pulumi.Input[str] name: The name which should be used for this Data Share Kusto Cluster Dataset. Changing this forces a new Data Share Kusto Cluster Dataset to be created.
        :param pulumi.Input[str] share_id: The resource ID of the Data Share where this Data Share Kusto Cluster Dataset should be created. Changing this forces a new Data Share Kusto Cluster Dataset to be created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DatasetKustoClusterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Data Share Kusto Cluster Dataset.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_account = azure.datashare.Account("exampleAccount",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            identity=azure.datashare.AccountIdentityArgs(
                type="SystemAssigned",
            ))
        example_share = azure.datashare.Share("exampleShare",
            account_id=example_account.id,
            kind="InPlace")
        example_cluster = azure.kusto.Cluster("exampleCluster",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            sku=azure.kusto.ClusterSkuArgs(
                name="Dev(No SLA)_Standard_D11_v2",
                capacity=1,
            ))
        example_assignment = azure.authorization.Assignment("exampleAssignment",
            scope=example_cluster.id,
            role_definition_name="Contributor",
            principal_id=example_account.identity.principal_id)
        example_dataset_kusto_cluster = azure.datashare.DatasetKustoCluster("exampleDatasetKustoCluster",
            share_id=example_share.id,
            kusto_cluster_id=example_cluster.id,
            opts=pulumi.ResourceOptions(depends_on=[example_assignment]))
        ```

        ## Import

        Data Share Kusto Cluster Datasets can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:datashare/datasetKustoCluster:DatasetKustoCluster example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/group1/providers/Microsoft.DataShare/accounts/account1/shares/share1/dataSets/dataSet1
        ```

        :param str resource_name: The name of the resource.
        :param DatasetKustoClusterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DatasetKustoClusterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 kusto_cluster_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 share_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = DatasetKustoClusterArgs.__new__(DatasetKustoClusterArgs)

            if kusto_cluster_id is None and not opts.urn:
                raise TypeError("Missing required property 'kusto_cluster_id'")
            __props__.__dict__["kusto_cluster_id"] = kusto_cluster_id
            __props__.__dict__["name"] = name
            if share_id is None and not opts.urn:
                raise TypeError("Missing required property 'share_id'")
            __props__.__dict__["share_id"] = share_id
            __props__.__dict__["display_name"] = None
            __props__.__dict__["kusto_cluster_location"] = None
        super(DatasetKustoCluster, __self__).__init__(
            'azure:datashare/datasetKustoCluster:DatasetKustoCluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            kusto_cluster_id: Optional[pulumi.Input[str]] = None,
            kusto_cluster_location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            share_id: Optional[pulumi.Input[str]] = None) -> 'DatasetKustoCluster':
        """
        Get an existing DatasetKustoCluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] display_name: The name of the Data Share Dataset.
        :param pulumi.Input[str] kusto_cluster_id: The resource ID of the Kusto Cluster to be shared with the receiver. Changing this forces a new Data Share Kusto Cluster Dataset to be created.
        :param pulumi.Input[str] kusto_cluster_location: The location of the Kusto Cluster.
        :param pulumi.Input[str] name: The name which should be used for this Data Share Kusto Cluster Dataset. Changing this forces a new Data Share Kusto Cluster Dataset to be created.
        :param pulumi.Input[str] share_id: The resource ID of the Data Share where this Data Share Kusto Cluster Dataset should be created. Changing this forces a new Data Share Kusto Cluster Dataset to be created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DatasetKustoClusterState.__new__(_DatasetKustoClusterState)

        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["kusto_cluster_id"] = kusto_cluster_id
        __props__.__dict__["kusto_cluster_location"] = kusto_cluster_location
        __props__.__dict__["name"] = name
        __props__.__dict__["share_id"] = share_id
        return DatasetKustoCluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        The name of the Data Share Dataset.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="kustoClusterId")
    def kusto_cluster_id(self) -> pulumi.Output[str]:
        """
        The resource ID of the Kusto Cluster to be shared with the receiver. Changing this forces a new Data Share Kusto Cluster Dataset to be created.
        """
        return pulumi.get(self, "kusto_cluster_id")

    @property
    @pulumi.getter(name="kustoClusterLocation")
    def kusto_cluster_location(self) -> pulumi.Output[str]:
        """
        The location of the Kusto Cluster.
        """
        return pulumi.get(self, "kusto_cluster_location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name which should be used for this Data Share Kusto Cluster Dataset. Changing this forces a new Data Share Kusto Cluster Dataset to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="shareId")
    def share_id(self) -> pulumi.Output[str]:
        """
        The resource ID of the Data Share where this Data Share Kusto Cluster Dataset should be created. Changing this forces a new Data Share Kusto Cluster Dataset to be created.
        """
        return pulumi.get(self, "share_id")

