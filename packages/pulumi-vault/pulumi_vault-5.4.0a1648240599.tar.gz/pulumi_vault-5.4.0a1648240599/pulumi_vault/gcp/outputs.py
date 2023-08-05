# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'SecretRolesetBinding',
    'SecretStaticAccountBinding',
]

@pulumi.output_type
class SecretRolesetBinding(dict):
    def __init__(__self__, *,
                 resource: str,
                 roles: Sequence[str]):
        """
        :param str resource: Resource or resource path for which IAM policy information will be bound. The resource path may be specified in a few different [formats](https://www.vaultproject.io/docs/secrets/gcp/index.html#roleset-bindings).
        :param Sequence[str] roles: List of [GCP IAM roles](https://cloud.google.com/iam/docs/understanding-roles) for the resource.
        """
        pulumi.set(__self__, "resource", resource)
        pulumi.set(__self__, "roles", roles)

    @property
    @pulumi.getter
    def resource(self) -> str:
        """
        Resource or resource path for which IAM policy information will be bound. The resource path may be specified in a few different [formats](https://www.vaultproject.io/docs/secrets/gcp/index.html#roleset-bindings).
        """
        return pulumi.get(self, "resource")

    @property
    @pulumi.getter
    def roles(self) -> Sequence[str]:
        """
        List of [GCP IAM roles](https://cloud.google.com/iam/docs/understanding-roles) for the resource.
        """
        return pulumi.get(self, "roles")


@pulumi.output_type
class SecretStaticAccountBinding(dict):
    def __init__(__self__, *,
                 resource: str,
                 roles: Sequence[str]):
        """
        :param str resource: Resource or resource path for which IAM policy information will be bound. The resource path may be specified in a few different [formats](https://www.vaultproject.io/docs/secrets/gcp/index.html#bindings).
        :param Sequence[str] roles: List of [GCP IAM roles](https://cloud.google.com/iam/docs/understanding-roles) for the resource.
        """
        pulumi.set(__self__, "resource", resource)
        pulumi.set(__self__, "roles", roles)

    @property
    @pulumi.getter
    def resource(self) -> str:
        """
        Resource or resource path for which IAM policy information will be bound. The resource path may be specified in a few different [formats](https://www.vaultproject.io/docs/secrets/gcp/index.html#bindings).
        """
        return pulumi.get(self, "resource")

    @property
    @pulumi.getter
    def roles(self) -> Sequence[str]:
        """
        List of [GCP IAM roles](https://cloud.google.com/iam/docs/understanding-roles) for the resource.
        """
        return pulumi.get(self, "roles")


