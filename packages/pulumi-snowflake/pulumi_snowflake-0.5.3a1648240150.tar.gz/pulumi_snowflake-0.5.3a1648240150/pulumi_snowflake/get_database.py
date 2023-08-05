# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetDatabaseResult',
    'AwaitableGetDatabaseResult',
    'get_database',
    'get_database_output',
]

@pulumi.output_type
class GetDatabaseResult:
    """
    A collection of values returned by getDatabase.
    """
    def __init__(__self__, comment=None, created_on=None, id=None, is_current=None, is_default=None, name=None, options=None, origin=None, owner=None, retention_time=None):
        if comment and not isinstance(comment, str):
            raise TypeError("Expected argument 'comment' to be a str")
        pulumi.set(__self__, "comment", comment)
        if created_on and not isinstance(created_on, str):
            raise TypeError("Expected argument 'created_on' to be a str")
        pulumi.set(__self__, "created_on", created_on)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_current and not isinstance(is_current, bool):
            raise TypeError("Expected argument 'is_current' to be a bool")
        pulumi.set(__self__, "is_current", is_current)
        if is_default and not isinstance(is_default, bool):
            raise TypeError("Expected argument 'is_default' to be a bool")
        pulumi.set(__self__, "is_default", is_default)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if options and not isinstance(options, str):
            raise TypeError("Expected argument 'options' to be a str")
        pulumi.set(__self__, "options", options)
        if origin and not isinstance(origin, str):
            raise TypeError("Expected argument 'origin' to be a str")
        pulumi.set(__self__, "origin", origin)
        if owner and not isinstance(owner, str):
            raise TypeError("Expected argument 'owner' to be a str")
        pulumi.set(__self__, "owner", owner)
        if retention_time and not isinstance(retention_time, int):
            raise TypeError("Expected argument 'retention_time' to be a int")
        pulumi.set(__self__, "retention_time", retention_time)

    @property
    @pulumi.getter
    def comment(self) -> str:
        return pulumi.get(self, "comment")

    @property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> str:
        return pulumi.get(self, "created_on")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isCurrent")
    def is_current(self) -> bool:
        return pulumi.get(self, "is_current")

    @property
    @pulumi.getter(name="isDefault")
    def is_default(self) -> bool:
        return pulumi.get(self, "is_default")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The database from which to return its metadata.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def options(self) -> str:
        return pulumi.get(self, "options")

    @property
    @pulumi.getter
    def origin(self) -> str:
        return pulumi.get(self, "origin")

    @property
    @pulumi.getter
    def owner(self) -> str:
        return pulumi.get(self, "owner")

    @property
    @pulumi.getter(name="retentionTime")
    def retention_time(self) -> int:
        return pulumi.get(self, "retention_time")


class AwaitableGetDatabaseResult(GetDatabaseResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDatabaseResult(
            comment=self.comment,
            created_on=self.created_on,
            id=self.id,
            is_current=self.is_current,
            is_default=self.is_default,
            name=self.name,
            options=self.options,
            origin=self.origin,
            owner=self.owner,
            retention_time=self.retention_time)


def get_database(name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDatabaseResult:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_snowflake as snowflake

    this = snowflake.get_database(name="DEMO_DB")
    ```


    :param str name: The database from which to return its metadata.
    """
    __args__ = dict()
    __args__['name'] = name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('snowflake:index/getDatabase:getDatabase', __args__, opts=opts, typ=GetDatabaseResult).value

    return AwaitableGetDatabaseResult(
        comment=__ret__.comment,
        created_on=__ret__.created_on,
        id=__ret__.id,
        is_current=__ret__.is_current,
        is_default=__ret__.is_default,
        name=__ret__.name,
        options=__ret__.options,
        origin=__ret__.origin,
        owner=__ret__.owner,
        retention_time=__ret__.retention_time)


@_utilities.lift_output_func(get_database)
def get_database_output(name: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDatabaseResult]:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_snowflake as snowflake

    this = snowflake.get_database(name="DEMO_DB")
    ```


    :param str name: The database from which to return its metadata.
    """
    ...
