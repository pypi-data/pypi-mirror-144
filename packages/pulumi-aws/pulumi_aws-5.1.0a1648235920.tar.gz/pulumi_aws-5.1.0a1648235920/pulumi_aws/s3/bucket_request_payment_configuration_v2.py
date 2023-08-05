# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['BucketRequestPaymentConfigurationV2Args', 'BucketRequestPaymentConfigurationV2']

@pulumi.input_type
class BucketRequestPaymentConfigurationV2Args:
    def __init__(__self__, *,
                 bucket: pulumi.Input[str],
                 payer: pulumi.Input[str],
                 expected_bucket_owner: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a BucketRequestPaymentConfigurationV2 resource.
        :param pulumi.Input[str] bucket: The name of the bucket.
        :param pulumi.Input[str] payer: Specifies who pays for the download and request fees. Valid values: `BucketOwner`, `Requester`.
        :param pulumi.Input[str] expected_bucket_owner: The account ID of the expected bucket owner.
        """
        pulumi.set(__self__, "bucket", bucket)
        pulumi.set(__self__, "payer", payer)
        if expected_bucket_owner is not None:
            pulumi.set(__self__, "expected_bucket_owner", expected_bucket_owner)

    @property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[str]:
        """
        The name of the bucket.
        """
        return pulumi.get(self, "bucket")

    @bucket.setter
    def bucket(self, value: pulumi.Input[str]):
        pulumi.set(self, "bucket", value)

    @property
    @pulumi.getter
    def payer(self) -> pulumi.Input[str]:
        """
        Specifies who pays for the download and request fees. Valid values: `BucketOwner`, `Requester`.
        """
        return pulumi.get(self, "payer")

    @payer.setter
    def payer(self, value: pulumi.Input[str]):
        pulumi.set(self, "payer", value)

    @property
    @pulumi.getter(name="expectedBucketOwner")
    def expected_bucket_owner(self) -> Optional[pulumi.Input[str]]:
        """
        The account ID of the expected bucket owner.
        """
        return pulumi.get(self, "expected_bucket_owner")

    @expected_bucket_owner.setter
    def expected_bucket_owner(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expected_bucket_owner", value)


@pulumi.input_type
class _BucketRequestPaymentConfigurationV2State:
    def __init__(__self__, *,
                 bucket: Optional[pulumi.Input[str]] = None,
                 expected_bucket_owner: Optional[pulumi.Input[str]] = None,
                 payer: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering BucketRequestPaymentConfigurationV2 resources.
        :param pulumi.Input[str] bucket: The name of the bucket.
        :param pulumi.Input[str] expected_bucket_owner: The account ID of the expected bucket owner.
        :param pulumi.Input[str] payer: Specifies who pays for the download and request fees. Valid values: `BucketOwner`, `Requester`.
        """
        if bucket is not None:
            pulumi.set(__self__, "bucket", bucket)
        if expected_bucket_owner is not None:
            pulumi.set(__self__, "expected_bucket_owner", expected_bucket_owner)
        if payer is not None:
            pulumi.set(__self__, "payer", payer)

    @property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the bucket.
        """
        return pulumi.get(self, "bucket")

    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bucket", value)

    @property
    @pulumi.getter(name="expectedBucketOwner")
    def expected_bucket_owner(self) -> Optional[pulumi.Input[str]]:
        """
        The account ID of the expected bucket owner.
        """
        return pulumi.get(self, "expected_bucket_owner")

    @expected_bucket_owner.setter
    def expected_bucket_owner(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expected_bucket_owner", value)

    @property
    @pulumi.getter
    def payer(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies who pays for the download and request fees. Valid values: `BucketOwner`, `Requester`.
        """
        return pulumi.get(self, "payer")

    @payer.setter
    def payer(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "payer", value)


class BucketRequestPaymentConfigurationV2(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 expected_bucket_owner: Optional[pulumi.Input[str]] = None,
                 payer: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides an S3 bucket request payment configuration resource. For more information, see [Requester Pays Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html).

        > **NOTE:** Destroying an `s3.BucketRequestPaymentConfigurationV2` resource resets the bucket's `payer` to the S3 default: the bucket owner.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.s3.BucketRequestPaymentConfigurationV2("example",
            bucket=aws_s3_bucket["example"]["bucket"],
            payer="Requester")
        ```

        ## Import

        S3 bucket request payment configuration can be imported in one of two ways. If the owner (account ID) of the source bucket is the same account used to configure the Terraform AWS Provider, the S3 bucket request payment configuration resource should be imported using the `bucket` e.g.,

        ```sh
         $ pulumi import aws:s3/bucketRequestPaymentConfigurationV2:BucketRequestPaymentConfigurationV2 example bucket-name
        ```

         If the owner (account ID) of the source bucket differs from the account used to configure the Terraform AWS Provider, the S3 bucket request payment configuration resource should be imported using the `bucket` and `expected_bucket_owner` separated by a comma (`,`) e.g.,

        ```sh
         $ pulumi import aws:s3/bucketRequestPaymentConfigurationV2:BucketRequestPaymentConfigurationV2 example bucket-name,123456789012
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bucket: The name of the bucket.
        :param pulumi.Input[str] expected_bucket_owner: The account ID of the expected bucket owner.
        :param pulumi.Input[str] payer: Specifies who pays for the download and request fees. Valid values: `BucketOwner`, `Requester`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BucketRequestPaymentConfigurationV2Args,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides an S3 bucket request payment configuration resource. For more information, see [Requester Pays Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html).

        > **NOTE:** Destroying an `s3.BucketRequestPaymentConfigurationV2` resource resets the bucket's `payer` to the S3 default: the bucket owner.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.s3.BucketRequestPaymentConfigurationV2("example",
            bucket=aws_s3_bucket["example"]["bucket"],
            payer="Requester")
        ```

        ## Import

        S3 bucket request payment configuration can be imported in one of two ways. If the owner (account ID) of the source bucket is the same account used to configure the Terraform AWS Provider, the S3 bucket request payment configuration resource should be imported using the `bucket` e.g.,

        ```sh
         $ pulumi import aws:s3/bucketRequestPaymentConfigurationV2:BucketRequestPaymentConfigurationV2 example bucket-name
        ```

         If the owner (account ID) of the source bucket differs from the account used to configure the Terraform AWS Provider, the S3 bucket request payment configuration resource should be imported using the `bucket` and `expected_bucket_owner` separated by a comma (`,`) e.g.,

        ```sh
         $ pulumi import aws:s3/bucketRequestPaymentConfigurationV2:BucketRequestPaymentConfigurationV2 example bucket-name,123456789012
        ```

        :param str resource_name: The name of the resource.
        :param BucketRequestPaymentConfigurationV2Args args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BucketRequestPaymentConfigurationV2Args, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 expected_bucket_owner: Optional[pulumi.Input[str]] = None,
                 payer: Optional[pulumi.Input[str]] = None,
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
            __props__ = BucketRequestPaymentConfigurationV2Args.__new__(BucketRequestPaymentConfigurationV2Args)

            if bucket is None and not opts.urn:
                raise TypeError("Missing required property 'bucket'")
            __props__.__dict__["bucket"] = bucket
            __props__.__dict__["expected_bucket_owner"] = expected_bucket_owner
            if payer is None and not opts.urn:
                raise TypeError("Missing required property 'payer'")
            __props__.__dict__["payer"] = payer
        super(BucketRequestPaymentConfigurationV2, __self__).__init__(
            'aws:s3/bucketRequestPaymentConfigurationV2:BucketRequestPaymentConfigurationV2',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            bucket: Optional[pulumi.Input[str]] = None,
            expected_bucket_owner: Optional[pulumi.Input[str]] = None,
            payer: Optional[pulumi.Input[str]] = None) -> 'BucketRequestPaymentConfigurationV2':
        """
        Get an existing BucketRequestPaymentConfigurationV2 resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bucket: The name of the bucket.
        :param pulumi.Input[str] expected_bucket_owner: The account ID of the expected bucket owner.
        :param pulumi.Input[str] payer: Specifies who pays for the download and request fees. Valid values: `BucketOwner`, `Requester`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _BucketRequestPaymentConfigurationV2State.__new__(_BucketRequestPaymentConfigurationV2State)

        __props__.__dict__["bucket"] = bucket
        __props__.__dict__["expected_bucket_owner"] = expected_bucket_owner
        __props__.__dict__["payer"] = payer
        return BucketRequestPaymentConfigurationV2(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def bucket(self) -> pulumi.Output[str]:
        """
        The name of the bucket.
        """
        return pulumi.get(self, "bucket")

    @property
    @pulumi.getter(name="expectedBucketOwner")
    def expected_bucket_owner(self) -> pulumi.Output[Optional[str]]:
        """
        The account ID of the expected bucket owner.
        """
        return pulumi.get(self, "expected_bucket_owner")

    @property
    @pulumi.getter
    def payer(self) -> pulumi.Output[str]:
        """
        Specifies who pays for the download and request fees. Valid values: `BucketOwner`, `Requester`.
        """
        return pulumi.get(self, "payer")

