# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['FieldExtractionRuleArgs', 'FieldExtractionRule']

@pulumi.input_type
class FieldExtractionRuleArgs:
    def __init__(__self__, *,
                 enabled: pulumi.Input[bool],
                 parse_expression: pulumi.Input[str],
                 scope: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a FieldExtractionRule resource.
        :param pulumi.Input[bool] enabled: Is the field extraction rule enabled.
        :param pulumi.Input[str] parse_expression: Describes the fields to be parsed.
        :param pulumi.Input[str] scope: Scope of the field extraction rule. This could be a sourceCategory, sourceHost, or any other metadata that describes the data you want to extract from. Think of the Scope as the first portion of an ad hoc search, before the first pipe ( | ). You'll use the Scope to run a search against the rule.
        :param pulumi.Input[str] name: Name of the field extraction rule. Use a name that makes it easy to identify the rule.
        """
        pulumi.set(__self__, "enabled", enabled)
        pulumi.set(__self__, "parse_expression", parse_expression)
        pulumi.set(__self__, "scope", scope)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[bool]:
        """
        Is the field extraction rule enabled.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="parseExpression")
    def parse_expression(self) -> pulumi.Input[str]:
        """
        Describes the fields to be parsed.
        """
        return pulumi.get(self, "parse_expression")

    @parse_expression.setter
    def parse_expression(self, value: pulumi.Input[str]):
        pulumi.set(self, "parse_expression", value)

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Input[str]:
        """
        Scope of the field extraction rule. This could be a sourceCategory, sourceHost, or any other metadata that describes the data you want to extract from. Think of the Scope as the first portion of an ad hoc search, before the first pipe ( | ). You'll use the Scope to run a search against the rule.
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: pulumi.Input[str]):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the field extraction rule. Use a name that makes it easy to identify the rule.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _FieldExtractionRuleState:
    def __init__(__self__, *,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parse_expression: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering FieldExtractionRule resources.
        :param pulumi.Input[bool] enabled: Is the field extraction rule enabled.
        :param pulumi.Input[str] name: Name of the field extraction rule. Use a name that makes it easy to identify the rule.
        :param pulumi.Input[str] parse_expression: Describes the fields to be parsed.
        :param pulumi.Input[str] scope: Scope of the field extraction rule. This could be a sourceCategory, sourceHost, or any other metadata that describes the data you want to extract from. Think of the Scope as the first portion of an ad hoc search, before the first pipe ( | ). You'll use the Scope to run a search against the rule.
        """
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if parse_expression is not None:
            pulumi.set(__self__, "parse_expression", parse_expression)
        if scope is not None:
            pulumi.set(__self__, "scope", scope)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Is the field extraction rule enabled.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the field extraction rule. Use a name that makes it easy to identify the rule.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="parseExpression")
    def parse_expression(self) -> Optional[pulumi.Input[str]]:
        """
        Describes the fields to be parsed.
        """
        return pulumi.get(self, "parse_expression")

    @parse_expression.setter
    def parse_expression(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parse_expression", value)

    @property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[str]]:
        """
        Scope of the field extraction rule. This could be a sourceCategory, sourceHost, or any other metadata that describes the data you want to extract from. Think of the Scope as the first portion of an ad hoc search, before the first pipe ( | ). You'll use the Scope to run a search against the rule.
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scope", value)


class FieldExtractionRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parse_expression: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a [Sumologic Field Extraction Rule](https://help.sumologic.com/Manage/Field-Extractions).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sumologic as sumologic

        field_extraction_rule = sumologic.FieldExtractionRule("fieldExtractionRule",
            enabled=True,
            parse_expression="csv _raw extract 1 as f1",
            scope="_sourceHost=127.0.0.1")
        ```
        ## Attributes reference

        The following attributes are exported:

        - `id` - Unique identifier for the field extraction rule.

        ## Import

        Extraction Rules can be imported using the extraction rule id, e.g.hcl

        ```sh
         $ pulumi import sumologic:index/fieldExtractionRule:FieldExtractionRule fieldExtractionRule id
        ```

         [1]https://help.sumologic.com/Manage/Field-Extractions

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enabled: Is the field extraction rule enabled.
        :param pulumi.Input[str] name: Name of the field extraction rule. Use a name that makes it easy to identify the rule.
        :param pulumi.Input[str] parse_expression: Describes the fields to be parsed.
        :param pulumi.Input[str] scope: Scope of the field extraction rule. This could be a sourceCategory, sourceHost, or any other metadata that describes the data you want to extract from. Think of the Scope as the first portion of an ad hoc search, before the first pipe ( | ). You'll use the Scope to run a search against the rule.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FieldExtractionRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a [Sumologic Field Extraction Rule](https://help.sumologic.com/Manage/Field-Extractions).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sumologic as sumologic

        field_extraction_rule = sumologic.FieldExtractionRule("fieldExtractionRule",
            enabled=True,
            parse_expression="csv _raw extract 1 as f1",
            scope="_sourceHost=127.0.0.1")
        ```
        ## Attributes reference

        The following attributes are exported:

        - `id` - Unique identifier for the field extraction rule.

        ## Import

        Extraction Rules can be imported using the extraction rule id, e.g.hcl

        ```sh
         $ pulumi import sumologic:index/fieldExtractionRule:FieldExtractionRule fieldExtractionRule id
        ```

         [1]https://help.sumologic.com/Manage/Field-Extractions

        :param str resource_name: The name of the resource.
        :param FieldExtractionRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FieldExtractionRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parse_expression: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
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
            __props__ = FieldExtractionRuleArgs.__new__(FieldExtractionRuleArgs)

            if enabled is None and not opts.urn:
                raise TypeError("Missing required property 'enabled'")
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["name"] = name
            if parse_expression is None and not opts.urn:
                raise TypeError("Missing required property 'parse_expression'")
            __props__.__dict__["parse_expression"] = parse_expression
            if scope is None and not opts.urn:
                raise TypeError("Missing required property 'scope'")
            __props__.__dict__["scope"] = scope
        super(FieldExtractionRule, __self__).__init__(
            'sumologic:index/fieldExtractionRule:FieldExtractionRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            parse_expression: Optional[pulumi.Input[str]] = None,
            scope: Optional[pulumi.Input[str]] = None) -> 'FieldExtractionRule':
        """
        Get an existing FieldExtractionRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enabled: Is the field extraction rule enabled.
        :param pulumi.Input[str] name: Name of the field extraction rule. Use a name that makes it easy to identify the rule.
        :param pulumi.Input[str] parse_expression: Describes the fields to be parsed.
        :param pulumi.Input[str] scope: Scope of the field extraction rule. This could be a sourceCategory, sourceHost, or any other metadata that describes the data you want to extract from. Think of the Scope as the first portion of an ad hoc search, before the first pipe ( | ). You'll use the Scope to run a search against the rule.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _FieldExtractionRuleState.__new__(_FieldExtractionRuleState)

        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["name"] = name
        __props__.__dict__["parse_expression"] = parse_expression
        __props__.__dict__["scope"] = scope
        return FieldExtractionRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[bool]:
        """
        Is the field extraction rule enabled.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the field extraction rule. Use a name that makes it easy to identify the rule.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="parseExpression")
    def parse_expression(self) -> pulumi.Output[str]:
        """
        Describes the fields to be parsed.
        """
        return pulumi.get(self, "parse_expression")

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Output[str]:
        """
        Scope of the field extraction rule. This could be a sourceCategory, sourceHost, or any other metadata that describes the data you want to extract from. Think of the Scope as the first portion of an ad hoc search, before the first pipe ( | ). You'll use the Scope to run a search against the rule.
        """
        return pulumi.get(self, "scope")

