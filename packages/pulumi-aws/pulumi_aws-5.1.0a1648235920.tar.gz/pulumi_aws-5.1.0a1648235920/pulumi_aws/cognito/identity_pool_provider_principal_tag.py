# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['IdentityPoolProviderPrincipalTagArgs', 'IdentityPoolProviderPrincipalTag']

@pulumi.input_type
class IdentityPoolProviderPrincipalTagArgs:
    def __init__(__self__, *,
                 identity_pool_id: pulumi.Input[str],
                 identity_provider_name: pulumi.Input[str],
                 principal_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 use_defaults: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a IdentityPoolProviderPrincipalTag resource.
        :param pulumi.Input[str] identity_pool_id: An identity pool ID.
        :param pulumi.Input[str] identity_provider_name: The name of the identity provider.
               * `principal_tags`: (Optional: []) - String to string map of variables.
               * `use_defaults`: (Optional: true) use default (username and clientID) attribute mappings.
        """
        pulumi.set(__self__, "identity_pool_id", identity_pool_id)
        pulumi.set(__self__, "identity_provider_name", identity_provider_name)
        if principal_tags is not None:
            pulumi.set(__self__, "principal_tags", principal_tags)
        if use_defaults is not None:
            pulumi.set(__self__, "use_defaults", use_defaults)

    @property
    @pulumi.getter(name="identityPoolId")
    def identity_pool_id(self) -> pulumi.Input[str]:
        """
        An identity pool ID.
        """
        return pulumi.get(self, "identity_pool_id")

    @identity_pool_id.setter
    def identity_pool_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "identity_pool_id", value)

    @property
    @pulumi.getter(name="identityProviderName")
    def identity_provider_name(self) -> pulumi.Input[str]:
        """
        The name of the identity provider.
        * `principal_tags`: (Optional: []) - String to string map of variables.
        * `use_defaults`: (Optional: true) use default (username and clientID) attribute mappings.
        """
        return pulumi.get(self, "identity_provider_name")

    @identity_provider_name.setter
    def identity_provider_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "identity_provider_name", value)

    @property
    @pulumi.getter(name="principalTags")
    def principal_tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "principal_tags")

    @principal_tags.setter
    def principal_tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "principal_tags", value)

    @property
    @pulumi.getter(name="useDefaults")
    def use_defaults(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "use_defaults")

    @use_defaults.setter
    def use_defaults(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "use_defaults", value)


@pulumi.input_type
class _IdentityPoolProviderPrincipalTagState:
    def __init__(__self__, *,
                 identity_pool_id: Optional[pulumi.Input[str]] = None,
                 identity_provider_name: Optional[pulumi.Input[str]] = None,
                 principal_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 use_defaults: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering IdentityPoolProviderPrincipalTag resources.
        :param pulumi.Input[str] identity_pool_id: An identity pool ID.
        :param pulumi.Input[str] identity_provider_name: The name of the identity provider.
               * `principal_tags`: (Optional: []) - String to string map of variables.
               * `use_defaults`: (Optional: true) use default (username and clientID) attribute mappings.
        """
        if identity_pool_id is not None:
            pulumi.set(__self__, "identity_pool_id", identity_pool_id)
        if identity_provider_name is not None:
            pulumi.set(__self__, "identity_provider_name", identity_provider_name)
        if principal_tags is not None:
            pulumi.set(__self__, "principal_tags", principal_tags)
        if use_defaults is not None:
            pulumi.set(__self__, "use_defaults", use_defaults)

    @property
    @pulumi.getter(name="identityPoolId")
    def identity_pool_id(self) -> Optional[pulumi.Input[str]]:
        """
        An identity pool ID.
        """
        return pulumi.get(self, "identity_pool_id")

    @identity_pool_id.setter
    def identity_pool_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "identity_pool_id", value)

    @property
    @pulumi.getter(name="identityProviderName")
    def identity_provider_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the identity provider.
        * `principal_tags`: (Optional: []) - String to string map of variables.
        * `use_defaults`: (Optional: true) use default (username and clientID) attribute mappings.
        """
        return pulumi.get(self, "identity_provider_name")

    @identity_provider_name.setter
    def identity_provider_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "identity_provider_name", value)

    @property
    @pulumi.getter(name="principalTags")
    def principal_tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "principal_tags")

    @principal_tags.setter
    def principal_tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "principal_tags", value)

    @property
    @pulumi.getter(name="useDefaults")
    def use_defaults(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "use_defaults")

    @use_defaults.setter
    def use_defaults(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "use_defaults", value)


class IdentityPoolProviderPrincipalTag(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 identity_pool_id: Optional[pulumi.Input[str]] = None,
                 identity_provider_name: Optional[pulumi.Input[str]] = None,
                 principal_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 use_defaults: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Provides an AWS Cognito Identity Principal Mapping.

        ## Import

        Cognito Identity Pool Roles Attachment can be imported using the Identity Pool ID and provider name, e.g.,

        ```sh
         $ pulumi import aws:cognito/identityPoolProviderPrincipalTag:IdentityPoolProviderPrincipalTag example us-west-2_abc123:CorpAD
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] identity_pool_id: An identity pool ID.
        :param pulumi.Input[str] identity_provider_name: The name of the identity provider.
               * `principal_tags`: (Optional: []) - String to string map of variables.
               * `use_defaults`: (Optional: true) use default (username and clientID) attribute mappings.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IdentityPoolProviderPrincipalTagArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides an AWS Cognito Identity Principal Mapping.

        ## Import

        Cognito Identity Pool Roles Attachment can be imported using the Identity Pool ID and provider name, e.g.,

        ```sh
         $ pulumi import aws:cognito/identityPoolProviderPrincipalTag:IdentityPoolProviderPrincipalTag example us-west-2_abc123:CorpAD
        ```

        :param str resource_name: The name of the resource.
        :param IdentityPoolProviderPrincipalTagArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IdentityPoolProviderPrincipalTagArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 identity_pool_id: Optional[pulumi.Input[str]] = None,
                 identity_provider_name: Optional[pulumi.Input[str]] = None,
                 principal_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 use_defaults: Optional[pulumi.Input[bool]] = None,
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
            __props__ = IdentityPoolProviderPrincipalTagArgs.__new__(IdentityPoolProviderPrincipalTagArgs)

            if identity_pool_id is None and not opts.urn:
                raise TypeError("Missing required property 'identity_pool_id'")
            __props__.__dict__["identity_pool_id"] = identity_pool_id
            if identity_provider_name is None and not opts.urn:
                raise TypeError("Missing required property 'identity_provider_name'")
            __props__.__dict__["identity_provider_name"] = identity_provider_name
            __props__.__dict__["principal_tags"] = principal_tags
            __props__.__dict__["use_defaults"] = use_defaults
        super(IdentityPoolProviderPrincipalTag, __self__).__init__(
            'aws:cognito/identityPoolProviderPrincipalTag:IdentityPoolProviderPrincipalTag',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            identity_pool_id: Optional[pulumi.Input[str]] = None,
            identity_provider_name: Optional[pulumi.Input[str]] = None,
            principal_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            use_defaults: Optional[pulumi.Input[bool]] = None) -> 'IdentityPoolProviderPrincipalTag':
        """
        Get an existing IdentityPoolProviderPrincipalTag resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] identity_pool_id: An identity pool ID.
        :param pulumi.Input[str] identity_provider_name: The name of the identity provider.
               * `principal_tags`: (Optional: []) - String to string map of variables.
               * `use_defaults`: (Optional: true) use default (username and clientID) attribute mappings.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _IdentityPoolProviderPrincipalTagState.__new__(_IdentityPoolProviderPrincipalTagState)

        __props__.__dict__["identity_pool_id"] = identity_pool_id
        __props__.__dict__["identity_provider_name"] = identity_provider_name
        __props__.__dict__["principal_tags"] = principal_tags
        __props__.__dict__["use_defaults"] = use_defaults
        return IdentityPoolProviderPrincipalTag(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="identityPoolId")
    def identity_pool_id(self) -> pulumi.Output[str]:
        """
        An identity pool ID.
        """
        return pulumi.get(self, "identity_pool_id")

    @property
    @pulumi.getter(name="identityProviderName")
    def identity_provider_name(self) -> pulumi.Output[str]:
        """
        The name of the identity provider.
        * `principal_tags`: (Optional: []) - String to string map of variables.
        * `use_defaults`: (Optional: true) use default (username and clientID) attribute mappings.
        """
        return pulumi.get(self, "identity_provider_name")

    @property
    @pulumi.getter(name="principalTags")
    def principal_tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        return pulumi.get(self, "principal_tags")

    @property
    @pulumi.getter(name="useDefaults")
    def use_defaults(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "use_defaults")

