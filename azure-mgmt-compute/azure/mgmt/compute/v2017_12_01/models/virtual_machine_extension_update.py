# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .update_resource import UpdateResource


class VirtualMachineExtensionUpdate(UpdateResource):
    """Describes a Virtual Machine Extension.

    :param tags: Resource tags
    :type tags: dict[str, str]
    :param force_update_tag: How the extension handler should be forced to
     update even if the extension configuration has not changed.
    :type force_update_tag: str
    :param publisher: The name of the extension handler publisher.
    :type publisher: str
    :param type: Specifies the type of the extension; an example is
     "CustomScriptExtension".
    :type type: str
    :param type_handler_version: Specifies the version of the script handler.
    :type type_handler_version: str
    :param auto_upgrade_minor_version: Indicates whether the extension should
     use a newer minor version if one is available at deployment time. Once
     deployed, however, the extension will not upgrade minor versions unless
     redeployed, even with this property set to true.
    :type auto_upgrade_minor_version: bool
    :param settings: Json formatted public settings for the extension.
    :type settings: object
    :param protected_settings: The extension can contain either
     protectedSettings or protectedSettingsFromKeyVault or no protected
     settings at all.
    :type protected_settings: object
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'force_update_tag': {'key': 'properties.forceUpdateTag', 'type': 'str'},
        'publisher': {'key': 'properties.publisher', 'type': 'str'},
        'type': {'key': 'properties.type', 'type': 'str'},
        'type_handler_version': {'key': 'properties.typeHandlerVersion', 'type': 'str'},
        'auto_upgrade_minor_version': {'key': 'properties.autoUpgradeMinorVersion', 'type': 'bool'},
        'settings': {'key': 'properties.settings', 'type': 'object'},
        'protected_settings': {'key': 'properties.protectedSettings', 'type': 'object'},
    }

    def __init__(self, **kwargs):
        super(VirtualMachineExtensionUpdate, self).__init__(**kwargs)
        self.force_update_tag = kwargs.get('force_update_tag', None)
        self.publisher = kwargs.get('publisher', None)
        self.type = kwargs.get('type', None)
        self.type_handler_version = kwargs.get('type_handler_version', None)
        self.auto_upgrade_minor_version = kwargs.get('auto_upgrade_minor_version', None)
        self.settings = kwargs.get('settings', None)
        self.protected_settings = kwargs.get('protected_settings', None)