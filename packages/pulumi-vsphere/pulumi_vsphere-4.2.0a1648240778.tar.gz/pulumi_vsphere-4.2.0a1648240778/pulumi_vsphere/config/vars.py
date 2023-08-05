# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

import types

__config__ = pulumi.Config('vsphere')


class _ExportableConfig(types.ModuleType):
    @property
    def allow_unverified_ssl(self) -> Optional[bool]:
        """
        If set, VMware vSphere client will permit unverifiable SSL certificates.
        """
        return __config__.get_bool('allowUnverifiedSsl') or _utilities.get_env_bool('VSPHERE_ALLOW_UNVERIFIED_SSL')

    @property
    def api_timeout(self) -> Optional[int]:
        """
        API timeout in minutes (Default: 5)
        """
        return __config__.get_int('apiTimeout')

    @property
    def client_debug(self) -> Optional[bool]:
        """
        govmomi debug
        """
        return __config__.get_bool('clientDebug') or _utilities.get_env_bool('VSPHERE_CLIENT_DEBUG')

    @property
    def client_debug_path(self) -> Optional[str]:
        """
        govmomi debug path for debug
        """
        return __config__.get('clientDebugPath') or _utilities.get_env('VSPHERE_CLIENT_DEBUG_PATH')

    @property
    def client_debug_path_run(self) -> Optional[str]:
        """
        govmomi debug path for a single run
        """
        return __config__.get('clientDebugPathRun') or _utilities.get_env('VSPHERE_CLIENT_DEBUG_PATH_RUN')

    @property
    def password(self) -> Optional[str]:
        """
        The user password for vSphere API operations.
        """
        return __config__.get('password')

    @property
    def persist_session(self) -> Optional[bool]:
        """
        Persist vSphere client sessions to disk
        """
        return __config__.get_bool('persistSession') or _utilities.get_env_bool('VSPHERE_PERSIST_SESSION')

    @property
    def rest_session_path(self) -> Optional[str]:
        """
        The directory to save vSphere REST API sessions to
        """
        return __config__.get('restSessionPath') or _utilities.get_env('VSPHERE_REST_SESSION_PATH')

    @property
    def user(self) -> Optional[str]:
        """
        The user name for vSphere API operations.
        """
        return __config__.get('user')

    @property
    def vcenter_server(self) -> Optional[str]:
        return __config__.get('vcenterServer')

    @property
    def vim_keep_alive(self) -> Optional[int]:
        """
        Keep alive interval for the VIM session in minutes
        """
        return __config__.get_int('vimKeepAlive') or _utilities.get_env_int('VSPHERE_VIM_KEEP_ALIVE')

    @property
    def vim_session_path(self) -> Optional[str]:
        """
        The directory to save vSphere SOAP API sessions to
        """
        return __config__.get('vimSessionPath') or _utilities.get_env('VSPHERE_VIM_SESSION_PATH')

    @property
    def vsphere_server(self) -> Optional[str]:
        """
        The vSphere Server name for vSphere API operations.
        """
        return __config__.get('vsphereServer')

