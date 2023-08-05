# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetRoleResult',
    'AwaitableGetRoleResult',
    'get_role',
    'get_role_output',
]

@pulumi.output_type
class GetRoleResult:
    """
    A collection of values returned by getRole.
    """
    def __init__(__self__, capabilities=None, description=None, filter_predicate=None, id=None, name=None):
        if capabilities and not isinstance(capabilities, list):
            raise TypeError("Expected argument 'capabilities' to be a list")
        pulumi.set(__self__, "capabilities", capabilities)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if filter_predicate and not isinstance(filter_predicate, str):
            raise TypeError("Expected argument 'filter_predicate' to be a str")
        pulumi.set(__self__, "filter_predicate", filter_predicate)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def capabilities(self) -> Sequence[str]:
        return pulumi.get(self, "capabilities")

    @property
    @pulumi.getter
    def description(self) -> str:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="filterPredicate")
    def filter_predicate(self) -> str:
        return pulumi.get(self, "filter_predicate")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")


class AwaitableGetRoleResult(GetRoleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRoleResult(
            capabilities=self.capabilities,
            description=self.description,
            filter_predicate=self.filter_predicate,
            id=self.id,
            name=self.name)


def get_role(id: Optional[str] = None,
             name: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRoleResult:
    """
    Provides a way to retrieve Sumo Logic role details (id, names, etc) for a role.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sumologic as sumologic

    this = sumologic.get_role(name="MyRole")
    ```

    ```python
    import pulumi
    import pulumi_sumologic as sumologic

    that = sumologic.get_role(id="1234567890")
    ```

    A role can be looked up by either `id` or `name`. One of those attributes needs to be specified.

    If both `id` and `name` have been specified, `id` takes precedence.
    ## Attributes reference

    The following attributes are exported:

    - `id` - The internal ID of the role. This can be used to create users having that role.
    - `name` - The name of the role.
    - `description` - The description of the role.
    - `filter_predicate` - The search filter to restrict access to specific logs.
    - `capabilities` - The list of capabilities associated with the role.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('sumologic:index/getRole:getRole', __args__, opts=opts, typ=GetRoleResult).value

    return AwaitableGetRoleResult(
        capabilities=__ret__.capabilities,
        description=__ret__.description,
        filter_predicate=__ret__.filter_predicate,
        id=__ret__.id,
        name=__ret__.name)


@_utilities.lift_output_func(get_role)
def get_role_output(id: Optional[pulumi.Input[Optional[str]]] = None,
                    name: Optional[pulumi.Input[Optional[str]]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRoleResult]:
    """
    Provides a way to retrieve Sumo Logic role details (id, names, etc) for a role.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sumologic as sumologic

    this = sumologic.get_role(name="MyRole")
    ```

    ```python
    import pulumi
    import pulumi_sumologic as sumologic

    that = sumologic.get_role(id="1234567890")
    ```

    A role can be looked up by either `id` or `name`. One of those attributes needs to be specified.

    If both `id` and `name` have been specified, `id` takes precedence.
    ## Attributes reference

    The following attributes are exported:

    - `id` - The internal ID of the role. This can be used to create users having that role.
    - `name` - The name of the role.
    - `description` - The description of the role.
    - `filter_predicate` - The search filter to restrict access to specific logs.
    - `capabilities` - The list of capabilities associated with the role.
    """
    ...
