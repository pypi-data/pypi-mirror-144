# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['DatacenterArgs', 'Datacenter']

@pulumi.input_type
class DatacenterArgs:
    def __init__(__self__, *,
                 custom_attributes: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 folder: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Datacenter resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] custom_attributes: Map of custom attribute ids to value 
               strings to set for datacenter resource. See
               [here][docs-setting-custom-attributes] for a reference on how to set values
               for custom attributes.
        :param pulumi.Input[str] folder: The folder where the datacenter should be created.
               Forces a new resource if changed.
        :param pulumi.Input[str] name: The name of the datacenter. This name needs to be unique
               within the folder. Forces a new resource if changed.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: The IDs of any tags to attach to this resource.
        """
        if custom_attributes is not None:
            pulumi.set(__self__, "custom_attributes", custom_attributes)
        if folder is not None:
            pulumi.set(__self__, "folder", folder)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="customAttributes")
    def custom_attributes(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Map of custom attribute ids to value 
        strings to set for datacenter resource. See
        [here][docs-setting-custom-attributes] for a reference on how to set values
        for custom attributes.
        """
        return pulumi.get(self, "custom_attributes")

    @custom_attributes.setter
    def custom_attributes(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "custom_attributes", value)

    @property
    @pulumi.getter
    def folder(self) -> Optional[pulumi.Input[str]]:
        """
        The folder where the datacenter should be created.
        Forces a new resource if changed.
        """
        return pulumi.get(self, "folder")

    @folder.setter
    def folder(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "folder", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the datacenter. This name needs to be unique
        within the folder. Forces a new resource if changed.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The IDs of any tags to attach to this resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _DatacenterState:
    def __init__(__self__, *,
                 custom_attributes: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 folder: Optional[pulumi.Input[str]] = None,
                 moid: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering Datacenter resources.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] custom_attributes: Map of custom attribute ids to value 
               strings to set for datacenter resource. See
               [here][docs-setting-custom-attributes] for a reference on how to set values
               for custom attributes.
        :param pulumi.Input[str] folder: The folder where the datacenter should be created.
               Forces a new resource if changed.
        :param pulumi.Input[str] moid: Managed object ID of this datacenter.
        :param pulumi.Input[str] name: The name of the datacenter. This name needs to be unique
               within the folder. Forces a new resource if changed.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: The IDs of any tags to attach to this resource.
        """
        if custom_attributes is not None:
            pulumi.set(__self__, "custom_attributes", custom_attributes)
        if folder is not None:
            pulumi.set(__self__, "folder", folder)
        if moid is not None:
            pulumi.set(__self__, "moid", moid)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="customAttributes")
    def custom_attributes(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Map of custom attribute ids to value 
        strings to set for datacenter resource. See
        [here][docs-setting-custom-attributes] for a reference on how to set values
        for custom attributes.
        """
        return pulumi.get(self, "custom_attributes")

    @custom_attributes.setter
    def custom_attributes(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "custom_attributes", value)

    @property
    @pulumi.getter
    def folder(self) -> Optional[pulumi.Input[str]]:
        """
        The folder where the datacenter should be created.
        Forces a new resource if changed.
        """
        return pulumi.get(self, "folder")

    @folder.setter
    def folder(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "folder", value)

    @property
    @pulumi.getter
    def moid(self) -> Optional[pulumi.Input[str]]:
        """
        Managed object ID of this datacenter.
        """
        return pulumi.get(self, "moid")

    @moid.setter
    def moid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "moid", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the datacenter. This name needs to be unique
        within the folder. Forces a new resource if changed.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The IDs of any tags to attach to this resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class Datacenter(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 custom_attributes: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 folder: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Provides a VMware vSphere datacenter resource. This can be used as the primary
        container of inventory objects such as hosts and virtual machines.

        ## Example Usage
        ### Create datacenter on the root folder

        ```python
        import pulumi
        import pulumi_vsphere as vsphere

        prod_datacenter = vsphere.Datacenter("prodDatacenter")
        ```
        ### Create datacenter on a subfolder

        ```python
        import pulumi
        import pulumi_vsphere as vsphere

        research_datacenter = vsphere.Datacenter("researchDatacenter", folder="/research/")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] custom_attributes: Map of custom attribute ids to value 
               strings to set for datacenter resource. See
               [here][docs-setting-custom-attributes] for a reference on how to set values
               for custom attributes.
        :param pulumi.Input[str] folder: The folder where the datacenter should be created.
               Forces a new resource if changed.
        :param pulumi.Input[str] name: The name of the datacenter. This name needs to be unique
               within the folder. Forces a new resource if changed.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: The IDs of any tags to attach to this resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[DatacenterArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a VMware vSphere datacenter resource. This can be used as the primary
        container of inventory objects such as hosts and virtual machines.

        ## Example Usage
        ### Create datacenter on the root folder

        ```python
        import pulumi
        import pulumi_vsphere as vsphere

        prod_datacenter = vsphere.Datacenter("prodDatacenter")
        ```
        ### Create datacenter on a subfolder

        ```python
        import pulumi
        import pulumi_vsphere as vsphere

        research_datacenter = vsphere.Datacenter("researchDatacenter", folder="/research/")
        ```

        :param str resource_name: The name of the resource.
        :param DatacenterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DatacenterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 custom_attributes: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 folder: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
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
            __props__ = DatacenterArgs.__new__(DatacenterArgs)

            __props__.__dict__["custom_attributes"] = custom_attributes
            __props__.__dict__["folder"] = folder
            __props__.__dict__["name"] = name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["moid"] = None
        super(Datacenter, __self__).__init__(
            'vsphere:index/datacenter:Datacenter',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            custom_attributes: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            folder: Optional[pulumi.Input[str]] = None,
            moid: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'Datacenter':
        """
        Get an existing Datacenter resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] custom_attributes: Map of custom attribute ids to value 
               strings to set for datacenter resource. See
               [here][docs-setting-custom-attributes] for a reference on how to set values
               for custom attributes.
        :param pulumi.Input[str] folder: The folder where the datacenter should be created.
               Forces a new resource if changed.
        :param pulumi.Input[str] moid: Managed object ID of this datacenter.
        :param pulumi.Input[str] name: The name of the datacenter. This name needs to be unique
               within the folder. Forces a new resource if changed.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: The IDs of any tags to attach to this resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DatacenterState.__new__(_DatacenterState)

        __props__.__dict__["custom_attributes"] = custom_attributes
        __props__.__dict__["folder"] = folder
        __props__.__dict__["moid"] = moid
        __props__.__dict__["name"] = name
        __props__.__dict__["tags"] = tags
        return Datacenter(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="customAttributes")
    def custom_attributes(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Map of custom attribute ids to value 
        strings to set for datacenter resource. See
        [here][docs-setting-custom-attributes] for a reference on how to set values
        for custom attributes.
        """
        return pulumi.get(self, "custom_attributes")

    @property
    @pulumi.getter
    def folder(self) -> pulumi.Output[Optional[str]]:
        """
        The folder where the datacenter should be created.
        Forces a new resource if changed.
        """
        return pulumi.get(self, "folder")

    @property
    @pulumi.getter
    def moid(self) -> pulumi.Output[str]:
        """
        Managed object ID of this datacenter.
        """
        return pulumi.get(self, "moid")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the datacenter. This name needs to be unique
        within the folder. Forces a new resource if changed.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The IDs of any tags to attach to this resource.
        """
        return pulumi.get(self, "tags")

