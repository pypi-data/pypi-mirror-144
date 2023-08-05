# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['EndpointGroupArgs', 'EndpointGroup']

@pulumi.input_type
class EndpointGroupArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 value_specs: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        """
        The set of arguments for constructing a EndpointGroup resource.
        :param pulumi.Input[str] description: The human-readable description for the group.
               Changing this updates the description of the existing group.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] endpoints: List of endpoints of the same type, for the endpoint group. The values will depend on the type.
               Changing this creates a new group.
        :param pulumi.Input[str] name: The name of the group. Changing this updates the name of
               the existing group.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Networking client.
               A Networking client is needed to create an endpoint group. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               group.
        :param pulumi.Input[str] tenant_id: The owner of the group. Required if admin wants to
               create an endpoint group for another project. Changing this creates a new group.
        :param pulumi.Input[str] type: The type of the endpoints in the group. A valid value is subnet, cidr, network, router, or vlan.
               Changing this creates a new group.
        :param pulumi.Input[Mapping[str, Any]] value_specs: Map of additional options.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if endpoints is not None:
            pulumi.set(__self__, "endpoints", endpoints)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if tenant_id is not None:
            pulumi.set(__self__, "tenant_id", tenant_id)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if value_specs is not None:
            pulumi.set(__self__, "value_specs", value_specs)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The human-readable description for the group.
        Changing this updates the description of the existing group.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def endpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of endpoints of the same type, for the endpoint group. The values will depend on the type.
        Changing this creates a new group.
        """
        return pulumi.get(self, "endpoints")

    @endpoints.setter
    def endpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "endpoints", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the group. Changing this updates the name of
        the existing group.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region in which to obtain the V2 Networking client.
        A Networking client is needed to create an endpoint group. If omitted, the
        `region` argument of the provider is used. Changing this creates a new
        group.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[str]]:
        """
        The owner of the group. Required if admin wants to
        create an endpoint group for another project. Changing this creates a new group.
        """
        return pulumi.get(self, "tenant_id")

    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tenant_id", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the endpoints in the group. A valid value is subnet, cidr, network, router, or vlan.
        Changing this creates a new group.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="valueSpecs")
    def value_specs(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Map of additional options.
        """
        return pulumi.get(self, "value_specs")

    @value_specs.setter
    def value_specs(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "value_specs", value)


@pulumi.input_type
class _EndpointGroupState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 value_specs: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        """
        Input properties used for looking up and filtering EndpointGroup resources.
        :param pulumi.Input[str] description: The human-readable description for the group.
               Changing this updates the description of the existing group.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] endpoints: List of endpoints of the same type, for the endpoint group. The values will depend on the type.
               Changing this creates a new group.
        :param pulumi.Input[str] name: The name of the group. Changing this updates the name of
               the existing group.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Networking client.
               A Networking client is needed to create an endpoint group. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               group.
        :param pulumi.Input[str] tenant_id: The owner of the group. Required if admin wants to
               create an endpoint group for another project. Changing this creates a new group.
        :param pulumi.Input[str] type: The type of the endpoints in the group. A valid value is subnet, cidr, network, router, or vlan.
               Changing this creates a new group.
        :param pulumi.Input[Mapping[str, Any]] value_specs: Map of additional options.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if endpoints is not None:
            pulumi.set(__self__, "endpoints", endpoints)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if tenant_id is not None:
            pulumi.set(__self__, "tenant_id", tenant_id)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if value_specs is not None:
            pulumi.set(__self__, "value_specs", value_specs)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The human-readable description for the group.
        Changing this updates the description of the existing group.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def endpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of endpoints of the same type, for the endpoint group. The values will depend on the type.
        Changing this creates a new group.
        """
        return pulumi.get(self, "endpoints")

    @endpoints.setter
    def endpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "endpoints", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the group. Changing this updates the name of
        the existing group.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region in which to obtain the V2 Networking client.
        A Networking client is needed to create an endpoint group. If omitted, the
        `region` argument of the provider is used. Changing this creates a new
        group.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[str]]:
        """
        The owner of the group. Required if admin wants to
        create an endpoint group for another project. Changing this creates a new group.
        """
        return pulumi.get(self, "tenant_id")

    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tenant_id", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the endpoints in the group. A valid value is subnet, cidr, network, router, or vlan.
        Changing this creates a new group.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="valueSpecs")
    def value_specs(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Map of additional options.
        """
        return pulumi.get(self, "value_specs")

    @value_specs.setter
    def value_specs(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "value_specs", value)


class EndpointGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 value_specs: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 __props__=None):
        """
        Manages a V2 Neutron Endpoint Group resource within OpenStack.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_openstack as openstack

        group1 = openstack.vpnaas.EndpointGroup("group1",
            endpoints=[
                "10.2.0.0/24",
                "10.3.0.0/24",
            ],
            type="cidr")
        ```

        ## Import

        Groups can be imported using the `id`, e.g.

        ```sh
         $ pulumi import openstack:vpnaas/endpointGroup:EndpointGroup group_1 832cb7f3-59fe-40cf-8f64-8350ffc03272
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The human-readable description for the group.
               Changing this updates the description of the existing group.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] endpoints: List of endpoints of the same type, for the endpoint group. The values will depend on the type.
               Changing this creates a new group.
        :param pulumi.Input[str] name: The name of the group. Changing this updates the name of
               the existing group.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Networking client.
               A Networking client is needed to create an endpoint group. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               group.
        :param pulumi.Input[str] tenant_id: The owner of the group. Required if admin wants to
               create an endpoint group for another project. Changing this creates a new group.
        :param pulumi.Input[str] type: The type of the endpoints in the group. A valid value is subnet, cidr, network, router, or vlan.
               Changing this creates a new group.
        :param pulumi.Input[Mapping[str, Any]] value_specs: Map of additional options.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[EndpointGroupArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a V2 Neutron Endpoint Group resource within OpenStack.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_openstack as openstack

        group1 = openstack.vpnaas.EndpointGroup("group1",
            endpoints=[
                "10.2.0.0/24",
                "10.3.0.0/24",
            ],
            type="cidr")
        ```

        ## Import

        Groups can be imported using the `id`, e.g.

        ```sh
         $ pulumi import openstack:vpnaas/endpointGroup:EndpointGroup group_1 832cb7f3-59fe-40cf-8f64-8350ffc03272
        ```

        :param str resource_name: The name of the resource.
        :param EndpointGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EndpointGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 value_specs: Optional[pulumi.Input[Mapping[str, Any]]] = None,
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
            __props__ = EndpointGroupArgs.__new__(EndpointGroupArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["endpoints"] = endpoints
            __props__.__dict__["name"] = name
            __props__.__dict__["region"] = region
            __props__.__dict__["tenant_id"] = tenant_id
            __props__.__dict__["type"] = type
            __props__.__dict__["value_specs"] = value_specs
        super(EndpointGroup, __self__).__init__(
            'openstack:vpnaas/endpointGroup:EndpointGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            tenant_id: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None,
            value_specs: Optional[pulumi.Input[Mapping[str, Any]]] = None) -> 'EndpointGroup':
        """
        Get an existing EndpointGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The human-readable description for the group.
               Changing this updates the description of the existing group.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] endpoints: List of endpoints of the same type, for the endpoint group. The values will depend on the type.
               Changing this creates a new group.
        :param pulumi.Input[str] name: The name of the group. Changing this updates the name of
               the existing group.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Networking client.
               A Networking client is needed to create an endpoint group. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               group.
        :param pulumi.Input[str] tenant_id: The owner of the group. Required if admin wants to
               create an endpoint group for another project. Changing this creates a new group.
        :param pulumi.Input[str] type: The type of the endpoints in the group. A valid value is subnet, cidr, network, router, or vlan.
               Changing this creates a new group.
        :param pulumi.Input[Mapping[str, Any]] value_specs: Map of additional options.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _EndpointGroupState.__new__(_EndpointGroupState)

        __props__.__dict__["description"] = description
        __props__.__dict__["endpoints"] = endpoints
        __props__.__dict__["name"] = name
        __props__.__dict__["region"] = region
        __props__.__dict__["tenant_id"] = tenant_id
        __props__.__dict__["type"] = type
        __props__.__dict__["value_specs"] = value_specs
        return EndpointGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The human-readable description for the group.
        Changing this updates the description of the existing group.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def endpoints(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of endpoints of the same type, for the endpoint group. The values will depend on the type.
        Changing this creates a new group.
        """
        return pulumi.get(self, "endpoints")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the group. Changing this updates the name of
        the existing group.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The region in which to obtain the V2 Networking client.
        A Networking client is needed to create an endpoint group. If omitted, the
        `region` argument of the provider is used. Changing this creates a new
        group.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[str]:
        """
        The owner of the group. Required if admin wants to
        create an endpoint group for another project. Changing this creates a new group.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the endpoints in the group. A valid value is subnet, cidr, network, router, or vlan.
        Changing this creates a new group.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="valueSpecs")
    def value_specs(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        Map of additional options.
        """
        return pulumi.get(self, "value_specs")

