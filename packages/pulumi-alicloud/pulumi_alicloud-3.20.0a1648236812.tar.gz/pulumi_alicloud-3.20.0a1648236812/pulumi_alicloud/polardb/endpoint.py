# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['EndpointArgs', 'Endpoint']

@pulumi.input_type
class EndpointArgs:
    def __init__(__self__, *,
                 db_cluster_id: pulumi.Input[str],
                 auto_add_new_nodes: Optional[pulumi.Input[str]] = None,
                 endpoint_config: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 endpoint_type: Optional[pulumi.Input[str]] = None,
                 net_type: Optional[pulumi.Input[str]] = None,
                 nodes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 read_write_mode: Optional[pulumi.Input[str]] = None,
                 ssl_auto_rotate: Optional[pulumi.Input[str]] = None,
                 ssl_enabled: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Endpoint resource.
        :param pulumi.Input[str] endpoint_type: Type of endpoint.
        """
        pulumi.set(__self__, "db_cluster_id", db_cluster_id)
        if auto_add_new_nodes is not None:
            pulumi.set(__self__, "auto_add_new_nodes", auto_add_new_nodes)
        if endpoint_config is not None:
            pulumi.set(__self__, "endpoint_config", endpoint_config)
        if endpoint_type is not None:
            pulumi.set(__self__, "endpoint_type", endpoint_type)
        if net_type is not None:
            pulumi.set(__self__, "net_type", net_type)
        if nodes is not None:
            pulumi.set(__self__, "nodes", nodes)
        if read_write_mode is not None:
            pulumi.set(__self__, "read_write_mode", read_write_mode)
        if ssl_auto_rotate is not None:
            pulumi.set(__self__, "ssl_auto_rotate", ssl_auto_rotate)
        if ssl_enabled is not None:
            pulumi.set(__self__, "ssl_enabled", ssl_enabled)

    @property
    @pulumi.getter(name="dbClusterId")
    def db_cluster_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "db_cluster_id")

    @db_cluster_id.setter
    def db_cluster_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "db_cluster_id", value)

    @property
    @pulumi.getter(name="autoAddNewNodes")
    def auto_add_new_nodes(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "auto_add_new_nodes")

    @auto_add_new_nodes.setter
    def auto_add_new_nodes(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "auto_add_new_nodes", value)

    @property
    @pulumi.getter(name="endpointConfig")
    def endpoint_config(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        return pulumi.get(self, "endpoint_config")

    @endpoint_config.setter
    def endpoint_config(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "endpoint_config", value)

    @property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> Optional[pulumi.Input[str]]:
        """
        Type of endpoint.
        """
        return pulumi.get(self, "endpoint_type")

    @endpoint_type.setter
    def endpoint_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "endpoint_type", value)

    @property
    @pulumi.getter(name="netType")
    def net_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "net_type")

    @net_type.setter
    def net_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "net_type", value)

    @property
    @pulumi.getter
    def nodes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "nodes")

    @nodes.setter
    def nodes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "nodes", value)

    @property
    @pulumi.getter(name="readWriteMode")
    def read_write_mode(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "read_write_mode")

    @read_write_mode.setter
    def read_write_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "read_write_mode", value)

    @property
    @pulumi.getter(name="sslAutoRotate")
    def ssl_auto_rotate(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "ssl_auto_rotate")

    @ssl_auto_rotate.setter
    def ssl_auto_rotate(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ssl_auto_rotate", value)

    @property
    @pulumi.getter(name="sslEnabled")
    def ssl_enabled(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "ssl_enabled")

    @ssl_enabled.setter
    def ssl_enabled(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ssl_enabled", value)


@pulumi.input_type
class _EndpointState:
    def __init__(__self__, *,
                 auto_add_new_nodes: Optional[pulumi.Input[str]] = None,
                 db_cluster_id: Optional[pulumi.Input[str]] = None,
                 endpoint_config: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 endpoint_type: Optional[pulumi.Input[str]] = None,
                 net_type: Optional[pulumi.Input[str]] = None,
                 nodes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 read_write_mode: Optional[pulumi.Input[str]] = None,
                 ssl_auto_rotate: Optional[pulumi.Input[str]] = None,
                 ssl_certificate_url: Optional[pulumi.Input[str]] = None,
                 ssl_connection_string: Optional[pulumi.Input[str]] = None,
                 ssl_enabled: Optional[pulumi.Input[str]] = None,
                 ssl_expire_time: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Endpoint resources.
        :param pulumi.Input[str] endpoint_type: Type of endpoint.
        :param pulumi.Input[str] ssl_connection_string: (Available in v1.121.0+) The SSL connection string.
        :param pulumi.Input[str] ssl_expire_time: (Available in v1.121.0+) The time when the SSL certificate expires. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        """
        if auto_add_new_nodes is not None:
            pulumi.set(__self__, "auto_add_new_nodes", auto_add_new_nodes)
        if db_cluster_id is not None:
            pulumi.set(__self__, "db_cluster_id", db_cluster_id)
        if endpoint_config is not None:
            pulumi.set(__self__, "endpoint_config", endpoint_config)
        if endpoint_type is not None:
            pulumi.set(__self__, "endpoint_type", endpoint_type)
        if net_type is not None:
            pulumi.set(__self__, "net_type", net_type)
        if nodes is not None:
            pulumi.set(__self__, "nodes", nodes)
        if read_write_mode is not None:
            pulumi.set(__self__, "read_write_mode", read_write_mode)
        if ssl_auto_rotate is not None:
            pulumi.set(__self__, "ssl_auto_rotate", ssl_auto_rotate)
        if ssl_certificate_url is not None:
            pulumi.set(__self__, "ssl_certificate_url", ssl_certificate_url)
        if ssl_connection_string is not None:
            pulumi.set(__self__, "ssl_connection_string", ssl_connection_string)
        if ssl_enabled is not None:
            pulumi.set(__self__, "ssl_enabled", ssl_enabled)
        if ssl_expire_time is not None:
            pulumi.set(__self__, "ssl_expire_time", ssl_expire_time)

    @property
    @pulumi.getter(name="autoAddNewNodes")
    def auto_add_new_nodes(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "auto_add_new_nodes")

    @auto_add_new_nodes.setter
    def auto_add_new_nodes(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "auto_add_new_nodes", value)

    @property
    @pulumi.getter(name="dbClusterId")
    def db_cluster_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "db_cluster_id")

    @db_cluster_id.setter
    def db_cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "db_cluster_id", value)

    @property
    @pulumi.getter(name="endpointConfig")
    def endpoint_config(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        return pulumi.get(self, "endpoint_config")

    @endpoint_config.setter
    def endpoint_config(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "endpoint_config", value)

    @property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> Optional[pulumi.Input[str]]:
        """
        Type of endpoint.
        """
        return pulumi.get(self, "endpoint_type")

    @endpoint_type.setter
    def endpoint_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "endpoint_type", value)

    @property
    @pulumi.getter(name="netType")
    def net_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "net_type")

    @net_type.setter
    def net_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "net_type", value)

    @property
    @pulumi.getter
    def nodes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "nodes")

    @nodes.setter
    def nodes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "nodes", value)

    @property
    @pulumi.getter(name="readWriteMode")
    def read_write_mode(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "read_write_mode")

    @read_write_mode.setter
    def read_write_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "read_write_mode", value)

    @property
    @pulumi.getter(name="sslAutoRotate")
    def ssl_auto_rotate(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "ssl_auto_rotate")

    @ssl_auto_rotate.setter
    def ssl_auto_rotate(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ssl_auto_rotate", value)

    @property
    @pulumi.getter(name="sslCertificateUrl")
    def ssl_certificate_url(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "ssl_certificate_url")

    @ssl_certificate_url.setter
    def ssl_certificate_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ssl_certificate_url", value)

    @property
    @pulumi.getter(name="sslConnectionString")
    def ssl_connection_string(self) -> Optional[pulumi.Input[str]]:
        """
        (Available in v1.121.0+) The SSL connection string.
        """
        return pulumi.get(self, "ssl_connection_string")

    @ssl_connection_string.setter
    def ssl_connection_string(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ssl_connection_string", value)

    @property
    @pulumi.getter(name="sslEnabled")
    def ssl_enabled(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "ssl_enabled")

    @ssl_enabled.setter
    def ssl_enabled(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ssl_enabled", value)

    @property
    @pulumi.getter(name="sslExpireTime")
    def ssl_expire_time(self) -> Optional[pulumi.Input[str]]:
        """
        (Available in v1.121.0+) The time when the SSL certificate expires. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        """
        return pulumi.get(self, "ssl_expire_time")

    @ssl_expire_time.setter
    def ssl_expire_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ssl_expire_time", value)


class Endpoint(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_add_new_nodes: Optional[pulumi.Input[str]] = None,
                 db_cluster_id: Optional[pulumi.Input[str]] = None,
                 endpoint_config: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 endpoint_type: Optional[pulumi.Input[str]] = None,
                 net_type: Optional[pulumi.Input[str]] = None,
                 nodes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 read_write_mode: Optional[pulumi.Input[str]] = None,
                 ssl_auto_rotate: Optional[pulumi.Input[str]] = None,
                 ssl_enabled: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a PolarDB endpoint resource to manage endpoint of PolarDB cluster.

        > **NOTE:** After v1.80.0 and before v1.121.0, you can only use this resource to manage the custom endpoint. Since v1.121.0, you also can import the primary endpoint and the cluster endpoint, to modify their ssl status and so on.

        > **NOTE:** The primary endpoint and the default cluster endpoint can not be created or deleted manually.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        creation = config.get("creation")
        if creation is None:
            creation = "PolarDB"
        name = config.get("name")
        if name is None:
            name = "polardbconnectionbasic"
        default_zones = alicloud.get_zones(available_resource_creation=creation)
        default_network = alicloud.vpc.Network("defaultNetwork", cidr_block="172.16.0.0/16")
        default_switch = alicloud.vpc.Switch("defaultSwitch",
            vpc_id=default_network.id,
            cidr_block="172.16.0.0/24",
            zone_id=default_zones.zones[0].id)
        default_cluster = alicloud.polardb.Cluster("defaultCluster",
            db_type="MySQL",
            db_version="8.0",
            pay_type="PostPaid",
            db_node_class="polar.mysql.x4.large",
            vswitch_id=default_switch.id,
            description=name)
        endpoint = alicloud.polardb.Endpoint("endpoint",
            db_cluster_id=default_cluster.id,
            endpoint_type="Custom")
        ```
        ## Argument Reference

        The following arguments are supported:

        * `db_cluster_id` - (Required, ForceNew) The Id of cluster that can run database.
        * `endpoint_type` - (Required & ForceNew before v1.121.0, Optional in v1.121.0+) Type of the endpoint. Before v1.121.0, it only can be `Custom`. since v1.121.0, `Custom`, `Cluster`, `Primary` are valid, default to `Custom`. However when creating a new endpoint, it also only can be `Custom`.
        * `read_write_mode` - (Optional) Read or write mode. Valid values are `ReadWrite`, `ReadOnly`. When creating a new custom endpoint, default to `ReadOnly`.
        * `nodes` - (Optional) Node id list for endpoint configuration. At least 2 nodes if specified, or if the cluster has more than 3 nodes, read-only endpoint is allowed to mount only one node. Default is all nodes.
        * `auto_add_new_nodes` - (Optional) Whether the new node automatically joins the default cluster address. Valid values are `Enable`, `Disable`. When creating a new custom endpoint, default to `Disable`.
        * `endpoint_config` - (Optional) The advanced settings of the endpoint of Apsara PolarDB clusters are in JSON format. Including the settings of consistency level, transaction splitting, connection pool, and offload reads from primary node. For more details, see the [description of EndpointConfig in the Request parameters table for details](https://www.alibabacloud.com/help/doc-detail/116593.htm).
        * `ssl_enabled` - (Optional, Available in v1.121.0+) Specifies how to modify the SSL encryption status. Valid values: `Disable`, `Enable`, `Update`.
        * `net_type` - (Optional, Available in v1.121.0+) The network type of the endpoint address.
        * `ssl_auto_rotate` - (Available in v1.132.0+) Specifies whether automatic rotation of SSL certificates is enabled. Valid values: `Enable`,`Disable`.
        * `ssl_certificate_url` - (Available in v1.132.0+) Specifies SSL certificate download link.\
            **NOTE:** For a PolarDB for MySQL cluster, this parameter is required, and only one connection string in each endpoint can enable the ssl, for other notes, see [Configure SSL encryption](https://www.alibabacloud.com/help/doc-detail/153182.htm).\
            For a PolarDB for PostgreSQL cluster or a PolarDB-O cluster, this parameter is not required, by default, SSL encryption is enabled for all endpoints.

        ## Import

        PolarDB endpoint can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:polardb/endpoint:Endpoint example pc-abc123456:pe-abc123456
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] endpoint_type: Type of endpoint.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EndpointArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a PolarDB endpoint resource to manage endpoint of PolarDB cluster.

        > **NOTE:** After v1.80.0 and before v1.121.0, you can only use this resource to manage the custom endpoint. Since v1.121.0, you also can import the primary endpoint and the cluster endpoint, to modify their ssl status and so on.

        > **NOTE:** The primary endpoint and the default cluster endpoint can not be created or deleted manually.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        creation = config.get("creation")
        if creation is None:
            creation = "PolarDB"
        name = config.get("name")
        if name is None:
            name = "polardbconnectionbasic"
        default_zones = alicloud.get_zones(available_resource_creation=creation)
        default_network = alicloud.vpc.Network("defaultNetwork", cidr_block="172.16.0.0/16")
        default_switch = alicloud.vpc.Switch("defaultSwitch",
            vpc_id=default_network.id,
            cidr_block="172.16.0.0/24",
            zone_id=default_zones.zones[0].id)
        default_cluster = alicloud.polardb.Cluster("defaultCluster",
            db_type="MySQL",
            db_version="8.0",
            pay_type="PostPaid",
            db_node_class="polar.mysql.x4.large",
            vswitch_id=default_switch.id,
            description=name)
        endpoint = alicloud.polardb.Endpoint("endpoint",
            db_cluster_id=default_cluster.id,
            endpoint_type="Custom")
        ```
        ## Argument Reference

        The following arguments are supported:

        * `db_cluster_id` - (Required, ForceNew) The Id of cluster that can run database.
        * `endpoint_type` - (Required & ForceNew before v1.121.0, Optional in v1.121.0+) Type of the endpoint. Before v1.121.0, it only can be `Custom`. since v1.121.0, `Custom`, `Cluster`, `Primary` are valid, default to `Custom`. However when creating a new endpoint, it also only can be `Custom`.
        * `read_write_mode` - (Optional) Read or write mode. Valid values are `ReadWrite`, `ReadOnly`. When creating a new custom endpoint, default to `ReadOnly`.
        * `nodes` - (Optional) Node id list for endpoint configuration. At least 2 nodes if specified, or if the cluster has more than 3 nodes, read-only endpoint is allowed to mount only one node. Default is all nodes.
        * `auto_add_new_nodes` - (Optional) Whether the new node automatically joins the default cluster address. Valid values are `Enable`, `Disable`. When creating a new custom endpoint, default to `Disable`.
        * `endpoint_config` - (Optional) The advanced settings of the endpoint of Apsara PolarDB clusters are in JSON format. Including the settings of consistency level, transaction splitting, connection pool, and offload reads from primary node. For more details, see the [description of EndpointConfig in the Request parameters table for details](https://www.alibabacloud.com/help/doc-detail/116593.htm).
        * `ssl_enabled` - (Optional, Available in v1.121.0+) Specifies how to modify the SSL encryption status. Valid values: `Disable`, `Enable`, `Update`.
        * `net_type` - (Optional, Available in v1.121.0+) The network type of the endpoint address.
        * `ssl_auto_rotate` - (Available in v1.132.0+) Specifies whether automatic rotation of SSL certificates is enabled. Valid values: `Enable`,`Disable`.
        * `ssl_certificate_url` - (Available in v1.132.0+) Specifies SSL certificate download link.\
            **NOTE:** For a PolarDB for MySQL cluster, this parameter is required, and only one connection string in each endpoint can enable the ssl, for other notes, see [Configure SSL encryption](https://www.alibabacloud.com/help/doc-detail/153182.htm).\
            For a PolarDB for PostgreSQL cluster or a PolarDB-O cluster, this parameter is not required, by default, SSL encryption is enabled for all endpoints.

        ## Import

        PolarDB endpoint can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:polardb/endpoint:Endpoint example pc-abc123456:pe-abc123456
        ```

        :param str resource_name: The name of the resource.
        :param EndpointArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EndpointArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_add_new_nodes: Optional[pulumi.Input[str]] = None,
                 db_cluster_id: Optional[pulumi.Input[str]] = None,
                 endpoint_config: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 endpoint_type: Optional[pulumi.Input[str]] = None,
                 net_type: Optional[pulumi.Input[str]] = None,
                 nodes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 read_write_mode: Optional[pulumi.Input[str]] = None,
                 ssl_auto_rotate: Optional[pulumi.Input[str]] = None,
                 ssl_enabled: Optional[pulumi.Input[str]] = None,
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
            __props__ = EndpointArgs.__new__(EndpointArgs)

            __props__.__dict__["auto_add_new_nodes"] = auto_add_new_nodes
            if db_cluster_id is None and not opts.urn:
                raise TypeError("Missing required property 'db_cluster_id'")
            __props__.__dict__["db_cluster_id"] = db_cluster_id
            __props__.__dict__["endpoint_config"] = endpoint_config
            __props__.__dict__["endpoint_type"] = endpoint_type
            __props__.__dict__["net_type"] = net_type
            __props__.__dict__["nodes"] = nodes
            __props__.__dict__["read_write_mode"] = read_write_mode
            __props__.__dict__["ssl_auto_rotate"] = ssl_auto_rotate
            __props__.__dict__["ssl_enabled"] = ssl_enabled
            __props__.__dict__["ssl_certificate_url"] = None
            __props__.__dict__["ssl_connection_string"] = None
            __props__.__dict__["ssl_expire_time"] = None
        super(Endpoint, __self__).__init__(
            'alicloud:polardb/endpoint:Endpoint',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            auto_add_new_nodes: Optional[pulumi.Input[str]] = None,
            db_cluster_id: Optional[pulumi.Input[str]] = None,
            endpoint_config: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            endpoint_type: Optional[pulumi.Input[str]] = None,
            net_type: Optional[pulumi.Input[str]] = None,
            nodes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            read_write_mode: Optional[pulumi.Input[str]] = None,
            ssl_auto_rotate: Optional[pulumi.Input[str]] = None,
            ssl_certificate_url: Optional[pulumi.Input[str]] = None,
            ssl_connection_string: Optional[pulumi.Input[str]] = None,
            ssl_enabled: Optional[pulumi.Input[str]] = None,
            ssl_expire_time: Optional[pulumi.Input[str]] = None) -> 'Endpoint':
        """
        Get an existing Endpoint resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] endpoint_type: Type of endpoint.
        :param pulumi.Input[str] ssl_connection_string: (Available in v1.121.0+) The SSL connection string.
        :param pulumi.Input[str] ssl_expire_time: (Available in v1.121.0+) The time when the SSL certificate expires. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _EndpointState.__new__(_EndpointState)

        __props__.__dict__["auto_add_new_nodes"] = auto_add_new_nodes
        __props__.__dict__["db_cluster_id"] = db_cluster_id
        __props__.__dict__["endpoint_config"] = endpoint_config
        __props__.__dict__["endpoint_type"] = endpoint_type
        __props__.__dict__["net_type"] = net_type
        __props__.__dict__["nodes"] = nodes
        __props__.__dict__["read_write_mode"] = read_write_mode
        __props__.__dict__["ssl_auto_rotate"] = ssl_auto_rotate
        __props__.__dict__["ssl_certificate_url"] = ssl_certificate_url
        __props__.__dict__["ssl_connection_string"] = ssl_connection_string
        __props__.__dict__["ssl_enabled"] = ssl_enabled
        __props__.__dict__["ssl_expire_time"] = ssl_expire_time
        return Endpoint(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="autoAddNewNodes")
    def auto_add_new_nodes(self) -> pulumi.Output[str]:
        return pulumi.get(self, "auto_add_new_nodes")

    @property
    @pulumi.getter(name="dbClusterId")
    def db_cluster_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "db_cluster_id")

    @property
    @pulumi.getter(name="endpointConfig")
    def endpoint_config(self) -> pulumi.Output[Mapping[str, Any]]:
        return pulumi.get(self, "endpoint_config")

    @property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Output[Optional[str]]:
        """
        Type of endpoint.
        """
        return pulumi.get(self, "endpoint_type")

    @property
    @pulumi.getter(name="netType")
    def net_type(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "net_type")

    @property
    @pulumi.getter
    def nodes(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "nodes")

    @property
    @pulumi.getter(name="readWriteMode")
    def read_write_mode(self) -> pulumi.Output[str]:
        return pulumi.get(self, "read_write_mode")

    @property
    @pulumi.getter(name="sslAutoRotate")
    def ssl_auto_rotate(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "ssl_auto_rotate")

    @property
    @pulumi.getter(name="sslCertificateUrl")
    def ssl_certificate_url(self) -> pulumi.Output[str]:
        return pulumi.get(self, "ssl_certificate_url")

    @property
    @pulumi.getter(name="sslConnectionString")
    def ssl_connection_string(self) -> pulumi.Output[str]:
        """
        (Available in v1.121.0+) The SSL connection string.
        """
        return pulumi.get(self, "ssl_connection_string")

    @property
    @pulumi.getter(name="sslEnabled")
    def ssl_enabled(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "ssl_enabled")

    @property
    @pulumi.getter(name="sslExpireTime")
    def ssl_expire_time(self) -> pulumi.Output[str]:
        """
        (Available in v1.121.0+) The time when the SSL certificate expires. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        """
        return pulumi.get(self, "ssl_expire_time")

