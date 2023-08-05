# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ScheduleArgs', 'Schedule']

@pulumi.input_type
class ScheduleArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 desired_capacity: Optional[pulumi.Input[int]] = None,
                 launch_expiration_time: Optional[pulumi.Input[int]] = None,
                 launch_time: Optional[pulumi.Input[str]] = None,
                 max_value: Optional[pulumi.Input[int]] = None,
                 min_value: Optional[pulumi.Input[int]] = None,
                 recurrence_end_time: Optional[pulumi.Input[str]] = None,
                 recurrence_type: Optional[pulumi.Input[str]] = None,
                 recurrence_value: Optional[pulumi.Input[str]] = None,
                 scaling_group_id: Optional[pulumi.Input[str]] = None,
                 scheduled_action: Optional[pulumi.Input[str]] = None,
                 scheduled_task_name: Optional[pulumi.Input[str]] = None,
                 task_enabled: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a Schedule resource.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if desired_capacity is not None:
            pulumi.set(__self__, "desired_capacity", desired_capacity)
        if launch_expiration_time is not None:
            pulumi.set(__self__, "launch_expiration_time", launch_expiration_time)
        if launch_time is not None:
            pulumi.set(__self__, "launch_time", launch_time)
        if max_value is not None:
            pulumi.set(__self__, "max_value", max_value)
        if min_value is not None:
            pulumi.set(__self__, "min_value", min_value)
        if recurrence_end_time is not None:
            pulumi.set(__self__, "recurrence_end_time", recurrence_end_time)
        if recurrence_type is not None:
            pulumi.set(__self__, "recurrence_type", recurrence_type)
        if recurrence_value is not None:
            pulumi.set(__self__, "recurrence_value", recurrence_value)
        if scaling_group_id is not None:
            pulumi.set(__self__, "scaling_group_id", scaling_group_id)
        if scheduled_action is not None:
            pulumi.set(__self__, "scheduled_action", scheduled_action)
        if scheduled_task_name is not None:
            pulumi.set(__self__, "scheduled_task_name", scheduled_task_name)
        if task_enabled is not None:
            pulumi.set(__self__, "task_enabled", task_enabled)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="desiredCapacity")
    def desired_capacity(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "desired_capacity")

    @desired_capacity.setter
    def desired_capacity(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "desired_capacity", value)

    @property
    @pulumi.getter(name="launchExpirationTime")
    def launch_expiration_time(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "launch_expiration_time")

    @launch_expiration_time.setter
    def launch_expiration_time(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "launch_expiration_time", value)

    @property
    @pulumi.getter(name="launchTime")
    def launch_time(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "launch_time")

    @launch_time.setter
    def launch_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "launch_time", value)

    @property
    @pulumi.getter(name="maxValue")
    def max_value(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "max_value")

    @max_value.setter
    def max_value(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_value", value)

    @property
    @pulumi.getter(name="minValue")
    def min_value(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "min_value")

    @min_value.setter
    def min_value(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "min_value", value)

    @property
    @pulumi.getter(name="recurrenceEndTime")
    def recurrence_end_time(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "recurrence_end_time")

    @recurrence_end_time.setter
    def recurrence_end_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "recurrence_end_time", value)

    @property
    @pulumi.getter(name="recurrenceType")
    def recurrence_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "recurrence_type")

    @recurrence_type.setter
    def recurrence_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "recurrence_type", value)

    @property
    @pulumi.getter(name="recurrenceValue")
    def recurrence_value(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "recurrence_value")

    @recurrence_value.setter
    def recurrence_value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "recurrence_value", value)

    @property
    @pulumi.getter(name="scalingGroupId")
    def scaling_group_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "scaling_group_id")

    @scaling_group_id.setter
    def scaling_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scaling_group_id", value)

    @property
    @pulumi.getter(name="scheduledAction")
    def scheduled_action(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "scheduled_action")

    @scheduled_action.setter
    def scheduled_action(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scheduled_action", value)

    @property
    @pulumi.getter(name="scheduledTaskName")
    def scheduled_task_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "scheduled_task_name")

    @scheduled_task_name.setter
    def scheduled_task_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scheduled_task_name", value)

    @property
    @pulumi.getter(name="taskEnabled")
    def task_enabled(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "task_enabled")

    @task_enabled.setter
    def task_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "task_enabled", value)


