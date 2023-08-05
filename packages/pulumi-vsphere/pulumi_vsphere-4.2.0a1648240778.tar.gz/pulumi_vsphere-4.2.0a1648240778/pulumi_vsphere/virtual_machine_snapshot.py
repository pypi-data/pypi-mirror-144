# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['VirtualMachineSnapshotArgs', 'VirtualMachineSnapshot']

@pulumi.input_type
class VirtualMachineSnapshotArgs:
    def __init__(__self__, *,
                 description: pulumi.Input[str],
                 memory: pulumi.Input[bool],
                 quiesce: pulumi.Input[bool],
                 snapshot_name: pulumi.Input[str],
                 virtual_machine_uuid: pulumi.Input[str],
                 consolidate: Optional[pulumi.Input[bool]] = None,
                 remove_children: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a VirtualMachineSnapshot resource.
        :param pulumi.Input[str] description: A description for the snapshot.
        :param pulumi.Input[bool] memory: If set to `true`, a dump of the internal state of the
               virtual machine is included in the snapshot.
        :param pulumi.Input[bool] quiesce: If set to `true`, and the virtual machine is powered
               on when the snapshot is taken, VMware Tools is used to quiesce the file
               system in the virtual machine.
        :param pulumi.Input[str] snapshot_name: The name of the snapshot.
        :param pulumi.Input[str] virtual_machine_uuid: The virtual machine UUID.
        :param pulumi.Input[bool] consolidate: If set to `true`, the delta disks involved in this
               snapshot will be consolidated into the parent when this resource is
               destroyed.
        :param pulumi.Input[bool] remove_children: If set to `true`, the entire snapshot subtree
               is removed when this resource is destroyed.
        """
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "memory", memory)
        pulumi.set(__self__, "quiesce", quiesce)
        pulumi.set(__self__, "snapshot_name", snapshot_name)
        pulumi.set(__self__, "virtual_machine_uuid", virtual_machine_uuid)
        if consolidate is not None:
            pulumi.set(__self__, "consolidate", consolidate)
        if remove_children is not None:
            pulumi.set(__self__, "remove_children", remove_children)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Input[str]:
        """
        A description for the snapshot.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: pulumi.Input[str]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def memory(self) -> pulumi.Input[bool]:
        """
        If set to `true`, a dump of the internal state of the
        virtual machine is included in the snapshot.
        """
        return pulumi.get(self, "memory")

    @memory.setter
    def memory(self, value: pulumi.Input[bool]):
        pulumi.set(self, "memory", value)

    @property
    @pulumi.getter
    def quiesce(self) -> pulumi.Input[bool]:
        """
        If set to `true`, and the virtual machine is powered
        on when the snapshot is taken, VMware Tools is used to quiesce the file
        system in the virtual machine.
        """
        return pulumi.get(self, "quiesce")

    @quiesce.setter
    def quiesce(self, value: pulumi.Input[bool]):
        pulumi.set(self, "quiesce", value)

    @property
    @pulumi.getter(name="snapshotName")
    def snapshot_name(self) -> pulumi.Input[str]:
        """
        The name of the snapshot.
        """
        return pulumi.get(self, "snapshot_name")

    @snapshot_name.setter
    def snapshot_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "snapshot_name", value)

    @property
    @pulumi.getter(name="virtualMachineUuid")
    def virtual_machine_uuid(self) -> pulumi.Input[str]:
        """
        The virtual machine UUID.
        """
        return pulumi.get(self, "virtual_machine_uuid")

    @virtual_machine_uuid.setter
    def virtual_machine_uuid(self, value: pulumi.Input[str]):
        pulumi.set(self, "virtual_machine_uuid", value)

    @property
    @pulumi.getter
    def consolidate(self) -> Optional[pulumi.Input[bool]]:
        """
        If set to `true`, the delta disks involved in this
        snapshot will be consolidated into the parent when this resource is
        destroyed.
        """
        return pulumi.get(self, "consolidate")

    @consolidate.setter
    def consolidate(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "consolidate", value)

    @property
    @pulumi.getter(name="removeChildren")
    def remove_children(self) -> Optional[pulumi.Input[bool]]:
        """
        If set to `true`, the entire snapshot subtree
        is removed when this resource is destroyed.
        """
        return pulumi.get(self, "remove_children")

    @remove_children.setter
    def remove_children(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "remove_children", value)


