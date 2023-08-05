# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs

__all__ = [
    'GetPipesResult',
    'AwaitableGetPipesResult',
    'get_pipes',
    'get_pipes_output',
]

@pulumi.output_type
class GetPipesResult:
    """
    A collection of values returned by getPipes.
    """
    def __init__(__self__, database=None, id=None, pipes=None, schema=None):
        if database and not isinstance(database, str):
            raise TypeError("Expected argument 'database' to be a str")
        pulumi.set(__self__, "database", database)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if pipes and not isinstance(pipes, list):
            raise TypeError("Expected argument 'pipes' to be a list")
        pulumi.set(__self__, "pipes", pipes)
        if schema and not isinstance(schema, str):
            raise TypeError("Expected argument 'schema' to be a str")
        pulumi.set(__self__, "schema", schema)

    @property
    @pulumi.getter
    def database(self) -> str:
        """
        The database from which to return the schemas from.
        """
        return pulumi.get(self, "database")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def pipes(self) -> Sequence['outputs.GetPipesPipeResult']:
        """
        The pipes in the schema
        """
        return pulumi.get(self, "pipes")

    @property
    @pulumi.getter
    def schema(self) -> str:
        """
        The schema from which to return the pipes from.
        """
        return pulumi.get(self, "schema")


class AwaitableGetPipesResult(GetPipesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPipesResult(
            database=self.database,
            id=self.id,
            pipes=self.pipes,
            schema=self.schema)


def get_pipes(database: Optional[str] = None,
              schema: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPipesResult:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_snowflake as snowflake

    current = snowflake.get_pipes(database="MYDB",
        schema="MYSCHEMA")
    ```


    :param str database: The database from which to return the schemas from.
    :param str schema: The schema from which to return the pipes from.
    """
    __args__ = dict()
    __args__['database'] = database
    __args__['schema'] = schema
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('snowflake:index/getPipes:getPipes', __args__, opts=opts, typ=GetPipesResult).value

    return AwaitableGetPipesResult(
        database=__ret__.database,
        id=__ret__.id,
        pipes=__ret__.pipes,
        schema=__ret__.schema)


@_utilities.lift_output_func(get_pipes)
def get_pipes_output(database: Optional[pulumi.Input[str]] = None,
                     schema: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPipesResult]:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_snowflake as snowflake

    current = snowflake.get_pipes(database="MYDB",
        schema="MYSCHEMA")
    ```


    :param str database: The database from which to return the schemas from.
    :param str schema: The schema from which to return the pipes from.
    """
    ...
