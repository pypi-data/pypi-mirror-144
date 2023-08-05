# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetAccessCredentialsResult',
    'AwaitableGetAccessCredentialsResult',
    'get_access_credentials',
    'get_access_credentials_output',
]

@pulumi.output_type
class GetAccessCredentialsResult:
    """
    A collection of values returned by getAccessCredentials.
    """
    def __init__(__self__, backend=None, current_password=None, id=None, last_password=None, role=None, username=None):
        if backend and not isinstance(backend, str):
            raise TypeError("Expected argument 'backend' to be a str")
        pulumi.set(__self__, "backend", backend)
        if current_password and not isinstance(current_password, str):
            raise TypeError("Expected argument 'current_password' to be a str")
        pulumi.set(__self__, "current_password", current_password)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if last_password and not isinstance(last_password, str):
            raise TypeError("Expected argument 'last_password' to be a str")
        pulumi.set(__self__, "last_password", last_password)
        if role and not isinstance(role, str):
            raise TypeError("Expected argument 'role' to be a str")
        pulumi.set(__self__, "role", role)
        if username and not isinstance(username, str):
            raise TypeError("Expected argument 'username' to be a str")
        pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter
    def backend(self) -> str:
        return pulumi.get(self, "backend")

    @property
    @pulumi.getter(name="currentPassword")
    def current_password(self) -> str:
        """
        The current set password on the Active Directory service account.
        """
        return pulumi.get(self, "current_password")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lastPassword")
    def last_password(self) -> str:
        """
        The current set password on the Active Directory service account, provided because AD is eventually consistent.
        """
        return pulumi.get(self, "last_password")

    @property
    @pulumi.getter
    def role(self) -> str:
        return pulumi.get(self, "role")

    @property
    @pulumi.getter
    def username(self) -> str:
        """
        The Active Directory service account username.
        """
        return pulumi.get(self, "username")


class AwaitableGetAccessCredentialsResult(GetAccessCredentialsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAccessCredentialsResult(
            backend=self.backend,
            current_password=self.current_password,
            id=self.id,
            last_password=self.last_password,
            role=self.role,
            username=self.username)


def get_access_credentials(backend: Optional[str] = None,
                           role: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAccessCredentialsResult:
    """
    Use this data source to access information about an existing resource.

    :param str backend: The path to the AD secret backend to
           read credentials from, with no leading or trailing `/`s.
    :param str role: The name of the AD secret backend role to read
           credentials from, with no leading or trailing `/`s.
    """
    __args__ = dict()
    __args__['backend'] = backend
    __args__['role'] = role
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('vault:ad/getAccessCredentials:getAccessCredentials', __args__, opts=opts, typ=GetAccessCredentialsResult).value

    return AwaitableGetAccessCredentialsResult(
        backend=__ret__.backend,
        current_password=__ret__.current_password,
        id=__ret__.id,
        last_password=__ret__.last_password,
        role=__ret__.role,
        username=__ret__.username)


@_utilities.lift_output_func(get_access_credentials)
def get_access_credentials_output(backend: Optional[pulumi.Input[str]] = None,
                                  role: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAccessCredentialsResult]:
    """
    Use this data source to access information about an existing resource.

    :param str backend: The path to the AD secret backend to
           read credentials from, with no leading or trailing `/`s.
    :param str role: The name of the AD secret backend role to read
           credentials from, with no leading or trailing `/`s.
    """
    ...
