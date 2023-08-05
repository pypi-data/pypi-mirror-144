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

__all__ = ['AccessPointArgs', 'AccessPoint']

@pulumi.input_type
class AccessPointArgs:
    def __init__(__self__, *,
                 bucket: pulumi.Input[str],
                 account_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 policy: Optional[pulumi.Input[str]] = None,
                 public_access_block_configuration: Optional[pulumi.Input['AccessPointPublicAccessBlockConfigurationArgs']] = None,
                 vpc_configuration: Optional[pulumi.Input['AccessPointVpcConfigurationArgs']] = None):
        """
        The set of arguments for constructing a AccessPoint resource.
        :param pulumi.Input[str] bucket: Name of an AWS Partition S3 Bucket or the Amazon Resource Name (ARN) of S3 on Outposts Bucket that you want to associate this access point with.
        :param pulumi.Input[str] account_id: AWS account ID for the owner of the bucket for which you want to create an access point. Defaults to automatically determined account ID of the AWS provider.
        :param pulumi.Input[str] name: Name you want to assign to this access point.
        :param pulumi.Input[str] policy: Valid JSON document that specifies the policy that you want to apply to this access point. Removing `policy` from your configuration or setting `policy` to null or an empty string (i.e., `policy = ""`) _will not_ delete the policy since it could have been set by `s3control.AccessPointPolicy`. To remove the `policy`, set it to `"{}"` (an empty JSON document).
        :param pulumi.Input['AccessPointPublicAccessBlockConfigurationArgs'] public_access_block_configuration: Configuration block to manage the `PublicAccessBlock` configuration that you want to apply to this Amazon S3 bucket. You can enable the configuration options in any combination. Detailed below.
        :param pulumi.Input['AccessPointVpcConfigurationArgs'] vpc_configuration: Configuration block to restrict access to this access point to requests from the specified Virtual Private Cloud (VPC). Required for S3 on Outposts. Detailed below.
        """
        pulumi.set(__self__, "bucket", bucket)
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if policy is not None:
            pulumi.set(__self__, "policy", policy)
        if public_access_block_configuration is not None:
            pulumi.set(__self__, "public_access_block_configuration", public_access_block_configuration)
        if vpc_configuration is not None:
            pulumi.set(__self__, "vpc_configuration", vpc_configuration)

    @property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[str]:
        """
        Name of an AWS Partition S3 Bucket or the Amazon Resource Name (ARN) of S3 on Outposts Bucket that you want to associate this access point with.
        """
        return pulumi.get(self, "bucket")

    @bucket.setter
    def bucket(self, value: pulumi.Input[str]):
        pulumi.set(self, "bucket", value)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        AWS account ID for the owner of the bucket for which you want to create an access point. Defaults to automatically determined account ID of the AWS provider.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name you want to assign to this access point.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[str]]:
        """
        Valid JSON document that specifies the policy that you want to apply to this access point. Removing `policy` from your configuration or setting `policy` to null or an empty string (i.e., `policy = ""`) _will not_ delete the policy since it could have been set by `s3control.AccessPointPolicy`. To remove the `policy`, set it to `"{}"` (an empty JSON document).
        """
        return pulumi.get(self, "policy")

    @policy.setter
    def policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy", value)

    @property
    @pulumi.getter(name="publicAccessBlockConfiguration")
    def public_access_block_configuration(self) -> Optional[pulumi.Input['AccessPointPublicAccessBlockConfigurationArgs']]:
        """
        Configuration block to manage the `PublicAccessBlock` configuration that you want to apply to this Amazon S3 bucket. You can enable the configuration options in any combination. Detailed below.
        """
        return pulumi.get(self, "public_access_block_configuration")

    @public_access_block_configuration.setter
    def public_access_block_configuration(self, value: Optional[pulumi.Input['AccessPointPublicAccessBlockConfigurationArgs']]):
        pulumi.set(self, "public_access_block_configuration", value)

    @property
    @pulumi.getter(name="vpcConfiguration")
    def vpc_configuration(self) -> Optional[pulumi.Input['AccessPointVpcConfigurationArgs']]:
        """
        Configuration block to restrict access to this access point to requests from the specified Virtual Private Cloud (VPC). Required for S3 on Outposts. Detailed below.
        """
        return pulumi.get(self, "vpc_configuration")

    @vpc_configuration.setter
    def vpc_configuration(self, value: Optional[pulumi.Input['AccessPointVpcConfigurationArgs']]):
        pulumi.set(self, "vpc_configuration", value)