@pulumi.input_type
class _VirtualMachineSnapshotState:
    def __init__(__self__, *,
                 consolidate: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 memory: Optional[pulumi.Input[bool]] = None,
                 quiesce: Optional[pulumi.Input[bool]] = None,
                 remove_children: Optional[pulumi.Input[bool]] = None,
                 snapshot_name: Optional[pulumi.Input[str]] = None,
                 virtual_machine_uuid: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering VirtualMachineSnapshot resources.
        :param pulumi.Input[bool] consolidate: If set to `true`, the delta disks involved in this
               snapshot will be consolidated into the parent when this resource is
               destroyed.
        :param pulumi.Input[str] description: A description for the snapshot.
        :param pulumi.Input[bool] memory: If set to `true`, a dump of the internal state of the
               virtual machine is included in the snapshot.
        :param pulumi.Input[bool] quiesce: If set to `true`, and the virtual machine is powered
               on when the snapshot is taken, VMware Tools is used to quiesce the file
               system in the virtual machine.
        :param pulumi.Input[bool] remove_children: If set to `true`, the entire snapshot subtree
               is removed when this resource is destroyed.
        :param pulumi.Input[str] snapshot_name: The name of the snapshot.
        :param pulumi.Input[str] virtual_machine_uuid: The virtual machine UUID.
        """
        if consolidate is not None:
            pulumi.set(__self__, "consolidate", consolidate)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if memory is not None:
            pulumi.set(__self__, "memory", memory)
        if quiesce is not None:
            pulumi.set(__self__, "quiesce", quiesce)
        if remove_children is not None:
            pulumi.set(__self__, "remove_children", remove_children)
        if snapshot_name is not None:
            pulumi.set(__self__, "snapshot_name", snapshot_name)
        if virtual_machine_uuid is not None:
            pulumi.set(__self__, "virtual_machine_uuid", virtual_machine_uuid)

    @property
    @pulumi.getter
    def consolidate(self) -> Optional[pulumi.Input[bool]]:
        """
        If set to `true`, the delta disks involved in this
        snapshot will be consolidated into the parent when this resource is
        destroyed.
        """
        return pulumi.get(self, "consolidate")

    @consolidate.setter
    def consolidate(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "consolidate", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description for the snapshot.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def memory(self) -> Optional[pulumi.Input[bool]]:
        """
        If set to `true`, a dump of the internal state of the
        virtual machine is included in the snapshot.
        """
        return pulumi.get(self, "memory")

    @memory.setter
    def memory(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "memory", value)

    @property
    @pulumi.getter
    def quiesce(self) -> Optional[pulumi.Input[bool]]:
        """
        If set to `true`, and the virtual machine is powered
        on when the snapshot is taken, VMware Tools is used to quiesce the file
        system in the virtual machine.
        """
        return pulumi.get(self, "quiesce")

    @quiesce.setter
    def quiesce(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "quiesce", value)

    @property
    @pulumi.getter(name="removeChildren")
    def remove_children(self) -> Optional[pulumi.Input[bool]]:
        """
        If set to `true`, the entire snapshot subtree
        is removed when this resource is destroyed.
        """
        return pulumi.get(self, "remove_children")

    @remove_children.setter
    def remove_children(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "remove_children", value)

    @property
    @pulumi.getter(name="snapshotName")
    def snapshot_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the snapshot.
        """
        return pulumi.get(self, "snapshot_name")

    @snapshot_name.setter
    def snapshot_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "snapshot_name", value)

    @property
    @pulumi.getter(name="virtualMachineUuid")
    def virtual_machine_uuid(self) -> Optional[pulumi.Input[str]]:
        """
        The virtual machine UUID.
        """
        return pulumi.get(self, "virtual_machine_uuid")

    @virtual_machine_uuid.setter
    def virtual_machine_uuid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "virtual_machine_uuid", value)


