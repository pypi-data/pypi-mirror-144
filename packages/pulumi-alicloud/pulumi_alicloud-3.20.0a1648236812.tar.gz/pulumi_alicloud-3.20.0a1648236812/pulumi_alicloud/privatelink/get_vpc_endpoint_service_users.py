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
    'GetVpcEndpointServiceUsersResult',
    'AwaitableGetVpcEndpointServiceUsersResult',
    'get_vpc_endpoint_service_users',
    'get_vpc_endpoint_service_users_output',
]

@pulumi.output_type
class GetVpcEndpointServiceUsersResult:
    """
    A collection of values returned by getVpcEndpointServiceUsers.
    """
    def __init__(__self__, id=None, ids=None, output_file=None, service_id=None, user_id=None, users=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if service_id and not isinstance(service_id, str):
            raise TypeError("Expected argument 'service_id' to be a str")
        pulumi.set(__self__, "service_id", service_id)
        if user_id and not isinstance(user_id, str):
            raise TypeError("Expected argument 'user_id' to be a str")
        pulumi.set(__self__, "user_id", user_id)
        if users and not isinstance(users, list):
            raise TypeError("Expected argument 'users' to be a list")
        pulumi.set(__self__, "users", users)

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
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> str:
        return pulumi.get(self, "service_id")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> Optional[str]:
        return pulumi.get(self, "user_id")

    @property
    @pulumi.getter
    def users(self) -> Sequence['outputs.GetVpcEndpointServiceUsersUserResult']:
        return pulumi.get(self, "users")


class AwaitableGetVpcEndpointServiceUsersResult(GetVpcEndpointServiceUsersResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVpcEndpointServiceUsersResult(
            id=self.id,
            ids=self.ids,
            output_file=self.output_file,
            service_id=self.service_id,
            user_id=self.user_id,
            users=self.users)


def get_vpc_endpoint_service_users(output_file: Optional[str] = None,
                                   service_id: Optional[str] = None,
                                   user_id: Optional[str] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVpcEndpointServiceUsersResult:
    """
    This data source provides the Privatelink Vpc Endpoint Service Users of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.110.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    example = alicloud.privatelink.get_vpc_endpoint_service_users(service_id="epsrv-gw81c6vxxxxxx")
    pulumi.export("firstPrivatelinkVpcEndpointServiceUserId", example.users[0].id)
    ```


    :param str service_id: The Id of Vpc Endpoint Service.
    :param str user_id: The Id of Ram User.
    """
    __args__ = dict()
    __args__['outputFile'] = output_file
    __args__['serviceId'] = service_id
    __args__['userId'] = user_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('alicloud:privatelink/getVpcEndpointServiceUsers:getVpcEndpointServiceUsers', __args__, opts=opts, typ=GetVpcEndpointServiceUsersResult).value

    return AwaitableGetVpcEndpointServiceUsersResult(
        id=__ret__.id,
        ids=__ret__.ids,
        output_file=__ret__.output_file,
        service_id=__ret__.service_id,
        user_id=__ret__.user_id,
        users=__ret__.users)


@_utilities.lift_output_func(get_vpc_endpoint_service_users)
def get_vpc_endpoint_service_users_output(output_file: Optional[pulumi.Input[Optional[str]]] = None,
                                          service_id: Optional[pulumi.Input[str]] = None,
                                          user_id: Optional[pulumi.Input[Optional[str]]] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVpcEndpointServiceUsersResult]:
    """
    This data source provides the Privatelink Vpc Endpoint Service Users of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.110.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    example = alicloud.privatelink.get_vpc_endpoint_service_users(service_id="epsrv-gw81c6vxxxxxx")
    pulumi.export("firstPrivatelinkVpcEndpointServiceUserId", example.users[0].id)
    ```


    :param str service_id: The Id of Vpc Endpoint Service.
    :param str user_id: The Id of Ram User.
    """
    ...
