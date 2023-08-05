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

__all__ = ['ProjectArgs', 'Project']

@pulumi.input_type
class ProjectArgs:
    def __init__(__self__, *,
                 org_id: pulumi.Input[str],
                 api_keys: Optional[pulumi.Input[Sequence[pulumi.Input['ProjectApiKeyArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project_owner_id: Optional[pulumi.Input[str]] = None,
                 teams: Optional[pulumi.Input[Sequence[pulumi.Input['ProjectTeamArgs']]]] = None,
                 with_default_alerts_settings: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a Project resource.
        :param pulumi.Input[str] org_id: The ID of the organization you want to create the project within.
        :param pulumi.Input[str] name: The name of the project you want to create. (Cannot be changed via this Provider after creation.)
        :param pulumi.Input[str] project_owner_id: Unique 24-hexadecimal digit string that identifies the Atlas user account to be granted the [Project Owner](https://docs.atlas.mongodb.com/reference/user-roles/#mongodb-authrole-Project-Owner) role on the specified project. If you set this parameter, it overrides the default value of the oldest [Organization Owner](https://docs.atlas.mongodb.com/reference/user-roles/#mongodb-authrole-Organization-Owner).
        :param pulumi.Input[bool] with_default_alerts_settings: It allows users to disable the creation of the default alert settings. By default, this flag is set to true.
        """
        pulumi.set(__self__, "org_id", org_id)
        if api_keys is not None:
            pulumi.set(__self__, "api_keys", api_keys)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project_owner_id is not None:
            pulumi.set(__self__, "project_owner_id", project_owner_id)
        if teams is not None:
            pulumi.set(__self__, "teams", teams)
        if with_default_alerts_settings is not None:
            pulumi.set(__self__, "with_default_alerts_settings", with_default_alerts_settings)

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Input[str]:
        """
        The ID of the organization you want to create the project within.
        """
        return pulumi.get(self, "org_id")

    @org_id.setter
    def org_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "org_id", value)

    @property
    @pulumi.getter(name="apiKeys")
    def api_keys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ProjectApiKeyArgs']]]]:
        return pulumi.get(self, "api_keys")

    @api_keys.setter
    def api_keys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ProjectApiKeyArgs']]]]):
        pulumi.set(self, "api_keys", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the project you want to create. (Cannot be changed via this Provider after creation.)
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="projectOwnerId")
    def project_owner_id(self) -> Optional[pulumi.Input[str]]:
        """
        Unique 24-hexadecimal digit string that identifies the Atlas user account to be granted the [Project Owner](https://docs.atlas.mongodb.com/reference/user-roles/#mongodb-authrole-Project-Owner) role on the specified project. If you set this parameter, it overrides the default value of the oldest [Organization Owner](https://docs.atlas.mongodb.com/reference/user-roles/#mongodb-authrole-Organization-Owner).
        """
        return pulumi.get(self, "project_owner_id")

    @project_owner_id.setter
    def project_owner_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_owner_id", value)

    @property
    @pulumi.getter
    def teams(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ProjectTeamArgs']]]]:
        return pulumi.get(self, "teams")

    @teams.setter
    def teams(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ProjectTeamArgs']]]]):
        pulumi.set(self, "teams", value)

    @property
    @pulumi.getter(name="withDefaultAlertsSettings")
    def with_default_alerts_settings(self) -> Optional[pulumi.Input[bool]]:
        """
        It allows users to disable the creation of the default alert settings. By default, this flag is set to true.
        """
        return pulumi.get(self, "with_default_alerts_settings")

    @with_default_alerts_settings.setter
    def with_default_alerts_settings(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "with_default_alerts_settings", value)


@pulumi.input_type
class _ProjectState:
    def __init__(__self__, *,
                 api_keys: Optional[pulumi.Input[Sequence[pulumi.Input['ProjectApiKeyArgs']]]] = None,
                 cluster_count: Optional[pulumi.Input[int]] = None,
                 created: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 project_owner_id: Optional[pulumi.Input[str]] = None,
                 teams: Optional[pulumi.Input[Sequence[pulumi.Input['ProjectTeamArgs']]]] = None,
                 with_default_alerts_settings: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering Project resources.
        :param pulumi.Input[int] cluster_count: The number of Atlas clusters deployed in the project..
        :param pulumi.Input[str] created: The ISO-8601-formatted timestamp of when Atlas created the project..
        :param pulumi.Input[str] name: The name of the project you want to create. (Cannot be changed via this Provider after creation.)
        :param pulumi.Input[str] org_id: The ID of the organization you want to create the project within.
        :param pulumi.Input[str] project_owner_id: Unique 24-hexadecimal digit string that identifies the Atlas user account to be granted the [Project Owner](https://docs.atlas.mongodb.com/reference/user-roles/#mongodb-authrole-Project-Owner) role on the specified project. If you set this parameter, it overrides the default value of the oldest [Organization Owner](https://docs.atlas.mongodb.com/reference/user-roles/#mongodb-authrole-Organization-Owner).
        :param pulumi.Input[bool] with_default_alerts_settings: It allows users to disable the creation of the default alert settings. By default, this flag is set to true.
        """
        if api_keys is not None:
            pulumi.set(__self__, "api_keys", api_keys)
        if cluster_count is not None:
            pulumi.set(__self__, "cluster_count", cluster_count)
        if created is not None:
            pulumi.set(__self__, "created", created)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if org_id is not None:
            pulumi.set(__self__, "org_id", org_id)
        if project_owner_id is not None:
            pulumi.set(__self__, "project_owner_id", project_owner_id)
        if teams is not None:
            pulumi.set(__self__, "teams", teams)
        if with_default_alerts_settings is not None:
            pulumi.set(__self__, "with_default_alerts_settings", with_default_alerts_settings)

    @property
    @pulumi.getter(name="apiKeys")
    def api_keys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ProjectApiKeyArgs']]]]:
        return pulumi.get(self, "api_keys")

    @api_keys.setter
    def api_keys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ProjectApiKeyArgs']]]]):
        pulumi.set(self, "api_keys", value)

    @property
    @pulumi.getter(name="clusterCount")
    def cluster_count(self) -> Optional[pulumi.Input[int]]:
        """
        The number of Atlas clusters deployed in the project..
        """
        return pulumi.get(self, "cluster_count")

    @cluster_count.setter
    def cluster_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "cluster_count", value)

    @property
    @pulumi.getter
    def created(self) -> Optional[pulumi.Input[str]]:
        """
        The ISO-8601-formatted timestamp of when Atlas created the project..
        """
        return pulumi.get(self, "created")

    @created.setter
    def created(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the project you want to create. (Cannot be changed via this Provider after creation.)
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the organization you want to create the project within.
        """
        return pulumi.get(self, "org_id")

    @org_id.setter
    def org_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "org_id", value)

    @property
    @pulumi.getter(name="projectOwnerId")
    def project_owner_id(self) -> Optional[pulumi.Input[str]]:
        """
        Unique 24-hexadecimal digit string that identifies the Atlas user account to be granted the [Project Owner](https://docs.atlas.mongodb.com/reference/user-roles/#mongodb-authrole-Project-Owner) role on the specified project. If you set this parameter, it overrides the default value of the oldest [Organization Owner](https://docs.atlas.mongodb.com/reference/user-roles/#mongodb-authrole-Organization-Owner).
        """
        return pulumi.get(self, "project_owner_id")

    @project_owner_id.setter
    def project_owner_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_owner_id", value)

    @property
    @pulumi.getter
    def teams(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ProjectTeamArgs']]]]:
        return pulumi.get(self, "teams")

    @teams.setter
    def teams(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ProjectTeamArgs']]]]):
        pulumi.set(self, "teams", value)

    @property
    @pulumi.getter(name="withDefaultAlertsSettings")
    def with_default_alerts_settings(self) -> Optional[pulumi.Input[bool]]:
        """
        It allows users to disable the creation of the default alert settings. By default, this flag is set to true.
        """
        return pulumi.get(self, "with_default_alerts_settings")

    @with_default_alerts_settings.setter
    def with_default_alerts_settings(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "with_default_alerts_settings", value)


class Project(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_keys: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ProjectApiKeyArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 project_owner_id: Optional[pulumi.Input[str]] = None,
                 teams: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ProjectTeamArgs']]]]] = None,
                 with_default_alerts_settings: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_mongodbatlas as mongodbatlas

        test = mongodbatlas.Project("test",
            api_keys=[mongodbatlas.ProjectApiKeyArgs(
                api_key_id="61003b299dda8d54a9d7d10c",
                role_names=["GROUP_READ_ONLY"],
            )],
            org_id="<ORG_ID>",
            project_owner_id="<OWNER_ACCOUNT_ID>",
            teams=[
                mongodbatlas.ProjectTeamArgs(
                    role_names=["GROUP_OWNER"],
                    team_id="5e0fa8c99ccf641c722fe645",
                ),
                mongodbatlas.ProjectTeamArgs(
                    role_names=[
                        "GROUP_READ_ONLY",
                        "GROUP_DATA_ACCESS_READ_WRITE",
                    ],
                    team_id="5e1dd7b4f2a30ba80a70cd4rw",
                ),
            ])
        ```

        ## Import

        Project must be imported using project ID, e.g.

        ```sh
         $ pulumi import mongodbatlas:index/project:Project my_project 5d09d6a59ccf6445652a444a
        ```

         For more information see[MongoDB Atlas API Reference.](https://docs.atlas.mongodb.com/reference/api/projects/) - [and MongoDB Atlas API - Teams](https://docs.atlas.mongodb.com/reference/api/teams/) Documentation for more information.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name of the project you want to create. (Cannot be changed via this Provider after creation.)
        :param pulumi.Input[str] org_id: The ID of the organization you want to create the project within.
        :param pulumi.Input[str] project_owner_id: Unique 24-hexadecimal digit string that identifies the Atlas user account to be granted the [Project Owner](https://docs.atlas.mongodb.com/reference/user-roles/#mongodb-authrole-Project-Owner) role on the specified project. If you set this parameter, it overrides the default value of the oldest [Organization Owner](https://docs.atlas.mongodb.com/reference/user-roles/#mongodb-authrole-Organization-Owner).
        :param pulumi.Input[bool] with_default_alerts_settings: It allows users to disable the creation of the default alert settings. By default, this flag is set to true.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProjectArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_mongodbatlas as mongodbatlas

        test = mongodbatlas.Project("test",
            api_keys=[mongodbatlas.ProjectApiKeyArgs(
                api_key_id="61003b299dda8d54a9d7d10c",
                role_names=["GROUP_READ_ONLY"],
            )],
            org_id="<ORG_ID>",
            project_owner_id="<OWNER_ACCOUNT_ID>",
            teams=[
                mongodbatlas.ProjectTeamArgs(
                    role_names=["GROUP_OWNER"],
                    team_id="5e0fa8c99ccf641c722fe645",
                ),
                mongodbatlas.ProjectTeamArgs(
                    role_names=[
                        "GROUP_READ_ONLY",
                        "GROUP_DATA_ACCESS_READ_WRITE",
                    ],
                    team_id="5e1dd7b4f2a30ba80a70cd4rw",
                ),
            ])
        ```

        ## Import

        Project must be imported using project ID, e.g.

        ```sh
         $ pulumi import mongodbatlas:index/project:Project my_project 5d09d6a59ccf6445652a444a
        ```

         For more information see[MongoDB Atlas API Reference.](https://docs.atlas.mongodb.com/reference/api/projects/) - [and MongoDB Atlas API - Teams](https://docs.atlas.mongodb.com/reference/api/teams/) Documentation for more information.

        :param str resource_name: The name of the resource.
        :param ProjectArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProjectArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_keys: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ProjectApiKeyArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 project_owner_id: Optional[pulumi.Input[str]] = None,
                 teams: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ProjectTeamArgs']]]]] = None,
                 with_default_alerts_settings: Optional[pulumi.Input[bool]] = None,
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
            __props__ = ProjectArgs.__new__(ProjectArgs)

            __props__.__dict__["api_keys"] = api_keys
            __props__.__dict__["name"] = name
            if org_id is None and not opts.urn:
                raise TypeError("Missing required property 'org_id'")
            __props__.__dict__["org_id"] = org_id
            __props__.__dict__["project_owner_id"] = project_owner_id
            __props__.__dict__["teams"] = teams
            __props__.__dict__["with_default_alerts_settings"] = with_default_alerts_settings
            __props__.__dict__["cluster_count"] = None
            __props__.__dict__["created"] = None
        super(Project, __self__).__init__(
            'mongodbatlas:index/project:Project',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            api_keys: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ProjectApiKeyArgs']]]]] = None,
            cluster_count: Optional[pulumi.Input[int]] = None,
            created: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            org_id: Optional[pulumi.Input[str]] = None,
            project_owner_id: Optional[pulumi.Input[str]] = None,
            teams: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ProjectTeamArgs']]]]] = None,
            with_default_alerts_settings: Optional[pulumi.Input[bool]] = None) -> 'Project':
        """
        Get an existing Project resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] cluster_count: The number of Atlas clusters deployed in the project..
        :param pulumi.Input[str] created: The ISO-8601-formatted timestamp of when Atlas created the project..
        :param pulumi.Input[str] name: The name of the project you want to create. (Cannot be changed via this Provider after creation.)
        :param pulumi.Input[str] org_id: The ID of the organization you want to create the project within.
        :param pulumi.Input[str] project_owner_id: Unique 24-hexadecimal digit string that identifies the Atlas user account to be granted the [Project Owner](https://docs.atlas.mongodb.com/reference/user-roles/#mongodb-authrole-Project-Owner) role on the specified project. If you set this parameter, it overrides the default value of the oldest [Organization Owner](https://docs.atlas.mongodb.com/reference/user-roles/#mongodb-authrole-Organization-Owner).
        :param pulumi.Input[bool] with_default_alerts_settings: It allows users to disable the creation of the default alert settings. By default, this flag is set to true.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ProjectState.__new__(_ProjectState)

        __props__.__dict__["api_keys"] = api_keys
        __props__.__dict__["cluster_count"] = cluster_count
        __props__.__dict__["created"] = created
        __props__.__dict__["name"] = name
        __props__.__dict__["org_id"] = org_id
        __props__.__dict__["project_owner_id"] = project_owner_id
        __props__.__dict__["teams"] = teams
        __props__.__dict__["with_default_alerts_settings"] = with_default_alerts_settings
        return Project(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiKeys")
    def api_keys(self) -> pulumi.Output[Sequence['outputs.ProjectApiKey']]:
        return pulumi.get(self, "api_keys")

    @property
    @pulumi.getter(name="clusterCount")
    def cluster_count(self) -> pulumi.Output[int]:
        """
        The number of Atlas clusters deployed in the project..
        """
        return pulumi.get(self, "cluster_count")

    @property
    @pulumi.getter
    def created(self) -> pulumi.Output[str]:
        """
        The ISO-8601-formatted timestamp of when Atlas created the project..
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the project you want to create. (Cannot be changed via this Provider after creation.)
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Output[str]:
        """
        The ID of the organization you want to create the project within.
        """
        return pulumi.get(self, "org_id")

    @property
    @pulumi.getter(name="projectOwnerId")
    def project_owner_id(self) -> pulumi.Output[Optional[str]]:
        """
        Unique 24-hexadecimal digit string that identifies the Atlas user account to be granted the [Project Owner](https://docs.atlas.mongodb.com/reference/user-roles/#mongodb-authrole-Project-Owner) role on the specified project. If you set this parameter, it overrides the default value of the oldest [Organization Owner](https://docs.atlas.mongodb.com/reference/user-roles/#mongodb-authrole-Organization-Owner).
        """
        return pulumi.get(self, "project_owner_id")

    @property
    @pulumi.getter
    def teams(self) -> pulumi.Output[Optional[Sequence['outputs.ProjectTeam']]]:
        return pulumi.get(self, "teams")

    @property
    @pulumi.getter(name="withDefaultAlertsSettings")
    def with_default_alerts_settings(self) -> pulumi.Output[Optional[bool]]:
        """
        It allows users to disable the creation of the default alert settings. By default, this flag is set to true.
        """
        return pulumi.get(self, "with_default_alerts_settings")