class VirtualMachineSnapshot(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 consolidate: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 memory: Optional[pulumi.Input[bool]] = None,
                 quiesce: Optional[pulumi.Input[bool]] = None,
                 remove_children: Optional[pulumi.Input[bool]] = None,
                 snapshot_name: Optional[pulumi.Input[str]] = None,
                 virtual_machine_uuid: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The `VirtualMachineSnapshot` resource can be used to manage snapshots
        for a virtual machine.

        For more information on managing snapshots and how they work in VMware, see
        [here][ext-vm-snapshot-management].

        [ext-vm-snapshot-management]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.vm_admin.doc/GUID-CA948C69-7F58-4519-AEB1-739545EA94E5.html

        > **NOTE:** A snapshot in VMware differs from traditional disk snapshots, and
        can contain the actual running state of the virtual machine, data for all disks
        that have not been set to be independent from the snapshot (including ones that
        have been attached via the `attach`
        parameter to the `VirtualMachine` `disk` block), and even the
        configuration of the virtual machine at the time of the snapshot. Virtual
        machine, disk activity, and configuration changes post-snapshot are not
        included in the original state. Use this resource with care! Neither VMware nor
        HashiCorp recommends retaining snapshots for a extended period of time and does
        NOT recommend using them as as backup feature. For more information on the
        limitation of virtual machine snapshots, see [here][ext-vm-snap-limitations].

        [ext-vm-snap-limitations]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.vm_admin.doc/GUID-53F65726-A23B-4CF0-A7D5-48E584B88613.html

        ## Example Usage

        ```python
        import pulumi
        import pulumi_vsphere as vsphere

        demo1 = vsphere.VirtualMachineSnapshot("demo1",
            consolidate=True,
            description="This is Demo Snapshot",
            memory=True,
            quiesce=True,
            remove_children=False,
            snapshot_name="Snapshot Name",
            virtual_machine_uuid="9aac5551-a351-4158-8c5c-15a71e8ec5c9")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] consolidate: If set to `true`, the delta disks involved in this
               snapshot will be consolidated into the parent when this resource is
               destroyed.
        :param pulumi.Input[str] description: A description for the snapshot.
        :param pulumi.Input[bool] memory: If set to `true`, a dump of the internal state of the
               virtual machine is included in the snapshot.
        :param pulumi.Input[bool] quiesce: If set to `true`, and the virtual machine is powered
               on when the snapshot is taken, VMware Tools is used to quiesce the file
               system in the virtual machine.
        :param pulumi.Input[bool] remove_children: If set to `true`, the entire snapshot subtree
               is removed when this resource is destroyed.
        :param pulumi.Input[str] snapshot_name: The name of the snapshot.
        :param pulumi.Input[str] virtual_machine_uuid: The virtual machine UUID.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VirtualMachineSnapshotArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The `VirtualMachineSnapshot` resource can be used to manage snapshots
        for a virtual machine.

        For more information on managing snapshots and how they work in VMware, see
        [here][ext-vm-snapshot-management].

        [ext-vm-snapshot-management]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.vm_admin.doc/GUID-CA948C69-7F58-4519-AEB1-739545EA94E5.html

        > **NOTE:** A snapshot in VMware differs from traditional disk snapshots, and
        can contain the actual running state of the virtual machine, data for all disks
        that have not been set to be independent from the snapshot (including ones that
        have been attached via the `attach`
        parameter to the `VirtualMachine` `disk` block), and even the
        configuration of the virtual machine at the time of the snapshot. Virtual
        machine, disk activity, and configuration changes post-snapshot are not
        included in the original state. Use this resource with care! Neither VMware nor
        HashiCorp recommends retaining snapshots for a extended period of time and does
        NOT recommend using them as as backup feature. For more information on the
        limitation of virtual machine snapshots, see [here][ext-vm-snap-limitations].

        [ext-vm-snap-limitations]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.vm_admin.doc/GUID-53F65726-A23B-4CF0-A7D5-48E584B88613.html

        ## Example Usage

        ```python
        import pulumi
        import pulumi_vsphere as vsphere

        demo1 = vsphere.VirtualMachineSnapshot("demo1",
            consolidate=True,
            description="This is Demo Snapshot",
            memory=True,
            quiesce=True,
            remove_children=False,
            snapshot_name="Snapshot Name",
            virtual_machine_uuid="9aac5551-a351-4158-8c5c-15a71e8ec5c9")
        ```

        :param str resource_name: The name of the resource.
        :param VirtualMachineSnapshotArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VirtualMachineSnapshotArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 consolidate: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 memory: Optional[pulumi.Input[bool]] = None,
                 quiesce: Optional[pulumi.Input[bool]] = None,
                 remove_children: Optional[pulumi.Input[bool]] = None,
                 snapshot_name: Optional[pulumi.Input[str]] = None,
                 virtual_machine_uuid: Optional[pulumi.Input[str]] = None,
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
            __props__ = VirtualMachineSnapshotArgs.__new__(VirtualMachineSnapshotArgs)

            __props__.__dict__["consolidate"] = consolidate
            if description is None and not opts.urn:
                raise TypeError("Missing required property 'description'")
            __props__.__dict__["description"] = description
            if memory is None and not opts.urn:
                raise TypeError("Missing required property 'memory'")
            __props__.__dict__["memory"] = memory
            if quiesce is None and not opts.urn:
                raise TypeError("Missing required property 'quiesce'")
            __props__.__dict__["quiesce"] = quiesce
            __props__.__dict__["remove_children"] = remove_children
            if snapshot_name is None and not opts.urn:
                raise TypeError("Missing required property 'snapshot_name'")
            __props__.__dict__["snapshot_name"] = snapshot_name
            if virtual_machine_uuid is None and not opts.urn:
                raise TypeError("Missing required property 'virtual_machine_uuid'")
            __props__.__dict__["virtual_machine_uuid"] = virtual_machine_uuid
        super(VirtualMachineSnapshot, __self__).__init__(
            'vsphere:index/virtualMachineSnapshot:VirtualMachineSnapshot',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            consolidate: Optional[pulumi.Input[bool]] = None,
            description: Optional[pulumi.Input[str]] = None,
            memory: Optional[pulumi.Input[bool]] = None,
            quiesce: Optional[pulumi.Input[bool]] = None,
            remove_children: Optional[pulumi.Input[bool]] = None,
            snapshot_name: Optional[pulumi.Input[str]] = None,
            virtual_machine_uuid: Optional[pulumi.Input[str]] = None) -> 'VirtualMachineSnapshot':
        """
        Get an existing VirtualMachineSnapshot resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] consolidate: If set to `true`, the delta disks involved in this
               snapshot will be consolidated into the parent when this resource is
               destroyed.
        :param pulumi.Input[str] description: A description for the snapshot.
        :param pulumi.Input[bool] memory: If set to `true`, a dump of the internal state of the
               virtual machine is included in the snapshot.
        :param pulumi.Input[bool] quiesce: If set to `true`, and the virtual machine is powered
               on when the snapshot is taken, VMware Tools is used to quiesce the file
               system in the virtual machine.
        :param pulumi.Input[bool] remove_children: If set to `true`, the entire snapshot subtree
               is removed when this resource is destroyed.
        :param pulumi.Input[str] snapshot_name: The name of the snapshot.
        :param pulumi.Input[str] virtual_machine_uuid: The virtual machine UUID.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _VirtualMachineSnapshotState.__new__(_VirtualMachineSnapshotState)

        __props__.__dict__["consolidate"] = consolidate
        __props__.__dict__["description"] = description
        __props__.__dict__["memory"] = memory
        __props__.__dict__["quiesce"] = quiesce
        __props__.__dict__["remove_children"] = remove_children
        __props__.__dict__["snapshot_name"] = snapshot_name
        __props__.__dict__["virtual_machine_uuid"] = virtual_machine_uuid
        return VirtualMachineSnapshot(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def consolidate(self) -> pulumi.Output[Optional[bool]]:
        """
        If set to `true`, the delta disks involved in this
        snapshot will be consolidated into the parent when this resource is
        destroyed.
        """
        return pulumi.get(self, "consolidate")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        A description for the snapshot.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def memory(self) -> pulumi.Output[bool]:
        """
        If set to `true`, a dump of the internal state of the
        virtual machine is included in the snapshot.
        """
        return pulumi.get(self, "memory")

    @property
    @pulumi.getter
    def quiesce(self) -> pulumi.Output[bool]:
        """
        If set to `true`, and the virtual machine is powered
        on when the snapshot is taken, VMware Tools is used to quiesce the file
        system in the virtual machine.
        """
        return pulumi.get(self, "quiesce")

    @property
    @pulumi.getter(name="removeChildren")
    def remove_children(self) -> pulumi.Output[Optional[bool]]:
        """
        If set to `true`, the entire snapshot subtree
        is removed when this resource is destroyed.
        """
        return pulumi.get(self, "remove_children")

    @property
    @pulumi.getter(name="snapshotName")
    def snapshot_name(self) -> pulumi.Output[str]:
        """
        The name of the snapshot.
        """
        return pulumi.get(self, "snapshot_name")

    @property
    @pulumi.getter(name="virtualMachineUuid")
    def virtual_machine_uuid(self) -> pulumi.Output[str]:
        """
        The virtual machine UUID.
        """
        return pulumi.get(self, "virtual_machine_uuid")

