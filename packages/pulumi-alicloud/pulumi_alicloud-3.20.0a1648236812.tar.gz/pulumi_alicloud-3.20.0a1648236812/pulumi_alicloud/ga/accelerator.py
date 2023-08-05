# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['AcceleratorArgs', 'Accelerator']

@pulumi.input_type
class AcceleratorArgs:
    def __init__(__self__, *,
                 duration: pulumi.Input[int],
                 spec: pulumi.Input[str],
                 accelerator_name: Optional[pulumi.Input[str]] = None,
                 auto_renew_duration: Optional[pulumi.Input[int]] = None,
                 auto_use_coupon: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 pricing_cycle: Optional[pulumi.Input[str]] = None,
                 renewal_status: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Accelerator resource.
        :param pulumi.Input[int] duration: The subscription duration. **NOTE:** Starting from v1.150.0+, the `duration` and  `pricing_cycle` are both required.
               * If the `pricing_cycle` parameter is set to `Month`, the valid values for the `duration` parameter are 1 to 9.
               * If the `pricing_cycle` parameter is set to `Year`, the valid values for the `duration` parameter are 1 to 3.
        :param pulumi.Input[str] spec: The instance type of the GA instance. Specification of global acceleration instance, value:
               `1`: Small 1.
               `2`: Small 2.
               `3`: Small 3.
               `5`: Medium 1.
               `8`: Medium 2.
               `10`: Medium 3.
        :param pulumi.Input[str] accelerator_name: The Name of the GA instance.
        :param pulumi.Input[int] auto_renew_duration: Auto renewal period of an instance, in the unit of month. The value range is 1-12.
        :param pulumi.Input[bool] auto_use_coupon: Use coupons to pay bills automatically. Default value is `false`. Valid value: `true`: Use, `false`: Not used.
        :param pulumi.Input[str] description: Descriptive information of the global acceleration instance.
        :param pulumi.Input[str] pricing_cycle: The billing cycle of the GA instance. Valid values: `Month`,`Year`. The default value: `Month`.
               * `Month`: billed on a monthly basis.
               * `Year`: billed on an annual basis.
        :param pulumi.Input[str] renewal_status: Whether to renew an accelerator automatically or not. Default to "Normal". Valid values:
               - `AutoRenewal`: Enable auto renewal.
               - `Normal`: Disable auto renewal.
               - `NotRenewal`: No renewal any longer. After you specify this value, Alibaba Cloud stop sending notification of instance expiry, and only gives a brief reminder on the third day before the instance expiry.
        """
        pulumi.set(__self__, "duration", duration)
        pulumi.set(__self__, "spec", spec)
        if accelerator_name is not None:
            pulumi.set(__self__, "accelerator_name", accelerator_name)
        if auto_renew_duration is not None:
            pulumi.set(__self__, "auto_renew_duration", auto_renew_duration)
        if auto_use_coupon is not None:
            pulumi.set(__self__, "auto_use_coupon", auto_use_coupon)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if pricing_cycle is not None:
            pulumi.set(__self__, "pricing_cycle", pricing_cycle)
        if renewal_status is not None:
            pulumi.set(__self__, "renewal_status", renewal_status)

    @property
    @pulumi.getter
    def duration(self) -> pulumi.Input[int]:
        """
        The subscription duration. **NOTE:** Starting from v1.150.0+, the `duration` and  `pricing_cycle` are both required.
        * If the `pricing_cycle` parameter is set to `Month`, the valid values for the `duration` parameter are 1 to 9.
        * If the `pricing_cycle` parameter is set to `Year`, the valid values for the `duration` parameter are 1 to 3.
        """
        return pulumi.get(self, "duration")

    @duration.setter
    def duration(self, value: pulumi.Input[int]):
        pulumi.set(self, "duration", value)

    @property
    @pulumi.getter
    def spec(self) -> pulumi.Input[str]:
        """
        The instance type of the GA instance. Specification of global acceleration instance, value:
        `1`: Small 1.
        `2`: Small 2.
        `3`: Small 3.
        `5`: Medium 1.
        `8`: Medium 2.
        `10`: Medium 3.
        """
        return pulumi.get(self, "spec")

    @spec.setter
    def spec(self, value: pulumi.Input[str]):
        pulumi.set(self, "spec", value)

    @property
    @pulumi.getter(name="acceleratorName")
    def accelerator_name(self) -> Optional[pulumi.Input[str]]:
        """
        The Name of the GA instance.
        """
        return pulumi.get(self, "accelerator_name")

    @accelerator_name.setter
    def accelerator_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "accelerator_name", value)

    @property
    @pulumi.getter(name="autoRenewDuration")
    def auto_renew_duration(self) -> Optional[pulumi.Input[int]]:
        """
        Auto renewal period of an instance, in the unit of month. The value range is 1-12.
        """
        return pulumi.get(self, "auto_renew_duration")

    @auto_renew_duration.setter
    def auto_renew_duration(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "auto_renew_duration", value)

    @property
    @pulumi.getter(name="autoUseCoupon")
    def auto_use_coupon(self) -> Optional[pulumi.Input[bool]]:
        """
        Use coupons to pay bills automatically. Default value is `false`. Valid value: `true`: Use, `false`: Not used.
        """
        return pulumi.get(self, "auto_use_coupon")

    @auto_use_coupon.setter
    def auto_use_coupon(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "auto_use_coupon", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Descriptive information of the global acceleration instance.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="pricingCycle")
    def pricing_cycle(self) -> Optional[pulumi.Input[str]]:
        """
        The billing cycle of the GA instance. Valid values: `Month`,`Year`. The default value: `Month`.
        * `Month`: billed on a monthly basis.
        * `Year`: billed on an annual basis.
        """
        return pulumi.get(self, "pricing_cycle")

    @pricing_cycle.setter
    def pricing_cycle(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pricing_cycle", value)

    @property
    @pulumi.getter(name="renewalStatus")
    def renewal_status(self) -> Optional[pulumi.Input[str]]:
        """
        Whether to renew an accelerator automatically or not. Default to "Normal". Valid values:
        - `AutoRenewal`: Enable auto renewal.
        - `Normal`: Disable auto renewal.
        - `NotRenewal`: No renewal any longer. After you specify this value, Alibaba Cloud stop sending notification of instance expiry, and only gives a brief reminder on the third day before the instance expiry.
        """
        return pulumi.get(self, "renewal_status")

    @renewal_status.setter
    def renewal_status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "renewal_status", value)


@pulumi.input_type
class _AcceleratorState:
    def __init__(__self__, *,
                 accelerator_name: Optional[pulumi.Input[str]] = None,
                 auto_renew_duration: Optional[pulumi.Input[int]] = None,
                 auto_use_coupon: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 duration: Optional[pulumi.Input[int]] = None,
                 pricing_cycle: Optional[pulumi.Input[str]] = None,
                 renewal_status: Optional[pulumi.Input[str]] = None,
                 spec: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Accelerator resources.
        :param pulumi.Input[str] accelerator_name: The Name of the GA instance.
        :param pulumi.Input[int] auto_renew_duration: Auto renewal period of an instance, in the unit of month. The value range is 1-12.
        :param pulumi.Input[bool] auto_use_coupon: Use coupons to pay bills automatically. Default value is `false`. Valid value: `true`: Use, `false`: Not used.
        :param pulumi.Input[str] description: Descriptive information of the global acceleration instance.
        :param pulumi.Input[int] duration: The subscription duration. **NOTE:** Starting from v1.150.0+, the `duration` and  `pricing_cycle` are both required.
               * If the `pricing_cycle` parameter is set to `Month`, the valid values for the `duration` parameter are 1 to 9.
               * If the `pricing_cycle` parameter is set to `Year`, the valid values for the `duration` parameter are 1 to 3.
        :param pulumi.Input[str] pricing_cycle: The billing cycle of the GA instance. Valid values: `Month`,`Year`. The default value: `Month`.
               * `Month`: billed on a monthly basis.
               * `Year`: billed on an annual basis.
        :param pulumi.Input[str] renewal_status: Whether to renew an accelerator automatically or not. Default to "Normal". Valid values:
               - `AutoRenewal`: Enable auto renewal.
               - `Normal`: Disable auto renewal.
               - `NotRenewal`: No renewal any longer. After you specify this value, Alibaba Cloud stop sending notification of instance expiry, and only gives a brief reminder on the third day before the instance expiry.
        :param pulumi.Input[str] spec: The instance type of the GA instance. Specification of global acceleration instance, value:
               `1`: Small 1.
               `2`: Small 2.
               `3`: Small 3.
               `5`: Medium 1.
               `8`: Medium 2.
               `10`: Medium 3.
        :param pulumi.Input[str] status: The status of the GA instance.
        """
        if accelerator_name is not None:
            pulumi.set(__self__, "accelerator_name", accelerator_name)
        if auto_renew_duration is not None:
            pulumi.set(__self__, "auto_renew_duration", auto_renew_duration)
        if auto_use_coupon is not None:
            pulumi.set(__self__, "auto_use_coupon", auto_use_coupon)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if duration is not None:
            pulumi.set(__self__, "duration", duration)
        if pricing_cycle is not None:
            pulumi.set(__self__, "pricing_cycle", pricing_cycle)
        if renewal_status is not None:
            pulumi.set(__self__, "renewal_status", renewal_status)
        if spec is not None:
            pulumi.set(__self__, "spec", spec)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="acceleratorName")
    def accelerator_name(self) -> Optional[pulumi.Input[str]]:
        """
        The Name of the GA instance.
        """
        return pulumi.get(self, "accelerator_name")

    @accelerator_name.setter
    def accelerator_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "accelerator_name", value)

    @property
    @pulumi.getter(name="autoRenewDuration")
    def auto_renew_duration(self) -> Optional[pulumi.Input[int]]:
        """
        Auto renewal period of an instance, in the unit of month. The value range is 1-12.
        """
        return pulumi.get(self, "auto_renew_duration")

    @auto_renew_duration.setter
    def auto_renew_duration(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "auto_renew_duration", value)

    @property
    @pulumi.getter(name="autoUseCoupon")
    def auto_use_coupon(self) -> Optional[pulumi.Input[bool]]:
        """
        Use coupons to pay bills automatically. Default value is `false`. Valid value: `true`: Use, `false`: Not used.
        """
        return pulumi.get(self, "auto_use_coupon")

    @auto_use_coupon.setter
    def auto_use_coupon(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "auto_use_coupon", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Descriptive information of the global acceleration instance.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def duration(self) -> Optional[pulumi.Input[int]]:
        """
        The subscription duration. **NOTE:** Starting from v1.150.0+, the `duration` and  `pricing_cycle` are both required.
        * If the `pricing_cycle` parameter is set to `Month`, the valid values for the `duration` parameter are 1 to 9.
        * If the `pricing_cycle` parameter is set to `Year`, the valid values for the `duration` parameter are 1 to 3.
        """
        return pulumi.get(self, "duration")

    @duration.setter
    def duration(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "duration", value)

    @property
    @pulumi.getter(name="pricingCycle")
    def pricing_cycle(self) -> Optional[pulumi.Input[str]]:
        """
        The billing cycle of the GA instance. Valid values: `Month`,`Year`. The default value: `Month`.
        * `Month`: billed on a monthly basis.
        * `Year`: billed on an annual basis.
        """
        return pulumi.get(self, "pricing_cycle")

    @pricing_cycle.setter
    def pricing_cycle(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pricing_cycle", value)

    @property
    @pulumi.getter(name="renewalStatus")
    def renewal_status(self) -> Optional[pulumi.Input[str]]:
        """
        Whether to renew an accelerator automatically or not. Default to "Normal". Valid values:
        - `AutoRenewal`: Enable auto renewal.
        - `Normal`: Disable auto renewal.
        - `NotRenewal`: No renewal any longer. After you specify this value, Alibaba Cloud stop sending notification of instance expiry, and only gives a brief reminder on the third day before the instance expiry.
        """
        return pulumi.get(self, "renewal_status")

    @renewal_status.setter
    def renewal_status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "renewal_status", value)

    @property
    @pulumi.getter
    def spec(self) -> Optional[pulumi.Input[str]]:
        """
        The instance type of the GA instance. Specification of global acceleration instance, value:
        `1`: Small 1.
        `2`: Small 2.
        `3`: Small 3.
        `5`: Medium 1.
        `8`: Medium 2.
        `10`: Medium 3.
        """
        return pulumi.get(self, "spec")

    @spec.setter
    def spec(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "spec", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        The status of the GA instance.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


class Accelerator(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accelerator_name: Optional[pulumi.Input[str]] = None,
                 auto_renew_duration: Optional[pulumi.Input[int]] = None,
                 auto_use_coupon: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 duration: Optional[pulumi.Input[int]] = None,
                 pricing_cycle: Optional[pulumi.Input[str]] = None,
                 renewal_status: Optional[pulumi.Input[str]] = None,
                 spec: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Global Accelerator (GA) Accelerator resource.

        For information about Global Accelerator (GA) Accelerator and how to use it, see [What is Accelerator](https://help.aliyun.com/document_detail/153235.html).

        > **NOTE:** At present, The `ga.Accelerator` cannot be deleted. you need to wait until the resource is outdated and released automatically.

        > **NOTE:** Available in v1.111.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        example = alicloud.ga.Accelerator("example",
            auto_use_coupon=True,
            duration=1,
            spec="1")
        ```

        ## Import

        Ga Accelerator can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:ga/accelerator:Accelerator example <accelerator_id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] accelerator_name: The Name of the GA instance.
        :param pulumi.Input[int] auto_renew_duration: Auto renewal period of an instance, in the unit of month. The value range is 1-12.
        :param pulumi.Input[bool] auto_use_coupon: Use coupons to pay bills automatically. Default value is `false`. Valid value: `true`: Use, `false`: Not used.
        :param pulumi.Input[str] description: Descriptive information of the global acceleration instance.
        :param pulumi.Input[int] duration: The subscription duration. **NOTE:** Starting from v1.150.0+, the `duration` and  `pricing_cycle` are both required.
               * If the `pricing_cycle` parameter is set to `Month`, the valid values for the `duration` parameter are 1 to 9.
               * If the `pricing_cycle` parameter is set to `Year`, the valid values for the `duration` parameter are 1 to 3.
        :param pulumi.Input[str] pricing_cycle: The billing cycle of the GA instance. Valid values: `Month`,`Year`. The default value: `Month`.
               * `Month`: billed on a monthly basis.
               * `Year`: billed on an annual basis.
        :param pulumi.Input[str] renewal_status: Whether to renew an accelerator automatically or not. Default to "Normal". Valid values:
               - `AutoRenewal`: Enable auto renewal.
               - `Normal`: Disable auto renewal.
               - `NotRenewal`: No renewal any longer. After you specify this value, Alibaba Cloud stop sending notification of instance expiry, and only gives a brief reminder on the third day before the instance expiry.
        :param pulumi.Input[str] spec: The instance type of the GA instance. Specification of global acceleration instance, value:
               `1`: Small 1.
               `2`: Small 2.
               `3`: Small 3.
               `5`: Medium 1.
               `8`: Medium 2.
               `10`: Medium 3.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AcceleratorArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Global Accelerator (GA) Accelerator resource.

        For information about Global Accelerator (GA) Accelerator and how to use it, see [What is Accelerator](https://help.aliyun.com/document_detail/153235.html).

        > **NOTE:** At present, The `ga.Accelerator` cannot be deleted. you need to wait until the resource is outdated and released automatically.

        > **NOTE:** Available in v1.111.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        example = alicloud.ga.Accelerator("example",
            auto_use_coupon=True,
            duration=1,
            spec="1")
        ```

        ## Import

        Ga Accelerator can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:ga/accelerator:Accelerator example <accelerator_id>
        ```

        :param str resource_name: The name of the resource.
        :param AcceleratorArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AcceleratorArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accelerator_name: Optional[pulumi.Input[str]] = None,
                 auto_renew_duration: Optional[pulumi.Input[int]] = None,
                 auto_use_coupon: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 duration: Optional[pulumi.Input[int]] = None,
                 pricing_cycle: Optional[pulumi.Input[str]] = None,
                 renewal_status: Optional[pulumi.Input[str]] = None,
                 spec: Optional[pulumi.Input[str]] = None,
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
            __props__ = AcceleratorArgs.__new__(AcceleratorArgs)

            __props__.__dict__["accelerator_name"] = accelerator_name
            __props__.__dict__["auto_renew_duration"] = auto_renew_duration
            __props__.__dict__["auto_use_coupon"] = auto_use_coupon
            __props__.__dict__["description"] = description
            if duration is None and not opts.urn:
                raise TypeError("Missing required property 'duration'")
            __props__.__dict__["duration"] = duration
            __props__.__dict__["pricing_cycle"] = pricing_cycle
            __props__.__dict__["renewal_status"] = renewal_status
            if spec is None and not opts.urn:
                raise TypeError("Missing required property 'spec'")
            __props__.__dict__["spec"] = spec
            __props__.__dict__["status"] = None
        super(Accelerator, __self__).__init__(
            'alicloud:ga/accelerator:Accelerator',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            accelerator_name: Optional[pulumi.Input[str]] = None,
            auto_renew_duration: Optional[pulumi.Input[int]] = None,
            auto_use_coupon: Optional[pulumi.Input[bool]] = None,
            description: Optional[pulumi.Input[str]] = None,
            duration: Optional[pulumi.Input[int]] = None,
            pricing_cycle: Optional[pulumi.Input[str]] = None,
            renewal_status: Optional[pulumi.Input[str]] = None,
            spec: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None) -> 'Accelerator':
        """
        Get an existing Accelerator resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] accelerator_name: The Name of the GA instance.
        :param pulumi.Input[int] auto_renew_duration: Auto renewal period of an instance, in the unit of month. The value range is 1-12.
        :param pulumi.Input[bool] auto_use_coupon: Use coupons to pay bills automatically. Default value is `false`. Valid value: `true`: Use, `false`: Not used.
        :param pulumi.Input[str] description: Descriptive information of the global acceleration instance.
        :param pulumi.Input[int] duration: The subscription duration. **NOTE:** Starting from v1.150.0+, the `duration` and  `pricing_cycle` are both required.
               * If the `pricing_cycle` parameter is set to `Month`, the valid values for the `duration` parameter are 1 to 9.
               * If the `pricing_cycle` parameter is set to `Year`, the valid values for the `duration` parameter are 1 to 3.
        :param pulumi.Input[str] pricing_cycle: The billing cycle of the GA instance. Valid values: `Month`,`Year`. The default value: `Month`.
               * `Month`: billed on a monthly basis.
               * `Year`: billed on an annual basis.
        :param pulumi.Input[str] renewal_status: Whether to renew an accelerator automatically or not. Default to "Normal". Valid values:
               - `AutoRenewal`: Enable auto renewal.
               - `Normal`: Disable auto renewal.
               - `NotRenewal`: No renewal any longer. After you specify this value, Alibaba Cloud stop sending notification of instance expiry, and only gives a brief reminder on the third day before the instance expiry.
        :param pulumi.Input[str] spec: The instance type of the GA instance. Specification of global acceleration instance, value:
               `1`: Small 1.
               `2`: Small 2.
               `3`: Small 3.
               `5`: Medium 1.
               `8`: Medium 2.
               `10`: Medium 3.
        :param pulumi.Input[str] status: The status of the GA instance.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AcceleratorState.__new__(_AcceleratorState)

        __props__.__dict__["accelerator_name"] = accelerator_name
        __props__.__dict__["auto_renew_duration"] = auto_renew_duration
        __props__.__dict__["auto_use_coupon"] = auto_use_coupon
        __props__.__dict__["description"] = description
        __props__.__dict__["duration"] = duration
        __props__.__dict__["pricing_cycle"] = pricing_cycle
        __props__.__dict__["renewal_status"] = renewal_status
        __props__.__dict__["spec"] = spec
        __props__.__dict__["status"] = status
        return Accelerator(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="acceleratorName")
    def accelerator_name(self) -> pulumi.Output[Optional[str]]:
        """
        The Name of the GA instance.
        """
        return pulumi.get(self, "accelerator_name")

    @property
    @pulumi.getter(name="autoRenewDuration")
    def auto_renew_duration(self) -> pulumi.Output[Optional[int]]:
        """
        Auto renewal period of an instance, in the unit of month. The value range is 1-12.
        """
        return pulumi.get(self, "auto_renew_duration")

    @property
    @pulumi.getter(name="autoUseCoupon")
    def auto_use_coupon(self) -> pulumi.Output[Optional[bool]]:
        """
        Use coupons to pay bills automatically. Default value is `false`. Valid value: `true`: Use, `false`: Not used.
        """
        return pulumi.get(self, "auto_use_coupon")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Descriptive information of the global acceleration instance.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def duration(self) -> pulumi.Output[int]:
        """
        The subscription duration. **NOTE:** Starting from v1.150.0+, the `duration` and  `pricing_cycle` are both required.
        * If the `pricing_cycle` parameter is set to `Month`, the valid values for the `duration` parameter are 1 to 9.
        * If the `pricing_cycle` parameter is set to `Year`, the valid values for the `duration` parameter are 1 to 3.
        """
        return pulumi.get(self, "duration")

    @property
    @pulumi.getter(name="pricingCycle")
    def pricing_cycle(self) -> pulumi.Output[str]:
        """
        The billing cycle of the GA instance. Valid values: `Month`,`Year`. The default value: `Month`.
        * `Month`: billed on a monthly basis.
        * `Year`: billed on an annual basis.
        """
        return pulumi.get(self, "pricing_cycle")

    @property
    @pulumi.getter(name="renewalStatus")
    def renewal_status(self) -> pulumi.Output[str]:
        """
        Whether to renew an accelerator automatically or not. Default to "Normal". Valid values:
        - `AutoRenewal`: Enable auto renewal.
        - `Normal`: Disable auto renewal.
        - `NotRenewal`: No renewal any longer. After you specify this value, Alibaba Cloud stop sending notification of instance expiry, and only gives a brief reminder on the third day before the instance expiry.
        """
        return pulumi.get(self, "renewal_status")

    @property
    @pulumi.getter
    def spec(self) -> pulumi.Output[str]:
        """
        The instance type of the GA instance. Specification of global acceleration instance, value:
        `1`: Small 1.
        `2`: Small 2.
        `3`: Small 3.
        `5`: Medium 1.
        `8`: Medium 2.
        `10`: Medium 3.
        """
        return pulumi.get(self, "spec")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of the GA instance.
        """
        return pulumi.get(self, "status")

