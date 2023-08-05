# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ExpressSyncArgs', 'ExpressSync']

@pulumi.input_type
class ExpressSyncArgs:
    def __init__(__self__, *,
                 bucket_name: pulumi.Input[str],
                 bucket_region: pulumi.Input[str],
                 express_sync_name: pulumi.Input[str],
                 bucket_prefix: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ExpressSync resource.
        :param pulumi.Input[str] bucket_name: The name of the OSS Bucket.
        :param pulumi.Input[str] bucket_region: The region of the OSS Bucket.
        :param pulumi.Input[str] express_sync_name: The name of the ExpressSync. The length of the name is limited to `1` to `128` characters. It can contain uppercase and lowercase letters, Chinese characters, numbers, English periods (.), underscores (_), or hyphens (-), and must start with  letters.
        :param pulumi.Input[str] bucket_prefix: The prefix of the OSS Bucket.
        :param pulumi.Input[str] description: The description of the Express Sync. The length of the name is limited to `1` to `255` characters.
        """
        pulumi.set(__self__, "bucket_name", bucket_name)
        pulumi.set(__self__, "bucket_region", bucket_region)
        pulumi.set(__self__, "express_sync_name", express_sync_name)
        if bucket_prefix is not None:
            pulumi.set(__self__, "bucket_prefix", bucket_prefix)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[str]:
        """
        The name of the OSS Bucket.
        """
        return pulumi.get(self, "bucket_name")

    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "bucket_name", value)

    @property
    @pulumi.getter(name="bucketRegion")
    def bucket_region(self) -> pulumi.Input[str]:
        """
        The region of the OSS Bucket.
        """
        return pulumi.get(self, "bucket_region")

    @bucket_region.setter
    def bucket_region(self, value: pulumi.Input[str]):
        pulumi.set(self, "bucket_region", value)

    @property
    @pulumi.getter(name="expressSyncName")
    def express_sync_name(self) -> pulumi.Input[str]:
        """
        The name of the ExpressSync. The length of the name is limited to `1` to `128` characters. It can contain uppercase and lowercase letters, Chinese characters, numbers, English periods (.), underscores (_), or hyphens (-), and must start with  letters.
        """
        return pulumi.get(self, "express_sync_name")

    @express_sync_name.setter
    def express_sync_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "express_sync_name", value)

    @property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        The prefix of the OSS Bucket.
        """
        return pulumi.get(self, "bucket_prefix")

    @bucket_prefix.setter
    def bucket_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bucket_prefix", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the Express Sync. The length of the name is limited to `1` to `255` characters.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


@pulumi.input_type
class _ExpressSyncState:
    def __init__(__self__, *,
                 bucket_name: Optional[pulumi.Input[str]] = None,
                 bucket_prefix: Optional[pulumi.Input[str]] = None,
                 bucket_region: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 express_sync_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ExpressSync resources.
        :param pulumi.Input[str] bucket_name: The name of the OSS Bucket.
        :param pulumi.Input[str] bucket_prefix: The prefix of the OSS Bucket.
        :param pulumi.Input[str] bucket_region: The region of the OSS Bucket.
        :param pulumi.Input[str] description: The description of the Express Sync. The length of the name is limited to `1` to `255` characters.
        :param pulumi.Input[str] express_sync_name: The name of the ExpressSync. The length of the name is limited to `1` to `128` characters. It can contain uppercase and lowercase letters, Chinese characters, numbers, English periods (.), underscores (_), or hyphens (-), and must start with  letters.
        """
        if bucket_name is not None:
            pulumi.set(__self__, "bucket_name", bucket_name)
        if bucket_prefix is not None:
            pulumi.set(__self__, "bucket_prefix", bucket_prefix)
        if bucket_region is not None:
            pulumi.set(__self__, "bucket_region", bucket_region)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if express_sync_name is not None:
            pulumi.set(__self__, "express_sync_name", express_sync_name)

    @property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the OSS Bucket.
        """
        return pulumi.get(self, "bucket_name")

    @bucket_name.setter
    def bucket_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bucket_name", value)

    @property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        The prefix of the OSS Bucket.
        """
        return pulumi.get(self, "bucket_prefix")

    @bucket_prefix.setter
    def bucket_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bucket_prefix", value)

    @property
    @pulumi.getter(name="bucketRegion")
    def bucket_region(self) -> Optional[pulumi.Input[str]]:
        """
        The region of the OSS Bucket.
        """
        return pulumi.get(self, "bucket_region")

    @bucket_region.setter
    def bucket_region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bucket_region", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the Express Sync. The length of the name is limited to `1` to `255` characters.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="expressSyncName")
    def express_sync_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the ExpressSync. The length of the name is limited to `1` to `128` characters. It can contain uppercase and lowercase letters, Chinese characters, numbers, English periods (.), underscores (_), or hyphens (-), and must start with  letters.
        """
        return pulumi.get(self, "express_sync_name")

    @express_sync_name.setter
    def express_sync_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "express_sync_name", value)


class ExpressSync(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket_name: Optional[pulumi.Input[str]] = None,
                 bucket_prefix: Optional[pulumi.Input[str]] = None,
                 bucket_region: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 express_sync_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Cloud Storage Gateway Express Sync resource.

        For information about Cloud Storage Gateway Express Sync and how to use it, see [What is Express Sync](https://www.alibabacloud.com/help/en/doc-detail/53972.htm).

        > **NOTE:** Available in v1.144.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "tftest"
        region = config.get("region")
        if region is None:
            region = "cn-shanghai"
        default_stocks = alicloud.cloudstoragegateway.get_stocks(gateway_class="Standard")
        vpc = alicloud.vpc.Network("vpc",
            vpc_name=name,
            cidr_block="172.16.0.0/12")
        default_switch = alicloud.vpc.Switch("defaultSwitch",
            vpc_id=vpc.id,
            cidr_block="172.16.0.0/21",
            zone_id=default_stocks.stocks[0].zone_id,
            vswitch_name=name)
        default_storage_bundle = alicloud.cloudstoragegateway.StorageBundle("defaultStorageBundle", storage_bundle_name=name)
        default_gateway = alicloud.cloudstoragegateway.Gateway("defaultGateway",
            description="tf-acctestDesalone",
            gateway_class="Standard",
            type="File",
            payment_type="PayAsYouGo",
            vswitch_id=default_switch.id,
            release_after_expiration=True,
            public_network_bandwidth=10,
            storage_bundle_id=default_storage_bundle.id,
            location="Cloud",
            gateway_name=name)
        default_gateway_cache_disk = alicloud.cloudstoragegateway.GatewayCacheDisk("defaultGatewayCacheDisk",
            cache_disk_category="cloud_efficiency",
            gateway_id=default_gateway.id,
            cache_disk_size_in_gb=50)
        default_bucket = alicloud.oss.Bucket("defaultBucket",
            bucket=name,
            acl="public-read-write")
        default_gateway_file_share = alicloud.cloudstoragegateway.GatewayFileShare("defaultGatewayFileShare",
            gateway_file_share_name=name,
            gateway_id=default_gateway.id,
            local_path=default_gateway_cache_disk.local_file_path,
            oss_bucket_name=default_bucket.bucket,
            oss_endpoint=default_bucket.extranet_endpoint,
            protocol="NFS",
            remote_sync=True,
            polling_interval=4500,
            fe_limit=0,
            backend_limit=0,
            cache_mode="Cache",
            squash="none",
            lag_period=5)
        default_express_sync = alicloud.cloudstoragegateway.ExpressSync("defaultExpressSync",
            bucket_name=default_gateway_file_share.oss_bucket_name,
            bucket_region=region,
            description=name,
            express_sync_name=name)
        ```

        ## Import

        Cloud Storage Gateway Express Sync can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:cloudstoragegateway/expressSync:ExpressSync example <id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bucket_name: The name of the OSS Bucket.
        :param pulumi.Input[str] bucket_prefix: The prefix of the OSS Bucket.
        :param pulumi.Input[str] bucket_region: The region of the OSS Bucket.
        :param pulumi.Input[str] description: The description of the Express Sync. The length of the name is limited to `1` to `255` characters.
        :param pulumi.Input[str] express_sync_name: The name of the ExpressSync. The length of the name is limited to `1` to `128` characters. It can contain uppercase and lowercase letters, Chinese characters, numbers, English periods (.), underscores (_), or hyphens (-), and must start with  letters.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ExpressSyncArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Cloud Storage Gateway Express Sync resource.

        For information about Cloud Storage Gateway Express Sync and how to use it, see [What is Express Sync](https://www.alibabacloud.com/help/en/doc-detail/53972.htm).

        > **NOTE:** Available in v1.144.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "tftest"
        region = config.get("region")
        if region is None:
            region = "cn-shanghai"
        default_stocks = alicloud.cloudstoragegateway.get_stocks(gateway_class="Standard")
        vpc = alicloud.vpc.Network("vpc",
            vpc_name=name,
            cidr_block="172.16.0.0/12")
        default_switch = alicloud.vpc.Switch("defaultSwitch",
            vpc_id=vpc.id,
            cidr_block="172.16.0.0/21",
            zone_id=default_stocks.stocks[0].zone_id,
            vswitch_name=name)
        default_storage_bundle = alicloud.cloudstoragegateway.StorageBundle("defaultStorageBundle", storage_bundle_name=name)
        default_gateway = alicloud.cloudstoragegateway.Gateway("defaultGateway",
            description="tf-acctestDesalone",
            gateway_class="Standard",
            type="File",
            payment_type="PayAsYouGo",
            vswitch_id=default_switch.id,
            release_after_expiration=True,
            public_network_bandwidth=10,
            storage_bundle_id=default_storage_bundle.id,
            location="Cloud",
            gateway_name=name)
        default_gateway_cache_disk = alicloud.cloudstoragegateway.GatewayCacheDisk("defaultGatewayCacheDisk",
            cache_disk_category="cloud_efficiency",
            gateway_id=default_gateway.id,
            cache_disk_size_in_gb=50)
        default_bucket = alicloud.oss.Bucket("defaultBucket",
            bucket=name,
            acl="public-read-write")
        default_gateway_file_share = alicloud.cloudstoragegateway.GatewayFileShare("defaultGatewayFileShare",
            gateway_file_share_name=name,
            gateway_id=default_gateway.id,
            local_path=default_gateway_cache_disk.local_file_path,
            oss_bucket_name=default_bucket.bucket,
            oss_endpoint=default_bucket.extranet_endpoint,
            protocol="NFS",
            remote_sync=True,
            polling_interval=4500,
            fe_limit=0,
            backend_limit=0,
            cache_mode="Cache",
            squash="none",
            lag_period=5)
        default_express_sync = alicloud.cloudstoragegateway.ExpressSync("defaultExpressSync",
            bucket_name=default_gateway_file_share.oss_bucket_name,
            bucket_region=region,
            description=name,
            express_sync_name=name)
        ```

        ## Import

        Cloud Storage Gateway Express Sync can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:cloudstoragegateway/expressSync:ExpressSync example <id>
        ```

        :param str resource_name: The name of the resource.
        :param ExpressSyncArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ExpressSyncArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket_name: Optional[pulumi.Input[str]] = None,
                 bucket_prefix: Optional[pulumi.Input[str]] = None,
                 bucket_region: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 express_sync_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = ExpressSyncArgs.__new__(ExpressSyncArgs)

            if bucket_name is None and not opts.urn:
                raise TypeError("Missing required property 'bucket_name'")
            __props__.__dict__["bucket_name"] = bucket_name
            __props__.__dict__["bucket_prefix"] = bucket_prefix
            if bucket_region is None and not opts.urn:
                raise TypeError("Missing required property 'bucket_region'")
            __props__.__dict__["bucket_region"] = bucket_region
            __props__.__dict__["description"] = description
            if express_sync_name is None and not opts.urn:
                raise TypeError("Missing required property 'express_sync_name'")
            __props__.__dict__["express_sync_name"] = express_sync_name
        super(ExpressSync, __self__).__init__(
            'alicloud:cloudstoragegateway/expressSync:ExpressSync',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            bucket_name: Optional[pulumi.Input[str]] = None,
            bucket_prefix: Optional[pulumi.Input[str]] = None,
            bucket_region: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            express_sync_name: Optional[pulumi.Input[str]] = None) -> 'ExpressSync':
        """
        Get an existing ExpressSync resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bucket_name: The name of the OSS Bucket.
        :param pulumi.Input[str] bucket_prefix: The prefix of the OSS Bucket.
        :param pulumi.Input[str] bucket_region: The region of the OSS Bucket.
        :param pulumi.Input[str] description: The description of the Express Sync. The length of the name is limited to `1` to `255` characters.
        :param pulumi.Input[str] express_sync_name: The name of the ExpressSync. The length of the name is limited to `1` to `128` characters. It can contain uppercase and lowercase letters, Chinese characters, numbers, English periods (.), underscores (_), or hyphens (-), and must start with  letters.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ExpressSyncState.__new__(_ExpressSyncState)

        __props__.__dict__["bucket_name"] = bucket_name
        __props__.__dict__["bucket_prefix"] = bucket_prefix
        __props__.__dict__["bucket_region"] = bucket_region
        __props__.__dict__["description"] = description
        __props__.__dict__["express_sync_name"] = express_sync_name
        return ExpressSync(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Output[str]:
        """
        The name of the OSS Bucket.
        """
        return pulumi.get(self, "bucket_name")

    @property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> pulumi.Output[Optional[str]]:
        """
        The prefix of the OSS Bucket.
        """
        return pulumi.get(self, "bucket_prefix")

    @property
    @pulumi.getter(name="bucketRegion")
    def bucket_region(self) -> pulumi.Output[str]:
        """
        The region of the OSS Bucket.
        """
        return pulumi.get(self, "bucket_region")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the Express Sync. The length of the name is limited to `1` to `255` characters.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="expressSyncName")
    def express_sync_name(self) -> pulumi.Output[str]:
        """
        The name of the ExpressSync. The length of the name is limited to `1` to `128` characters. It can contain uppercase and lowercase letters, Chinese characters, numbers, English periods (.), underscores (_), or hyphens (-), and must start with  letters.
        """
        return pulumi.get(self, "express_sync_name")

