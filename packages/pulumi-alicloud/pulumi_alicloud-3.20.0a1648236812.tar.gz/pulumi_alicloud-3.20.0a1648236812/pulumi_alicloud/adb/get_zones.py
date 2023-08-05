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
    'GetZonesResult',
    'AwaitableGetZonesResult',
    'get_zones',
    'get_zones_output',
]

@pulumi.output_type
class GetZonesResult:
    """
    A collection of values returned by getZones.
    """
    def __init__(__self__, id=None, ids=None, multi=None, output_file=None, zones=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if multi and not isinstance(multi, bool):
            raise TypeError("Expected argument 'multi' to be a bool")
        pulumi.set(__self__, "multi", multi)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if zones and not isinstance(zones, list):
            raise TypeError("Expected argument 'zones' to be a list")
        pulumi.set(__self__, "zones", zones)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ids(self) -> Sequence[str]:
        """
        A list of zone IDs.
        """
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter
    def multi(self) -> Optional[bool]:
        return pulumi.get(self, "multi")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter
    def zones(self) -> Sequence['outputs.GetZonesZoneResult']:
        """
        A list of availability zones. Each element contains the following attributes:
        """
        return pulumi.get(self, "zones")


class AwaitableGetZonesResult(GetZonesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetZonesResult(
            id=self.id,
            ids=self.ids,
            multi=self.multi,
            output_file=self.output_file,
            zones=self.zones)


def get_zones(multi: Optional[bool] = None,
              output_file: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetZonesResult:
    """
    This data source provides availability zones for ADB that can be accessed by an Alibaba Cloud account within the region configured in the provider.

    > **NOTE:** Available in v1.73.0+.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    zones_ids = alicloud.adb.get_zones()
    ```


    :param bool multi: Indicate whether the zones can be used in a multi AZ configuration. Default to `false`. Multi AZ is usually used to launch ADB instances.
    """
    __args__ = dict()
    __args__['multi'] = multi
    __args__['outputFile'] = output_file
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('alicloud:adb/getZones:getZones', __args__, opts=opts, typ=GetZonesResult).value

    return AwaitableGetZonesResult(
        id=__ret__.id,
        ids=__ret__.ids,
        multi=__ret__.multi,
        output_file=__ret__.output_file,
        zones=__ret__.zones)


@_utilities.lift_output_func(get_zones)
def get_zones_output(multi: Optional[pulumi.Input[Optional[bool]]] = None,
                     output_file: Optional[pulumi.Input[Optional[str]]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetZonesResult]:
    """
    This data source provides availability zones for ADB that can be accessed by an Alibaba Cloud account within the region configured in the provider.

    > **NOTE:** Available in v1.73.0+.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    zones_ids = alicloud.adb.get_zones()
    ```


    :param bool multi: Indicate whether the zones can be used in a multi AZ configuration. Default to `false`. Multi AZ is usually used to launch ADB instances.
    """
    ...
