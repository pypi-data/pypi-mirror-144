# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['DeploymentTrafficFilterAssociationArgs', 'DeploymentTrafficFilterAssociation']

@pulumi.input_type
class DeploymentTrafficFilterAssociationArgs:
    def __init__(__self__, *,
                 deployment_id: pulumi.Input[str],
                 traffic_filter_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a DeploymentTrafficFilterAssociation resource.
        :param pulumi.Input[str] deployment_id: Deployment ID of the deployment to which the traffic filter rule is attached.
        :param pulumi.Input[str] traffic_filter_id: Traffic filter ID of the rule to use for the attachment.
        """
        pulumi.set(__self__, "deployment_id", deployment_id)
        pulumi.set(__self__, "traffic_filter_id", traffic_filter_id)

    @property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> pulumi.Input[str]:
        """
        Deployment ID of the deployment to which the traffic filter rule is attached.
        """
        return pulumi.get(self, "deployment_id")

    @deployment_id.setter
    def deployment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "deployment_id", value)

    @property
    @pulumi.getter(name="trafficFilterId")
    def traffic_filter_id(self) -> pulumi.Input[str]:
        """
        Traffic filter ID of the rule to use for the attachment.
        """
        return pulumi.get(self, "traffic_filter_id")

    @traffic_filter_id.setter
    def traffic_filter_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "traffic_filter_id", value)


@pulumi.input_type
class _DeploymentTrafficFilterAssociationState:
    def __init__(__self__, *,
                 deployment_id: Optional[pulumi.Input[str]] = None,
                 traffic_filter_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering DeploymentTrafficFilterAssociation resources.
        :param pulumi.Input[str] deployment_id: Deployment ID of the deployment to which the traffic filter rule is attached.
        :param pulumi.Input[str] traffic_filter_id: Traffic filter ID of the rule to use for the attachment.
        """
        if deployment_id is not None:
            pulumi.set(__self__, "deployment_id", deployment_id)
        if traffic_filter_id is not None:
            pulumi.set(__self__, "traffic_filter_id", traffic_filter_id)

    @property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> Optional[pulumi.Input[str]]:
        """
        Deployment ID of the deployment to which the traffic filter rule is attached.
        """
        return pulumi.get(self, "deployment_id")

    @deployment_id.setter
    def deployment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deployment_id", value)

    @property
    @pulumi.getter(name="trafficFilterId")
    def traffic_filter_id(self) -> Optional[pulumi.Input[str]]:
        """
        Traffic filter ID of the rule to use for the attachment.
        """
        return pulumi.get(self, "traffic_filter_id")

    @traffic_filter_id.setter
    def traffic_filter_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "traffic_filter_id", value)


class DeploymentTrafficFilterAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 deployment_id: Optional[pulumi.Input[str]] = None,
                 traffic_filter_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_ec as ec

        example_deployment = ec.get_deployment(id="320b7b540dfc967a7a649c18e2fce4ed")
        example_deployment_traffic_filter = ec.DeploymentTrafficFilter("exampleDeploymentTrafficFilter",
            region="us-east-1",
            type="ip",
            rules=[ec.DeploymentTrafficFilterRuleArgs(
                source="0.0.0.0/0",
            )])
        example_deployment_traffic_filter_association = ec.DeploymentTrafficFilterAssociation("exampleDeploymentTrafficFilterAssociation",
            traffic_filter_id=example_deployment_traffic_filter.id,
            deployment_id=ec_deployment["example"]["id"])
        ```

        ## Import

        Import is not supported on this resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] deployment_id: Deployment ID of the deployment to which the traffic filter rule is attached.
        :param pulumi.Input[str] traffic_filter_id: Traffic filter ID of the rule to use for the attachment.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DeploymentTrafficFilterAssociationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_ec as ec

        example_deployment = ec.get_deployment(id="320b7b540dfc967a7a649c18e2fce4ed")
        example_deployment_traffic_filter = ec.DeploymentTrafficFilter("exampleDeploymentTrafficFilter",
            region="us-east-1",
            type="ip",
            rules=[ec.DeploymentTrafficFilterRuleArgs(
                source="0.0.0.0/0",
            )])
        example_deployment_traffic_filter_association = ec.DeploymentTrafficFilterAssociation("exampleDeploymentTrafficFilterAssociation",
            traffic_filter_id=example_deployment_traffic_filter.id,
            deployment_id=ec_deployment["example"]["id"])
        ```

        ## Import

        Import is not supported on this resource.

        :param str resource_name: The name of the resource.
        :param DeploymentTrafficFilterAssociationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DeploymentTrafficFilterAssociationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 deployment_id: Optional[pulumi.Input[str]] = None,
                 traffic_filter_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = DeploymentTrafficFilterAssociationArgs.__new__(DeploymentTrafficFilterAssociationArgs)

            if deployment_id is None and not opts.urn:
                raise TypeError("Missing required property 'deployment_id'")
            __props__.__dict__["deployment_id"] = deployment_id
            if traffic_filter_id is None and not opts.urn:
                raise TypeError("Missing required property 'traffic_filter_id'")
            __props__.__dict__["traffic_filter_id"] = traffic_filter_id
        super(DeploymentTrafficFilterAssociation, __self__).__init__(
            'ec:index/deploymentTrafficFilterAssociation:DeploymentTrafficFilterAssociation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            deployment_id: Optional[pulumi.Input[str]] = None,
            traffic_filter_id: Optional[pulumi.Input[str]] = None) -> 'DeploymentTrafficFilterAssociation':
        """
        Get an existing DeploymentTrafficFilterAssociation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] deployment_id: Deployment ID of the deployment to which the traffic filter rule is attached.
        :param pulumi.Input[str] traffic_filter_id: Traffic filter ID of the rule to use for the attachment.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DeploymentTrafficFilterAssociationState.__new__(_DeploymentTrafficFilterAssociationState)

        __props__.__dict__["deployment_id"] = deployment_id
        __props__.__dict__["traffic_filter_id"] = traffic_filter_id
        return DeploymentTrafficFilterAssociation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> pulumi.Output[str]:
        """
        Deployment ID of the deployment to which the traffic filter rule is attached.
        """
        return pulumi.get(self, "deployment_id")

    @property
    @pulumi.getter(name="trafficFilterId")
    def traffic_filter_id(self) -> pulumi.Output[str]:
        """
        Traffic filter ID of the rule to use for the attachment.
        """
        return pulumi.get(self, "traffic_filter_id")

