# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ControlPolicyArgs', 'ControlPolicy']

@pulumi.input_type
class ControlPolicyArgs:
    def __init__(__self__, *,
                 control_policy_name: pulumi.Input[str],
                 effect_scope: pulumi.Input[str],
                 policy_document: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ControlPolicy resource.
        :param pulumi.Input[str] control_policy_name: The name of control policy.
        :param pulumi.Input[str] effect_scope: The effect scope. Valid values `RAM`.
        :param pulumi.Input[str] policy_document: The policy document of control policy.
        :param pulumi.Input[str] description: The description of control policy.
        """
        pulumi.set(__self__, "control_policy_name", control_policy_name)
        pulumi.set(__self__, "effect_scope", effect_scope)
        pulumi.set(__self__, "policy_document", policy_document)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter(name="controlPolicyName")
    def control_policy_name(self) -> pulumi.Input[str]:
        """
        The name of control policy.
        """
        return pulumi.get(self, "control_policy_name")

    @control_policy_name.setter
    def control_policy_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "control_policy_name", value)

    @property
    @pulumi.getter(name="effectScope")
    def effect_scope(self) -> pulumi.Input[str]:
        """
        The effect scope. Valid values `RAM`.
        """
        return pulumi.get(self, "effect_scope")

    @effect_scope.setter
    def effect_scope(self, value: pulumi.Input[str]):
        pulumi.set(self, "effect_scope", value)

    @property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> pulumi.Input[str]:
        """
        The policy document of control policy.
        """
        return pulumi.get(self, "policy_document")

    @policy_document.setter
    def policy_document(self, value: pulumi.Input[str]):
        pulumi.set(self, "policy_document", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of control policy.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


@pulumi.input_type
class _ControlPolicyState:
    def __init__(__self__, *,
                 control_policy_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 effect_scope: Optional[pulumi.Input[str]] = None,
                 policy_document: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ControlPolicy resources.
        :param pulumi.Input[str] control_policy_name: The name of control policy.
        :param pulumi.Input[str] description: The description of control policy.
        :param pulumi.Input[str] effect_scope: The effect scope. Valid values `RAM`.
        :param pulumi.Input[str] policy_document: The policy document of control policy.
        """
        if control_policy_name is not None:
            pulumi.set(__self__, "control_policy_name", control_policy_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if effect_scope is not None:
            pulumi.set(__self__, "effect_scope", effect_scope)
        if policy_document is not None:
            pulumi.set(__self__, "policy_document", policy_document)

    @property
    @pulumi.getter(name="controlPolicyName")
    def control_policy_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of control policy.
        """
        return pulumi.get(self, "control_policy_name")

    @control_policy_name.setter
    def control_policy_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "control_policy_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of control policy.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="effectScope")
    def effect_scope(self) -> Optional[pulumi.Input[str]]:
        """
        The effect scope. Valid values `RAM`.
        """
        return pulumi.get(self, "effect_scope")

    @effect_scope.setter
    def effect_scope(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "effect_scope", value)

    @property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> Optional[pulumi.Input[str]]:
        """
        The policy document of control policy.
        """
        return pulumi.get(self, "policy_document")

    @policy_document.setter
    def policy_document(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_document", value)


class ControlPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 control_policy_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 effect_scope: Optional[pulumi.Input[str]] = None,
                 policy_document: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Resource Manager Control Policy resource.

        For information about Resource Manager Control Policy and how to use it, see [What is Control Policy](https://help.aliyun.com/document_detail/208287.html).

        > **NOTE:** Available in v1.120.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        example = alicloud.resourcemanager.ControlPolicy("example",
            control_policy_name="tf-testAccRDControlPolicy",
            description="tf-testAccRDControlPolicy",
            effect_scope="RAM",
            policy_document=\"\"\"  {
            "Version": "1",
            "Statement": [
              {
                "Effect": "Deny",
                "Action": [
                  "ram:UpdateRole",
                  "ram:DeleteRole",
                  "ram:AttachPolicyToRole",
                  "ram:DetachPolicyFromRole"
                ],
                "Resource": "acs:ram:*:*:role/ResourceDirectoryAccountAccessRole"
              }
            ]
          }
          
        \"\"\")
        ```

        ## Import

        Resource Manager Control Policy can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:resourcemanager/controlPolicy:ControlPolicy example <id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] control_policy_name: The name of control policy.
        :param pulumi.Input[str] description: The description of control policy.
        :param pulumi.Input[str] effect_scope: The effect scope. Valid values `RAM`.
        :param pulumi.Input[str] policy_document: The policy document of control policy.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ControlPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Resource Manager Control Policy resource.

        For information about Resource Manager Control Policy and how to use it, see [What is Control Policy](https://help.aliyun.com/document_detail/208287.html).

        > **NOTE:** Available in v1.120.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        example = alicloud.resourcemanager.ControlPolicy("example",
            control_policy_name="tf-testAccRDControlPolicy",
            description="tf-testAccRDControlPolicy",
            effect_scope="RAM",
            policy_document=\"\"\"  {
            "Version": "1",
            "Statement": [
              {
                "Effect": "Deny",
                "Action": [
                  "ram:UpdateRole",
                  "ram:DeleteRole",
                  "ram:AttachPolicyToRole",
                  "ram:DetachPolicyFromRole"
                ],
                "Resource": "acs:ram:*:*:role/ResourceDirectoryAccountAccessRole"
              }
            ]
          }
          
        \"\"\")
        ```

        ## Import

        Resource Manager Control Policy can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:resourcemanager/controlPolicy:ControlPolicy example <id>
        ```

        :param str resource_name: The name of the resource.
        :param ControlPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ControlPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 control_policy_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 effect_scope: Optional[pulumi.Input[str]] = None,
                 policy_document: Optional[pulumi.Input[str]] = None,
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
            __props__ = ControlPolicyArgs.__new__(ControlPolicyArgs)

            if control_policy_name is None and not opts.urn:
                raise TypeError("Missing required property 'control_policy_name'")
            __props__.__dict__["control_policy_name"] = control_policy_name
            __props__.__dict__["description"] = description
            if effect_scope is None and not opts.urn:
                raise TypeError("Missing required property 'effect_scope'")
            __props__.__dict__["effect_scope"] = effect_scope
            if policy_document is None and not opts.urn:
                raise TypeError("Missing required property 'policy_document'")
            __props__.__dict__["policy_document"] = policy_document
        super(ControlPolicy, __self__).__init__(
            'alicloud:resourcemanager/controlPolicy:ControlPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            control_policy_name: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            effect_scope: Optional[pulumi.Input[str]] = None,
            policy_document: Optional[pulumi.Input[str]] = None) -> 'ControlPolicy':
        """
        Get an existing ControlPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] control_policy_name: The name of control policy.
        :param pulumi.Input[str] description: The description of control policy.
        :param pulumi.Input[str] effect_scope: The effect scope. Valid values `RAM`.
        :param pulumi.Input[str] policy_document: The policy document of control policy.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ControlPolicyState.__new__(_ControlPolicyState)

        __props__.__dict__["control_policy_name"] = control_policy_name
        __props__.__dict__["description"] = description
        __props__.__dict__["effect_scope"] = effect_scope
        __props__.__dict__["policy_document"] = policy_document
        return ControlPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="controlPolicyName")
    def control_policy_name(self) -> pulumi.Output[str]:
        """
        The name of control policy.
        """
        return pulumi.get(self, "control_policy_name")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of control policy.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="effectScope")
    def effect_scope(self) -> pulumi.Output[str]:
        """
        The effect scope. Valid values `RAM`.
        """
        return pulumi.get(self, "effect_scope")

    @property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> pulumi.Output[str]:
        """
        The policy document of control policy.
        """
        return pulumi.get(self, "policy_document")

