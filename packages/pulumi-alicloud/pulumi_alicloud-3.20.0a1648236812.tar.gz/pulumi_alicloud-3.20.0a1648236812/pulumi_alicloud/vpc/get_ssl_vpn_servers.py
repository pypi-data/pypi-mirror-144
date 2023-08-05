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
    'GetSslVpnServersResult',
    'AwaitableGetSslVpnServersResult',
    'get_ssl_vpn_servers',
    'get_ssl_vpn_servers_output',
]

@pulumi.output_type
class GetSslVpnServersResult:
    """
    A collection of values returned by getSslVpnServers.
    """
    def __init__(__self__, id=None, ids=None, name_regex=None, names=None, output_file=None, servers=None, vpn_gateway_id=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if name_regex and not isinstance(name_regex, str):
            raise TypeError("Expected argument 'name_regex' to be a str")
        pulumi.set(__self__, "name_regex", name_regex)
        if names and not isinstance(names, list):
            raise TypeError("Expected argument 'names' to be a list")
        pulumi.set(__self__, "names", names)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if servers and not isinstance(servers, list):
            raise TypeError("Expected argument 'servers' to be a list")
        pulumi.set(__self__, "servers", servers)
        if vpn_gateway_id and not isinstance(vpn_gateway_id, str):
            raise TypeError("Expected argument 'vpn_gateway_id' to be a str")
        pulumi.set(__self__, "vpn_gateway_id", vpn_gateway_id)

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
        A list of SSL-VPN server IDs.
        """
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter(name="nameRegex")
    def name_regex(self) -> Optional[str]:
        return pulumi.get(self, "name_regex")

    @property
    @pulumi.getter
    def names(self) -> Sequence[str]:
        """
        A list of SSL-VPN server names.
        """
        return pulumi.get(self, "names")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter
    def servers(self) -> Sequence['outputs.GetSslVpnServersServerResult']:
        """
        A list of SSL-VPN servers. Each element contains the following attributes:
        """
        return pulumi.get(self, "servers")

    @property
    @pulumi.getter(name="vpnGatewayId")
    def vpn_gateway_id(self) -> Optional[str]:
        """
        The ID of the VPN gateway instance.
        """
        return pulumi.get(self, "vpn_gateway_id")


class AwaitableGetSslVpnServersResult(GetSslVpnServersResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSslVpnServersResult(
            id=self.id,
            ids=self.ids,
            name_regex=self.name_regex,
            names=self.names,
            output_file=self.output_file,
            servers=self.servers,
            vpn_gateway_id=self.vpn_gateway_id)


def get_ssl_vpn_servers(ids: Optional[Sequence[str]] = None,
                        name_regex: Optional[str] = None,
                        output_file: Optional[str] = None,
                        vpn_gateway_id: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSslVpnServersResult:
    """
    The SSL-VPN servers data source lists lots of SSL-VPN servers resource information owned by an Alicloud account.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    foo = alicloud.vpc.get_ssl_vpn_servers(ids=["fake-server-id"],
        name_regex="^foo",
        output_file="/tmp/sslserver",
        vpn_gateway_id="fake-vpn-id")
    ```


    :param Sequence[str] ids: IDs of the SSL-VPN servers.
    :param str name_regex: A regex string of SSL-VPN server name.
    :param str output_file: Save the result to the file.
    :param str vpn_gateway_id: Use the VPN gateway ID as the search key.
    """
    __args__ = dict()
    __args__['ids'] = ids
    __args__['nameRegex'] = name_regex
    __args__['outputFile'] = output_file
    __args__['vpnGatewayId'] = vpn_gateway_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('alicloud:vpc/getSslVpnServers:getSslVpnServers', __args__, opts=opts, typ=GetSslVpnServersResult).value

    return AwaitableGetSslVpnServersResult(
        id=__ret__.id,
        ids=__ret__.ids,
        name_regex=__ret__.name_regex,
        names=__ret__.names,
        output_file=__ret__.output_file,
        servers=__ret__.servers,
        vpn_gateway_id=__ret__.vpn_gateway_id)


@_utilities.lift_output_func(get_ssl_vpn_servers)
def get_ssl_vpn_servers_output(ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                               name_regex: Optional[pulumi.Input[Optional[str]]] = None,
                               output_file: Optional[pulumi.Input[Optional[str]]] = None,
                               vpn_gateway_id: Optional[pulumi.Input[Optional[str]]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSslVpnServersResult]:
    """
    The SSL-VPN servers data source lists lots of SSL-VPN servers resource information owned by an Alicloud account.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    foo = alicloud.vpc.get_ssl_vpn_servers(ids=["fake-server-id"],
        name_regex="^foo",
        output_file="/tmp/sslserver",
        vpn_gateway_id="fake-vpn-id")
    ```


    :param Sequence[str] ids: IDs of the SSL-VPN servers.
    :param str name_regex: A regex string of SSL-VPN server name.
    :param str output_file: Save the result to the file.
    :param str vpn_gateway_id: Use the VPN gateway ID as the search key.
    """
    ...
