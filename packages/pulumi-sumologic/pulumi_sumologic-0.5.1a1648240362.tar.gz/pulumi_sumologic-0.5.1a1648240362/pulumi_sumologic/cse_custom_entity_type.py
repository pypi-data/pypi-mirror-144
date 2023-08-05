# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['CseCustomEntityTypeArgs', 'CseCustomEntityType']

@pulumi.input_type
class CseCustomEntityTypeArgs:
    def __init__(__self__, *,
                 fields: pulumi.Input[Sequence[pulumi.Input[str]]],
                 identifier: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a CseCustomEntityType resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] fields: Record schema fields. Examples: "file_hash_md5", "file_hash_sha1".".
        :param pulumi.Input[str] identifier: Machine friendly and unique identifier. Example: "filehash".
        :param pulumi.Input[str] name: Human friend and unique name. Example: "File Hash".
        """
        pulumi.set(__self__, "fields", fields)
        pulumi.set(__self__, "identifier", identifier)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def fields(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        Record schema fields. Examples: "file_hash_md5", "file_hash_sha1".".
        """
        return pulumi.get(self, "fields")

    @fields.setter
    def fields(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "fields", value)

    @property
    @pulumi.getter
    def identifier(self) -> pulumi.Input[str]:
        """
        Machine friendly and unique identifier. Example: "filehash".
        """
        return pulumi.get(self, "identifier")

    @identifier.setter
    def identifier(self, value: pulumi.Input[str]):
        pulumi.set(self, "identifier", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Human friend and unique name. Example: "File Hash".
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _CseCustomEntityTypeState:
    def __init__(__self__, *,
                 fields: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 identifier: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering CseCustomEntityType resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] fields: Record schema fields. Examples: "file_hash_md5", "file_hash_sha1".".
        :param pulumi.Input[str] identifier: Machine friendly and unique identifier. Example: "filehash".
        :param pulumi.Input[str] name: Human friend and unique name. Example: "File Hash".
        """
        if fields is not None:
            pulumi.set(__self__, "fields", fields)
        if identifier is not None:
            pulumi.set(__self__, "identifier", identifier)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def fields(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Record schema fields. Examples: "file_hash_md5", "file_hash_sha1".".
        """
        return pulumi.get(self, "fields")

    @fields.setter
    def fields(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "fields", value)

    @property
    @pulumi.getter
    def identifier(self) -> Optional[pulumi.Input[str]]:
        """
        Machine friendly and unique identifier. Example: "filehash".
        """
        return pulumi.get(self, "identifier")

    @identifier.setter
    def identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "identifier", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Human friend and unique name. Example: "File Hash".
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class CseCustomEntityType(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 fields: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 identifier: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Sumologic CSE Custom Entity Type.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sumologic as sumologic

        custom_entity_type = sumologic.CseCustomEntityType("customEntityType",
            fields=[
                "file_hash_md5",
                "file_hash_sha1",
            ],
            identifier="identifier")
        ```

        ## Import

        Custom entity type can be imported using the field id, e.g.hcl

        ```sh
         $ pulumi import sumologic:index/cseCustomEntityType:CseCustomEntityType custom_entity_type id
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] fields: Record schema fields. Examples: "file_hash_md5", "file_hash_sha1".".
        :param pulumi.Input[str] identifier: Machine friendly and unique identifier. Example: "filehash".
        :param pulumi.Input[str] name: Human friend and unique name. Example: "File Hash".
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CseCustomEntityTypeArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Sumologic CSE Custom Entity Type.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sumologic as sumologic

        custom_entity_type = sumologic.CseCustomEntityType("customEntityType",
            fields=[
                "file_hash_md5",
                "file_hash_sha1",
            ],
            identifier="identifier")
        ```

        ## Import

        Custom entity type can be imported using the field id, e.g.hcl

        ```sh
         $ pulumi import sumologic:index/cseCustomEntityType:CseCustomEntityType custom_entity_type id
        ```

        :param str resource_name: The name of the resource.
        :param CseCustomEntityTypeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CseCustomEntityTypeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 fields: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 identifier: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
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
            __props__ = CseCustomEntityTypeArgs.__new__(CseCustomEntityTypeArgs)

            if fields is None and not opts.urn:
                raise TypeError("Missing required property 'fields'")
            __props__.__dict__["fields"] = fields
            if identifier is None and not opts.urn:
                raise TypeError("Missing required property 'identifier'")
            __props__.__dict__["identifier"] = identifier
            __props__.__dict__["name"] = name
        super(CseCustomEntityType, __self__).__init__(
            'sumologic:index/cseCustomEntityType:CseCustomEntityType',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            fields: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            identifier: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None) -> 'CseCustomEntityType':
        """
        Get an existing CseCustomEntityType resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] fields: Record schema fields. Examples: "file_hash_md5", "file_hash_sha1".".
        :param pulumi.Input[str] identifier: Machine friendly and unique identifier. Example: "filehash".
        :param pulumi.Input[str] name: Human friend and unique name. Example: "File Hash".
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CseCustomEntityTypeState.__new__(_CseCustomEntityTypeState)

        __props__.__dict__["fields"] = fields
        __props__.__dict__["identifier"] = identifier
        __props__.__dict__["name"] = name
        return CseCustomEntityType(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def fields(self) -> pulumi.Output[Sequence[str]]:
        """
        Record schema fields. Examples: "file_hash_md5", "file_hash_sha1".".
        """
        return pulumi.get(self, "fields")

    @property
    @pulumi.getter
    def identifier(self) -> pulumi.Output[str]:
        """
        Machine friendly and unique identifier. Example: "filehash".
        """
        return pulumi.get(self, "identifier")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Human friend and unique name. Example: "File Hash".
        """
        return pulumi.get(self, "name")

