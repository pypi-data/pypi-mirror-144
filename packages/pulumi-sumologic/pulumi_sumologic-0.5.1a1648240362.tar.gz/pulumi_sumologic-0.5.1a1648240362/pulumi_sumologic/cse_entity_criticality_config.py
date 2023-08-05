# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['CseEntityCriticalityConfigArgs', 'CseEntityCriticalityConfig']

@pulumi.input_type
class CseEntityCriticalityConfigArgs:
    def __init__(__self__, *,
                 severity_expression: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a CseEntityCriticalityConfig resource.
        :param pulumi.Input[str] severity_expression: Algebraic expression representing this entity\'s criticality. Examples: "severity * 2", "severity - 5", "severity / 3".
        :param pulumi.Input[str] name: Human friendly and unique name. Examples: "Executive Laptop", "Bastion Host".
        """
        pulumi.set(__self__, "severity_expression", severity_expression)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="severityExpression")
    def severity_expression(self) -> pulumi.Input[str]:
        """
        Algebraic expression representing this entity\'s criticality. Examples: "severity * 2", "severity - 5", "severity / 3".
        """
        return pulumi.get(self, "severity_expression")

    @severity_expression.setter
    def severity_expression(self, value: pulumi.Input[str]):
        pulumi.set(self, "severity_expression", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Human friendly and unique name. Examples: "Executive Laptop", "Bastion Host".
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _CseEntityCriticalityConfigState:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 severity_expression: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering CseEntityCriticalityConfig resources.
        :param pulumi.Input[str] name: Human friendly and unique name. Examples: "Executive Laptop", "Bastion Host".
        :param pulumi.Input[str] severity_expression: Algebraic expression representing this entity\'s criticality. Examples: "severity * 2", "severity - 5", "severity / 3".
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if severity_expression is not None:
            pulumi.set(__self__, "severity_expression", severity_expression)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Human friendly and unique name. Examples: "Executive Laptop", "Bastion Host".
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="severityExpression")
    def severity_expression(self) -> Optional[pulumi.Input[str]]:
        """
        Algebraic expression representing this entity\'s criticality. Examples: "severity * 2", "severity - 5", "severity / 3".
        """
        return pulumi.get(self, "severity_expression")

    @severity_expression.setter
    def severity_expression(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "severity_expression", value)


class CseEntityCriticalityConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 severity_expression: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Sumologic CSE Entity Criticality Configuration.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sumologic as sumologic

        entity_criticality_config = sumologic.CseEntityCriticalityConfig("entityCriticalityConfig", severity_expression="severity + 2")
        ```

        ## Import

        Entity criticality configuration can be imported using the field id, e.g.hcl

        ```sh
         $ pulumi import sumologic:index/cseEntityCriticalityConfig:CseEntityCriticalityConfig entity_criticality_config id
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: Human friendly and unique name. Examples: "Executive Laptop", "Bastion Host".
        :param pulumi.Input[str] severity_expression: Algebraic expression representing this entity\'s criticality. Examples: "severity * 2", "severity - 5", "severity / 3".
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CseEntityCriticalityConfigArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Sumologic CSE Entity Criticality Configuration.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sumologic as sumologic

        entity_criticality_config = sumologic.CseEntityCriticalityConfig("entityCriticalityConfig", severity_expression="severity + 2")
        ```

        ## Import

        Entity criticality configuration can be imported using the field id, e.g.hcl

        ```sh
         $ pulumi import sumologic:index/cseEntityCriticalityConfig:CseEntityCriticalityConfig entity_criticality_config id
        ```

        :param str resource_name: The name of the resource.
        :param CseEntityCriticalityConfigArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CseEntityCriticalityConfigArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 severity_expression: Optional[pulumi.Input[str]] = None,
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
            __props__ = CseEntityCriticalityConfigArgs.__new__(CseEntityCriticalityConfigArgs)

            __props__.__dict__["name"] = name
            if severity_expression is None and not opts.urn:
                raise TypeError("Missing required property 'severity_expression'")
            __props__.__dict__["severity_expression"] = severity_expression
        super(CseEntityCriticalityConfig, __self__).__init__(
            'sumologic:index/cseEntityCriticalityConfig:CseEntityCriticalityConfig',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            name: Optional[pulumi.Input[str]] = None,
            severity_expression: Optional[pulumi.Input[str]] = None) -> 'CseEntityCriticalityConfig':
        """
        Get an existing CseEntityCriticalityConfig resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: Human friendly and unique name. Examples: "Executive Laptop", "Bastion Host".
        :param pulumi.Input[str] severity_expression: Algebraic expression representing this entity\'s criticality. Examples: "severity * 2", "severity - 5", "severity / 3".
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CseEntityCriticalityConfigState.__new__(_CseEntityCriticalityConfigState)

        __props__.__dict__["name"] = name
        __props__.__dict__["severity_expression"] = severity_expression
        return CseEntityCriticalityConfig(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Human friendly and unique name. Examples: "Executive Laptop", "Bastion Host".
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="severityExpression")
    def severity_expression(self) -> pulumi.Output[str]:
        """
        Algebraic expression representing this entity\'s criticality. Examples: "severity * 2", "severity - 5", "severity / 3".
        """
        return pulumi.get(self, "severity_expression")

