# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['NetworkInsightsPathArgs', 'NetworkInsightsPath']

@pulumi.input_type
class NetworkInsightsPathArgs:
    def __init__(__self__, *,
                 destination: pulumi.Input[str],
                 protocol: pulumi.Input[str],
                 source: pulumi.Input[str],
                 destination_ip: Optional[pulumi.Input[str]] = None,
                 destination_port: Optional[pulumi.Input[int]] = None,
                 source_ip: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a NetworkInsightsPath resource.
        :param pulumi.Input[str] destination: ID of the resource which is the source of the path. Can be an Instance, Internet Gateway, Network Interface, Transit Gateway, VPC Endpoint, VPC Peering Connection or VPN Gateway.
        :param pulumi.Input[str] protocol: Protocol to use for analysis. Valid options are `tcp` or `udp`.
        :param pulumi.Input[str] source: ID of the resource which is the source of the path. Can be an Instance, Internet Gateway, Network Interface, Transit Gateway, VPC Endpoint, VPC Peering Connection or VPN Gateway.
        :param pulumi.Input[str] destination_ip: IP address of the destination resource.
        :param pulumi.Input[int] destination_port: Destination port to analyze access to.
        :param pulumi.Input[str] source_ip: IP address of the source resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Map of tags to assign to the resource. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: Map of tags assigned to the resource, including those inherited from the provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block).
        """
        pulumi.set(__self__, "destination", destination)
        pulumi.set(__self__, "protocol", protocol)
        pulumi.set(__self__, "source", source)
        if destination_ip is not None:
            pulumi.set(__self__, "destination_ip", destination_ip)
        if destination_port is not None:
            pulumi.set(__self__, "destination_port", destination_port)
        if source_ip is not None:
            pulumi.set(__self__, "source_ip", source_ip)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)

    @property
    @pulumi.getter
    def destination(self) -> pulumi.Input[str]:
        """
        ID of the resource which is the source of the path. Can be an Instance, Internet Gateway, Network Interface, Transit Gateway, VPC Endpoint, VPC Peering Connection or VPN Gateway.
        """
        return pulumi.get(self, "destination")

    @destination.setter
    def destination(self, value: pulumi.Input[str]):
        pulumi.set(self, "destination", value)

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[str]:
        """
        Protocol to use for analysis. Valid options are `tcp` or `udp`.
        """
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: pulumi.Input[str]):
        pulumi.set(self, "protocol", value)

    @property
    @pulumi.getter
    def source(self) -> pulumi.Input[str]:
        """
        ID of the resource which is the source of the path. Can be an Instance, Internet Gateway, Network Interface, Transit Gateway, VPC Endpoint, VPC Peering Connection or VPN Gateway.
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: pulumi.Input[str]):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter(name="destinationIp")
    def destination_ip(self) -> Optional[pulumi.Input[str]]:
        """
        IP address of the destination resource.
        """
        return pulumi.get(self, "destination_ip")

    @destination_ip.setter
    def destination_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "destination_ip", value)

    @property
    @pulumi.getter(name="destinationPort")
    def destination_port(self) -> Optional[pulumi.Input[int]]:
        """
        Destination port to analyze access to.
        """
        return pulumi.get(self, "destination_port")

    @destination_port.setter
    def destination_port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "destination_port", value)

    @property
    @pulumi.getter(name="sourceIp")
    def source_ip(self) -> Optional[pulumi.Input[str]]:
        """
        IP address of the source resource.
        """
        return pulumi.get(self, "source_ip")

    @source_ip.setter
    def source_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_ip", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Map of tags to assign to the resource. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Map of tags assigned to the resource, including those inherited from the provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block).
        """
        return pulumi.get(self, "tags_all")

    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags_all", value)


@pulumi.input_type
class _NetworkInsightsPathState:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[str]] = None,
                 destination: Optional[pulumi.Input[str]] = None,
                 destination_ip: Optional[pulumi.Input[str]] = None,
                 destination_port: Optional[pulumi.Input[int]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 source_ip: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering NetworkInsightsPath resources.
        :param pulumi.Input[str] arn: ARN of the Network Insights Path.
        :param pulumi.Input[str] destination: ID of the resource which is the source of the path. Can be an Instance, Internet Gateway, Network Interface, Transit Gateway, VPC Endpoint, VPC Peering Connection or VPN Gateway.
        :param pulumi.Input[str] destination_ip: IP address of the destination resource.
        :param pulumi.Input[int] destination_port: Destination port to analyze access to.
        :param pulumi.Input[str] protocol: Protocol to use for analysis. Valid options are `tcp` or `udp`.
        :param pulumi.Input[str] source: ID of the resource which is the source of the path. Can be an Instance, Internet Gateway, Network Interface, Transit Gateway, VPC Endpoint, VPC Peering Connection or VPN Gateway.
        :param pulumi.Input[str] source_ip: IP address of the source resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Map of tags to assign to the resource. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: Map of tags assigned to the resource, including those inherited from the provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block).
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if destination is not None:
            pulumi.set(__self__, "destination", destination)
        if destination_ip is not None:
            pulumi.set(__self__, "destination_ip", destination_ip)
        if destination_port is not None:
            pulumi.set(__self__, "destination_port", destination_port)
        if protocol is not None:
            pulumi.set(__self__, "protocol", protocol)
        if source is not None:
            pulumi.set(__self__, "source", source)
        if source_ip is not None:
            pulumi.set(__self__, "source_ip", source_ip)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        ARN of the Network Insights Path.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter
    def destination(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the resource which is the source of the path. Can be an Instance, Internet Gateway, Network Interface, Transit Gateway, VPC Endpoint, VPC Peering Connection or VPN Gateway.
        """
        return pulumi.get(self, "destination")

    @destination.setter
    def destination(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "destination", value)

    @property
    @pulumi.getter(name="destinationIp")
    def destination_ip(self) -> Optional[pulumi.Input[str]]:
        """
        IP address of the destination resource.
        """
        return pulumi.get(self, "destination_ip")

    @destination_ip.setter
    def destination_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "destination_ip", value)

    @property
    @pulumi.getter(name="destinationPort")
    def destination_port(self) -> Optional[pulumi.Input[int]]:
        """
        Destination port to analyze access to.
        """
        return pulumi.get(self, "destination_port")

    @destination_port.setter
    def destination_port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "destination_port", value)

    @property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[str]]:
        """
        Protocol to use for analysis. Valid options are `tcp` or `udp`.
        """
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "protocol", value)

    @property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the resource which is the source of the path. Can be an Instance, Internet Gateway, Network Interface, Transit Gateway, VPC Endpoint, VPC Peering Connection or VPN Gateway.
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter(name="sourceIp")
    def source_ip(self) -> Optional[pulumi.Input[str]]:
        """
        IP address of the source resource.
        """
        return pulumi.get(self, "source_ip")

    @source_ip.setter
    def source_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_ip", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Map of tags to assign to the resource. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Map of tags assigned to the resource, including those inherited from the provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block).
        """
        return pulumi.get(self, "tags_all")

    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags_all", value)


class NetworkInsightsPath(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 destination: Optional[pulumi.Input[str]] = None,
                 destination_ip: Optional[pulumi.Input[str]] = None,
                 destination_port: Optional[pulumi.Input[int]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 source_ip: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Provides a Network Insights Path resource. Part of the "Reachability Analyzer" service in the AWS VPC console.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        test = aws.ec2.NetworkInsightsPath("test",
            source=aws_network_interface["source"]["id"],
            destination=aws_network_interface["destination"]["id"],
            protocol="tcp")
        ```

        ## Import

        Network Insights Paths can be imported using the `id`, e.g.,

        ```sh
         $ pulumi import aws:ec2/networkInsightsPath:NetworkInsightsPath test nip-00edfba169923aefd
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] destination: ID of the resource which is the source of the path. Can be an Instance, Internet Gateway, Network Interface, Transit Gateway, VPC Endpoint, VPC Peering Connection or VPN Gateway.
        :param pulumi.Input[str] destination_ip: IP address of the destination resource.
        :param pulumi.Input[int] destination_port: Destination port to analyze access to.
        :param pulumi.Input[str] protocol: Protocol to use for analysis. Valid options are `tcp` or `udp`.
        :param pulumi.Input[str] source: ID of the resource which is the source of the path. Can be an Instance, Internet Gateway, Network Interface, Transit Gateway, VPC Endpoint, VPC Peering Connection or VPN Gateway.
        :param pulumi.Input[str] source_ip: IP address of the source resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Map of tags to assign to the resource. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: Map of tags assigned to the resource, including those inherited from the provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NetworkInsightsPathArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Network Insights Path resource. Part of the "Reachability Analyzer" service in the AWS VPC console.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        test = aws.ec2.NetworkInsightsPath("test",
            source=aws_network_interface["source"]["id"],
            destination=aws_network_interface["destination"]["id"],
            protocol="tcp")
        ```

        ## Import

        Network Insights Paths can be imported using the `id`, e.g.,

        ```sh
         $ pulumi import aws:ec2/networkInsightsPath:NetworkInsightsPath test nip-00edfba169923aefd
        ```

        :param str resource_name: The name of the resource.
        :param NetworkInsightsPathArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NetworkInsightsPathArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 destination: Optional[pulumi.Input[str]] = None,
                 destination_ip: Optional[pulumi.Input[str]] = None,
                 destination_port: Optional[pulumi.Input[int]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 source_ip: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
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
            __props__ = NetworkInsightsPathArgs.__new__(NetworkInsightsPathArgs)

            if destination is None and not opts.urn:
                raise TypeError("Missing required property 'destination'")
            __props__.__dict__["destination"] = destination
            __props__.__dict__["destination_ip"] = destination_ip
            __props__.__dict__["destination_port"] = destination_port
            if protocol is None and not opts.urn:
                raise TypeError("Missing required property 'protocol'")
            __props__.__dict__["protocol"] = protocol
            if source is None and not opts.urn:
                raise TypeError("Missing required property 'source'")
            __props__.__dict__["source"] = source
            __props__.__dict__["source_ip"] = source_ip
            __props__.__dict__["tags"] = tags
            __props__.__dict__["tags_all"] = tags_all
            __props__.__dict__["arn"] = None
        super(NetworkInsightsPath, __self__).__init__(
            'aws:ec2/networkInsightsPath:NetworkInsightsPath',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            destination: Optional[pulumi.Input[str]] = None,
            destination_ip: Optional[pulumi.Input[str]] = None,
            destination_port: Optional[pulumi.Input[int]] = None,
            protocol: Optional[pulumi.Input[str]] = None,
            source: Optional[pulumi.Input[str]] = None,
            source_ip: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'NetworkInsightsPath':
        """
        Get an existing NetworkInsightsPath resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: ARN of the Network Insights Path.
        :param pulumi.Input[str] destination: ID of the resource which is the source of the path. Can be an Instance, Internet Gateway, Network Interface, Transit Gateway, VPC Endpoint, VPC Peering Connection or VPN Gateway.
        :param pulumi.Input[str] destination_ip: IP address of the destination resource.
        :param pulumi.Input[int] destination_port: Destination port to analyze access to.
        :param pulumi.Input[str] protocol: Protocol to use for analysis. Valid options are `tcp` or `udp`.
        :param pulumi.Input[str] source: ID of the resource which is the source of the path. Can be an Instance, Internet Gateway, Network Interface, Transit Gateway, VPC Endpoint, VPC Peering Connection or VPN Gateway.
        :param pulumi.Input[str] source_ip: IP address of the source resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Map of tags to assign to the resource. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: Map of tags assigned to the resource, including those inherited from the provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block).
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _NetworkInsightsPathState.__new__(_NetworkInsightsPathState)

        __props__.__dict__["arn"] = arn
        __props__.__dict__["destination"] = destination
        __props__.__dict__["destination_ip"] = destination_ip
        __props__.__dict__["destination_port"] = destination_port
        __props__.__dict__["protocol"] = protocol
        __props__.__dict__["source"] = source
        __props__.__dict__["source_ip"] = source_ip
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tags_all"] = tags_all
        return NetworkInsightsPath(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        ARN of the Network Insights Path.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def destination(self) -> pulumi.Output[str]:
        """
        ID of the resource which is the source of the path. Can be an Instance, Internet Gateway, Network Interface, Transit Gateway, VPC Endpoint, VPC Peering Connection or VPN Gateway.
        """
        return pulumi.get(self, "destination")

    @property
    @pulumi.getter(name="destinationIp")
    def destination_ip(self) -> pulumi.Output[Optional[str]]:
        """
        IP address of the destination resource.
        """
        return pulumi.get(self, "destination_ip")

    @property
    @pulumi.getter(name="destinationPort")
    def destination_port(self) -> pulumi.Output[Optional[int]]:
        """
        Destination port to analyze access to.
        """
        return pulumi.get(self, "destination_port")

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[str]:
        """
        Protocol to use for analysis. Valid options are `tcp` or `udp`.
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter
    def source(self) -> pulumi.Output[str]:
        """
        ID of the resource which is the source of the path. Can be an Instance, Internet Gateway, Network Interface, Transit Gateway, VPC Endpoint, VPC Peering Connection or VPN Gateway.
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter(name="sourceIp")
    def source_ip(self) -> pulumi.Output[Optional[str]]:
        """
        IP address of the source resource.
        """
        return pulumi.get(self, "source_ip")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Map of tags to assign to the resource. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Map of tags assigned to the resource, including those inherited from the provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block).
        """
        return pulumi.get(self, "tags_all")

