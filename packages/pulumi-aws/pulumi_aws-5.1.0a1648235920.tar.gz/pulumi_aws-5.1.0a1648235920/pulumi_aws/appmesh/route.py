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

__all__ = ['RouteArgs', 'Route']

@pulumi.input_type
class RouteArgs:
    def __init__(__self__, *,
                 mesh_name: pulumi.Input[str],
                 spec: pulumi.Input['RouteSpecArgs'],
                 virtual_router_name: pulumi.Input[str],
                 mesh_owner: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Route resource.
        :param pulumi.Input[str] mesh_name: The name of the service mesh in which to create the route. Must be between 1 and 255 characters in length.
        :param pulumi.Input['RouteSpecArgs'] spec: The route specification to apply.
        :param pulumi.Input[str] virtual_router_name: The name of the virtual router in which to create the route. Must be between 1 and 255 characters in length.
        :param pulumi.Input[str] mesh_owner: The AWS account ID of the service mesh's owner. Defaults to the account ID the [AWS provider](https://www.terraform.io/docs/providers/aws/index.html) is currently connected to.
        :param pulumi.Input[str] name: The name to use for the route. Must be between 1 and 255 characters in length.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        pulumi.set(__self__, "mesh_name", mesh_name)
        pulumi.set(__self__, "spec", spec)
        pulumi.set(__self__, "virtual_router_name", virtual_router_name)
        if mesh_owner is not None:
            pulumi.set(__self__, "mesh_owner", mesh_owner)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="meshName")
    def mesh_name(self) -> pulumi.Input[str]:
        """
        The name of the service mesh in which to create the route. Must be between 1 and 255 characters in length.
        """
        return pulumi.get(self, "mesh_name")

    @mesh_name.setter
    def mesh_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "mesh_name", value)

    @property
    @pulumi.getter
    def spec(self) -> pulumi.Input['RouteSpecArgs']:
        """
        The route specification to apply.
        """
        return pulumi.get(self, "spec")

    @spec.setter
    def spec(self, value: pulumi.Input['RouteSpecArgs']):
        pulumi.set(self, "spec", value)

    @property
    @pulumi.getter(name="virtualRouterName")
    def virtual_router_name(self) -> pulumi.Input[str]:
        """
        The name of the virtual router in which to create the route. Must be between 1 and 255 characters in length.
        """
        return pulumi.get(self, "virtual_router_name")

    @virtual_router_name.setter
    def virtual_router_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "virtual_router_name", value)

    @property
    @pulumi.getter(name="meshOwner")
    def mesh_owner(self) -> Optional[pulumi.Input[str]]:
        """
        The AWS account ID of the service mesh's owner. Defaults to the account ID the [AWS provider](https://www.terraform.io/docs/providers/aws/index.html) is currently connected to.
        """
        return pulumi.get(self, "mesh_owner")

    @mesh_owner.setter
    def mesh_owner(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mesh_owner", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name to use for the route. Must be between 1 and 255 characters in length.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags to assign to the resource. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _RouteState:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[str]] = None,
                 created_date: Optional[pulumi.Input[str]] = None,
                 last_updated_date: Optional[pulumi.Input[str]] = None,
                 mesh_name: Optional[pulumi.Input[str]] = None,
                 mesh_owner: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_owner: Optional[pulumi.Input[str]] = None,
                 spec: Optional[pulumi.Input['RouteSpecArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_router_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Route resources.
        :param pulumi.Input[str] arn: The ARN of the route.
        :param pulumi.Input[str] created_date: The creation date of the route.
        :param pulumi.Input[str] last_updated_date: The last update date of the route.
        :param pulumi.Input[str] mesh_name: The name of the service mesh in which to create the route. Must be between 1 and 255 characters in length.
        :param pulumi.Input[str] mesh_owner: The AWS account ID of the service mesh's owner. Defaults to the account ID the [AWS provider](https://www.terraform.io/docs/providers/aws/index.html) is currently connected to.
        :param pulumi.Input[str] name: The name to use for the route. Must be between 1 and 255 characters in length.
        :param pulumi.Input[str] resource_owner: The resource owner's AWS account ID.
        :param pulumi.Input['RouteSpecArgs'] spec: The route specification to apply.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider .
        :param pulumi.Input[str] virtual_router_name: The name of the virtual router in which to create the route. Must be between 1 and 255 characters in length.
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if created_date is not None:
            pulumi.set(__self__, "created_date", created_date)
        if last_updated_date is not None:
            pulumi.set(__self__, "last_updated_date", last_updated_date)
        if mesh_name is not None:
            pulumi.set(__self__, "mesh_name", mesh_name)
        if mesh_owner is not None:
            pulumi.set(__self__, "mesh_owner", mesh_owner)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if resource_owner is not None:
            pulumi.set(__self__, "resource_owner", resource_owner)
        if spec is not None:
            pulumi.set(__self__, "spec", spec)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)
        if virtual_router_name is not None:
            pulumi.set(__self__, "virtual_router_name", virtual_router_name)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN of the route.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> Optional[pulumi.Input[str]]:
        """
        The creation date of the route.
        """
        return pulumi.get(self, "created_date")

    @created_date.setter
    def created_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_date", value)

    @property
    @pulumi.getter(name="lastUpdatedDate")
    def last_updated_date(self) -> Optional[pulumi.Input[str]]:
        """
        The last update date of the route.
        """
        return pulumi.get(self, "last_updated_date")

    @last_updated_date.setter
    def last_updated_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_updated_date", value)

    @property
    @pulumi.getter(name="meshName")
    def mesh_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the service mesh in which to create the route. Must be between 1 and 255 characters in length.
        """
        return pulumi.get(self, "mesh_name")

    @mesh_name.setter
    def mesh_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mesh_name", value)

    @property
    @pulumi.getter(name="meshOwner")
    def mesh_owner(self) -> Optional[pulumi.Input[str]]:
        """
        The AWS account ID of the service mesh's owner. Defaults to the account ID the [AWS provider](https://www.terraform.io/docs/providers/aws/index.html) is currently connected to.
        """
        return pulumi.get(self, "mesh_owner")

    @mesh_owner.setter
    def mesh_owner(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mesh_owner", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name to use for the route. Must be between 1 and 255 characters in length.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceOwner")
    def resource_owner(self) -> Optional[pulumi.Input[str]]:
        """
        The resource owner's AWS account ID.
        """
        return pulumi.get(self, "resource_owner")

    @resource_owner.setter
    def resource_owner(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_owner", value)

    @property
    @pulumi.getter
    def spec(self) -> Optional[pulumi.Input['RouteSpecArgs']]:
        """
        The route specification to apply.
        """
        return pulumi.get(self, "spec")

    @spec.setter
    def spec(self, value: Optional[pulumi.Input['RouteSpecArgs']]):
        pulumi.set(self, "spec", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags to assign to the resource. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider .
        """
        return pulumi.get(self, "tags_all")

    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags_all", value)

    @property
    @pulumi.getter(name="virtualRouterName")
    def virtual_router_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the virtual router in which to create the route. Must be between 1 and 255 characters in length.
        """
        return pulumi.get(self, "virtual_router_name")

    @virtual_router_name.setter
    def virtual_router_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "virtual_router_name", value)


class Route(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 mesh_name: Optional[pulumi.Input[str]] = None,
                 mesh_owner: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 spec: Optional[pulumi.Input[pulumi.InputType['RouteSpecArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_router_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides an AWS App Mesh route resource.

        ## Example Usage
        ### HTTP Routing

        ```python
        import pulumi
        import pulumi_aws as aws

        serviceb = aws.appmesh.Route("serviceb",
            mesh_name=aws_appmesh_mesh["simple"]["id"],
            virtual_router_name=aws_appmesh_virtual_router["serviceb"]["name"],
            spec=aws.appmesh.RouteSpecArgs(
                http_route=aws.appmesh.RouteSpecHttpRouteArgs(
                    match=aws.appmesh.RouteSpecHttpRouteMatchArgs(
                        prefix="/",
                    ),
                    action=aws.appmesh.RouteSpecHttpRouteActionArgs(
                        weighted_targets=[
                            aws.appmesh.RouteSpecHttpRouteActionWeightedTargetArgs(
                                virtual_node=aws_appmesh_virtual_node["serviceb1"]["name"],
                                weight=90,
                            ),
                            aws.appmesh.RouteSpecHttpRouteActionWeightedTargetArgs(
                                virtual_node=aws_appmesh_virtual_node["serviceb2"]["name"],
                                weight=10,
                            ),
                        ],
                    ),
                ),
            ))
        ```
        ### HTTP Header Routing

        ```python
        import pulumi
        import pulumi_aws as aws

        serviceb = aws.appmesh.Route("serviceb",
            mesh_name=aws_appmesh_mesh["simple"]["id"],
            virtual_router_name=aws_appmesh_virtual_router["serviceb"]["name"],
            spec=aws.appmesh.RouteSpecArgs(
                http_route=aws.appmesh.RouteSpecHttpRouteArgs(
                    match=aws.appmesh.RouteSpecHttpRouteMatchArgs(
                        method="POST",
                        prefix="/",
                        scheme="https",
                        headers=[aws.appmesh.RouteSpecHttpRouteMatchHeaderArgs(
                            name="clientRequestId",
                            match=aws.appmesh.RouteSpecHttpRouteMatchHeaderMatchArgs(
                                prefix="123",
                            ),
                        )],
                    ),
                    action=aws.appmesh.RouteSpecHttpRouteActionArgs(
                        weighted_targets=[aws.appmesh.RouteSpecHttpRouteActionWeightedTargetArgs(
                            virtual_node=aws_appmesh_virtual_node["serviceb"]["name"],
                            weight=100,
                        )],
                    ),
                ),
            ))
        ```
        ### Retry Policy

        ```python
        import pulumi
        import pulumi_aws as aws

        serviceb = aws.appmesh.Route("serviceb",
            mesh_name=aws_appmesh_mesh["simple"]["id"],
            virtual_router_name=aws_appmesh_virtual_router["serviceb"]["name"],
            spec=aws.appmesh.RouteSpecArgs(
                http_route=aws.appmesh.RouteSpecHttpRouteArgs(
                    match=aws.appmesh.RouteSpecHttpRouteMatchArgs(
                        prefix="/",
                    ),
                    retry_policy=aws.appmesh.RouteSpecHttpRouteRetryPolicyArgs(
                        http_retry_events=["server-error"],
                        max_retries=1,
                        per_retry_timeout=aws.appmesh.RouteSpecHttpRouteRetryPolicyPerRetryTimeoutArgs(
                            unit="s",
                            value=15,
                        ),
                    ),
                    action=aws.appmesh.RouteSpecHttpRouteActionArgs(
                        weighted_targets=[aws.appmesh.RouteSpecHttpRouteActionWeightedTargetArgs(
                            virtual_node=aws_appmesh_virtual_node["serviceb"]["name"],
                            weight=100,
                        )],
                    ),
                ),
            ))
        ```
        ### TCP Routing

        ```python
        import pulumi
        import pulumi_aws as aws

        serviceb = aws.appmesh.Route("serviceb",
            mesh_name=aws_appmesh_mesh["simple"]["id"],
            virtual_router_name=aws_appmesh_virtual_router["serviceb"]["name"],
            spec=aws.appmesh.RouteSpecArgs(
                tcp_route=aws.appmesh.RouteSpecTcpRouteArgs(
                    action=aws.appmesh.RouteSpecTcpRouteActionArgs(
                        weighted_targets=[aws.appmesh.RouteSpecTcpRouteActionWeightedTargetArgs(
                            virtual_node=aws_appmesh_virtual_node["serviceb1"]["name"],
                            weight=100,
                        )],
                    ),
                ),
            ))
        ```

        ## Import

        App Mesh virtual routes can be imported using `mesh_name` and `virtual_router_name` together with the route's `name`, e.g.,

        ```sh
         $ pulumi import aws:appmesh/route:Route serviceb simpleapp/serviceB/serviceB-route
        ```

         [1]/docs/providers/aws/index.html

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] mesh_name: The name of the service mesh in which to create the route. Must be between 1 and 255 characters in length.
        :param pulumi.Input[str] mesh_owner: The AWS account ID of the service mesh's owner. Defaults to the account ID the [AWS provider](https://www.terraform.io/docs/providers/aws/index.html) is currently connected to.
        :param pulumi.Input[str] name: The name to use for the route. Must be between 1 and 255 characters in length.
        :param pulumi.Input[pulumi.InputType['RouteSpecArgs']] spec: The route specification to apply.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[str] virtual_router_name: The name of the virtual router in which to create the route. Must be between 1 and 255 characters in length.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RouteArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides an AWS App Mesh route resource.

        ## Example Usage
        ### HTTP Routing

        ```python
        import pulumi
        import pulumi_aws as aws

        serviceb = aws.appmesh.Route("serviceb",
            mesh_name=aws_appmesh_mesh["simple"]["id"],
            virtual_router_name=aws_appmesh_virtual_router["serviceb"]["name"],
            spec=aws.appmesh.RouteSpecArgs(
                http_route=aws.appmesh.RouteSpecHttpRouteArgs(
                    match=aws.appmesh.RouteSpecHttpRouteMatchArgs(
                        prefix="/",
                    ),
                    action=aws.appmesh.RouteSpecHttpRouteActionArgs(
                        weighted_targets=[
                            aws.appmesh.RouteSpecHttpRouteActionWeightedTargetArgs(
                                virtual_node=aws_appmesh_virtual_node["serviceb1"]["name"],
                                weight=90,
                            ),
                            aws.appmesh.RouteSpecHttpRouteActionWeightedTargetArgs(
                                virtual_node=aws_appmesh_virtual_node["serviceb2"]["name"],
                                weight=10,
                            ),
                        ],
                    ),
                ),
            ))
        ```
        ### HTTP Header Routing

        ```python
        import pulumi
        import pulumi_aws as aws

        serviceb = aws.appmesh.Route("serviceb",
            mesh_name=aws_appmesh_mesh["simple"]["id"],
            virtual_router_name=aws_appmesh_virtual_router["serviceb"]["name"],
            spec=aws.appmesh.RouteSpecArgs(
                http_route=aws.appmesh.RouteSpecHttpRouteArgs(
                    match=aws.appmesh.RouteSpecHttpRouteMatchArgs(
                        method="POST",
                        prefix="/",
                        scheme="https",
                        headers=[aws.appmesh.RouteSpecHttpRouteMatchHeaderArgs(
                            name="clientRequestId",
                            match=aws.appmesh.RouteSpecHttpRouteMatchHeaderMatchArgs(
                                prefix="123",
                            ),
                        )],
                    ),
                    action=aws.appmesh.RouteSpecHttpRouteActionArgs(
                        weighted_targets=[aws.appmesh.RouteSpecHttpRouteActionWeightedTargetArgs(
                            virtual_node=aws_appmesh_virtual_node["serviceb"]["name"],
                            weight=100,
                        )],
                    ),
                ),
            ))
        ```
        ### Retry Policy

        ```python
        import pulumi
        import pulumi_aws as aws

        serviceb = aws.appmesh.Route("serviceb",
            mesh_name=aws_appmesh_mesh["simple"]["id"],
            virtual_router_name=aws_appmesh_virtual_router["serviceb"]["name"],
            spec=aws.appmesh.RouteSpecArgs(
                http_route=aws.appmesh.RouteSpecHttpRouteArgs(
                    match=aws.appmesh.RouteSpecHttpRouteMatchArgs(
                        prefix="/",
                    ),
                    retry_policy=aws.appmesh.RouteSpecHttpRouteRetryPolicyArgs(
                        http_retry_events=["server-error"],
                        max_retries=1,
                        per_retry_timeout=aws.appmesh.RouteSpecHttpRouteRetryPolicyPerRetryTimeoutArgs(
                            unit="s",
                            value=15,
                        ),
                    ),
                    action=aws.appmesh.RouteSpecHttpRouteActionArgs(
                        weighted_targets=[aws.appmesh.RouteSpecHttpRouteActionWeightedTargetArgs(
                            virtual_node=aws_appmesh_virtual_node["serviceb"]["name"],
                            weight=100,
                        )],
                    ),
                ),
            ))
        ```
        ### TCP Routing

        ```python
        import pulumi
        import pulumi_aws as aws

        serviceb = aws.appmesh.Route("serviceb",
            mesh_name=aws_appmesh_mesh["simple"]["id"],
            virtual_router_name=aws_appmesh_virtual_router["serviceb"]["name"],
            spec=aws.appmesh.RouteSpecArgs(
                tcp_route=aws.appmesh.RouteSpecTcpRouteArgs(
                    action=aws.appmesh.RouteSpecTcpRouteActionArgs(
                        weighted_targets=[aws.appmesh.RouteSpecTcpRouteActionWeightedTargetArgs(
                            virtual_node=aws_appmesh_virtual_node["serviceb1"]["name"],
                            weight=100,
                        )],
                    ),
                ),
            ))
        ```

        ## Import

        App Mesh virtual routes can be imported using `mesh_name` and `virtual_router_name` together with the route's `name`, e.g.,

        ```sh
         $ pulumi import aws:appmesh/route:Route serviceb simpleapp/serviceB/serviceB-route
        ```

         [1]/docs/providers/aws/index.html

        :param str resource_name: The name of the resource.
        :param RouteArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RouteArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 mesh_name: Optional[pulumi.Input[str]] = None,
                 mesh_owner: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 spec: Optional[pulumi.Input[pulumi.InputType['RouteSpecArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_router_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = RouteArgs.__new__(RouteArgs)

            if mesh_name is None and not opts.urn:
                raise TypeError("Missing required property 'mesh_name'")
            __props__.__dict__["mesh_name"] = mesh_name
            __props__.__dict__["mesh_owner"] = mesh_owner
            __props__.__dict__["name"] = name
            if spec is None and not opts.urn:
                raise TypeError("Missing required property 'spec'")
            __props__.__dict__["spec"] = spec
            __props__.__dict__["tags"] = tags
            if virtual_router_name is None and not opts.urn:
                raise TypeError("Missing required property 'virtual_router_name'")
            __props__.__dict__["virtual_router_name"] = virtual_router_name
            __props__.__dict__["arn"] = None
            __props__.__dict__["created_date"] = None
            __props__.__dict__["last_updated_date"] = None
            __props__.__dict__["resource_owner"] = None
            __props__.__dict__["tags_all"] = None
        super(Route, __self__).__init__(
            'aws:appmesh/route:Route',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            created_date: Optional[pulumi.Input[str]] = None,
            last_updated_date: Optional[pulumi.Input[str]] = None,
            mesh_name: Optional[pulumi.Input[str]] = None,
            mesh_owner: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resource_owner: Optional[pulumi.Input[str]] = None,
            spec: Optional[pulumi.Input[pulumi.InputType['RouteSpecArgs']]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            virtual_router_name: Optional[pulumi.Input[str]] = None) -> 'Route':
        """
        Get an existing Route resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The ARN of the route.
        :param pulumi.Input[str] created_date: The creation date of the route.
        :param pulumi.Input[str] last_updated_date: The last update date of the route.
        :param pulumi.Input[str] mesh_name: The name of the service mesh in which to create the route. Must be between 1 and 255 characters in length.
        :param pulumi.Input[str] mesh_owner: The AWS account ID of the service mesh's owner. Defaults to the account ID the [AWS provider](https://www.terraform.io/docs/providers/aws/index.html) is currently connected to.
        :param pulumi.Input[str] name: The name to use for the route. Must be between 1 and 255 characters in length.
        :param pulumi.Input[str] resource_owner: The resource owner's AWS account ID.
        :param pulumi.Input[pulumi.InputType['RouteSpecArgs']] spec: The route specification to apply.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider .
        :param pulumi.Input[str] virtual_router_name: The name of the virtual router in which to create the route. Must be between 1 and 255 characters in length.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RouteState.__new__(_RouteState)

        __props__.__dict__["arn"] = arn
        __props__.__dict__["created_date"] = created_date
        __props__.__dict__["last_updated_date"] = last_updated_date
        __props__.__dict__["mesh_name"] = mesh_name
        __props__.__dict__["mesh_owner"] = mesh_owner
        __props__.__dict__["name"] = name
        __props__.__dict__["resource_owner"] = resource_owner
        __props__.__dict__["spec"] = spec
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tags_all"] = tags_all
        __props__.__dict__["virtual_router_name"] = virtual_router_name
        return Route(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The ARN of the route.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> pulumi.Output[str]:
        """
        The creation date of the route.
        """
        return pulumi.get(self, "created_date")

    @property
    @pulumi.getter(name="lastUpdatedDate")
    def last_updated_date(self) -> pulumi.Output[str]:
        """
        The last update date of the route.
        """
        return pulumi.get(self, "last_updated_date")

    @property
    @pulumi.getter(name="meshName")
    def mesh_name(self) -> pulumi.Output[str]:
        """
        The name of the service mesh in which to create the route. Must be between 1 and 255 characters in length.
        """
        return pulumi.get(self, "mesh_name")

    @property
    @pulumi.getter(name="meshOwner")
    def mesh_owner(self) -> pulumi.Output[str]:
        """
        The AWS account ID of the service mesh's owner. Defaults to the account ID the [AWS provider](https://www.terraform.io/docs/providers/aws/index.html) is currently connected to.
        """
        return pulumi.get(self, "mesh_owner")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name to use for the route. Must be between 1 and 255 characters in length.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceOwner")
    def resource_owner(self) -> pulumi.Output[str]:
        """
        The resource owner's AWS account ID.
        """
        return pulumi.get(self, "resource_owner")

    @property
    @pulumi.getter
    def spec(self) -> pulumi.Output['outputs.RouteSpec']:
        """
        The route specification to apply.
        """
        return pulumi.get(self, "spec")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of tags to assign to the resource. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, str]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider .
        """
        return pulumi.get(self, "tags_all")

    @property
    @pulumi.getter(name="virtualRouterName")
    def virtual_router_name(self) -> pulumi.Output[str]:
        """
        The name of the virtual router in which to create the route. Must be between 1 and 255 characters in length.
        """
        return pulumi.get(self, "virtual_router_name")

