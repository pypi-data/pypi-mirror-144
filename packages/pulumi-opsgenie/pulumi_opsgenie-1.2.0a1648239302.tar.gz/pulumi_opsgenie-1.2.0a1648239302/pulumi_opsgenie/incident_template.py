# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['IncidentTemplateArgs', 'IncidentTemplate']

@pulumi.input_type
class IncidentTemplateArgs:
    def __init__(__self__, *,
                 message: pulumi.Input[str],
                 priority: pulumi.Input[str],
                 stakeholder_properties: pulumi.Input[Sequence[pulumi.Input['IncidentTemplateStakeholderPropertyArgs']]],
                 description: Optional[pulumi.Input[str]] = None,
                 details: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 impacted_services: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a IncidentTemplate resource.
        :param pulumi.Input[str] message: Message that is to be passed to audience that is generally used to provide a content information about the alert.
        :param pulumi.Input[str] priority: Priority level of the incident. Possible values are `P1`, `P2`, `P3`, `P4` and `P5`.
        :param pulumi.Input[str] description: Description that is generally used to provide a detailed information about the alert. This field must not be longer than 15000 characters.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] details: Map of key-value pairs to use as custom properties of the incident template. This field must not be longer than 8000 characters.
        :param pulumi.Input[str] name: Name of the incident template.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Tags of the incident template.
        """
        pulumi.set(__self__, "message", message)
        pulumi.set(__self__, "priority", priority)
        pulumi.set(__self__, "stakeholder_properties", stakeholder_properties)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if details is not None:
            pulumi.set(__self__, "details", details)
        if impacted_services is not None:
            pulumi.set(__self__, "impacted_services", impacted_services)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def message(self) -> pulumi.Input[str]:
        """
        Message that is to be passed to audience that is generally used to provide a content information about the alert.
        """
        return pulumi.get(self, "message")

    @message.setter
    def message(self, value: pulumi.Input[str]):
        pulumi.set(self, "message", value)

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Input[str]:
        """
        Priority level of the incident. Possible values are `P1`, `P2`, `P3`, `P4` and `P5`.
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: pulumi.Input[str]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter(name="stakeholderProperties")
    def stakeholder_properties(self) -> pulumi.Input[Sequence[pulumi.Input['IncidentTemplateStakeholderPropertyArgs']]]:
        return pulumi.get(self, "stakeholder_properties")

    @stakeholder_properties.setter
    def stakeholder_properties(self, value: pulumi.Input[Sequence[pulumi.Input['IncidentTemplateStakeholderPropertyArgs']]]):
        pulumi.set(self, "stakeholder_properties", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description that is generally used to provide a detailed information about the alert. This field must not be longer than 15000 characters.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def details(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Map of key-value pairs to use as custom properties of the incident template. This field must not be longer than 8000 characters.
        """
        return pulumi.get(self, "details")

    @details.setter
    def details(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "details", value)

    @property
    @pulumi.getter(name="impactedServices")
    def impacted_services(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "impacted_services")

    @impacted_services.setter
    def impacted_services(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "impacted_services", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the incident template.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Tags of the incident template.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _IncidentTemplateState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 details: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 impacted_services: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 message: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[str]] = None,
                 stakeholder_properties: Optional[pulumi.Input[Sequence[pulumi.Input['IncidentTemplateStakeholderPropertyArgs']]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering IncidentTemplate resources.
        :param pulumi.Input[str] description: Description that is generally used to provide a detailed information about the alert. This field must not be longer than 15000 characters.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] details: Map of key-value pairs to use as custom properties of the incident template. This field must not be longer than 8000 characters.
        :param pulumi.Input[str] message: Message that is to be passed to audience that is generally used to provide a content information about the alert.
        :param pulumi.Input[str] name: Name of the incident template.
        :param pulumi.Input[str] priority: Priority level of the incident. Possible values are `P1`, `P2`, `P3`, `P4` and `P5`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Tags of the incident template.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if details is not None:
            pulumi.set(__self__, "details", details)
        if impacted_services is not None:
            pulumi.set(__self__, "impacted_services", impacted_services)
        if message is not None:
            pulumi.set(__self__, "message", message)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if stakeholder_properties is not None:
            pulumi.set(__self__, "stakeholder_properties", stakeholder_properties)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description that is generally used to provide a detailed information about the alert. This field must not be longer than 15000 characters.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def details(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Map of key-value pairs to use as custom properties of the incident template. This field must not be longer than 8000 characters.
        """
        return pulumi.get(self, "details")

    @details.setter
    def details(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "details", value)

    @property
    @pulumi.getter(name="impactedServices")
    def impacted_services(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "impacted_services")

    @impacted_services.setter
    def impacted_services(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "impacted_services", value)

    @property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[str]]:
        """
        Message that is to be passed to audience that is generally used to provide a content information about the alert.
        """
        return pulumi.get(self, "message")

    @message.setter
    def message(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "message", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the incident template.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[str]]:
        """
        Priority level of the incident. Possible values are `P1`, `P2`, `P3`, `P4` and `P5`.
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter(name="stakeholderProperties")
    def stakeholder_properties(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['IncidentTemplateStakeholderPropertyArgs']]]]:
        return pulumi.get(self, "stakeholder_properties")

    @stakeholder_properties.setter
    def stakeholder_properties(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['IncidentTemplateStakeholderPropertyArgs']]]]):
        pulumi.set(self, "stakeholder_properties", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Tags of the incident template.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class IncidentTemplate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 details: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 impacted_services: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 message: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[str]] = None,
                 stakeholder_properties: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IncidentTemplateStakeholderPropertyArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Manages an Incident Template within Opsgenie.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_opsgenie as opsgenie

        test_team = opsgenie.Team("testTeam", description="This team deals with all the things")
        test_service = opsgenie.Service("testService", team_id=test_team.id)
        test_incident_template = opsgenie.IncidentTemplate("testIncidentTemplate",
            message="Incident Message",
            priority="P2",
            stakeholder_properties=[opsgenie.IncidentTemplateStakeholderPropertyArgs(
                enable=True,
                message="Stakeholder Message",
                description="Stakeholder Description",
            )],
            tags=[
                "tag1",
                "tag2",
            ],
            description="Incident Description",
            details={
                "key1": "value1",
                "key2": "value2",
            },
            impacted_services=[test_service.id])
        ```

        ## Import

        Service can be imported using the `template_id`, e.g.

        ```sh
         $ pulumi import opsgenie:index/incidentTemplate:IncidentTemplate test template_id`
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Description that is generally used to provide a detailed information about the alert. This field must not be longer than 15000 characters.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] details: Map of key-value pairs to use as custom properties of the incident template. This field must not be longer than 8000 characters.
        :param pulumi.Input[str] message: Message that is to be passed to audience that is generally used to provide a content information about the alert.
        :param pulumi.Input[str] name: Name of the incident template.
        :param pulumi.Input[str] priority: Priority level of the incident. Possible values are `P1`, `P2`, `P3`, `P4` and `P5`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Tags of the incident template.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IncidentTemplateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages an Incident Template within Opsgenie.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_opsgenie as opsgenie

        test_team = opsgenie.Team("testTeam", description="This team deals with all the things")
        test_service = opsgenie.Service("testService", team_id=test_team.id)
        test_incident_template = opsgenie.IncidentTemplate("testIncidentTemplate",
            message="Incident Message",
            priority="P2",
            stakeholder_properties=[opsgenie.IncidentTemplateStakeholderPropertyArgs(
                enable=True,
                message="Stakeholder Message",
                description="Stakeholder Description",
            )],
            tags=[
                "tag1",
                "tag2",
            ],
            description="Incident Description",
            details={
                "key1": "value1",
                "key2": "value2",
            },
            impacted_services=[test_service.id])
        ```

        ## Import

        Service can be imported using the `template_id`, e.g.

        ```sh
         $ pulumi import opsgenie:index/incidentTemplate:IncidentTemplate test template_id`
        ```

        :param str resource_name: The name of the resource.
        :param IncidentTemplateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IncidentTemplateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 details: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 impacted_services: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 message: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[str]] = None,
                 stakeholder_properties: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IncidentTemplateStakeholderPropertyArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
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
            __props__ = IncidentTemplateArgs.__new__(IncidentTemplateArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["details"] = details
            __props__.__dict__["impacted_services"] = impacted_services
            if message is None and not opts.urn:
                raise TypeError("Missing required property 'message'")
            __props__.__dict__["message"] = message
            __props__.__dict__["name"] = name
            if priority is None and not opts.urn:
                raise TypeError("Missing required property 'priority'")
            __props__.__dict__["priority"] = priority
            if stakeholder_properties is None and not opts.urn:
                raise TypeError("Missing required property 'stakeholder_properties'")
            __props__.__dict__["stakeholder_properties"] = stakeholder_properties
            __props__.__dict__["tags"] = tags
        super(IncidentTemplate, __self__).__init__(
            'opsgenie:index/incidentTemplate:IncidentTemplate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            details: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            impacted_services: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            message: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            priority: Optional[pulumi.Input[str]] = None,
            stakeholder_properties: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IncidentTemplateStakeholderPropertyArgs']]]]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'IncidentTemplate':
        """
        Get an existing IncidentTemplate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Description that is generally used to provide a detailed information about the alert. This field must not be longer than 15000 characters.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] details: Map of key-value pairs to use as custom properties of the incident template. This field must not be longer than 8000 characters.
        :param pulumi.Input[str] message: Message that is to be passed to audience that is generally used to provide a content information about the alert.
        :param pulumi.Input[str] name: Name of the incident template.
        :param pulumi.Input[str] priority: Priority level of the incident. Possible values are `P1`, `P2`, `P3`, `P4` and `P5`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: Tags of the incident template.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _IncidentTemplateState.__new__(_IncidentTemplateState)

        __props__.__dict__["description"] = description
        __props__.__dict__["details"] = details
        __props__.__dict__["impacted_services"] = impacted_services
        __props__.__dict__["message"] = message
        __props__.__dict__["name"] = name
        __props__.__dict__["priority"] = priority
        __props__.__dict__["stakeholder_properties"] = stakeholder_properties
        __props__.__dict__["tags"] = tags
        return IncidentTemplate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description that is generally used to provide a detailed information about the alert. This field must not be longer than 15000 characters.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def details(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Map of key-value pairs to use as custom properties of the incident template. This field must not be longer than 8000 characters.
        """
        return pulumi.get(self, "details")

    @property
    @pulumi.getter(name="impactedServices")
    def impacted_services(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "impacted_services")

    @property
    @pulumi.getter
    def message(self) -> pulumi.Output[str]:
        """
        Message that is to be passed to audience that is generally used to provide a content information about the alert.
        """
        return pulumi.get(self, "message")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the incident template.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[str]:
        """
        Priority level of the incident. Possible values are `P1`, `P2`, `P3`, `P4` and `P5`.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="stakeholderProperties")
    def stakeholder_properties(self) -> pulumi.Output[Sequence['outputs.IncidentTemplateStakeholderProperty']]:
        return pulumi.get(self, "stakeholder_properties")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Tags of the incident template.
        """
        return pulumi.get(self, "tags")