@pulumi.input_type
class _ScheduleState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 desired_capacity: Optional[pulumi.Input[int]] = None,
                 launch_expiration_time: Optional[pulumi.Input[int]] = None,
                 launch_time: Optional[pulumi.Input[str]] = None,
                 max_value: Optional[pulumi.Input[int]] = None,
                 min_value: Optional[pulumi.Input[int]] = None,
                 recurrence_end_time: Optional[pulumi.Input[str]] = None,
                 recurrence_type: Optional[pulumi.Input[str]] = None,
                 recurrence_value: Optional[pulumi.Input[str]] = None,
                 scaling_group_id: Optional[pulumi.Input[str]] = None,
                 scheduled_action: Optional[pulumi.Input[str]] = None,
                 scheduled_task_name: Optional[pulumi.Input[str]] = None,
                 task_enabled: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering Schedule resources.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if desired_capacity is not None:
            pulumi.set(__self__, "desired_capacity", desired_capacity)
        if launch_expiration_time is not None:
            pulumi.set(__self__, "launch_expiration_time", launch_expiration_time)
        if launch_time is not None:
            pulumi.set(__self__, "launch_time", launch_time)
        if max_value is not None:
            pulumi.set(__self__, "max_value", max_value)
        if min_value is not None:
            pulumi.set(__self__, "min_value", min_value)
        if recurrence_end_time is not None:
            pulumi.set(__self__, "recurrence_end_time", recurrence_end_time)
        if recurrence_type is not None:
            pulumi.set(__self__, "recurrence_type", recurrence_type)
        if recurrence_value is not None:
            pulumi.set(__self__, "recurrence_value", recurrence_value)
        if scaling_group_id is not None:
            pulumi.set(__self__, "scaling_group_id", scaling_group_id)
        if scheduled_action is not None:
            pulumi.set(__self__, "scheduled_action", scheduled_action)
        if scheduled_task_name is not None:
            pulumi.set(__self__, "scheduled_task_name", scheduled_task_name)
        if task_enabled is not None:
            pulumi.set(__self__, "task_enabled", task_enabled)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="desiredCapacity")
    def desired_capacity(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "desired_capacity")

    @desired_capacity.setter
    def desired_capacity(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "desired_capacity", value)

    @property
    @pulumi.getter(name="launchExpirationTime")
    def launch_expiration_time(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "launch_expiration_time")

    @launch_expiration_time.setter
    def launch_expiration_time(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "launch_expiration_time", value)

    @property
    @pulumi.getter(name="launchTime")
    def launch_time(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "launch_time")

    @launch_time.setter
    def launch_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "launch_time", value)

    @property
    @pulumi.getter(name="maxValue")
    def max_value(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "max_value")

    @max_value.setter
    def max_value(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_value", value)

    @property
    @pulumi.getter(name="minValue")
    def min_value(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "min_value")

    @min_value.setter
    def min_value(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "min_value", value)

    @property
    @pulumi.getter(name="recurrenceEndTime")
    def recurrence_end_time(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "recurrence_end_time")

    @recurrence_end_time.setter
    def recurrence_end_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "recurrence_end_time", value)

    @property
    @pulumi.getter(name="recurrenceType")
    def recurrence_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "recurrence_type")

    @recurrence_type.setter
    def recurrence_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "recurrence_type", value)

    @property
    @pulumi.getter(name="recurrenceValue")
    def recurrence_value(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "recurrence_value")

    @recurrence_value.setter
    def recurrence_value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "recurrence_value", value)

    @property
    @pulumi.getter(name="scalingGroupId")
    def scaling_group_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "scaling_group_id")

    @scaling_group_id.setter
    def scaling_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scaling_group_id", value)

    @property
    @pulumi.getter(name="scheduledAction")
    def scheduled_action(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "scheduled_action")

    @scheduled_action.setter
    def scheduled_action(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scheduled_action", value)

    @property
    @pulumi.getter(name="scheduledTaskName")
    def scheduled_task_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "scheduled_task_name")

    @scheduled_task_name.setter
    def scheduled_task_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scheduled_task_name", value)

    @property
    @pulumi.getter(name="taskEnabled")
    def task_enabled(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "task_enabled")

    @task_enabled.setter
    def task_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "task_enabled", value)


