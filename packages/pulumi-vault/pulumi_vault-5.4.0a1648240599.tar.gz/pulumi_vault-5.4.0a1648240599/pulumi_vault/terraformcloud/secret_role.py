# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['SecretRoleArgs', 'SecretRole']

@pulumi.input_type
class SecretRoleArgs:
    def __init__(__self__, *,
                 backend: Optional[pulumi.Input[str]] = None,
                 max_ttl: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization: Optional[pulumi.Input[str]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 ttl: Optional[pulumi.Input[int]] = None,
                 user_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SecretRole resource.
        :param pulumi.Input[str] backend: The path of the Terraform Cloud Secret Backend the role belongs to.
        :param pulumi.Input[int] max_ttl: Maximum TTL for leases associated with this role, in seconds.
        :param pulumi.Input[str] name: The name of an existing role against which to create this Terraform Cloud credential
        :param pulumi.Input[str] organization: Name of the Terraform Cloud or Enterprise organization
        :param pulumi.Input[str] team_id: ID of the Terraform Cloud or Enterprise team under organization (e.g., settings/teams/team-xxxxxxxxxxxxx)
        :param pulumi.Input[int] ttl: Specifies the TTL for this role.
        :param pulumi.Input[str] user_id: ID of the Terraform Cloud or Enterprise user (e.g., user-xxxxxxxxxxxxxxxx)
        """
        if backend is not None:
            pulumi.set(__self__, "backend", backend)
        if max_ttl is not None:
            pulumi.set(__self__, "max_ttl", max_ttl)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if organization is not None:
            pulumi.set(__self__, "organization", organization)
        if team_id is not None:
            pulumi.set(__self__, "team_id", team_id)
        if ttl is not None:
            pulumi.set(__self__, "ttl", ttl)
        if user_id is not None:
            pulumi.set(__self__, "user_id", user_id)

    @property
    @pulumi.getter
    def backend(self) -> Optional[pulumi.Input[str]]:
        """
        The path of the Terraform Cloud Secret Backend the role belongs to.
        """
        return pulumi.get(self, "backend")

    @backend.setter
    def backend(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "backend", value)

    @property
    @pulumi.getter(name="maxTtl")
    def max_ttl(self) -> Optional[pulumi.Input[int]]:
        """
        Maximum TTL for leases associated with this role, in seconds.
        """
        return pulumi.get(self, "max_ttl")

    @max_ttl.setter
    def max_ttl(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_ttl", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of an existing role against which to create this Terraform Cloud credential
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def organization(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Terraform Cloud or Enterprise organization
        """
        return pulumi.get(self, "organization")

    @organization.setter
    def organization(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "organization", value)

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the Terraform Cloud or Enterprise team under organization (e.g., settings/teams/team-xxxxxxxxxxxxx)
        """
        return pulumi.get(self, "team_id")

    @team_id.setter
    def team_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "team_id", value)

    @property
    @pulumi.getter
    def ttl(self) -> Optional[pulumi.Input[int]]:
        """
        Specifies the TTL for this role.
        """
        return pulumi.get(self, "ttl")

    @ttl.setter
    def ttl(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ttl", value)

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the Terraform Cloud or Enterprise user (e.g., user-xxxxxxxxxxxxxxxx)
        """
        return pulumi.get(self, "user_id")

    @user_id.setter
    def user_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_id", value)


@pulumi.input_type
class _SecretRoleState:
    def __init__(__self__, *,
                 backend: Optional[pulumi.Input[str]] = None,
                 max_ttl: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization: Optional[pulumi.Input[str]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 ttl: Optional[pulumi.Input[int]] = None,
                 user_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering SecretRole resources.
        :param pulumi.Input[str] backend: The path of the Terraform Cloud Secret Backend the role belongs to.
        :param pulumi.Input[int] max_ttl: Maximum TTL for leases associated with this role, in seconds.
        :param pulumi.Input[str] name: The name of an existing role against which to create this Terraform Cloud credential
        :param pulumi.Input[str] organization: Name of the Terraform Cloud or Enterprise organization
        :param pulumi.Input[str] team_id: ID of the Terraform Cloud or Enterprise team under organization (e.g., settings/teams/team-xxxxxxxxxxxxx)
        :param pulumi.Input[int] ttl: Specifies the TTL for this role.
        :param pulumi.Input[str] user_id: ID of the Terraform Cloud or Enterprise user (e.g., user-xxxxxxxxxxxxxxxx)
        """
        if backend is not None:
            pulumi.set(__self__, "backend", backend)
        if max_ttl is not None:
            pulumi.set(__self__, "max_ttl", max_ttl)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if organization is not None:
            pulumi.set(__self__, "organization", organization)
        if team_id is not None:
            pulumi.set(__self__, "team_id", team_id)
        if ttl is not None:
            pulumi.set(__self__, "ttl", ttl)
        if user_id is not None:
            pulumi.set(__self__, "user_id", user_id)

    @property
    @pulumi.getter
    def backend(self) -> Optional[pulumi.Input[str]]:
        """
        The path of the Terraform Cloud Secret Backend the role belongs to.
        """
        return pulumi.get(self, "backend")

    @backend.setter
    def backend(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "backend", value)

    @property
    @pulumi.getter(name="maxTtl")
    def max_ttl(self) -> Optional[pulumi.Input[int]]:
        """
        Maximum TTL for leases associated with this role, in seconds.
        """
        return pulumi.get(self, "max_ttl")

    @max_ttl.setter
    def max_ttl(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_ttl", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of an existing role against which to create this Terraform Cloud credential
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def organization(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Terraform Cloud or Enterprise organization
        """
        return pulumi.get(self, "organization")

    @organization.setter
    def organization(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "organization", value)

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the Terraform Cloud or Enterprise team under organization (e.g., settings/teams/team-xxxxxxxxxxxxx)
        """
        return pulumi.get(self, "team_id")

    @team_id.setter
    def team_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "team_id", value)

    @property
    @pulumi.getter
    def ttl(self) -> Optional[pulumi.Input[int]]:
        """
        Specifies the TTL for this role.
        """
        return pulumi.get(self, "ttl")

    @ttl.setter
    def ttl(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ttl", value)

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the Terraform Cloud or Enterprise user (e.g., user-xxxxxxxxxxxxxxxx)
        """
        return pulumi.get(self, "user_id")

    @user_id.setter
    def user_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_id", value)


class SecretRole(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 backend: Optional[pulumi.Input[str]] = None,
                 max_ttl: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization: Optional[pulumi.Input[str]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 ttl: Optional[pulumi.Input[int]] = None,
                 user_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Import

        Terraform Cloud secret backend roles can be imported using the `backend`, `/roles/`, and the `name` e.g.

        ```sh
         $ pulumi import vault:terraformcloud/secretRole:SecretRole example terraform/roles/my-role
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] backend: The path of the Terraform Cloud Secret Backend the role belongs to.
        :param pulumi.Input[int] max_ttl: Maximum TTL for leases associated with this role, in seconds.
        :param pulumi.Input[str] name: The name of an existing role against which to create this Terraform Cloud credential
        :param pulumi.Input[str] organization: Name of the Terraform Cloud or Enterprise organization
        :param pulumi.Input[str] team_id: ID of the Terraform Cloud or Enterprise team under organization (e.g., settings/teams/team-xxxxxxxxxxxxx)
        :param pulumi.Input[int] ttl: Specifies the TTL for this role.
        :param pulumi.Input[str] user_id: ID of the Terraform Cloud or Enterprise user (e.g., user-xxxxxxxxxxxxxxxx)
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[SecretRoleArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Import

        Terraform Cloud secret backend roles can be imported using the `backend`, `/roles/`, and the `name` e.g.

        ```sh
         $ pulumi import vault:terraformcloud/secretRole:SecretRole example terraform/roles/my-role
        ```

        :param str resource_name: The name of the resource.
        :param SecretRoleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SecretRoleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 backend: Optional[pulumi.Input[str]] = None,
                 max_ttl: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization: Optional[pulumi.Input[str]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 ttl: Optional[pulumi.Input[int]] = None,
                 user_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = SecretRoleArgs.__new__(SecretRoleArgs)

            __props__.__dict__["backend"] = backend
            __props__.__dict__["max_ttl"] = max_ttl
            __props__.__dict__["name"] = name
            __props__.__dict__["organization"] = organization
            __props__.__dict__["team_id"] = team_id
            __props__.__dict__["ttl"] = ttl
            __props__.__dict__["user_id"] = user_id
        super(SecretRole, __self__).__init__(
            'vault:terraformcloud/secretRole:SecretRole',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            backend: Optional[pulumi.Input[str]] = None,
            max_ttl: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            organization: Optional[pulumi.Input[str]] = None,
            team_id: Optional[pulumi.Input[str]] = None,
            ttl: Optional[pulumi.Input[int]] = None,
            user_id: Optional[pulumi.Input[str]] = None) -> 'SecretRole':
        """
        Get an existing SecretRole resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] backend: The path of the Terraform Cloud Secret Backend the role belongs to.
        :param pulumi.Input[int] max_ttl: Maximum TTL for leases associated with this role, in seconds.
        :param pulumi.Input[str] name: The name of an existing role against which to create this Terraform Cloud credential
        :param pulumi.Input[str] organization: Name of the Terraform Cloud or Enterprise organization
        :param pulumi.Input[str] team_id: ID of the Terraform Cloud or Enterprise team under organization (e.g., settings/teams/team-xxxxxxxxxxxxx)
        :param pulumi.Input[int] ttl: Specifies the TTL for this role.
        :param pulumi.Input[str] user_id: ID of the Terraform Cloud or Enterprise user (e.g., user-xxxxxxxxxxxxxxxx)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SecretRoleState.__new__(_SecretRoleState)

        __props__.__dict__["backend"] = backend
        __props__.__dict__["max_ttl"] = max_ttl
        __props__.__dict__["name"] = name
        __props__.__dict__["organization"] = organization
        __props__.__dict__["team_id"] = team_id
        __props__.__dict__["ttl"] = ttl
        __props__.__dict__["user_id"] = user_id
        return SecretRole(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def backend(self) -> pulumi.Output[Optional[str]]:
        """
        The path of the Terraform Cloud Secret Backend the role belongs to.
        """
        return pulumi.get(self, "backend")

    @property
    @pulumi.getter(name="maxTtl")
    def max_ttl(self) -> pulumi.Output[Optional[int]]:
        """
        Maximum TTL for leases associated with this role, in seconds.
        """
        return pulumi.get(self, "max_ttl")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of an existing role against which to create this Terraform Cloud credential
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def organization(self) -> pulumi.Output[Optional[str]]:
        """
        Name of the Terraform Cloud or Enterprise organization
        """
        return pulumi.get(self, "organization")

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> pulumi.Output[Optional[str]]:
        """
        ID of the Terraform Cloud or Enterprise team under organization (e.g., settings/teams/team-xxxxxxxxxxxxx)
        """
        return pulumi.get(self, "team_id")

    @property
    @pulumi.getter
    def ttl(self) -> pulumi.Output[Optional[int]]:
        """
        Specifies the TTL for this role.
        """
        return pulumi.get(self, "ttl")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Output[Optional[str]]:
        """
        ID of the Terraform Cloud or Enterprise user (e.g., user-xxxxxxxxxxxxxxxx)
        """
        return pulumi.get(self, "user_id")

