# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['WorkflowArgs', 'Workflow']

@pulumi.input_type
class WorkflowArgs:
    def __init__(__self__, *,
                 default_run_properties: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 max_concurrent_runs: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Workflow resource.
        :param pulumi.Input[Mapping[str, Any]] default_run_properties: A map of default run properties for this workflow. These properties are passed to all jobs associated to the workflow.
        :param pulumi.Input[str] description: Description of the workflow.
        :param pulumi.Input[int] max_concurrent_runs: Prevents exceeding the maximum number of concurrent runs of any of the component jobs. If you leave this parameter blank, there is no limit to the number of concurrent workflow runs.
        :param pulumi.Input[str] name: The name you assign to this workflow.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        if default_run_properties is not None:
            pulumi.set(__self__, "default_run_properties", default_run_properties)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if max_concurrent_runs is not None:
            pulumi.set(__self__, "max_concurrent_runs", max_concurrent_runs)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="defaultRunProperties")
    def default_run_properties(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        A map of default run properties for this workflow. These properties are passed to all jobs associated to the workflow.
        """
        return pulumi.get(self, "default_run_properties")

    @default_run_properties.setter
    def default_run_properties(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "default_run_properties", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the workflow.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="maxConcurrentRuns")
    def max_concurrent_runs(self) -> Optional[pulumi.Input[int]]:
        """
        Prevents exceeding the maximum number of concurrent runs of any of the component jobs. If you leave this parameter blank, there is no limit to the number of concurrent workflow runs.
        """
        return pulumi.get(self, "max_concurrent_runs")

    @max_concurrent_runs.setter
    def max_concurrent_runs(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_concurrent_runs", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name you assign to this workflow.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Key-value map of resource tags. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _WorkflowState:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[str]] = None,
                 default_run_properties: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 max_concurrent_runs: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering Workflow resources.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) of Glue Workflow
        :param pulumi.Input[Mapping[str, Any]] default_run_properties: A map of default run properties for this workflow. These properties are passed to all jobs associated to the workflow.
        :param pulumi.Input[str] description: Description of the workflow.
        :param pulumi.Input[int] max_concurrent_runs: Prevents exceeding the maximum number of concurrent runs of any of the component jobs. If you leave this parameter blank, there is no limit to the number of concurrent workflow runs.
        :param pulumi.Input[str] name: The name you assign to this workflow.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if default_run_properties is not None:
            pulumi.set(__self__, "default_run_properties", default_run_properties)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if max_concurrent_runs is not None:
            pulumi.set(__self__, "max_concurrent_runs", max_concurrent_runs)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tags_all is not None:
            pulumi.set(__self__, "tags_all", tags_all)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        Amazon Resource Name (ARN) of Glue Workflow
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter(name="defaultRunProperties")
    def default_run_properties(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        A map of default run properties for this workflow. These properties are passed to all jobs associated to the workflow.
        """
        return pulumi.get(self, "default_run_properties")

    @default_run_properties.setter
    def default_run_properties(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "default_run_properties", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the workflow.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="maxConcurrentRuns")
    def max_concurrent_runs(self) -> Optional[pulumi.Input[int]]:
        """
        Prevents exceeding the maximum number of concurrent runs of any of the component jobs. If you leave this parameter blank, there is no limit to the number of concurrent workflow runs.
        """
        return pulumi.get(self, "max_concurrent_runs")

    @max_concurrent_runs.setter
    def max_concurrent_runs(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_concurrent_runs", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name you assign to this workflow.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Key-value map of resource tags. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        return pulumi.get(self, "tags_all")

    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags_all", value)


class Workflow(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_run_properties: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 max_concurrent_runs: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Provides a Glue Workflow resource.
        The workflow graph (DAG) can be build using the `glue.Trigger` resource.
        See the example below for creating a graph with four nodes (two triggers and two jobs).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.glue.Workflow("example")
        example_start = aws.glue.Trigger("example-start",
            type="ON_DEMAND",
            workflow_name=example.name,
            actions=[aws.glue.TriggerActionArgs(
                job_name="example-job",
            )])
        example_inner = aws.glue.Trigger("example-inner",
            type="CONDITIONAL",
            workflow_name=example.name,
            predicate=aws.glue.TriggerPredicateArgs(
                conditions=[aws.glue.TriggerPredicateConditionArgs(
                    job_name="example-job",
                    state="SUCCEEDED",
                )],
            ),
            actions=[aws.glue.TriggerActionArgs(
                job_name="another-example-job",
            )])
        ```

        ## Import

        Glue Workflows can be imported using `name`, e.g.,

        ```sh
         $ pulumi import aws:glue/workflow:Workflow MyWorkflow MyWorkflow
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, Any]] default_run_properties: A map of default run properties for this workflow. These properties are passed to all jobs associated to the workflow.
        :param pulumi.Input[str] description: Description of the workflow.
        :param pulumi.Input[int] max_concurrent_runs: Prevents exceeding the maximum number of concurrent runs of any of the component jobs. If you leave this parameter blank, there is no limit to the number of concurrent workflow runs.
        :param pulumi.Input[str] name: The name you assign to this workflow.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[WorkflowArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Glue Workflow resource.
        The workflow graph (DAG) can be build using the `glue.Trigger` resource.
        See the example below for creating a graph with four nodes (two triggers and two jobs).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.glue.Workflow("example")
        example_start = aws.glue.Trigger("example-start",
            type="ON_DEMAND",
            workflow_name=example.name,
            actions=[aws.glue.TriggerActionArgs(
                job_name="example-job",
            )])
        example_inner = aws.glue.Trigger("example-inner",
            type="CONDITIONAL",
            workflow_name=example.name,
            predicate=aws.glue.TriggerPredicateArgs(
                conditions=[aws.glue.TriggerPredicateConditionArgs(
                    job_name="example-job",
                    state="SUCCEEDED",
                )],
            ),
            actions=[aws.glue.TriggerActionArgs(
                job_name="another-example-job",
            )])
        ```

        ## Import

        Glue Workflows can be imported using `name`, e.g.,

        ```sh
         $ pulumi import aws:glue/workflow:Workflow MyWorkflow MyWorkflow
        ```

        :param str resource_name: The name of the resource.
        :param WorkflowArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkflowArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_run_properties: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 max_concurrent_runs: Optional[pulumi.Input[int]] = None,
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
            __props__ = WorkflowArgs.__new__(WorkflowArgs)

            __props__.__dict__["default_run_properties"] = default_run_properties
            __props__.__dict__["description"] = description
            __props__.__dict__["max_concurrent_runs"] = max_concurrent_runs
            __props__.__dict__["name"] = name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["tags_all"] = None
        super(Workflow, __self__).__init__(
            'aws:glue/workflow:Workflow',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            default_run_properties: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            max_concurrent_runs: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'Workflow':
        """
        Get an existing Workflow resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) of Glue Workflow
        :param pulumi.Input[Mapping[str, Any]] default_run_properties: A map of default run properties for this workflow. These properties are passed to all jobs associated to the workflow.
        :param pulumi.Input[str] description: Description of the workflow.
        :param pulumi.Input[int] max_concurrent_runs: Prevents exceeding the maximum number of concurrent runs of any of the component jobs. If you leave this parameter blank, there is no limit to the number of concurrent workflow runs.
        :param pulumi.Input[str] name: The name you assign to this workflow.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _WorkflowState.__new__(_WorkflowState)

        __props__.__dict__["arn"] = arn
        __props__.__dict__["default_run_properties"] = default_run_properties
        __props__.__dict__["description"] = description
        __props__.__dict__["max_concurrent_runs"] = max_concurrent_runs
        __props__.__dict__["name"] = name
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tags_all"] = tags_all
        return Workflow(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Amazon Resource Name (ARN) of Glue Workflow
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="defaultRunProperties")
    def default_run_properties(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        A map of default run properties for this workflow. These properties are passed to all jobs associated to the workflow.
        """
        return pulumi.get(self, "default_run_properties")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the workflow.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="maxConcurrentRuns")
    def max_concurrent_runs(self) -> pulumi.Output[Optional[int]]:
        """
        Prevents exceeding the maximum number of concurrent runs of any of the component jobs. If you leave this parameter blank, there is no limit to the number of concurrent workflow runs.
        """
        return pulumi.get(self, "max_concurrent_runs")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name you assign to this workflow.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Key-value map of resource tags. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, str]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        return pulumi.get(self, "tags_all")

