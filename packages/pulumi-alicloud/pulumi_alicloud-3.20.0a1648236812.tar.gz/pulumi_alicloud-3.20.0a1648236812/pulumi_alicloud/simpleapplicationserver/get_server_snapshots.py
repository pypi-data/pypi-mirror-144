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
    'GetServerSnapshotsResult',
    'AwaitableGetServerSnapshotsResult',
    'get_server_snapshots',
    'get_server_snapshots_output',
]

@pulumi.output_type
class GetServerSnapshotsResult:
    """
    A collection of values returned by getServerSnapshots.
    """
    def __init__(__self__, disk_id=None, id=None, ids=None, instance_id=None, name_regex=None, names=None, output_file=None, snapshots=None, status=None):
        if disk_id and not isinstance(disk_id, str):
            raise TypeError("Expected argument 'disk_id' to be a str")
        pulumi.set(__self__, "disk_id", disk_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if instance_id and not isinstance(instance_id, str):
            raise TypeError("Expected argument 'instance_id' to be a str")
        pulumi.set(__self__, "instance_id", instance_id)
        if name_regex and not isinstance(name_regex, str):
            raise TypeError("Expected argument 'name_regex' to be a str")
        pulumi.set(__self__, "name_regex", name_regex)
        if names and not isinstance(names, list):
            raise TypeError("Expected argument 'names' to be a list")
        pulumi.set(__self__, "names", names)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if snapshots and not isinstance(snapshots, list):
            raise TypeError("Expected argument 'snapshots' to be a list")
        pulumi.set(__self__, "snapshots", snapshots)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="diskId")
    def disk_id(self) -> Optional[str]:
        return pulumi.get(self, "disk_id")

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
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[str]:
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter(name="nameRegex")
    def name_regex(self) -> Optional[str]:
        return pulumi.get(self, "name_regex")

    @property
    @pulumi.getter
    def names(self) -> Sequence[str]:
        return pulumi.get(self, "names")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter
    def snapshots(self) -> Sequence['outputs.GetServerSnapshotsSnapshotResult']:
        return pulumi.get(self, "snapshots")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        return pulumi.get(self, "status")


class AwaitableGetServerSnapshotsResult(GetServerSnapshotsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServerSnapshotsResult(
            disk_id=self.disk_id,
            id=self.id,
            ids=self.ids,
            instance_id=self.instance_id,
            name_regex=self.name_regex,
            names=self.names,
            output_file=self.output_file,
            snapshots=self.snapshots,
            status=self.status)


def get_server_snapshots(disk_id: Optional[str] = None,
                         ids: Optional[Sequence[str]] = None,
                         instance_id: Optional[str] = None,
                         name_regex: Optional[str] = None,
                         output_file: Optional[str] = None,
                         status: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServerSnapshotsResult:
    """
    This data source provides the Simple Application Server Snapshots of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.143.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ids = alicloud.simpleapplicationserver.get_server_snapshots(ids=["example_id"])
    pulumi.export("simpleApplicationServerSnapshotId1", ids.snapshots[0].id)
    name_regex = alicloud.simpleapplicationserver.get_server_snapshots(name_regex="^my-Snapshot")
    pulumi.export("simpleApplicationServerSnapshotId2", name_regex.snapshots[0].id)
    disk_id_conf = alicloud.simpleapplicationserver.get_server_snapshots(ids=["example_id"],
        disk_id="example_value")
    pulumi.export("simpleApplicationServerSnapshotId3", disk_id_conf.snapshots[0].id)
    instance_id_conf = alicloud.simpleapplicationserver.get_server_snapshots(ids=["example_id"],
        instance_id="example_value")
    pulumi.export("simpleApplicationServerSnapshotId4", instance_id_conf.snapshots[0].id)
    ```


    :param str disk_id: The ID of the source disk. This parameter has a value even after the source disk is released.
    :param Sequence[str] ids: A list of Snapshot IDs.
    :param str instance_id: The ID of the simple application server.
    :param str name_regex: A regex string to filter results by Snapshot name.
    :param str status: The status of the snapshots. Valid values: `Progressing`, `Accomplished` and `Failed`.
    """
    __args__ = dict()
    __args__['diskId'] = disk_id
    __args__['ids'] = ids
    __args__['instanceId'] = instance_id
    __args__['nameRegex'] = name_regex
    __args__['outputFile'] = output_file
    __args__['status'] = status
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('alicloud:simpleapplicationserver/getServerSnapshots:getServerSnapshots', __args__, opts=opts, typ=GetServerSnapshotsResult).value

    return AwaitableGetServerSnapshotsResult(
        disk_id=__ret__.disk_id,
        id=__ret__.id,
        ids=__ret__.ids,
        instance_id=__ret__.instance_id,
        name_regex=__ret__.name_regex,
        names=__ret__.names,
        output_file=__ret__.output_file,
        snapshots=__ret__.snapshots,
        status=__ret__.status)


@_utilities.lift_output_func(get_server_snapshots)
def get_server_snapshots_output(disk_id: Optional[pulumi.Input[Optional[str]]] = None,
                                ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                instance_id: Optional[pulumi.Input[Optional[str]]] = None,
                                name_regex: Optional[pulumi.Input[Optional[str]]] = None,
                                output_file: Optional[pulumi.Input[Optional[str]]] = None,
                                status: Optional[pulumi.Input[Optional[str]]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetServerSnapshotsResult]:
    """
    This data source provides the Simple Application Server Snapshots of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.143.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ids = alicloud.simpleapplicationserver.get_server_snapshots(ids=["example_id"])
    pulumi.export("simpleApplicationServerSnapshotId1", ids.snapshots[0].id)
    name_regex = alicloud.simpleapplicationserver.get_server_snapshots(name_regex="^my-Snapshot")
    pulumi.export("simpleApplicationServerSnapshotId2", name_regex.snapshots[0].id)
    disk_id_conf = alicloud.simpleapplicationserver.get_server_snapshots(ids=["example_id"],
        disk_id="example_value")
    pulumi.export("simpleApplicationServerSnapshotId3", disk_id_conf.snapshots[0].id)
    instance_id_conf = alicloud.simpleapplicationserver.get_server_snapshots(ids=["example_id"],
        instance_id="example_value")
    pulumi.export("simpleApplicationServerSnapshotId4", instance_id_conf.snapshots[0].id)
    ```


    :param str disk_id: The ID of the source disk. This parameter has a value even after the source disk is released.
    :param Sequence[str] ids: A list of Snapshot IDs.
    :param str instance_id: The ID of the simple application server.
    :param str name_regex: A regex string to filter results by Snapshot name.
    :param str status: The status of the snapshots. Valid values: `Progressing`, `Accomplished` and `Failed`.
    """
    ...
