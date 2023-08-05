# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['StorageDrsVmOverrideArgs', 'StorageDrsVmOverride']

@pulumi.input_type
class StorageDrsVmOverrideArgs:
    def __init__(__self__, *,
                 datastore_cluster_id: pulumi.Input[str],
                 virtual_machine_id: pulumi.Input[str],
                 sdrs_automation_level: Optional[pulumi.Input[str]] = None,
                 sdrs_enabled: Optional[pulumi.Input[str]] = None,
                 sdrs_intra_vm_affinity: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a StorageDrsVmOverride resource.
        :param pulumi.Input[str] datastore_cluster_id: The managed object reference
               ID of the datastore cluster to put the override in.
               Forces a new resource if changed.
        :param pulumi.Input[str] virtual_machine_id: The UUID of the virtual machine to create
               the override for.  Forces a new resource if changed.
        :param pulumi.Input[str] sdrs_automation_level: Overrides any Storage DRS automation
               levels for this virtual machine. Can be one of `automated` or `manual`. When
               not specified, the datastore cluster's settings are used according to the
               specific SDRS subsystem.
        :param pulumi.Input[str] sdrs_enabled: Overrides the default Storage DRS setting for
               this virtual machine. When not specified, the datastore cluster setting is
               used.
        :param pulumi.Input[str] sdrs_intra_vm_affinity: Overrides the intra-VM affinity setting
               for this virtual machine. When `true`, all disks for this virtual machine
               will be kept on the same datastore. When `false`, Storage DRS may locate
               individual disks on different datastores if it helps satisfy cluster
               requirements. When not specified, the datastore cluster's settings are used.
        """
        pulumi.set(__self__, "datastore_cluster_id", datastore_cluster_id)
        pulumi.set(__self__, "virtual_machine_id", virtual_machine_id)
        if sdrs_automation_level is not None:
            pulumi.set(__self__, "sdrs_automation_level", sdrs_automation_level)
        if sdrs_enabled is not None:
            pulumi.set(__self__, "sdrs_enabled", sdrs_enabled)
        if sdrs_intra_vm_affinity is not None:
            pulumi.set(__self__, "sdrs_intra_vm_affinity", sdrs_intra_vm_affinity)

    @property
    @pulumi.getter(name="datastoreClusterId")
    def datastore_cluster_id(self) -> pulumi.Input[str]:
        """
        The managed object reference
        ID of the datastore cluster to put the override in.
        Forces a new resource if changed.
        """
        return pulumi.get(self, "datastore_cluster_id")

    @datastore_cluster_id.setter
    def datastore_cluster_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "datastore_cluster_id", value)

    @property
    @pulumi.getter(name="virtualMachineId")
    def virtual_machine_id(self) -> pulumi.Input[str]:
        """
        The UUID of the virtual machine to create
        the override for.  Forces a new resource if changed.
        """
        return pulumi.get(self, "virtual_machine_id")

    @virtual_machine_id.setter
    def virtual_machine_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "virtual_machine_id", value)

    @property
    @pulumi.getter(name="sdrsAutomationLevel")
    def sdrs_automation_level(self) -> Optional[pulumi.Input[str]]:
        """
        Overrides any Storage DRS automation
        levels for this virtual machine. Can be one of `automated` or `manual`. When
        not specified, the datastore cluster's settings are used according to the
        specific SDRS subsystem.
        """
        return pulumi.get(self, "sdrs_automation_level")

    @sdrs_automation_level.setter
    def sdrs_automation_level(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sdrs_automation_level", value)

    @property
    @pulumi.getter(name="sdrsEnabled")
    def sdrs_enabled(self) -> Optional[pulumi.Input[str]]:
        """
        Overrides the default Storage DRS setting for
        this virtual machine. When not specified, the datastore cluster setting is
        used.
        """
        return pulumi.get(self, "sdrs_enabled")

    @sdrs_enabled.setter
    def sdrs_enabled(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sdrs_enabled", value)

    @property
    @pulumi.getter(name="sdrsIntraVmAffinity")
    def sdrs_intra_vm_affinity(self) -> Optional[pulumi.Input[str]]:
        """
        Overrides the intra-VM affinity setting
        for this virtual machine. When `true`, all disks for this virtual machine
        will be kept on the same datastore. When `false`, Storage DRS may locate
        individual disks on different datastores if it helps satisfy cluster
        requirements. When not specified, the datastore cluster's settings are used.
        """
        return pulumi.get(self, "sdrs_intra_vm_affinity")

    @sdrs_intra_vm_affinity.setter
    def sdrs_intra_vm_affinity(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sdrs_intra_vm_affinity", value)


@pulumi.input_type
class _StorageDrsVmOverrideState:
    def __init__(__self__, *,
                 datastore_cluster_id: Optional[pulumi.Input[str]] = None,
                 sdrs_automation_level: Optional[pulumi.Input[str]] = None,
                 sdrs_enabled: Optional[pulumi.Input[str]] = None,
                 sdrs_intra_vm_affinity: Optional[pulumi.Input[str]] = None,
                 virtual_machine_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering StorageDrsVmOverride resources.
        :param pulumi.Input[str] datastore_cluster_id: The managed object reference
               ID of the datastore cluster to put the override in.
               Forces a new resource if changed.
        :param pulumi.Input[str] sdrs_automation_level: Overrides any Storage DRS automation
               levels for this virtual machine. Can be one of `automated` or `manual`. When
               not specified, the datastore cluster's settings are used according to the
               specific SDRS subsystem.
        :param pulumi.Input[str] sdrs_enabled: Overrides the default Storage DRS setting for
               this virtual machine. When not specified, the datastore cluster setting is
               used.
        :param pulumi.Input[str] sdrs_intra_vm_affinity: Overrides the intra-VM affinity setting
               for this virtual machine. When `true`, all disks for this virtual machine
               will be kept on the same datastore. When `false`, Storage DRS may locate
               individual disks on different datastores if it helps satisfy cluster
               requirements. When not specified, the datastore cluster's settings are used.
        :param pulumi.Input[str] virtual_machine_id: The UUID of the virtual machine to create
               the override for.  Forces a new resource if changed.
        """
        if datastore_cluster_id is not None:
            pulumi.set(__self__, "datastore_cluster_id", datastore_cluster_id)
        if sdrs_automation_level is not None:
            pulumi.set(__self__, "sdrs_automation_level", sdrs_automation_level)
        if sdrs_enabled is not None:
            pulumi.set(__self__, "sdrs_enabled", sdrs_enabled)
        if sdrs_intra_vm_affinity is not None:
            pulumi.set(__self__, "sdrs_intra_vm_affinity", sdrs_intra_vm_affinity)
        if virtual_machine_id is not None:
            pulumi.set(__self__, "virtual_machine_id", virtual_machine_id)

    @property
    @pulumi.getter(name="datastoreClusterId")
    def datastore_cluster_id(self) -> Optional[pulumi.Input[str]]:
        """
        The managed object reference
        ID of the datastore cluster to put the override in.
        Forces a new resource if changed.
        """
        return pulumi.get(self, "datastore_cluster_id")

    @datastore_cluster_id.setter
    def datastore_cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "datastore_cluster_id", value)

    @property
    @pulumi.getter(name="sdrsAutomationLevel")
    def sdrs_automation_level(self) -> Optional[pulumi.Input[str]]:
        """
        Overrides any Storage DRS automation
        levels for this virtual machine. Can be one of `automated` or `manual`. When
        not specified, the datastore cluster's settings are used according to the
        specific SDRS subsystem.
        """
        return pulumi.get(self, "sdrs_automation_level")

    @sdrs_automation_level.setter
    def sdrs_automation_level(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sdrs_automation_level", value)

    @property
    @pulumi.getter(name="sdrsEnabled")
    def sdrs_enabled(self) -> Optional[pulumi.Input[str]]:
        """
        Overrides the default Storage DRS setting for
        this virtual machine. When not specified, the datastore cluster setting is
        used.
        """
        return pulumi.get(self, "sdrs_enabled")

    @sdrs_enabled.setter
    def sdrs_enabled(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sdrs_enabled", value)

    @property
    @pulumi.getter(name="sdrsIntraVmAffinity")
    def sdrs_intra_vm_affinity(self) -> Optional[pulumi.Input[str]]:
        """
        Overrides the intra-VM affinity setting
        for this virtual machine. When `true`, all disks for this virtual machine
        will be kept on the same datastore. When `false`, Storage DRS may locate
        individual disks on different datastores if it helps satisfy cluster
        requirements. When not specified, the datastore cluster's settings are used.
        """
        return pulumi.get(self, "sdrs_intra_vm_affinity")

    @sdrs_intra_vm_affinity.setter
    def sdrs_intra_vm_affinity(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sdrs_intra_vm_affinity", value)

    @property
    @pulumi.getter(name="virtualMachineId")
    def virtual_machine_id(self) -> Optional[pulumi.Input[str]]:
        """
        The UUID of the virtual machine to create
        the override for.  Forces a new resource if changed.
        """
        return pulumi.get(self, "virtual_machine_id")

    @virtual_machine_id.setter
    def virtual_machine_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "virtual_machine_id", value)


class StorageDrsVmOverride(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 datastore_cluster_id: Optional[pulumi.Input[str]] = None,
                 sdrs_automation_level: Optional[pulumi.Input[str]] = None,
                 sdrs_enabled: Optional[pulumi.Input[str]] = None,
                 sdrs_intra_vm_affinity: Optional[pulumi.Input[str]] = None,
                 virtual_machine_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a StorageDrsVmOverride resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] datastore_cluster_id: The managed object reference
               ID of the datastore cluster to put the override in.
               Forces a new resource if changed.
        :param pulumi.Input[str] sdrs_automation_level: Overrides any Storage DRS automation
               levels for this virtual machine. Can be one of `automated` or `manual`. When
               not specified, the datastore cluster's settings are used according to the
               specific SDRS subsystem.
        :param pulumi.Input[str] sdrs_enabled: Overrides the default Storage DRS setting for
               this virtual machine. When not specified, the datastore cluster setting is
               used.
        :param pulumi.Input[str] sdrs_intra_vm_affinity: Overrides the intra-VM affinity setting
               for this virtual machine. When `true`, all disks for this virtual machine
               will be kept on the same datastore. When `false`, Storage DRS may locate
               individual disks on different datastores if it helps satisfy cluster
               requirements. When not specified, the datastore cluster's settings are used.
        :param pulumi.Input[str] virtual_machine_id: The UUID of the virtual machine to create
               the override for.  Forces a new resource if changed.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: StorageDrsVmOverrideArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a StorageDrsVmOverride resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param StorageDrsVmOverrideArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(StorageDrsVmOverrideArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 datastore_cluster_id: Optional[pulumi.Input[str]] = None,
                 sdrs_automation_level: Optional[pulumi.Input[str]] = None,
                 sdrs_enabled: Optional[pulumi.Input[str]] = None,
                 sdrs_intra_vm_affinity: Optional[pulumi.Input[str]] = None,
                 virtual_machine_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = StorageDrsVmOverrideArgs.__new__(StorageDrsVmOverrideArgs)

            if datastore_cluster_id is None and not opts.urn:
                raise TypeError("Missing required property 'datastore_cluster_id'")
            __props__.__dict__["datastore_cluster_id"] = datastore_cluster_id
            __props__.__dict__["sdrs_automation_level"] = sdrs_automation_level
            __props__.__dict__["sdrs_enabled"] = sdrs_enabled
            __props__.__dict__["sdrs_intra_vm_affinity"] = sdrs_intra_vm_affinity
            if virtual_machine_id is None and not opts.urn:
                raise TypeError("Missing required property 'virtual_machine_id'")
            __props__.__dict__["virtual_machine_id"] = virtual_machine_id
        super(StorageDrsVmOverride, __self__).__init__(
            'vsphere:index/storageDrsVmOverride:StorageDrsVmOverride',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            datastore_cluster_id: Optional[pulumi.Input[str]] = None,
            sdrs_automation_level: Optional[pulumi.Input[str]] = None,
            sdrs_enabled: Optional[pulumi.Input[str]] = None,
            sdrs_intra_vm_affinity: Optional[pulumi.Input[str]] = None,
            virtual_machine_id: Optional[pulumi.Input[str]] = None) -> 'StorageDrsVmOverride':
        """
        Get an existing StorageDrsVmOverride resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] datastore_cluster_id: The managed object reference
               ID of the datastore cluster to put the override in.
               Forces a new resource if changed.
        :param pulumi.Input[str] sdrs_automation_level: Overrides any Storage DRS automation
               levels for this virtual machine. Can be one of `automated` or `manual`. When
               not specified, the datastore cluster's settings are used according to the
               specific SDRS subsystem.
        :param pulumi.Input[str] sdrs_enabled: Overrides the default Storage DRS setting for
               this virtual machine. When not specified, the datastore cluster setting is
               used.
        :param pulumi.Input[str] sdrs_intra_vm_affinity: Overrides the intra-VM affinity setting
               for this virtual machine. When `true`, all disks for this virtual machine
               will be kept on the same datastore. When `false`, Storage DRS may locate
               individual disks on different datastores if it helps satisfy cluster
               requirements. When not specified, the datastore cluster's settings are used.
        :param pulumi.Input[str] virtual_machine_id: The UUID of the virtual machine to create
               the override for.  Forces a new resource if changed.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _StorageDrsVmOverrideState.__new__(_StorageDrsVmOverrideState)

        __props__.__dict__["datastore_cluster_id"] = datastore_cluster_id
        __props__.__dict__["sdrs_automation_level"] = sdrs_automation_level
        __props__.__dict__["sdrs_enabled"] = sdrs_enabled
        __props__.__dict__["sdrs_intra_vm_affinity"] = sdrs_intra_vm_affinity
        __props__.__dict__["virtual_machine_id"] = virtual_machine_id
        return StorageDrsVmOverride(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="datastoreClusterId")
    def datastore_cluster_id(self) -> pulumi.Output[str]:
        """
        The managed object reference
        ID of the datastore cluster to put the override in.
        Forces a new resource if changed.
        """
        return pulumi.get(self, "datastore_cluster_id")

    @property
    @pulumi.getter(name="sdrsAutomationLevel")
    def sdrs_automation_level(self) -> pulumi.Output[Optional[str]]:
        """
        Overrides any Storage DRS automation
        levels for this virtual machine. Can be one of `automated` or `manual`. When
        not specified, the datastore cluster's settings are used according to the
        specific SDRS subsystem.
        """
        return pulumi.get(self, "sdrs_automation_level")

    @property
    @pulumi.getter(name="sdrsEnabled")
    def sdrs_enabled(self) -> pulumi.Output[Optional[str]]:
        """
        Overrides the default Storage DRS setting for
        this virtual machine. When not specified, the datastore cluster setting is
        used.
        """
        return pulumi.get(self, "sdrs_enabled")

    @property
    @pulumi.getter(name="sdrsIntraVmAffinity")
    def sdrs_intra_vm_affinity(self) -> pulumi.Output[Optional[str]]:
        """
        Overrides the intra-VM affinity setting
        for this virtual machine. When `true`, all disks for this virtual machine
        will be kept on the same datastore. When `false`, Storage DRS may locate
        individual disks on different datastores if it helps satisfy cluster
        requirements. When not specified, the datastore cluster's settings are used.
        """
        return pulumi.get(self, "sdrs_intra_vm_affinity")

    @property
    @pulumi.getter(name="virtualMachineId")
    def virtual_machine_id(self) -> pulumi.Output[str]:
        """
        The UUID of the virtual machine to create
        the override for.  Forces a new resource if changed.
        """
        return pulumi.get(self, "virtual_machine_id")

