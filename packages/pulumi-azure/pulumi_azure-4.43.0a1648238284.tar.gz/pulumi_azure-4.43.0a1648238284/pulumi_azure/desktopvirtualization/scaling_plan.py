# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['ScalingPlanArgs', 'ScalingPlan']

@pulumi.input_type
class ScalingPlanArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 schedules: pulumi.Input[Sequence[pulumi.Input['ScalingPlanScheduleArgs']]],
                 time_zone: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 exclusion_tag: Optional[pulumi.Input[str]] = None,
                 friendly_name: Optional[pulumi.Input[str]] = None,
                 host_pools: Optional[pulumi.Input[Sequence[pulumi.Input['ScalingPlanHostPoolArgs']]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a ScalingPlan resource.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Virtual Desktop Scaling Plan should exist. Changing this forces a new Virtual Desktop Scaling Plan  to be created.
        :param pulumi.Input[Sequence[pulumi.Input['ScalingPlanScheduleArgs']]] schedules: One or more `schedule` blocks as defined below.
        :param pulumi.Input[str] time_zone: Specifies the Time Zone which should be used by the Scaling Plan for time based events, [the possible values are defined here](https://jackstromberg.com/2017/01/list-of-time-zones-consumed-by-azure/).
        :param pulumi.Input[str] description: A description of the Scaling Plan.
        :param pulumi.Input[str] exclusion_tag: The name of the tag associated with the VMs you want to exclude from autoscaling.
        :param pulumi.Input[str] friendly_name: Friendly name of the Scaling Plan.
        :param pulumi.Input[Sequence[pulumi.Input['ScalingPlanHostPoolArgs']]] host_pools: One or more `host_pool` blocks as defined below.
        :param pulumi.Input[str] location: The Azure Region where the Virtual Desktop Scaling Plan  should exist. Changing this forces a new Virtual Desktop Scaling Plan to be created.
        :param pulumi.Input[str] name: The name which should be used for this Virtual Desktop Scaling Plan . Changing this forces a new Virtual Desktop Scaling Plan to be created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags which should be assigned to the Virtual Desktop Scaling Plan .
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "schedules", schedules)
        pulumi.set(__self__, "time_zone", time_zone)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if exclusion_tag is not None:
            pulumi.set(__self__, "exclusion_tag", exclusion_tag)
        if friendly_name is not None:
            pulumi.set(__self__, "friendly_name", friendly_name)
        if host_pools is not None:
            pulumi.set(__self__, "host_pools", host_pools)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the Resource Group where the Virtual Desktop Scaling Plan should exist. Changing this forces a new Virtual Desktop Scaling Plan  to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def schedules(self) -> pulumi.Input[Sequence[pulumi.Input['ScalingPlanScheduleArgs']]]:
        """
        One or more `schedule` blocks as defined below.
        """
        return pulumi.get(self, "schedules")

    @schedules.setter
    def schedules(self, value: pulumi.Input[Sequence[pulumi.Input['ScalingPlanScheduleArgs']]]):
        pulumi.set(self, "schedules", value)

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> pulumi.Input[str]:
        """
        Specifies the Time Zone which should be used by the Scaling Plan for time based events, [the possible values are defined here](https://jackstromberg.com/2017/01/list-of-time-zones-consumed-by-azure/).
        """
        return pulumi.get(self, "time_zone")

    @time_zone.setter
    def time_zone(self, value: pulumi.Input[str]):
        pulumi.set(self, "time_zone", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description of the Scaling Plan.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="exclusionTag")
    def exclusion_tag(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the tag associated with the VMs you want to exclude from autoscaling.
        """
        return pulumi.get(self, "exclusion_tag")

    @exclusion_tag.setter
    def exclusion_tag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "exclusion_tag", value)

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[str]]:
        """
        Friendly name of the Scaling Plan.
        """
        return pulumi.get(self, "friendly_name")

    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "friendly_name", value)

    @property
    @pulumi.getter(name="hostPools")
    def host_pools(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ScalingPlanHostPoolArgs']]]]:
        """
        One or more `host_pool` blocks as defined below.
        """
        return pulumi.get(self, "host_pools")

    @host_pools.setter
    def host_pools(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ScalingPlanHostPoolArgs']]]]):
        pulumi.set(self, "host_pools", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The Azure Region where the Virtual Desktop Scaling Plan  should exist. Changing this forces a new Virtual Desktop Scaling Plan to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Virtual Desktop Scaling Plan . Changing this forces a new Virtual Desktop Scaling Plan to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of tags which should be assigned to the Virtual Desktop Scaling Plan .
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _ScalingPlanState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 exclusion_tag: Optional[pulumi.Input[str]] = None,
                 friendly_name: Optional[pulumi.Input[str]] = None,
                 host_pools: Optional[pulumi.Input[Sequence[pulumi.Input['ScalingPlanHostPoolArgs']]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 schedules: Optional[pulumi.Input[Sequence[pulumi.Input['ScalingPlanScheduleArgs']]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 time_zone: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ScalingPlan resources.
        :param pulumi.Input[str] description: A description of the Scaling Plan.
        :param pulumi.Input[str] exclusion_tag: The name of the tag associated with the VMs you want to exclude from autoscaling.
        :param pulumi.Input[str] friendly_name: Friendly name of the Scaling Plan.
        :param pulumi.Input[Sequence[pulumi.Input['ScalingPlanHostPoolArgs']]] host_pools: One or more `host_pool` blocks as defined below.
        :param pulumi.Input[str] location: The Azure Region where the Virtual Desktop Scaling Plan  should exist. Changing this forces a new Virtual Desktop Scaling Plan to be created.
        :param pulumi.Input[str] name: The name which should be used for this Virtual Desktop Scaling Plan . Changing this forces a new Virtual Desktop Scaling Plan to be created.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Virtual Desktop Scaling Plan should exist. Changing this forces a new Virtual Desktop Scaling Plan  to be created.
        :param pulumi.Input[Sequence[pulumi.Input['ScalingPlanScheduleArgs']]] schedules: One or more `schedule` blocks as defined below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags which should be assigned to the Virtual Desktop Scaling Plan .
        :param pulumi.Input[str] time_zone: Specifies the Time Zone which should be used by the Scaling Plan for time based events, [the possible values are defined here](https://jackstromberg.com/2017/01/list-of-time-zones-consumed-by-azure/).
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if exclusion_tag is not None:
            pulumi.set(__self__, "exclusion_tag", exclusion_tag)
        if friendly_name is not None:
            pulumi.set(__self__, "friendly_name", friendly_name)
        if host_pools is not None:
            pulumi.set(__self__, "host_pools", host_pools)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if resource_group_name is not None:
            pulumi.set(__self__, "resource_group_name", resource_group_name)
        if schedules is not None:
            pulumi.set(__self__, "schedules", schedules)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if time_zone is not None:
            pulumi.set(__self__, "time_zone", time_zone)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description of the Scaling Plan.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="exclusionTag")
    def exclusion_tag(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the tag associated with the VMs you want to exclude from autoscaling.
        """
        return pulumi.get(self, "exclusion_tag")

    @exclusion_tag.setter
    def exclusion_tag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "exclusion_tag", value)

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[str]]:
        """
        Friendly name of the Scaling Plan.
        """
        return pulumi.get(self, "friendly_name")

    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "friendly_name", value)

    @property
    @pulumi.getter(name="hostPools")
    def host_pools(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ScalingPlanHostPoolArgs']]]]:
        """
        One or more `host_pool` blocks as defined below.
        """
        return pulumi.get(self, "host_pools")

    @host_pools.setter
    def host_pools(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ScalingPlanHostPoolArgs']]]]):
        pulumi.set(self, "host_pools", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The Azure Region where the Virtual Desktop Scaling Plan  should exist. Changing this forces a new Virtual Desktop Scaling Plan to be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name which should be used for this Virtual Desktop Scaling Plan . Changing this forces a new Virtual Desktop Scaling Plan to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Resource Group where the Virtual Desktop Scaling Plan should exist. Changing this forces a new Virtual Desktop Scaling Plan  to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def schedules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ScalingPlanScheduleArgs']]]]:
        """
        One or more `schedule` blocks as defined below.
        """
        return pulumi.get(self, "schedules")

    @schedules.setter
    def schedules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ScalingPlanScheduleArgs']]]]):
        pulumi.set(self, "schedules", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping of tags which should be assigned to the Virtual Desktop Scaling Plan .
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the Time Zone which should be used by the Scaling Plan for time based events, [the possible values are defined here](https://jackstromberg.com/2017/01/list-of-time-zones-consumed-by-azure/).
        """
        return pulumi.get(self, "time_zone")

    @time_zone.setter
    def time_zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_zone", value)


class ScalingPlan(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 exclusion_tag: Optional[pulumi.Input[str]] = None,
                 friendly_name: Optional[pulumi.Input[str]] = None,
                 host_pools: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScalingPlanHostPoolArgs']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 schedules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScalingPlanScheduleArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 time_zone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a Virtual Desktop Scaling Plan.

        ## Disclaimers

        > **Note** Scaling Plans are currently in preview and are only supported in a limited number of regions. Both the Scaling Plan and any referenced Host Pools must be deployed in a supported region. [Autoscale (preview) for Azure Virtual Desktop host pools](https://docs.microsoft.com/en-us/azure/virtual-desktop/autoscale-scaling-plan).

        > **Note** Scaling Plans require specific permissions to be granted to the Windows Virtual Desktop application before a 'host_pool' can be configured. [Required Permissions for Scaling Plans](https://docs.microsoft.com/en-us/azure/virtual-desktop/autoscale-scaling-plan#create-a-custom-rbac-role).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure
        import pulumi_azuread as azuread

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_role_definition = azure.authorization.RoleDefinition("exampleRoleDefinition",
            scope=example_resource_group.id,
            description="AVD AutoScale Role",
            permissions=[azure.authorization.RoleDefinitionPermissionArgs(
                actions=[
                    "Microsoft.Insights/eventtypes/values/read",
                    "Microsoft.Compute/virtualMachines/deallocate/action",
                    "Microsoft.Compute/virtualMachines/restart/action",
                    "Microsoft.Compute/virtualMachines/powerOff/action",
                    "Microsoft.Compute/virtualMachines/start/action",
                    "Microsoft.Compute/virtualMachines/read",
                    "Microsoft.DesktopVirtualization/hostpools/read",
                    "Microsoft.DesktopVirtualization/hostpools/write",
                    "Microsoft.DesktopVirtualization/hostpools/sessionhosts/read",
                    "Microsoft.DesktopVirtualization/hostpools/sessionhosts/write",
                    "Microsoft.DesktopVirtualization/hostpools/sessionhosts/usersessions/delete",
                    "Microsoft.DesktopVirtualization/hostpools/sessionhosts/usersessions/read",
                    "Microsoft.DesktopVirtualization/hostpools/sessionhosts/usersessions/sendMessage/action",
                    "Microsoft.DesktopVirtualization/hostpools/sessionhosts/usersessions/read",
                ],
                not_actions=[],
            )],
            assignable_scopes=[example_resource_group.id])
        example_service_principal = azuread.get_service_principal(display_name="Windows Virtual Desktop")
        example_assignment = azure.authorization.Assignment("exampleAssignment",
            name=random_uuid["example"]["result"],
            scope=example_resource_group.id,
            role_definition_id=example_role_definition.role_definition_resource_id,
            principal_id=example_service_principal.application_id,
            skip_service_principal_aad_check=True)
        example_host_pool = azure.desktopvirtualization.HostPool("exampleHostPool",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            type="Pooled",
            validate_environment=True,
            load_balancer_type="BreadthFirst")
        example_scaling_plan = azure.desktopvirtualization.ScalingPlan("exampleScalingPlan",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            friendly_name="Scaling Plan Example",
            description="Example Scaling Plan",
            time_zone="GMT Standard Time",
            schedules=[azure.desktopvirtualization.ScalingPlanScheduleArgs(
                name="Weekdays",
                days_of_weeks=[
                    "Monday",
                    "Tuesday",
                    "Wednesday",
                    "Thursday",
                    "Friday",
                ],
                ramp_up_start_time="05:00",
                ramp_up_load_balancing_algorithm="BreadthFirst",
                ramp_up_minimum_hosts_percent=20,
                ramp_up_capacity_threshold_percent=10,
                peak_start_time="09:00",
                peak_load_balancing_algorithm="BreadthFirst",
                ramp_down_start_time="19:00",
                ramp_down_load_balancing_algorithm="DepthFirst",
                ramp_down_minimum_hosts_percent=10,
                ramp_down_force_logoff_users=False,
                ramp_down_wait_time_minutes=45,
                ramp_down_notification_message="Please log off in the next 45 minutes...",
                ramp_down_capacity_threshold_percent=5,
                ramp_down_stop_hosts_when="ZeroSessions",
                off_peak_start_time="22:00",
                off_peak_load_balancing_algorithm="DepthFirst",
            )],
            host_pools=[azure.desktopvirtualization.ScalingPlanHostPoolArgs(
                hostpool_id=example_host_pool.id,
                scaling_plan_enabled=True,
            )])
        ```

        ## Import

        Virtual Desktop Scaling Plans can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:desktopvirtualization/scalingPlan:ScalingPlan example /subscriptions/12345678-1234-9876-4563-123456789012/resourceGroups/resGroup1/providers/Microsoft.DesktopVirtualization/scalingPlans/plan1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A description of the Scaling Plan.
        :param pulumi.Input[str] exclusion_tag: The name of the tag associated with the VMs you want to exclude from autoscaling.
        :param pulumi.Input[str] friendly_name: Friendly name of the Scaling Plan.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScalingPlanHostPoolArgs']]]] host_pools: One or more `host_pool` blocks as defined below.
        :param pulumi.Input[str] location: The Azure Region where the Virtual Desktop Scaling Plan  should exist. Changing this forces a new Virtual Desktop Scaling Plan to be created.
        :param pulumi.Input[str] name: The name which should be used for this Virtual Desktop Scaling Plan . Changing this forces a new Virtual Desktop Scaling Plan to be created.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Virtual Desktop Scaling Plan should exist. Changing this forces a new Virtual Desktop Scaling Plan  to be created.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScalingPlanScheduleArgs']]]] schedules: One or more `schedule` blocks as defined below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags which should be assigned to the Virtual Desktop Scaling Plan .
        :param pulumi.Input[str] time_zone: Specifies the Time Zone which should be used by the Scaling Plan for time based events, [the possible values are defined here](https://jackstromberg.com/2017/01/list-of-time-zones-consumed-by-azure/).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ScalingPlanArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Virtual Desktop Scaling Plan.

        ## Disclaimers

        > **Note** Scaling Plans are currently in preview and are only supported in a limited number of regions. Both the Scaling Plan and any referenced Host Pools must be deployed in a supported region. [Autoscale (preview) for Azure Virtual Desktop host pools](https://docs.microsoft.com/en-us/azure/virtual-desktop/autoscale-scaling-plan).

        > **Note** Scaling Plans require specific permissions to be granted to the Windows Virtual Desktop application before a 'host_pool' can be configured. [Required Permissions for Scaling Plans](https://docs.microsoft.com/en-us/azure/virtual-desktop/autoscale-scaling-plan#create-a-custom-rbac-role).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure
        import pulumi_azuread as azuread

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_role_definition = azure.authorization.RoleDefinition("exampleRoleDefinition",
            scope=example_resource_group.id,
            description="AVD AutoScale Role",
            permissions=[azure.authorization.RoleDefinitionPermissionArgs(
                actions=[
                    "Microsoft.Insights/eventtypes/values/read",
                    "Microsoft.Compute/virtualMachines/deallocate/action",
                    "Microsoft.Compute/virtualMachines/restart/action",
                    "Microsoft.Compute/virtualMachines/powerOff/action",
                    "Microsoft.Compute/virtualMachines/start/action",
                    "Microsoft.Compute/virtualMachines/read",
                    "Microsoft.DesktopVirtualization/hostpools/read",
                    "Microsoft.DesktopVirtualization/hostpools/write",
                    "Microsoft.DesktopVirtualization/hostpools/sessionhosts/read",
                    "Microsoft.DesktopVirtualization/hostpools/sessionhosts/write",
                    "Microsoft.DesktopVirtualization/hostpools/sessionhosts/usersessions/delete",
                    "Microsoft.DesktopVirtualization/hostpools/sessionhosts/usersessions/read",
                    "Microsoft.DesktopVirtualization/hostpools/sessionhosts/usersessions/sendMessage/action",
                    "Microsoft.DesktopVirtualization/hostpools/sessionhosts/usersessions/read",
                ],
                not_actions=[],
            )],
            assignable_scopes=[example_resource_group.id])
        example_service_principal = azuread.get_service_principal(display_name="Windows Virtual Desktop")
        example_assignment = azure.authorization.Assignment("exampleAssignment",
            name=random_uuid["example"]["result"],
            scope=example_resource_group.id,
            role_definition_id=example_role_definition.role_definition_resource_id,
            principal_id=example_service_principal.application_id,
            skip_service_principal_aad_check=True)
        example_host_pool = azure.desktopvirtualization.HostPool("exampleHostPool",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            type="Pooled",
            validate_environment=True,
            load_balancer_type="BreadthFirst")
        example_scaling_plan = azure.desktopvirtualization.ScalingPlan("exampleScalingPlan",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            friendly_name="Scaling Plan Example",
            description="Example Scaling Plan",
            time_zone="GMT Standard Time",
            schedules=[azure.desktopvirtualization.ScalingPlanScheduleArgs(
                name="Weekdays",
                days_of_weeks=[
                    "Monday",
                    "Tuesday",
                    "Wednesday",
                    "Thursday",
                    "Friday",
                ],
                ramp_up_start_time="05:00",
                ramp_up_load_balancing_algorithm="BreadthFirst",
                ramp_up_minimum_hosts_percent=20,
                ramp_up_capacity_threshold_percent=10,
                peak_start_time="09:00",
                peak_load_balancing_algorithm="BreadthFirst",
                ramp_down_start_time="19:00",
                ramp_down_load_balancing_algorithm="DepthFirst",
                ramp_down_minimum_hosts_percent=10,
                ramp_down_force_logoff_users=False,
                ramp_down_wait_time_minutes=45,
                ramp_down_notification_message="Please log off in the next 45 minutes...",
                ramp_down_capacity_threshold_percent=5,
                ramp_down_stop_hosts_when="ZeroSessions",
                off_peak_start_time="22:00",
                off_peak_load_balancing_algorithm="DepthFirst",
            )],
            host_pools=[azure.desktopvirtualization.ScalingPlanHostPoolArgs(
                hostpool_id=example_host_pool.id,
                scaling_plan_enabled=True,
            )])
        ```

        ## Import

        Virtual Desktop Scaling Plans can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:desktopvirtualization/scalingPlan:ScalingPlan example /subscriptions/12345678-1234-9876-4563-123456789012/resourceGroups/resGroup1/providers/Microsoft.DesktopVirtualization/scalingPlans/plan1
        ```

        :param str resource_name: The name of the resource.
        :param ScalingPlanArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ScalingPlanArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 exclusion_tag: Optional[pulumi.Input[str]] = None,
                 friendly_name: Optional[pulumi.Input[str]] = None,
                 host_pools: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScalingPlanHostPoolArgs']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 schedules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScalingPlanScheduleArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 time_zone: Optional[pulumi.Input[str]] = None,
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
            __props__ = ScalingPlanArgs.__new__(ScalingPlanArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["exclusion_tag"] = exclusion_tag
            __props__.__dict__["friendly_name"] = friendly_name
            __props__.__dict__["host_pools"] = host_pools
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if schedules is None and not opts.urn:
                raise TypeError("Missing required property 'schedules'")
            __props__.__dict__["schedules"] = schedules
            __props__.__dict__["tags"] = tags
            if time_zone is None and not opts.urn:
                raise TypeError("Missing required property 'time_zone'")
            __props__.__dict__["time_zone"] = time_zone
        super(ScalingPlan, __self__).__init__(
            'azure:desktopvirtualization/scalingPlan:ScalingPlan',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            exclusion_tag: Optional[pulumi.Input[str]] = None,
            friendly_name: Optional[pulumi.Input[str]] = None,
            host_pools: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScalingPlanHostPoolArgs']]]]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            schedules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScalingPlanScheduleArgs']]]]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            time_zone: Optional[pulumi.Input[str]] = None) -> 'ScalingPlan':
        """
        Get an existing ScalingPlan resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A description of the Scaling Plan.
        :param pulumi.Input[str] exclusion_tag: The name of the tag associated with the VMs you want to exclude from autoscaling.
        :param pulumi.Input[str] friendly_name: Friendly name of the Scaling Plan.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScalingPlanHostPoolArgs']]]] host_pools: One or more `host_pool` blocks as defined below.
        :param pulumi.Input[str] location: The Azure Region where the Virtual Desktop Scaling Plan  should exist. Changing this forces a new Virtual Desktop Scaling Plan to be created.
        :param pulumi.Input[str] name: The name which should be used for this Virtual Desktop Scaling Plan . Changing this forces a new Virtual Desktop Scaling Plan to be created.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group where the Virtual Desktop Scaling Plan should exist. Changing this forces a new Virtual Desktop Scaling Plan  to be created.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScalingPlanScheduleArgs']]]] schedules: One or more `schedule` blocks as defined below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A mapping of tags which should be assigned to the Virtual Desktop Scaling Plan .
        :param pulumi.Input[str] time_zone: Specifies the Time Zone which should be used by the Scaling Plan for time based events, [the possible values are defined here](https://jackstromberg.com/2017/01/list-of-time-zones-consumed-by-azure/).
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ScalingPlanState.__new__(_ScalingPlanState)

        __props__.__dict__["description"] = description
        __props__.__dict__["exclusion_tag"] = exclusion_tag
        __props__.__dict__["friendly_name"] = friendly_name
        __props__.__dict__["host_pools"] = host_pools
        __props__.__dict__["location"] = location
        __props__.__dict__["name"] = name
        __props__.__dict__["resource_group_name"] = resource_group_name
        __props__.__dict__["schedules"] = schedules
        __props__.__dict__["tags"] = tags
        __props__.__dict__["time_zone"] = time_zone
        return ScalingPlan(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description of the Scaling Plan.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="exclusionTag")
    def exclusion_tag(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the tag associated with the VMs you want to exclude from autoscaling.
        """
        return pulumi.get(self, "exclusion_tag")

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> pulumi.Output[Optional[str]]:
        """
        Friendly name of the Scaling Plan.
        """
        return pulumi.get(self, "friendly_name")

    @property
    @pulumi.getter(name="hostPools")
    def host_pools(self) -> pulumi.Output[Optional[Sequence['outputs.ScalingPlanHostPool']]]:
        """
        One or more `host_pool` blocks as defined below.
        """
        return pulumi.get(self, "host_pools")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The Azure Region where the Virtual Desktop Scaling Plan  should exist. Changing this forces a new Virtual Desktop Scaling Plan to be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name which should be used for this Virtual Desktop Scaling Plan . Changing this forces a new Virtual Desktop Scaling Plan to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the Resource Group where the Virtual Desktop Scaling Plan should exist. Changing this forces a new Virtual Desktop Scaling Plan  to be created.
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter
    def schedules(self) -> pulumi.Output[Sequence['outputs.ScalingPlanSchedule']]:
        """
        One or more `schedule` blocks as defined below.
        """
        return pulumi.get(self, "schedules")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping of tags which should be assigned to the Virtual Desktop Scaling Plan .
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> pulumi.Output[str]:
        """
        Specifies the Time Zone which should be used by the Scaling Plan for time based events, [the possible values are defined here](https://jackstromberg.com/2017/01/list-of-time-zones-consumed-by-azure/).
        """
        return pulumi.get(self, "time_zone")

