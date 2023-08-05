# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'SecretBackendRoleVhostArgs',
    'SecretBackendRoleVhostTopicArgs',
    'SecretBackendRoleVhostTopicVhostArgs',
]

@pulumi.input_type
class SecretBackendRoleVhostArgs:
    def __init__(__self__, *,
                 configure: pulumi.Input[str],
                 host: pulumi.Input[str],
                 read: pulumi.Input[str],
                 write: pulumi.Input[str]):
        pulumi.set(__self__, "configure", configure)
        pulumi.set(__self__, "host", host)
        pulumi.set(__self__, "read", read)
        pulumi.set(__self__, "write", write)

    @property
    @pulumi.getter
    def configure(self) -> pulumi.Input[str]:
        return pulumi.get(self, "configure")

    @configure.setter
    def configure(self, value: pulumi.Input[str]):
        pulumi.set(self, "configure", value)

    @property
    @pulumi.getter
    def host(self) -> pulumi.Input[str]:
        return pulumi.get(self, "host")

    @host.setter
    def host(self, value: pulumi.Input[str]):
        pulumi.set(self, "host", value)

    @property
    @pulumi.getter
    def read(self) -> pulumi.Input[str]:
        return pulumi.get(self, "read")

    @read.setter
    def read(self, value: pulumi.Input[str]):
        pulumi.set(self, "read", value)

    @property
    @pulumi.getter
    def write(self) -> pulumi.Input[str]:
        return pulumi.get(self, "write")

    @write.setter
    def write(self, value: pulumi.Input[str]):
        pulumi.set(self, "write", value)


@pulumi.input_type
class SecretBackendRoleVhostTopicArgs:
    def __init__(__self__, *,
                 host: pulumi.Input[str],
                 vhosts: Optional[pulumi.Input[Sequence[pulumi.Input['SecretBackendRoleVhostTopicVhostArgs']]]] = None):
        """
        :param pulumi.Input[Sequence[pulumi.Input['SecretBackendRoleVhostTopicVhostArgs']]] vhosts: Specifies a map of virtual hosts to permissions.
        """
        pulumi.set(__self__, "host", host)
        if vhosts is not None:
            pulumi.set(__self__, "vhosts", vhosts)

    @property
    @pulumi.getter
    def host(self) -> pulumi.Input[str]:
        return pulumi.get(self, "host")

    @host.setter
    def host(self, value: pulumi.Input[str]):
        pulumi.set(self, "host", value)

    @property
    @pulumi.getter
    def vhosts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SecretBackendRoleVhostTopicVhostArgs']]]]:
        """
        Specifies a map of virtual hosts to permissions.
        """
        return pulumi.get(self, "vhosts")

    @vhosts.setter
    def vhosts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SecretBackendRoleVhostTopicVhostArgs']]]]):
        pulumi.set(self, "vhosts", value)


@pulumi.input_type
class SecretBackendRoleVhostTopicVhostArgs:
    def __init__(__self__, *,
                 read: pulumi.Input[str],
                 topic: pulumi.Input[str],
                 write: pulumi.Input[str]):
        pulumi.set(__self__, "read", read)
        pulumi.set(__self__, "topic", topic)
        pulumi.set(__self__, "write", write)

    @property
    @pulumi.getter
    def read(self) -> pulumi.Input[str]:
        return pulumi.get(self, "read")

    @read.setter
    def read(self, value: pulumi.Input[str]):
        pulumi.set(self, "read", value)

    @property
    @pulumi.getter
    def topic(self) -> pulumi.Input[str]:
        return pulumi.get(self, "topic")

    @topic.setter
    def topic(self, value: pulumi.Input[str]):
        pulumi.set(self, "topic", value)

    @property
    @pulumi.getter
    def write(self) -> pulumi.Input[str]:
        return pulumi.get(self, "write")

    @write.setter
    def write(self, value: pulumi.Input[str]):
        pulumi.set(self, "write", value)