class Schedule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 desired_capacity: Optional[pulumi.Input[int]] = None,
                 launch_expiration_time: Optional[pulumi.Input[int]] = None,
                 launch_time: Optional[pulumi.Input[str]] = None,
                 max_value: Optional[pulumi.Input[int]] = None,
                 min_value: Optional[pulumi.Input[int]] = None,
                 recurrence_end_time: Optional[pulumi.Input[str]] = None,
                 recurrence_type: Optional[pulumi.Input[str]] = None,
                 recurrence_value: Optional[pulumi.Input[str]] = None,
                 scaling_group_id: Optional[pulumi.Input[str]] = None,
                 scheduled_action: Optional[pulumi.Input[str]] = None,
                 scheduled_task_name: Optional[pulumi.Input[str]] = None,
                 task_enabled: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Create a Schedule resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ScheduleArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Schedule resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ScheduleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ScheduleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 desired_capacity: Optional[pulumi.Input[int]] = None,
                 launch_expiration_time: Optional[pulumi.Input[int]] = None,
                 launch_time: Optional[pulumi.Input[str]] = None,
                 max_value: Optional[pulumi.Input[int]] = None,
                 min_value: Optional[pulumi.Input[int]] = None,
                 recurrence_end_time: Optional[pulumi.Input[str]] = None,
                 recurrence_type: Optional[pulumi.Input[str]] = None,
                 recurrence_value: Optional[pulumi.Input[str]] = None,
                 scaling_group_id: Optional[pulumi.Input[str]] = None,
                 scheduled_action: Optional[pulumi.Input[str]] = None,
                 scheduled_task_name: Optional[pulumi.Input[str]] = None,
                 task_enabled: Optional[pulumi.Input[bool]] = None,
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
            __props__ = ScheduleArgs.__new__(ScheduleArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["desired_capacity"] = desired_capacity
            __props__.__dict__["launch_expiration_time"] = launch_expiration_time
            __props__.__dict__["launch_time"] = launch_time
            __props__.__dict__["max_value"] = max_value
            __props__.__dict__["min_value"] = min_value
            __props__.__dict__["recurrence_end_time"] = recurrence_end_time
            __props__.__dict__["recurrence_type"] = recurrence_type
            __props__.__dict__["recurrence_value"] = recurrence_value
            __props__.__dict__["scaling_group_id"] = scaling_group_id
            __props__.__dict__["scheduled_action"] = scheduled_action
            __props__.__dict__["scheduled_task_name"] = scheduled_task_name
            __props__.__dict__["task_enabled"] = task_enabled
        super(Schedule, __self__).__init__(
            'alicloud:ess/schedule:Schedule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            desired_capacity: Optional[pulumi.Input[int]] = None,
            launch_expiration_time: Optional[pulumi.Input[int]] = None,
            launch_time: Optional[pulumi.Input[str]] = None,
            max_value: Optional[pulumi.Input[int]] = None,
            min_value: Optional[pulumi.Input[int]] = None,
            recurrence_end_time: Optional[pulumi.Input[str]] = None,
            recurrence_type: Optional[pulumi.Input[str]] = None,
            recurrence_value: Optional[pulumi.Input[str]] = None,
            scaling_group_id: Optional[pulumi.Input[str]] = None,
            scheduled_action: Optional[pulumi.Input[str]] = None,
            scheduled_task_name: Optional[pulumi.Input[str]] = None,
            task_enabled: Optional[pulumi.Input[bool]] = None) -> 'Schedule':
        """
        Get an existing Schedule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ScheduleState.__new__(_ScheduleState)

        __props__.__dict__["description"] = description
        __props__.__dict__["desired_capacity"] = desired_capacity
        __props__.__dict__["launch_expiration_time"] = launch_expiration_time
        __props__.__dict__["launch_time"] = launch_time
        __props__.__dict__["max_value"] = max_value
        __props__.__dict__["min_value"] = min_value
        __props__.__dict__["recurrence_end_time"] = recurrence_end_time
        __props__.__dict__["recurrence_type"] = recurrence_type
        __props__.__dict__["recurrence_value"] = recurrence_value
        __props__.__dict__["scaling_group_id"] = scaling_group_id
        __props__.__dict__["scheduled_action"] = scheduled_action
        __props__.__dict__["scheduled_task_name"] = scheduled_task_name
        __props__.__dict__["task_enabled"] = task_enabled
        return Schedule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="desiredCapacity")
    def desired_capacity(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "desired_capacity")

    @property
    @pulumi.getter(name="launchExpirationTime")
    def launch_expiration_time(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "launch_expiration_time")

    @property
    @pulumi.getter(name="launchTime")
    def launch_time(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "launch_time")

    @property
    @pulumi.getter(name="maxValue")
    def max_value(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "max_value")

    @property
    @pulumi.getter(name="minValue")
    def min_value(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "min_value")

    @property
    @pulumi.getter(name="recurrenceEndTime")
    def recurrence_end_time(self) -> pulumi.Output[str]:
        return pulumi.get(self, "recurrence_end_time")

    @property
    @pulumi.getter(name="recurrenceType")
    def recurrence_type(self) -> pulumi.Output[str]:
        return pulumi.get(self, "recurrence_type")

    @property
    @pulumi.getter(name="recurrenceValue")
    def recurrence_value(self) -> pulumi.Output[str]:
        return pulumi.get(self, "recurrence_value")

    @property
    @pulumi.getter(name="scalingGroupId")
    def scaling_group_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "scaling_group_id")

    @property
    @pulumi.getter(name="scheduledAction")
    def scheduled_action(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "scheduled_action")

    @property
    @pulumi.getter(name="scheduledTaskName")
    def scheduled_task_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "scheduled_task_name")

    @property
    @pulumi.getter(name="taskEnabled")
    def task_enabled(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "task_enabled")