@pulumi.input_type
class _AccessPointState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[str]] = None,
                 alias: Optional[pulumi.Input[str]] = None,
                 arn: Optional[pulumi.Input[str]] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 endpoints: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 has_public_access_policy: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_origin: Optional[pulumi.Input[str]] = None,
                 policy: Optional[pulumi.Input[str]] = None,
                 public_access_block_configuration: Optional[pulumi.Input['AccessPointPublicAccessBlockConfigurationArgs']] = None,
                 vpc_configuration: Optional[pulumi.Input['AccessPointVpcConfigurationArgs']] = None):
        """
        Input properties used for looking up and filtering AccessPoint resources.
        :param pulumi.Input[str] account_id: AWS account ID for the owner of the bucket for which you want to create an access point. Defaults to automatically determined account ID of the AWS provider.
        :param pulumi.Input[str] alias: The alias of the S3 Access Point.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) of the S3 Access Point.
        :param pulumi.Input[str] bucket: Name of an AWS Partition S3 Bucket or the Amazon Resource Name (ARN) of S3 on Outposts Bucket that you want to associate this access point with.
        :param pulumi.Input[str] domain_name: The DNS domain name of the S3 Access Point in the format _`name`_-_`account_id`_.s3-accesspoint._region_.amazonaws.com.
               Note: S3 access points only support secure access by HTTPS. HTTP isn't supported.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] endpoints: The VPC endpoints for the S3 Access Point.
        :param pulumi.Input[bool] has_public_access_policy: Indicates whether this access point currently has a policy that allows public access.
        :param pulumi.Input[str] name: Name you want to assign to this access point.
        :param pulumi.Input[str] network_origin: Indicates whether this access point allows access from the public Internet. Values are `VPC` (the access point doesn't allow access from the public Internet) and `Internet` (the access point allows access from the public Internet, subject to the access point and bucket access policies).
        :param pulumi.Input[str] policy: Valid JSON document that specifies the policy that you want to apply to this access point. Removing `policy` from your configuration or setting `policy` to null or an empty string (i.e., `policy = ""`) _will not_ delete the policy since it could have been set by `s3control.AccessPointPolicy`. To remove the `policy`, set it to `"{}"` (an empty JSON document).
        :param pulumi.Input['AccessPointPublicAccessBlockConfigurationArgs'] public_access_block_configuration: Configuration block to manage the `PublicAccessBlock` configuration that you want to apply to this Amazon S3 bucket. You can enable the configuration options in any combination. Detailed below.
        :param pulumi.Input['AccessPointVpcConfigurationArgs'] vpc_configuration: Configuration block to restrict access to this access point to requests from the specified Virtual Private Cloud (VPC). Required for S3 on Outposts. Detailed below.
        """
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if alias is not None:
            pulumi.set(__self__, "alias", alias)
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if bucket is not None:
            pulumi.set(__self__, "bucket", bucket)
        if domain_name is not None:
            pulumi.set(__self__, "domain_name", domain_name)
        if endpoints is not None:
            pulumi.set(__self__, "endpoints", endpoints)
        if has_public_access_policy is not None:
            pulumi.set(__self__, "has_public_access_policy", has_public_access_policy)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if network_origin is not None:
            pulumi.set(__self__, "network_origin", network_origin)
        if policy is not None:
            pulumi.set(__self__, "policy", policy)
        if public_access_block_configuration is not None:
            pulumi.set(__self__, "public_access_block_configuration", public_access_block_configuration)
        if vpc_configuration is not None:
            pulumi.set(__self__, "vpc_configuration", vpc_configuration)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        AWS account ID for the owner of the bucket for which you want to create an access point. Defaults to automatically determined account ID of the AWS provider.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter
    def alias(self) -> Optional[pulumi.Input[str]]:
        """
        The alias of the S3 Access Point.
        """
        return pulumi.get(self, "alias")

    @alias.setter
    def alias(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "alias", value)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        Amazon Resource Name (ARN) of the S3 Access Point.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[str]]:
        """
        Name of an AWS Partition S3 Bucket or the Amazon Resource Name (ARN) of S3 on Outposts Bucket that you want to associate this access point with.
        """
        return pulumi.get(self, "bucket")

    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bucket", value)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[str]]:
        """
        The DNS domain name of the S3 Access Point in the format _`name`_-_`account_id`_.s3-accesspoint._region_.amazonaws.com.
        Note: S3 access points only support secure access by HTTPS. HTTP isn't supported.
        """
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain_name", value)

    @property
    @pulumi.getter
    def endpoints(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The VPC endpoints for the S3 Access Point.
        """
        return pulumi.get(self, "endpoints")

    @endpoints.setter
    def endpoints(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "endpoints", value)

    @property
    @pulumi.getter(name="hasPublicAccessPolicy")
    def has_public_access_policy(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether this access point currently has a policy that allows public access.
        """
        return pulumi.get(self, "has_public_access_policy")

    @has_public_access_policy.setter
    def has_public_access_policy(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "has_public_access_policy", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name you want to assign to this access point.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="networkOrigin")
    def network_origin(self) -> Optional[pulumi.Input[str]]:
        """
        Indicates whether this access point allows access from the public Internet. Values are `VPC` (the access point doesn't allow access from the public Internet) and `Internet` (the access point allows access from the public Internet, subject to the access point and bucket access policies).
        """
        return pulumi.get(self, "network_origin")

    @network_origin.setter
    def network_origin(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_origin", value)

    @property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[str]]:
        """
        Valid JSON document that specifies the policy that you want to apply to this access point. Removing `policy` from your configuration or setting `policy` to null or an empty string (i.e., `policy = ""`) _will not_ delete the policy since it could have been set by `s3control.AccessPointPolicy`. To remove the `policy`, set it to `"{}"` (an empty JSON document).
        """
        return pulumi.get(self, "policy")

    @policy.setter
    def policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy", value)

    @property
    @pulumi.getter(name="publicAccessBlockConfiguration")
    def public_access_block_configuration(self) -> Optional[pulumi.Input['AccessPointPublicAccessBlockConfigurationArgs']]:
        """
        Configuration block to manage the `PublicAccessBlock` configuration that you want to apply to this Amazon S3 bucket. You can enable the configuration options in any combination. Detailed below.
        """
        return pulumi.get(self, "public_access_block_configuration")

    @public_access_block_configuration.setter
    def public_access_block_configuration(self, value: Optional[pulumi.Input['AccessPointPublicAccessBlockConfigurationArgs']]):
        pulumi.set(self, "public_access_block_configuration", value)

    @property
    @pulumi.getter(name="vpcConfiguration")
    def vpc_configuration(self) -> Optional[pulumi.Input['AccessPointVpcConfigurationArgs']]:
        """
        Configuration block to restrict access to this access point to requests from the specified Virtual Private Cloud (VPC). Required for S3 on Outposts. Detailed below.
        """
        return pulumi.get(self, "vpc_configuration")

    @vpc_configuration.setter
    def vpc_configuration(self, value: Optional[pulumi.Input['AccessPointVpcConfigurationArgs']]):
        pulumi.set(self, "vpc_configuration", value)


class AccessPoint(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 policy: Optional[pulumi.Input[str]] = None,
                 public_access_block_configuration: Optional[pulumi.Input[pulumi.InputType['AccessPointPublicAccessBlockConfigurationArgs']]] = None,
                 vpc_configuration: Optional[pulumi.Input[pulumi.InputType['AccessPointVpcConfigurationArgs']]] = None,
                 __props__=None):
        """
        Provides a resource to manage an S3 Access Point.

        > **NOTE on Access Points and Access Point Policies:** This provider provides both a standalone Access Point Policy resource and an Access Point resource with a resource policy defined in-line. You cannot use an Access Point with in-line resource policy in conjunction with an Access Point Policy resource. Doing so will cause a conflict of policies and will overwrite the access point's resource policy.

        > Advanced usage: To use a custom API endpoint for this resource, use the `s3control` endpoint provider configuration), not the `s3` endpoint provider configuration.

        ## Example Usage
        ### AWS Partition Bucket

        ```python
        import pulumi
        import pulumi_aws as aws

        example_bucket_v2 = aws.s3.BucketV2("exampleBucketV2")
        example_access_point = aws.s3.AccessPoint("exampleAccessPoint", bucket=example_bucket_v2.id)
        ```
        ### S3 on Outposts Bucket

        ```python
        import pulumi
        import pulumi_aws as aws

        example_bucket = aws.s3control.Bucket("exampleBucket", bucket="example")
        example_vpc = aws.ec2.Vpc("exampleVpc", cidr_block="10.0.0.0/16")
        example_access_point = aws.s3.AccessPoint("exampleAccessPoint",
            bucket=example_bucket.arn,
            vpc_configuration=aws.s3.AccessPointVpcConfigurationArgs(
                vpc_id=example_vpc.id,
            ))
        ```

        ## Import

        For Access Points associated with an AWS Partition S3 Bucket, this resource can be imported using the `account_id` and `name` separated by a colon (`:`), e.g.,

        ```sh
         $ pulumi import aws:s3/accessPoint:AccessPoint example 123456789012:example
        ```

         For Access Points associated with an S3 on Outposts Bucket, this resource can be imported using the Amazon Resource Name (ARN), e.g.,

        ```sh
         $ pulumi import aws:s3/accessPoint:AccessPoint example arn:aws:s3-outposts:us-east-1:123456789012:outpost/op-1234567890123456/accesspoint/example
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: AWS account ID for the owner of the bucket for which you want to create an access point. Defaults to automatically determined account ID of the AWS provider.
        :param pulumi.Input[str] bucket: Name of an AWS Partition S3 Bucket or the Amazon Resource Name (ARN) of S3 on Outposts Bucket that you want to associate this access point with.
        :param pulumi.Input[str] name: Name you want to assign to this access point.
        :param pulumi.Input[str] policy: Valid JSON document that specifies the policy that you want to apply to this access point. Removing `policy` from your configuration or setting `policy` to null or an empty string (i.e., `policy = ""`) _will not_ delete the policy since it could have been set by `s3control.AccessPointPolicy`. To remove the `policy`, set it to `"{}"` (an empty JSON document).
        :param pulumi.Input[pulumi.InputType['AccessPointPublicAccessBlockConfigurationArgs']] public_access_block_configuration: Configuration block to manage the `PublicAccessBlock` configuration that you want to apply to this Amazon S3 bucket. You can enable the configuration options in any combination. Detailed below.
        :param pulumi.Input[pulumi.InputType['AccessPointVpcConfigurationArgs']] vpc_configuration: Configuration block to restrict access to this access point to requests from the specified Virtual Private Cloud (VPC). Required for S3 on Outposts. Detailed below.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AccessPointArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a resource to manage an S3 Access Point.

        > **NOTE on Access Points and Access Point Policies:** This provider provides both a standalone Access Point Policy resource and an Access Point resource with a resource policy defined in-line. You cannot use an Access Point with in-line resource policy in conjunction with an Access Point Policy resource. Doing so will cause a conflict of policies and will overwrite the access point's resource policy.

        > Advanced usage: To use a custom API endpoint for this resource, use the `s3control` endpoint provider configuration), not the `s3` endpoint provider configuration.

        ## Example Usage
        ### AWS Partition Bucket

        ```python
        import pulumi
        import pulumi_aws as aws

        example_bucket_v2 = aws.s3.BucketV2("exampleBucketV2")
        example_access_point = aws.s3.AccessPoint("exampleAccessPoint", bucket=example_bucket_v2.id)
        ```
        ### S3 on Outposts Bucket

        ```python
        import pulumi
        import pulumi_aws as aws

        example_bucket = aws.s3control.Bucket("exampleBucket", bucket="example")
        example_vpc = aws.ec2.Vpc("exampleVpc", cidr_block="10.0.0.0/16")
        example_access_point = aws.s3.AccessPoint("exampleAccessPoint",
            bucket=example_bucket.arn,
            vpc_configuration=aws.s3.AccessPointVpcConfigurationArgs(
                vpc_id=example_vpc.id,
            ))
        ```

        ## Import

        For Access Points associated with an AWS Partition S3 Bucket, this resource can be imported using the `account_id` and `name` separated by a colon (`:`), e.g.,

        ```sh
         $ pulumi import aws:s3/accessPoint:AccessPoint example 123456789012:example
        ```

         For Access Points associated with an S3 on Outposts Bucket, this resource can be imported using the Amazon Resource Name (ARN), e.g.,

        ```sh
         $ pulumi import aws:s3/accessPoint:AccessPoint example arn:aws:s3-outposts:us-east-1:123456789012:outpost/op-1234567890123456/accesspoint/example
        ```

        :param str resource_name: The name of the resource.
        :param AccessPointArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AccessPointArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 policy: Optional[pulumi.Input[str]] = None,
                 public_access_block_configuration: Optional[pulumi.Input[pulumi.InputType['AccessPointPublicAccessBlockConfigurationArgs']]] = None,
                 vpc_configuration: Optional[pulumi.Input[pulumi.InputType['AccessPointVpcConfigurationArgs']]] = None,
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
            __props__ = AccessPointArgs.__new__(AccessPointArgs)

            __props__.__dict__["account_id"] = account_id
            if bucket is None and not opts.urn:
                raise TypeError("Missing required property 'bucket'")
            __props__.__dict__["bucket"] = bucket
            __props__.__dict__["name"] = name
            __props__.__dict__["policy"] = policy
            __props__.__dict__["public_access_block_configuration"] = public_access_block_configuration
            __props__.__dict__["vpc_configuration"] = vpc_configuration
            __props__.__dict__["alias"] = None
            __props__.__dict__["arn"] = None
            __props__.__dict__["domain_name"] = None
            __props__.__dict__["endpoints"] = None
            __props__.__dict__["has_public_access_policy"] = None
            __props__.__dict__["network_origin"] = None
        super(AccessPoint, __self__).__init__(
            'aws:s3/accessPoint:AccessPoint',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            alias: Optional[pulumi.Input[str]] = None,
            arn: Optional[pulumi.Input[str]] = None,
            bucket: Optional[pulumi.Input[str]] = None,
            domain_name: Optional[pulumi.Input[str]] = None,
            endpoints: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            has_public_access_policy: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            network_origin: Optional[pulumi.Input[str]] = None,
            policy: Optional[pulumi.Input[str]] = None,
            public_access_block_configuration: Optional[pulumi.Input[pulumi.InputType['AccessPointPublicAccessBlockConfigurationArgs']]] = None,
            vpc_configuration: Optional[pulumi.Input[pulumi.InputType['AccessPointVpcConfigurationArgs']]] = None) -> 'AccessPoint':
        """
        Get an existing AccessPoint resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: AWS account ID for the owner of the bucket for which you want to create an access point. Defaults to automatically determined account ID of the AWS provider.
        :param pulumi.Input[str] alias: The alias of the S3 Access Point.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) of the S3 Access Point.
        :param pulumi.Input[str] bucket: Name of an AWS Partition S3 Bucket or the Amazon Resource Name (ARN) of S3 on Outposts Bucket that you want to associate this access point with.
        :param pulumi.Input[str] domain_name: The DNS domain name of the S3 Access Point in the format _`name`_-_`account_id`_.s3-accesspoint._region_.amazonaws.com.
               Note: S3 access points only support secure access by HTTPS. HTTP isn't supported.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] endpoints: The VPC endpoints for the S3 Access Point.
        :param pulumi.Input[bool] has_public_access_policy: Indicates whether this access point currently has a policy that allows public access.
        :param pulumi.Input[str] name: Name you want to assign to this access point.
        :param pulumi.Input[str] network_origin: Indicates whether this access point allows access from the public Internet. Values are `VPC` (the access point doesn't allow access from the public Internet) and `Internet` (the access point allows access from the public Internet, subject to the access point and bucket access policies).
        :param pulumi.Input[str] policy: Valid JSON document that specifies the policy that you want to apply to this access point. Removing `policy` from your configuration or setting `policy` to null or an empty string (i.e., `policy = ""`) _will not_ delete the policy since it could have been set by `s3control.AccessPointPolicy`. To remove the `policy`, set it to `"{}"` (an empty JSON document).
        :param pulumi.Input[pulumi.InputType['AccessPointPublicAccessBlockConfigurationArgs']] public_access_block_configuration: Configuration block to manage the `PublicAccessBlock` configuration that you want to apply to this Amazon S3 bucket. You can enable the configuration options in any combination. Detailed below.
        :param pulumi.Input[pulumi.InputType['AccessPointVpcConfigurationArgs']] vpc_configuration: Configuration block to restrict access to this access point to requests from the specified Virtual Private Cloud (VPC). Required for S3 on Outposts. Detailed below.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AccessPointState.__new__(_AccessPointState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["alias"] = alias
        __props__.__dict__["arn"] = arn
        __props__.__dict__["bucket"] = bucket
        __props__.__dict__["domain_name"] = domain_name
        __props__.__dict__["endpoints"] = endpoints
        __props__.__dict__["has_public_access_policy"] = has_public_access_policy
        __props__.__dict__["name"] = name
        __props__.__dict__["network_origin"] = network_origin
        __props__.__dict__["policy"] = policy
        __props__.__dict__["public_access_block_configuration"] = public_access_block_configuration
        __props__.__dict__["vpc_configuration"] = vpc_configuration
        return AccessPoint(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[str]:
        """
        AWS account ID for the owner of the bucket for which you want to create an access point. Defaults to automatically determined account ID of the AWS provider.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter
    def alias(self) -> pulumi.Output[str]:
        """
        The alias of the S3 Access Point.
        """
        return pulumi.get(self, "alias")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Amazon Resource Name (ARN) of the S3 Access Point.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def bucket(self) -> pulumi.Output[str]:
        """
        Name of an AWS Partition S3 Bucket or the Amazon Resource Name (ARN) of S3 on Outposts Bucket that you want to associate this access point with.
        """
        return pulumi.get(self, "bucket")

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[str]:
        """
        The DNS domain name of the S3 Access Point in the format _`name`_-_`account_id`_.s3-accesspoint._region_.amazonaws.com.
        Note: S3 access points only support secure access by HTTPS. HTTP isn't supported.
        """
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter
    def endpoints(self) -> pulumi.Output[Mapping[str, str]]:
        """
        The VPC endpoints for the S3 Access Point.
        """
        return pulumi.get(self, "endpoints")

    @property
    @pulumi.getter(name="hasPublicAccessPolicy")
    def has_public_access_policy(self) -> pulumi.Output[bool]:
        """
        Indicates whether this access point currently has a policy that allows public access.
        """
        return pulumi.get(self, "has_public_access_policy")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name you want to assign to this access point.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkOrigin")
    def network_origin(self) -> pulumi.Output[str]:
        """
        Indicates whether this access point allows access from the public Internet. Values are `VPC` (the access point doesn't allow access from the public Internet) and `Internet` (the access point allows access from the public Internet, subject to the access point and bucket access policies).
        """
        return pulumi.get(self, "network_origin")

    @property
    @pulumi.getter
    def policy(self) -> pulumi.Output[str]:
        """
        Valid JSON document that specifies the policy that you want to apply to this access point. Removing `policy` from your configuration or setting `policy` to null or an empty string (i.e., `policy = ""`) _will not_ delete the policy since it could have been set by `s3control.AccessPointPolicy`. To remove the `policy`, set it to `"{}"` (an empty JSON document).
        """
        return pulumi.get(self, "policy")

    @property
    @pulumi.getter(name="publicAccessBlockConfiguration")
    def public_access_block_configuration(self) -> pulumi.Output[Optional['outputs.AccessPointPublicAccessBlockConfiguration']]:
        """
        Configuration block to manage the `PublicAccessBlock` configuration that you want to apply to this Amazon S3 bucket. You can enable the configuration options in any combination. Detailed below.
        """
        return pulumi.get(self, "public_access_block_configuration")

    @property
    @pulumi.getter(name="vpcConfiguration")
    def vpc_configuration(self) -> pulumi.Output[Optional['outputs.AccessPointVpcConfiguration']]:
        """
        Configuration block to restrict access to this access point to requests from the specified Virtual Private Cloud (VPC). Required for S3 on Outposts. Detailed below.
        """
        return pulumi.get(self, "vpc_configuration")

