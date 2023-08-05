# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'DomainEndpointOptions',
    'DomainIndexField',
    'DomainScalingParameters',
]

@pulumi.output_type
class DomainEndpointOptions(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "enforceHttps":
            suggest = "enforce_https"
        elif key == "tlsSecurityPolicy":
            suggest = "tls_security_policy"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DomainEndpointOptions. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DomainEndpointOptions.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DomainEndpointOptions.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 enforce_https: Optional[bool] = None,
                 tls_security_policy: Optional[str] = None):
        """
        :param bool enforce_https: Enables or disables the requirement that all requests to the domain arrive over HTTPS.
        :param str tls_security_policy: The minimum required TLS version. See the [AWS documentation](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DomainEndpointOptions.html) for valid values.
        """
        if enforce_https is not None:
            pulumi.set(__self__, "enforce_https", enforce_https)
        if tls_security_policy is not None:
            pulumi.set(__self__, "tls_security_policy", tls_security_policy)

    @property
    @pulumi.getter(name="enforceHttps")
    def enforce_https(self) -> Optional[bool]:
        """
        Enables or disables the requirement that all requests to the domain arrive over HTTPS.
        """
        return pulumi.get(self, "enforce_https")

    @property
    @pulumi.getter(name="tlsSecurityPolicy")
    def tls_security_policy(self) -> Optional[str]:
        """
        The minimum required TLS version. See the [AWS documentation](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DomainEndpointOptions.html) for valid values.
        """
        return pulumi.get(self, "tls_security_policy")


@pulumi.output_type
class DomainIndexField(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "analysisScheme":
            suggest = "analysis_scheme"
        elif key == "defaultValue":
            suggest = "default_value"
        elif key == "return":
            suggest = "return_"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DomainIndexField. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DomainIndexField.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DomainIndexField.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 name: str,
                 type: str,
                 analysis_scheme: Optional[str] = None,
                 default_value: Optional[str] = None,
                 facet: Optional[bool] = None,
                 highlight: Optional[bool] = None,
                 return_: Optional[bool] = None,
                 search: Optional[bool] = None,
                 sort: Optional[bool] = None):
        """
        :param str name: A unique name for the field. Field names must begin with a letter and be at least 3 and no more than 64 characters long. The allowed characters are: `a`-`z` (lower-case letters), `0`-`9`, and `_` (underscore). The name `score` is reserved and cannot be used as a field name.
        :param str type: The field type. Valid values: `date`, `date-array`, `double`, `double-array`, `int`, `int-array`, `literal`, `literal-array`, `text`, `text-array`.
        :param str analysis_scheme: The analysis scheme you want to use for a `text` field. The analysis scheme specifies the language-specific text processing options that are used during indexing.
        :param str default_value: The default value for the field. This value is used when no value is specified for the field in the document data.
        :param bool facet: You can get facet information by enabling this.
        :param bool highlight: You can highlight information.
        :param bool return_: You can enable returning the value of all searchable fields.
        :param bool search: You can set whether this index should be searchable or not.
        :param bool sort: You can enable the property to be sortable.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "type", type)
        if analysis_scheme is not None:
            pulumi.set(__self__, "analysis_scheme", analysis_scheme)
        if default_value is not None:
            pulumi.set(__self__, "default_value", default_value)
        if facet is not None:
            pulumi.set(__self__, "facet", facet)
        if highlight is not None:
            pulumi.set(__self__, "highlight", highlight)
        if return_ is not None:
            pulumi.set(__self__, "return_", return_)
        if search is not None:
            pulumi.set(__self__, "search", search)
        if sort is not None:
            pulumi.set(__self__, "sort", sort)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        A unique name for the field. Field names must begin with a letter and be at least 3 and no more than 64 characters long. The allowed characters are: `a`-`z` (lower-case letters), `0`-`9`, and `_` (underscore). The name `score` is reserved and cannot be used as a field name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The field type. Valid values: `date`, `date-array`, `double`, `double-array`, `int`, `int-array`, `literal`, `literal-array`, `text`, `text-array`.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="analysisScheme")
    def analysis_scheme(self) -> Optional[str]:
        """
        The analysis scheme you want to use for a `text` field. The analysis scheme specifies the language-specific text processing options that are used during indexing.
        """
        return pulumi.get(self, "analysis_scheme")

    @property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> Optional[str]:
        """
        The default value for the field. This value is used when no value is specified for the field in the document data.
        """
        return pulumi.get(self, "default_value")

    @property
    @pulumi.getter
    def facet(self) -> Optional[bool]:
        """
        You can get facet information by enabling this.
        """
        return pulumi.get(self, "facet")

    @property
    @pulumi.getter
    def highlight(self) -> Optional[bool]:
        """
        You can highlight information.
        """
        return pulumi.get(self, "highlight")

    @property
    @pulumi.getter(name="return")
    def return_(self) -> Optional[bool]:
        """
        You can enable returning the value of all searchable fields.
        """
        return pulumi.get(self, "return_")

    @property
    @pulumi.getter
    def search(self) -> Optional[bool]:
        """
        You can set whether this index should be searchable or not.
        """
        return pulumi.get(self, "search")

    @property
    @pulumi.getter
    def sort(self) -> Optional[bool]:
        """
        You can enable the property to be sortable.
        """
        return pulumi.get(self, "sort")


@pulumi.output_type
class DomainScalingParameters(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "desiredInstanceType":
            suggest = "desired_instance_type"
        elif key == "desiredPartitionCount":
            suggest = "desired_partition_count"
        elif key == "desiredReplicationCount":
            suggest = "desired_replication_count"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DomainScalingParameters. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DomainScalingParameters.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DomainScalingParameters.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 desired_instance_type: Optional[str] = None,
                 desired_partition_count: Optional[int] = None,
                 desired_replication_count: Optional[int] = None):
        """
        :param str desired_instance_type: The instance type that you want to preconfigure for your domain. See the [AWS documentation](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_ScalingParameters.html) for valid values.
        :param int desired_partition_count: The number of partitions you want to preconfigure for your domain. Only valid when you select `search.2xlarge` as the instance type.
        :param int desired_replication_count: The number of replicas you want to preconfigure for each index partition.
        """
        if desired_instance_type is not None:
            pulumi.set(__self__, "desired_instance_type", desired_instance_type)
        if desired_partition_count is not None:
            pulumi.set(__self__, "desired_partition_count", desired_partition_count)
        if desired_replication_count is not None:
            pulumi.set(__self__, "desired_replication_count", desired_replication_count)

    @property
    @pulumi.getter(name="desiredInstanceType")
    def desired_instance_type(self) -> Optional[str]:
        """
        The instance type that you want to preconfigure for your domain. See the [AWS documentation](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_ScalingParameters.html) for valid values.
        """
        return pulumi.get(self, "desired_instance_type")

    @property
    @pulumi.getter(name="desiredPartitionCount")
    def desired_partition_count(self) -> Optional[int]:
        """
        The number of partitions you want to preconfigure for your domain. Only valid when you select `search.2xlarge` as the instance type.
        """
        return pulumi.get(self, "desired_partition_count")

    @property
    @pulumi.getter(name="desiredReplicationCount")
    def desired_replication_count(self) -> Optional[int]:
        """
        The number of replicas you want to preconfigure for each index partition.
        """
        return pulumi.get(self, "desired_replication_count")


