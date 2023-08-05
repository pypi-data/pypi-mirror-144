# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetSystemGetPrivateLinkConfigResult',
    'AwaitableGetSystemGetPrivateLinkConfigResult',
    'get_system_get_private_link_config',
]

@pulumi.output_type
class GetSystemGetPrivateLinkConfigResult:
    """
    A collection of values returned by getSystemGetPrivateLinkConfig.
    """
    def __init__(__self__, account_name=None, account_url=None, aws_vpce_id=None, azure_pls_id=None, id=None, ocsp_url=None):
        if account_name and not isinstance(account_name, str):
            raise TypeError("Expected argument 'account_name' to be a str")
        pulumi.set(__self__, "account_name", account_name)
        if account_url and not isinstance(account_url, str):
            raise TypeError("Expected argument 'account_url' to be a str")
        pulumi.set(__self__, "account_url", account_url)
        if aws_vpce_id and not isinstance(aws_vpce_id, str):
            raise TypeError("Expected argument 'aws_vpce_id' to be a str")
        pulumi.set(__self__, "aws_vpce_id", aws_vpce_id)
        if azure_pls_id and not isinstance(azure_pls_id, str):
            raise TypeError("Expected argument 'azure_pls_id' to be a str")
        pulumi.set(__self__, "azure_pls_id", azure_pls_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ocsp_url and not isinstance(ocsp_url, str):
            raise TypeError("Expected argument 'ocsp_url' to be a str")
        pulumi.set(__self__, "ocsp_url", ocsp_url)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> str:
        """
        The name of your Snowflake account.
        """
        return pulumi.get(self, "account_name")

    @property
    @pulumi.getter(name="accountUrl")
    def account_url(self) -> str:
        """
        The URL used to connect to Snowflake through AWS PrivateLink or Azure Private Link.
        """
        return pulumi.get(self, "account_url")

    @property
    @pulumi.getter(name="awsVpceId")
    def aws_vpce_id(self) -> str:
        """
        The AWS VPCE ID for your account.
        """
        return pulumi.get(self, "aws_vpce_id")

    @property
    @pulumi.getter(name="azurePlsId")
    def azure_pls_id(self) -> str:
        """
        The Azure Private Link Service ID for your account.
        """
        return pulumi.get(self, "azure_pls_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ocspUrl")
    def ocsp_url(self) -> str:
        """
        The OCSP URL corresponding to your Snowflake account that uses AWS PrivateLink or Azure Private Link.
        """
        return pulumi.get(self, "ocsp_url")


class AwaitableGetSystemGetPrivateLinkConfigResult(GetSystemGetPrivateLinkConfigResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSystemGetPrivateLinkConfigResult(
            account_name=self.account_name,
            account_url=self.account_url,
            aws_vpce_id=self.aws_vpce_id,
            azure_pls_id=self.azure_pls_id,
            id=self.id,
            ocsp_url=self.ocsp_url)


def get_system_get_private_link_config(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSystemGetPrivateLinkConfigResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('snowflake:index/getSystemGetPrivateLinkConfig:getSystemGetPrivateLinkConfig', __args__, opts=opts, typ=GetSystemGetPrivateLinkConfigResult).value

    return AwaitableGetSystemGetPrivateLinkConfigResult(
        account_name=__ret__.account_name,
        account_url=__ret__.account_url,
        aws_vpce_id=__ret__.aws_vpce_id,
        azure_pls_id=__ret__.azure_pls_id,
        id=__ret__.id,
        ocsp_url=__ret__.ocsp_url)
