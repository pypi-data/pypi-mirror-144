# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['ManagedPrefixListArgs', 'ManagedPrefixList']

@pulumi.input_type
class ManagedPrefixListArgs:
    def __init__(__self__, *,
                 address_family: pulumi.Input[str],
                 max_entries: pulumi.Input[int],
                 entries: Optional[pulumi.Input[Sequence[pulumi.Input['ManagedPrefixListEntryArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a ManagedPrefixList resource.
        :param pulumi.Input[str] address_family: Address family (`IPv4` or `IPv6`) of this prefix list.
        :param pulumi.Input[int] max_entries: Maximum number of entries that this prefix list can contain.
        :param pulumi.Input[Sequence[pulumi.Input['ManagedPrefixListEntryArgs']]] entries: Configuration block for prefix list entry. Detailed below. Different entries may have overlapping CIDR blocks, but a particular CIDR should not be duplicated.
        :param pulumi.Input[str] name: Name of this resource. The name must not start with `com.amazonaws`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Map of tags to assign to this resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        pulumi.set(__self__, "address_family", address_family)
        pulumi.set(__self__, "max_entries", max_entries)
        if entries is not None:
            pulumi.set(__self__, "entries", entries)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="addressFamily")
    def address_family(self) -> pulumi.Input[str]:
        """
        Address family (`IPv4` or `IPv6`) of this prefix list.
        """
        return pulumi.get(self, "address_family")

    @address_family.setter
    def address_family(self, value: pulumi.Input[str]):
        pulumi.set(self, "address_family", value)

    @property
    @pulumi.getter(name="maxEntries")
    def max_entries(self) -> pulumi.Input[int]:
        """
        Maximum number of entries that this prefix list can contain.
        """
        return pulumi.get(self, "max_entries")

    @max_entries.setter
    def max_entries(self, value: pulumi.Input[int]):
        pulumi.set(self, "max_entries", value)

    @property
    @pulumi.getter
    def entries(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ManagedPrefixListEntryArgs']]]]:
        """
        Configuration block for prefix list entry. Detailed below. Different entries may have overlapping CIDR blocks, but a particular CIDR should not be duplicated.
        """
        return pulumi.get(self, "entries")

    @entries.setter
    def entries(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ManagedPrefixListEntryArgs']]]]):
        pulumi.set(self, "entries", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of this resource. The name must not start with `com.amazonaws`.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Map of tags to assign to this resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _ManagedPrefixListState:
    def __init__(__self__, *,
                 address_family: Optional[pulumi.Input[str]] = None,
                 arn: Optional[pulumi.Input[str]] = None,
                 entries: Optional[pulumi.Input[Sequence[pulumi.Input['ManagedPrefixListEntryArgs']]]] = None,
                 max_entries: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 owner_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 version: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering ManagedPrefixList resources.
        :param pulumi.Input[str] address_family: Address family (`IPv4` or `IPv6`) of this prefix list.
        :param pulumi.Input[str] arn: ARN of the prefix list.
        :param pulumi.Input[Sequence[pulumi.Input['ManagedPrefixListEntryArgs']]] entries: Configuration block for prefix list entry. Detailed below. Different entries may have overlapping CIDR blocks, but a particular CIDR should not be duplicated.
        :param pulumi.Input[int] max_entries: Maximum number of entries that this prefix list can contain.
        :param pulumi.Input[str] name: Name of this resource. The name must not start with `com.amazonaws`.
        :param pulumi.Input[str] owner_id: ID of the AWS account that owns this prefix list.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Map of tags to assign to this resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[int] version: Latest version of this prefix list.
        """
        if address_family is not None:
            pulumi.set(__self__, "address_family", address_family)
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if entries is not None:
            pulumi.set(__self__, "entries", entries)
        if max_entries is not None:
            pulumi.set(__self__, "max_entries", max_entries)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if owner_id is not None:
            pulumi.set(__self__, "owner_id", owner_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="addressFamily")
    def address_family(self) -> Optional[pulumi.Input[str]]:
        """
        Address family (`IPv4` or `IPv6`) of this prefix list.
        """
        return pulumi.get(self, "address_family")

    @address_family.setter
    def address_family(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "address_family", value)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        ARN of the prefix list.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter
    def entries(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ManagedPrefixListEntryArgs']]]]:
        """
        Configuration block for prefix list entry. Detailed below. Different entries may have overlapping CIDR blocks, but a particular CIDR should not be duplicated.
        """
        return pulumi.get(self, "entries")

    @entries.setter
    def entries(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ManagedPrefixListEntryArgs']]]]):
        pulumi.set(self, "entries", value)

    @property
    @pulumi.getter(name="maxEntries")
    def max_entries(self) -> Optional[pulumi.Input[int]]:
        """
        Maximum number of entries that this prefix list can contain.
        """
        return pulumi.get(self, "max_entries")

    @max_entries.setter
    def max_entries(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_entries", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of this resource. The name must not start with `com.amazonaws`.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the AWS account that owns this prefix list.
        """
        return pulumi.get(self, "owner_id")

    @owner_id.setter
    def owner_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "owner_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Map of tags to assign to this resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "tags_all")

    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags_all", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[int]]:
        """
        Latest version of this prefix list.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "version", value)


class ManagedPrefixList(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 address_family: Optional[pulumi.Input[str]] = None,
                 entries: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ManagedPrefixListEntryArgs']]]]] = None,
                 max_entries: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        ## Example Usage

        Basic usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.ec2.ManagedPrefixList("example",
            address_family="IPv4",
            max_entries=5,
            entries=[
                aws.ec2.ManagedPrefixListEntryArgs(
                    cidr=aws_vpc["example"]["cidr_block"],
                    description="Primary",
                ),
                aws.ec2.ManagedPrefixListEntryArgs(
                    cidr=aws_vpc_ipv4_cidr_block_association["example"]["cidr_block"],
                    description="Secondary",
                ),
            ],
            tags={
                "Env": "live",
            })
        ```

        ## Import

        Prefix Lists can be imported using the `id`, e.g.,

        ```sh
         $ pulumi import aws:ec2/managedPrefixList:ManagedPrefixList default pl-0570a1d2d725c16be
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] address_family: Address family (`IPv4` or `IPv6`) of this prefix list.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ManagedPrefixListEntryArgs']]]] entries: Configuration block for prefix list entry. Detailed below. Different entries may have overlapping CIDR blocks, but a particular CIDR should not be duplicated.
        :param pulumi.Input[int] max_entries: Maximum number of entries that this prefix list can contain.
        :param pulumi.Input[str] name: Name of this resource. The name must not start with `com.amazonaws`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Map of tags to assign to this resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ManagedPrefixListArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        Basic usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.ec2.ManagedPrefixList("example",
            address_family="IPv4",
            max_entries=5,
            entries=[
                aws.ec2.ManagedPrefixListEntryArgs(
                    cidr=aws_vpc["example"]["cidr_block"],
                    description="Primary",
                ),
                aws.ec2.ManagedPrefixListEntryArgs(
                    cidr=aws_vpc_ipv4_cidr_block_association["example"]["cidr_block"],
                    description="Secondary",
                ),
            ],
            tags={
                "Env": "live",
            })
        ```

        ## Import

        Prefix Lists can be imported using the `id`, e.g.,

        ```sh
         $ pulumi import aws:ec2/managedPrefixList:ManagedPrefixList default pl-0570a1d2d725c16be
        ```

        :param str resource_name: The name of the resource.
        :param ManagedPrefixListArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ManagedPrefixListArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 address_family: Optional[pulumi.Input[str]] = None,
                 entries: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ManagedPrefixListEntryArgs']]]]] = None,
                 max_entries: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
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
            __props__ = ManagedPrefixListArgs.__new__(ManagedPrefixListArgs)

            if address_family is None and not opts.urn:
                raise TypeError("Missing required property 'address_family'")
            __props__.__dict__["address_family"] = address_family
            __props__.__dict__["entries"] = entries
            if max_entries is None and not opts.urn:
                raise TypeError("Missing required property 'max_entries'")
            __props__.__dict__["max_entries"] = max_entries
            __props__.__dict__["name"] = name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["owner_id"] = None
            __props__.__dict__["tags_all"] = None
            __props__.__dict__["version"] = None
        super(ManagedPrefixList, __self__).__init__(
            'aws:ec2/managedPrefixList:ManagedPrefixList',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            address_family: Optional[pulumi.Input[str]] = None,
            arn: Optional[pulumi.Input[str]] = None,
            entries: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ManagedPrefixListEntryArgs']]]]] = None,
            max_entries: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            owner_id: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            version: Optional[pulumi.Input[int]] = None) -> 'ManagedPrefixList':
        """
        Get an existing ManagedPrefixList resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] address_family: Address family (`IPv4` or `IPv6`) of this prefix list.
        :param pulumi.Input[str] arn: ARN of the prefix list.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ManagedPrefixListEntryArgs']]]] entries: Configuration block for prefix list entry. Detailed below. Different entries may have overlapping CIDR blocks, but a particular CIDR should not be duplicated.
        :param pulumi.Input[int] max_entries: Maximum number of entries that this prefix list can contain.
        :param pulumi.Input[str] name: Name of this resource. The name must not start with `com.amazonaws`.
        :param pulumi.Input[str] owner_id: ID of the AWS account that owns this prefix list.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Map of tags to assign to this resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[int] version: Latest version of this prefix list.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ManagedPrefixListState.__new__(_ManagedPrefixListState)

        __props__.__dict__["address_family"] = address_family
        __props__.__dict__["arn"] = arn
        __props__.__dict__["entries"] = entries
        __props__.__dict__["max_entries"] = max_entries
        __props__.__dict__["name"] = name
        __props__.__dict__["owner_id"] = owner_id
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tags_all"] = tags_all
        __props__.__dict__["version"] = version
        return ManagedPrefixList(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="addressFamily")
    def address_family(self) -> pulumi.Output[str]:
        """
        Address family (`IPv4` or `IPv6`) of this prefix list.
        """
        return pulumi.get(self, "address_family")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        ARN of the prefix list.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def entries(self) -> pulumi.Output[Sequence['outputs.ManagedPrefixListEntry']]:
        """
        Configuration block for prefix list entry. Detailed below. Different entries may have overlapping CIDR blocks, but a particular CIDR should not be duplicated.
        """
        return pulumi.get(self, "entries")

    @property
    @pulumi.getter(name="maxEntries")
    def max_entries(self) -> pulumi.Output[int]:
        """
        Maximum number of entries that this prefix list can contain.
        """
        return pulumi.get(self, "max_entries")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of this resource. The name must not start with `com.amazonaws`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> pulumi.Output[str]:
        """
        ID of the AWS account that owns this prefix list.
        """
        return pulumi.get(self, "owner_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Map of tags to assign to this resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, str]]:
        return pulumi.get(self, "tags_all")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[int]:
        """
        Latest version of this prefix list.
        """
        return pulumi.get(self, "version")

