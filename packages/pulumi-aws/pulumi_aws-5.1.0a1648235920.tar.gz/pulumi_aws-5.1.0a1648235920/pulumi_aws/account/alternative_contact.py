# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['AlternativeContactArgs', 'AlternativeContact']

@pulumi.input_type
class AlternativeContactArgs:
    def __init__(__self__, *,
                 alternate_contact_type: pulumi.Input[str],
                 email_address: pulumi.Input[str],
                 phone_number: pulumi.Input[str],
                 title: pulumi.Input[str],
                 account_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AlternativeContact resource.
        :param pulumi.Input[str] alternate_contact_type: The type of the alternate contact. Allowed values are: `BILLING`, `OPERATIONS`, `SECURITY`.
        :param pulumi.Input[str] email_address: An email address for the alternate contact.
        :param pulumi.Input[str] phone_number: A phone number for the alternate contact.
        :param pulumi.Input[str] title: A title for the alternate contact.
        :param pulumi.Input[str] account_id: The ID of the target account when managing member accounts. Will manage current user's account by default if omitted.
        :param pulumi.Input[str] name: The name of the alternate contact.
        """
        pulumi.set(__self__, "alternate_contact_type", alternate_contact_type)
        pulumi.set(__self__, "email_address", email_address)
        pulumi.set(__self__, "phone_number", phone_number)
        pulumi.set(__self__, "title", title)
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="alternateContactType")
    def alternate_contact_type(self) -> pulumi.Input[str]:
        """
        The type of the alternate contact. Allowed values are: `BILLING`, `OPERATIONS`, `SECURITY`.
        """
        return pulumi.get(self, "alternate_contact_type")

    @alternate_contact_type.setter
    def alternate_contact_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "alternate_contact_type", value)

    @property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> pulumi.Input[str]:
        """
        An email address for the alternate contact.
        """
        return pulumi.get(self, "email_address")

    @email_address.setter
    def email_address(self, value: pulumi.Input[str]):
        pulumi.set(self, "email_address", value)

    @property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> pulumi.Input[str]:
        """
        A phone number for the alternate contact.
        """
        return pulumi.get(self, "phone_number")

    @phone_number.setter
    def phone_number(self, value: pulumi.Input[str]):
        pulumi.set(self, "phone_number", value)

    @property
    @pulumi.getter
    def title(self) -> pulumi.Input[str]:
        """
        A title for the alternate contact.
        """
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: pulumi.Input[str]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the target account when managing member accounts. Will manage current user's account by default if omitted.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the alternate contact.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _AlternativeContactState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[str]] = None,
                 alternate_contact_type: Optional[pulumi.Input[str]] = None,
                 email_address: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 phone_number: Optional[pulumi.Input[str]] = None,
                 title: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AlternativeContact resources.
        :param pulumi.Input[str] account_id: The ID of the target account when managing member accounts. Will manage current user's account by default if omitted.
        :param pulumi.Input[str] alternate_contact_type: The type of the alternate contact. Allowed values are: `BILLING`, `OPERATIONS`, `SECURITY`.
        :param pulumi.Input[str] email_address: An email address for the alternate contact.
        :param pulumi.Input[str] name: The name of the alternate contact.
        :param pulumi.Input[str] phone_number: A phone number for the alternate contact.
        :param pulumi.Input[str] title: A title for the alternate contact.
        """
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if alternate_contact_type is not None:
            pulumi.set(__self__, "alternate_contact_type", alternate_contact_type)
        if email_address is not None:
            pulumi.set(__self__, "email_address", email_address)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if phone_number is not None:
            pulumi.set(__self__, "phone_number", phone_number)
        if title is not None:
            pulumi.set(__self__, "title", title)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the target account when managing member accounts. Will manage current user's account by default if omitted.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="alternateContactType")
    def alternate_contact_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the alternate contact. Allowed values are: `BILLING`, `OPERATIONS`, `SECURITY`.
        """
        return pulumi.get(self, "alternate_contact_type")

    @alternate_contact_type.setter
    def alternate_contact_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "alternate_contact_type", value)

    @property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> Optional[pulumi.Input[str]]:
        """
        An email address for the alternate contact.
        """
        return pulumi.get(self, "email_address")

    @email_address.setter
    def email_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "email_address", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the alternate contact.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> Optional[pulumi.Input[str]]:
        """
        A phone number for the alternate contact.
        """
        return pulumi.get(self, "phone_number")

    @phone_number.setter
    def phone_number(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "phone_number", value)

    @property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[str]]:
        """
        A title for the alternate contact.
        """
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "title", value)


class AlternativeContact(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 alternate_contact_type: Optional[pulumi.Input[str]] = None,
                 email_address: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 phone_number: Optional[pulumi.Input[str]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages the specified alternate contact attached to an AWS Account.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        operations = aws.account.AlternativeContact("operations",
            alternate_contact_type="OPERATIONS",
            email_address="test@example.com",
            phone_number="+1234567890",
            title="Example")
        ```

        ## Import

        The Alternate Contact for the current account can be imported using the `alternate_contact_type`, e.g.,

        ```sh
         $ pulumi import aws:account/alternativeContact:AlternativeContact operations OPERATIONS
        ```

         If you provide an account ID, the Alternate Contact can be imported using the `account_id` and `alternate_contact_type` separated by a forward slash (`/`) e.g.,

        ```sh
         $ pulumi import aws:account/alternativeContact:AlternativeContact operations 1234567890/OPERATIONS
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The ID of the target account when managing member accounts. Will manage current user's account by default if omitted.
        :param pulumi.Input[str] alternate_contact_type: The type of the alternate contact. Allowed values are: `BILLING`, `OPERATIONS`, `SECURITY`.
        :param pulumi.Input[str] email_address: An email address for the alternate contact.
        :param pulumi.Input[str] name: The name of the alternate contact.
        :param pulumi.Input[str] phone_number: A phone number for the alternate contact.
        :param pulumi.Input[str] title: A title for the alternate contact.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AlternativeContactArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages the specified alternate contact attached to an AWS Account.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        operations = aws.account.AlternativeContact("operations",
            alternate_contact_type="OPERATIONS",
            email_address="test@example.com",
            phone_number="+1234567890",
            title="Example")
        ```

        ## Import

        The Alternate Contact for the current account can be imported using the `alternate_contact_type`, e.g.,

        ```sh
         $ pulumi import aws:account/alternativeContact:AlternativeContact operations OPERATIONS
        ```

         If you provide an account ID, the Alternate Contact can be imported using the `account_id` and `alternate_contact_type` separated by a forward slash (`/`) e.g.,

        ```sh
         $ pulumi import aws:account/alternativeContact:AlternativeContact operations 1234567890/OPERATIONS
        ```

        :param str resource_name: The name of the resource.
        :param AlternativeContactArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AlternativeContactArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 alternate_contact_type: Optional[pulumi.Input[str]] = None,
                 email_address: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 phone_number: Optional[pulumi.Input[str]] = None,
                 title: Optional[pulumi.Input[str]] = None,
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
            __props__ = AlternativeContactArgs.__new__(AlternativeContactArgs)

            __props__.__dict__["account_id"] = account_id
            if alternate_contact_type is None and not opts.urn:
                raise TypeError("Missing required property 'alternate_contact_type'")
            __props__.__dict__["alternate_contact_type"] = alternate_contact_type
            if email_address is None and not opts.urn:
                raise TypeError("Missing required property 'email_address'")
            __props__.__dict__["email_address"] = email_address
            __props__.__dict__["name"] = name
            if phone_number is None and not opts.urn:
                raise TypeError("Missing required property 'phone_number'")
            __props__.__dict__["phone_number"] = phone_number
            if title is None and not opts.urn:
                raise TypeError("Missing required property 'title'")
            __props__.__dict__["title"] = title
        super(AlternativeContact, __self__).__init__(
            'aws:account/alternativeContact:AlternativeContact',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            alternate_contact_type: Optional[pulumi.Input[str]] = None,
            email_address: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            phone_number: Optional[pulumi.Input[str]] = None,
            title: Optional[pulumi.Input[str]] = None) -> 'AlternativeContact':
        """
        Get an existing AlternativeContact resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The ID of the target account when managing member accounts. Will manage current user's account by default if omitted.
        :param pulumi.Input[str] alternate_contact_type: The type of the alternate contact. Allowed values are: `BILLING`, `OPERATIONS`, `SECURITY`.
        :param pulumi.Input[str] email_address: An email address for the alternate contact.
        :param pulumi.Input[str] name: The name of the alternate contact.
        :param pulumi.Input[str] phone_number: A phone number for the alternate contact.
        :param pulumi.Input[str] title: A title for the alternate contact.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AlternativeContactState.__new__(_AlternativeContactState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["alternate_contact_type"] = alternate_contact_type
        __props__.__dict__["email_address"] = email_address
        __props__.__dict__["name"] = name
        __props__.__dict__["phone_number"] = phone_number
        __props__.__dict__["title"] = title
        return AlternativeContact(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the target account when managing member accounts. Will manage current user's account by default if omitted.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="alternateContactType")
    def alternate_contact_type(self) -> pulumi.Output[str]:
        """
        The type of the alternate contact. Allowed values are: `BILLING`, `OPERATIONS`, `SECURITY`.
        """
        return pulumi.get(self, "alternate_contact_type")

    @property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> pulumi.Output[str]:
        """
        An email address for the alternate contact.
        """
        return pulumi.get(self, "email_address")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the alternate contact.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> pulumi.Output[str]:
        """
        A phone number for the alternate contact.
        """
        return pulumi.get(self, "phone_number")

    @property
    @pulumi.getter
    def title(self) -> pulumi.Output[str]:
        """
        A title for the alternate contact.
        """
        return pulumi.get(self, "title")

