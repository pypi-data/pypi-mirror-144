"""
Type annotations for opsworks service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/type_defs/)

Usage::

    ```python
    from mypy_boto3_opsworks.type_defs import AgentVersionTypeDef

    data: AgentVersionTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    AppAttributesKeysType,
    AppTypeType,
    ArchitectureType,
    AutoScalingTypeType,
    CloudWatchLogsEncodingType,
    CloudWatchLogsInitialPositionType,
    CloudWatchLogsTimeZoneType,
    DeploymentCommandNameType,
    LayerAttributesKeysType,
    LayerTypeType,
    RootDeviceTypeType,
    SourceTypeType,
    VirtualizationTypeType,
    VolumeTypeType,
)

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AgentVersionTypeDef",
    "AppTypeDef",
    "AssignInstanceRequestRequestTypeDef",
    "AssignVolumeRequestRequestTypeDef",
    "AssociateElasticIpRequestRequestTypeDef",
    "AttachElasticLoadBalancerRequestRequestTypeDef",
    "AutoScalingThresholdsTypeDef",
    "BlockDeviceMappingTypeDef",
    "ChefConfigurationResponseMetadataTypeDef",
    "ChefConfigurationTypeDef",
    "CloneStackRequestRequestTypeDef",
    "CloneStackResultTypeDef",
    "CloudWatchLogsConfigurationResponseMetadataTypeDef",
    "CloudWatchLogsConfigurationTypeDef",
    "CloudWatchLogsLogStreamTypeDef",
    "CommandTypeDef",
    "CreateAppRequestRequestTypeDef",
    "CreateAppResultTypeDef",
    "CreateDeploymentRequestRequestTypeDef",
    "CreateDeploymentResultTypeDef",
    "CreateInstanceRequestRequestTypeDef",
    "CreateInstanceResultTypeDef",
    "CreateLayerRequestRequestTypeDef",
    "CreateLayerRequestStackCreateLayerTypeDef",
    "CreateLayerResultTypeDef",
    "CreateStackRequestRequestTypeDef",
    "CreateStackRequestServiceResourceCreateStackTypeDef",
    "CreateStackResultTypeDef",
    "CreateUserProfileRequestRequestTypeDef",
    "CreateUserProfileResultTypeDef",
    "DataSourceTypeDef",
    "DeleteAppRequestRequestTypeDef",
    "DeleteInstanceRequestRequestTypeDef",
    "DeleteLayerRequestRequestTypeDef",
    "DeleteStackRequestRequestTypeDef",
    "DeleteUserProfileRequestRequestTypeDef",
    "DeploymentCommandTypeDef",
    "DeploymentTypeDef",
    "DeregisterEcsClusterRequestRequestTypeDef",
    "DeregisterElasticIpRequestRequestTypeDef",
    "DeregisterInstanceRequestRequestTypeDef",
    "DeregisterRdsDbInstanceRequestRequestTypeDef",
    "DeregisterVolumeRequestRequestTypeDef",
    "DescribeAgentVersionsRequestRequestTypeDef",
    "DescribeAgentVersionsResultTypeDef",
    "DescribeAppsRequestAppExistsWaitTypeDef",
    "DescribeAppsRequestRequestTypeDef",
    "DescribeAppsResultTypeDef",
    "DescribeCommandsRequestRequestTypeDef",
    "DescribeCommandsResultTypeDef",
    "DescribeDeploymentsRequestDeploymentSuccessfulWaitTypeDef",
    "DescribeDeploymentsRequestRequestTypeDef",
    "DescribeDeploymentsResultTypeDef",
    "DescribeEcsClustersRequestDescribeEcsClustersPaginateTypeDef",
    "DescribeEcsClustersRequestRequestTypeDef",
    "DescribeEcsClustersResultTypeDef",
    "DescribeElasticIpsRequestRequestTypeDef",
    "DescribeElasticIpsResultTypeDef",
    "DescribeElasticLoadBalancersRequestRequestTypeDef",
    "DescribeElasticLoadBalancersResultTypeDef",
    "DescribeInstancesRequestInstanceOnlineWaitTypeDef",
    "DescribeInstancesRequestInstanceRegisteredWaitTypeDef",
    "DescribeInstancesRequestInstanceStoppedWaitTypeDef",
    "DescribeInstancesRequestInstanceTerminatedWaitTypeDef",
    "DescribeInstancesRequestRequestTypeDef",
    "DescribeInstancesResultTypeDef",
    "DescribeLayersRequestRequestTypeDef",
    "DescribeLayersResultTypeDef",
    "DescribeLoadBasedAutoScalingRequestRequestTypeDef",
    "DescribeLoadBasedAutoScalingResultTypeDef",
    "DescribeMyUserProfileResultTypeDef",
    "DescribeOperatingSystemsResponseTypeDef",
    "DescribePermissionsRequestRequestTypeDef",
    "DescribePermissionsResultTypeDef",
    "DescribeRaidArraysRequestRequestTypeDef",
    "DescribeRaidArraysResultTypeDef",
    "DescribeRdsDbInstancesRequestRequestTypeDef",
    "DescribeRdsDbInstancesResultTypeDef",
    "DescribeServiceErrorsRequestRequestTypeDef",
    "DescribeServiceErrorsResultTypeDef",
    "DescribeStackProvisioningParametersRequestRequestTypeDef",
    "DescribeStackProvisioningParametersResultTypeDef",
    "DescribeStackSummaryRequestRequestTypeDef",
    "DescribeStackSummaryResultTypeDef",
    "DescribeStacksRequestRequestTypeDef",
    "DescribeStacksResultTypeDef",
    "DescribeTimeBasedAutoScalingRequestRequestTypeDef",
    "DescribeTimeBasedAutoScalingResultTypeDef",
    "DescribeUserProfilesRequestRequestTypeDef",
    "DescribeUserProfilesResultTypeDef",
    "DescribeVolumesRequestRequestTypeDef",
    "DescribeVolumesResultTypeDef",
    "DetachElasticLoadBalancerRequestRequestTypeDef",
    "DisassociateElasticIpRequestRequestTypeDef",
    "EbsBlockDeviceTypeDef",
    "EcsClusterTypeDef",
    "ElasticIpTypeDef",
    "ElasticLoadBalancerTypeDef",
    "EnvironmentVariableTypeDef",
    "GetHostnameSuggestionRequestRequestTypeDef",
    "GetHostnameSuggestionResultTypeDef",
    "GrantAccessRequestRequestTypeDef",
    "GrantAccessResultTypeDef",
    "InstanceIdentityTypeDef",
    "InstanceTypeDef",
    "InstancesCountResponseMetadataTypeDef",
    "InstancesCountTypeDef",
    "LayerTypeDef",
    "LifecycleEventConfigurationResponseMetadataTypeDef",
    "LifecycleEventConfigurationTypeDef",
    "ListTagsRequestRequestTypeDef",
    "ListTagsResultTypeDef",
    "LoadBasedAutoScalingConfigurationTypeDef",
    "OperatingSystemConfigurationManagerTypeDef",
    "OperatingSystemTypeDef",
    "PaginatorConfigTypeDef",
    "PermissionTypeDef",
    "RaidArrayTypeDef",
    "RdsDbInstanceTypeDef",
    "RebootInstanceRequestRequestTypeDef",
    "RecipesResponseMetadataTypeDef",
    "RecipesTypeDef",
    "RegisterEcsClusterRequestRequestTypeDef",
    "RegisterEcsClusterResultTypeDef",
    "RegisterElasticIpRequestRequestTypeDef",
    "RegisterElasticIpResultTypeDef",
    "RegisterInstanceRequestRequestTypeDef",
    "RegisterInstanceResultTypeDef",
    "RegisterRdsDbInstanceRequestRequestTypeDef",
    "RegisterVolumeRequestRequestTypeDef",
    "RegisterVolumeResultTypeDef",
    "ReportedOsTypeDef",
    "ResponseMetadataTypeDef",
    "SelfUserProfileTypeDef",
    "ServiceErrorTypeDef",
    "ServiceResourceLayerRequestTypeDef",
    "ServiceResourceStackRequestTypeDef",
    "ServiceResourceStackSummaryRequestTypeDef",
    "SetLoadBasedAutoScalingRequestRequestTypeDef",
    "SetPermissionRequestRequestTypeDef",
    "SetTimeBasedAutoScalingRequestRequestTypeDef",
    "ShutdownEventConfigurationTypeDef",
    "SourceResponseMetadataTypeDef",
    "SourceTypeDef",
    "SslConfigurationTypeDef",
    "StackConfigurationManagerResponseMetadataTypeDef",
    "StackConfigurationManagerTypeDef",
    "StackSummaryTypeDef",
    "StackTypeDef",
    "StartInstanceRequestRequestTypeDef",
    "StartStackRequestRequestTypeDef",
    "StopInstanceRequestRequestTypeDef",
    "StopStackRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TemporaryCredentialTypeDef",
    "TimeBasedAutoScalingConfigurationTypeDef",
    "UnassignInstanceRequestRequestTypeDef",
    "UnassignVolumeRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAppRequestRequestTypeDef",
    "UpdateElasticIpRequestRequestTypeDef",
    "UpdateInstanceRequestRequestTypeDef",
    "UpdateLayerRequestRequestTypeDef",
    "UpdateMyUserProfileRequestRequestTypeDef",
    "UpdateRdsDbInstanceRequestRequestTypeDef",
    "UpdateStackRequestRequestTypeDef",
    "UpdateUserProfileRequestRequestTypeDef",
    "UpdateVolumeRequestRequestTypeDef",
    "UserProfileTypeDef",
    "VolumeConfigurationTypeDef",
    "VolumeTypeDef",
    "WaiterConfigTypeDef",
    "WeeklyAutoScalingScheduleTypeDef",
)

AgentVersionTypeDef = TypedDict(
    "AgentVersionTypeDef",
    {
        "Version": NotRequired[str],
        "ConfigurationManager": NotRequired["StackConfigurationManagerTypeDef"],
    },
)

AppTypeDef = TypedDict(
    "AppTypeDef",
    {
        "AppId": NotRequired[str],
        "StackId": NotRequired[str],
        "Shortname": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "DataSources": NotRequired[List["DataSourceTypeDef"]],
        "Type": NotRequired[AppTypeType],
        "AppSource": NotRequired["SourceTypeDef"],
        "Domains": NotRequired[List[str]],
        "EnableSsl": NotRequired[bool],
        "SslConfiguration": NotRequired["SslConfigurationTypeDef"],
        "Attributes": NotRequired[Dict[AppAttributesKeysType, str]],
        "CreatedAt": NotRequired[str],
        "Environment": NotRequired[List["EnvironmentVariableTypeDef"]],
    },
)

AssignInstanceRequestRequestTypeDef = TypedDict(
    "AssignInstanceRequestRequestTypeDef",
    {
        "InstanceId": str,
        "LayerIds": Sequence[str],
    },
)

AssignVolumeRequestRequestTypeDef = TypedDict(
    "AssignVolumeRequestRequestTypeDef",
    {
        "VolumeId": str,
        "InstanceId": NotRequired[str],
    },
)

AssociateElasticIpRequestRequestTypeDef = TypedDict(
    "AssociateElasticIpRequestRequestTypeDef",
    {
        "ElasticIp": str,
        "InstanceId": NotRequired[str],
    },
)

AttachElasticLoadBalancerRequestRequestTypeDef = TypedDict(
    "AttachElasticLoadBalancerRequestRequestTypeDef",
    {
        "ElasticLoadBalancerName": str,
        "LayerId": str,
    },
)

AutoScalingThresholdsTypeDef = TypedDict(
    "AutoScalingThresholdsTypeDef",
    {
        "InstanceCount": NotRequired[int],
        "ThresholdsWaitTime": NotRequired[int],
        "IgnoreMetricsTime": NotRequired[int],
        "CpuThreshold": NotRequired[float],
        "MemoryThreshold": NotRequired[float],
        "LoadThreshold": NotRequired[float],
        "Alarms": NotRequired[List[str]],
    },
)

BlockDeviceMappingTypeDef = TypedDict(
    "BlockDeviceMappingTypeDef",
    {
        "DeviceName": NotRequired[str],
        "NoDevice": NotRequired[str],
        "VirtualName": NotRequired[str],
        "Ebs": NotRequired["EbsBlockDeviceTypeDef"],
    },
)

ChefConfigurationResponseMetadataTypeDef = TypedDict(
    "ChefConfigurationResponseMetadataTypeDef",
    {
        "ManageBerkshelf": bool,
        "BerkshelfVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ChefConfigurationTypeDef = TypedDict(
    "ChefConfigurationTypeDef",
    {
        "ManageBerkshelf": NotRequired[bool],
        "BerkshelfVersion": NotRequired[str],
    },
)

CloneStackRequestRequestTypeDef = TypedDict(
    "CloneStackRequestRequestTypeDef",
    {
        "SourceStackId": str,
        "ServiceRoleArn": str,
        "Name": NotRequired[str],
        "Region": NotRequired[str],
        "VpcId": NotRequired[str],
        "Attributes": NotRequired[Mapping[Literal["Color"], str]],
        "DefaultInstanceProfileArn": NotRequired[str],
        "DefaultOs": NotRequired[str],
        "HostnameTheme": NotRequired[str],
        "DefaultAvailabilityZone": NotRequired[str],
        "DefaultSubnetId": NotRequired[str],
        "CustomJson": NotRequired[str],
        "ConfigurationManager": NotRequired["StackConfigurationManagerTypeDef"],
        "ChefConfiguration": NotRequired["ChefConfigurationTypeDef"],
        "UseCustomCookbooks": NotRequired[bool],
        "UseOpsworksSecurityGroups": NotRequired[bool],
        "CustomCookbooksSource": NotRequired["SourceTypeDef"],
        "DefaultSshKeyName": NotRequired[str],
        "ClonePermissions": NotRequired[bool],
        "CloneAppIds": NotRequired[Sequence[str]],
        "DefaultRootDeviceType": NotRequired[RootDeviceTypeType],
        "AgentVersion": NotRequired[str],
    },
)

CloneStackResultTypeDef = TypedDict(
    "CloneStackResultTypeDef",
    {
        "StackId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CloudWatchLogsConfigurationResponseMetadataTypeDef = TypedDict(
    "CloudWatchLogsConfigurationResponseMetadataTypeDef",
    {
        "Enabled": bool,
        "LogStreams": List["CloudWatchLogsLogStreamTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CloudWatchLogsConfigurationTypeDef = TypedDict(
    "CloudWatchLogsConfigurationTypeDef",
    {
        "Enabled": NotRequired[bool],
        "LogStreams": NotRequired[Sequence["CloudWatchLogsLogStreamTypeDef"]],
    },
)

CloudWatchLogsLogStreamTypeDef = TypedDict(
    "CloudWatchLogsLogStreamTypeDef",
    {
        "LogGroupName": NotRequired[str],
        "DatetimeFormat": NotRequired[str],
        "TimeZone": NotRequired[CloudWatchLogsTimeZoneType],
        "File": NotRequired[str],
        "FileFingerprintLines": NotRequired[str],
        "MultiLineStartPattern": NotRequired[str],
        "InitialPosition": NotRequired[CloudWatchLogsInitialPositionType],
        "Encoding": NotRequired[CloudWatchLogsEncodingType],
        "BufferDuration": NotRequired[int],
        "BatchCount": NotRequired[int],
        "BatchSize": NotRequired[int],
    },
)

CommandTypeDef = TypedDict(
    "CommandTypeDef",
    {
        "CommandId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "DeploymentId": NotRequired[str],
        "CreatedAt": NotRequired[str],
        "AcknowledgedAt": NotRequired[str],
        "CompletedAt": NotRequired[str],
        "Status": NotRequired[str],
        "ExitCode": NotRequired[int],
        "LogUrl": NotRequired[str],
        "Type": NotRequired[str],
    },
)

CreateAppRequestRequestTypeDef = TypedDict(
    "CreateAppRequestRequestTypeDef",
    {
        "StackId": str,
        "Name": str,
        "Type": AppTypeType,
        "Shortname": NotRequired[str],
        "Description": NotRequired[str],
        "DataSources": NotRequired[Sequence["DataSourceTypeDef"]],
        "AppSource": NotRequired["SourceTypeDef"],
        "Domains": NotRequired[Sequence[str]],
        "EnableSsl": NotRequired[bool],
        "SslConfiguration": NotRequired["SslConfigurationTypeDef"],
        "Attributes": NotRequired[Mapping[AppAttributesKeysType, str]],
        "Environment": NotRequired[Sequence["EnvironmentVariableTypeDef"]],
    },
)

CreateAppResultTypeDef = TypedDict(
    "CreateAppResultTypeDef",
    {
        "AppId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDeploymentRequestRequestTypeDef = TypedDict(
    "CreateDeploymentRequestRequestTypeDef",
    {
        "StackId": str,
        "Command": "DeploymentCommandTypeDef",
        "AppId": NotRequired[str],
        "InstanceIds": NotRequired[Sequence[str]],
        "LayerIds": NotRequired[Sequence[str]],
        "Comment": NotRequired[str],
        "CustomJson": NotRequired[str],
    },
)

CreateDeploymentResultTypeDef = TypedDict(
    "CreateDeploymentResultTypeDef",
    {
        "DeploymentId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateInstanceRequestRequestTypeDef = TypedDict(
    "CreateInstanceRequestRequestTypeDef",
    {
        "StackId": str,
        "LayerIds": Sequence[str],
        "InstanceType": str,
        "AutoScalingType": NotRequired[AutoScalingTypeType],
        "Hostname": NotRequired[str],
        "Os": NotRequired[str],
        "AmiId": NotRequired[str],
        "SshKeyName": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "VirtualizationType": NotRequired[str],
        "SubnetId": NotRequired[str],
        "Architecture": NotRequired[ArchitectureType],
        "RootDeviceType": NotRequired[RootDeviceTypeType],
        "BlockDeviceMappings": NotRequired[Sequence["BlockDeviceMappingTypeDef"]],
        "InstallUpdatesOnBoot": NotRequired[bool],
        "EbsOptimized": NotRequired[bool],
        "AgentVersion": NotRequired[str],
        "Tenancy": NotRequired[str],
    },
)

CreateInstanceResultTypeDef = TypedDict(
    "CreateInstanceResultTypeDef",
    {
        "InstanceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateLayerRequestRequestTypeDef = TypedDict(
    "CreateLayerRequestRequestTypeDef",
    {
        "StackId": str,
        "Type": LayerTypeType,
        "Name": str,
        "Shortname": str,
        "Attributes": NotRequired[Mapping[LayerAttributesKeysType, str]],
        "CloudWatchLogsConfiguration": NotRequired["CloudWatchLogsConfigurationTypeDef"],
        "CustomInstanceProfileArn": NotRequired[str],
        "CustomJson": NotRequired[str],
        "CustomSecurityGroupIds": NotRequired[Sequence[str]],
        "Packages": NotRequired[Sequence[str]],
        "VolumeConfigurations": NotRequired[Sequence["VolumeConfigurationTypeDef"]],
        "EnableAutoHealing": NotRequired[bool],
        "AutoAssignElasticIps": NotRequired[bool],
        "AutoAssignPublicIps": NotRequired[bool],
        "CustomRecipes": NotRequired["RecipesTypeDef"],
        "InstallUpdatesOnBoot": NotRequired[bool],
        "UseEbsOptimizedInstances": NotRequired[bool],
        "LifecycleEventConfiguration": NotRequired["LifecycleEventConfigurationTypeDef"],
    },
)

CreateLayerRequestStackCreateLayerTypeDef = TypedDict(
    "CreateLayerRequestStackCreateLayerTypeDef",
    {
        "Type": LayerTypeType,
        "Name": str,
        "Shortname": str,
        "Attributes": NotRequired[Mapping[LayerAttributesKeysType, str]],
        "CloudWatchLogsConfiguration": NotRequired["CloudWatchLogsConfigurationTypeDef"],
        "CustomInstanceProfileArn": NotRequired[str],
        "CustomJson": NotRequired[str],
        "CustomSecurityGroupIds": NotRequired[Sequence[str]],
        "Packages": NotRequired[Sequence[str]],
        "VolumeConfigurations": NotRequired[Sequence["VolumeConfigurationTypeDef"]],
        "EnableAutoHealing": NotRequired[bool],
        "AutoAssignElasticIps": NotRequired[bool],
        "AutoAssignPublicIps": NotRequired[bool],
        "CustomRecipes": NotRequired["RecipesTypeDef"],
        "InstallUpdatesOnBoot": NotRequired[bool],
        "UseEbsOptimizedInstances": NotRequired[bool],
        "LifecycleEventConfiguration": NotRequired["LifecycleEventConfigurationTypeDef"],
    },
)

CreateLayerResultTypeDef = TypedDict(
    "CreateLayerResultTypeDef",
    {
        "LayerId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateStackRequestRequestTypeDef = TypedDict(
    "CreateStackRequestRequestTypeDef",
    {
        "Name": str,
        "Region": str,
        "ServiceRoleArn": str,
        "DefaultInstanceProfileArn": str,
        "VpcId": NotRequired[str],
        "Attributes": NotRequired[Mapping[Literal["Color"], str]],
        "DefaultOs": NotRequired[str],
        "HostnameTheme": NotRequired[str],
        "DefaultAvailabilityZone": NotRequired[str],
        "DefaultSubnetId": NotRequired[str],
        "CustomJson": NotRequired[str],
        "ConfigurationManager": NotRequired["StackConfigurationManagerTypeDef"],
        "ChefConfiguration": NotRequired["ChefConfigurationTypeDef"],
        "UseCustomCookbooks": NotRequired[bool],
        "UseOpsworksSecurityGroups": NotRequired[bool],
        "CustomCookbooksSource": NotRequired["SourceTypeDef"],
        "DefaultSshKeyName": NotRequired[str],
        "DefaultRootDeviceType": NotRequired[RootDeviceTypeType],
        "AgentVersion": NotRequired[str],
    },
)

CreateStackRequestServiceResourceCreateStackTypeDef = TypedDict(
    "CreateStackRequestServiceResourceCreateStackTypeDef",
    {
        "Name": str,
        "Region": str,
        "ServiceRoleArn": str,
        "DefaultInstanceProfileArn": str,
        "VpcId": NotRequired[str],
        "Attributes": NotRequired[Mapping[Literal["Color"], str]],
        "DefaultOs": NotRequired[str],
        "HostnameTheme": NotRequired[str],
        "DefaultAvailabilityZone": NotRequired[str],
        "DefaultSubnetId": NotRequired[str],
        "CustomJson": NotRequired[str],
        "ConfigurationManager": NotRequired["StackConfigurationManagerTypeDef"],
        "ChefConfiguration": NotRequired["ChefConfigurationTypeDef"],
        "UseCustomCookbooks": NotRequired[bool],
        "UseOpsworksSecurityGroups": NotRequired[bool],
        "CustomCookbooksSource": NotRequired["SourceTypeDef"],
        "DefaultSshKeyName": NotRequired[str],
        "DefaultRootDeviceType": NotRequired[RootDeviceTypeType],
        "AgentVersion": NotRequired[str],
    },
)

CreateStackResultTypeDef = TypedDict(
    "CreateStackResultTypeDef",
    {
        "StackId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateUserProfileRequestRequestTypeDef = TypedDict(
    "CreateUserProfileRequestRequestTypeDef",
    {
        "IamUserArn": str,
        "SshUsername": NotRequired[str],
        "SshPublicKey": NotRequired[str],
        "AllowSelfManagement": NotRequired[bool],
    },
)

CreateUserProfileResultTypeDef = TypedDict(
    "CreateUserProfileResultTypeDef",
    {
        "IamUserArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "Type": NotRequired[str],
        "Arn": NotRequired[str],
        "DatabaseName": NotRequired[str],
    },
)

DeleteAppRequestRequestTypeDef = TypedDict(
    "DeleteAppRequestRequestTypeDef",
    {
        "AppId": str,
    },
)

DeleteInstanceRequestRequestTypeDef = TypedDict(
    "DeleteInstanceRequestRequestTypeDef",
    {
        "InstanceId": str,
        "DeleteElasticIp": NotRequired[bool],
        "DeleteVolumes": NotRequired[bool],
    },
)

DeleteLayerRequestRequestTypeDef = TypedDict(
    "DeleteLayerRequestRequestTypeDef",
    {
        "LayerId": str,
    },
)

DeleteStackRequestRequestTypeDef = TypedDict(
    "DeleteStackRequestRequestTypeDef",
    {
        "StackId": str,
    },
)

DeleteUserProfileRequestRequestTypeDef = TypedDict(
    "DeleteUserProfileRequestRequestTypeDef",
    {
        "IamUserArn": str,
    },
)

DeploymentCommandTypeDef = TypedDict(
    "DeploymentCommandTypeDef",
    {
        "Name": DeploymentCommandNameType,
        "Args": NotRequired[Mapping[str, Sequence[str]]],
    },
)

DeploymentTypeDef = TypedDict(
    "DeploymentTypeDef",
    {
        "DeploymentId": NotRequired[str],
        "StackId": NotRequired[str],
        "AppId": NotRequired[str],
        "CreatedAt": NotRequired[str],
        "CompletedAt": NotRequired[str],
        "Duration": NotRequired[int],
        "IamUserArn": NotRequired[str],
        "Comment": NotRequired[str],
        "Command": NotRequired["DeploymentCommandTypeDef"],
        "Status": NotRequired[str],
        "CustomJson": NotRequired[str],
        "InstanceIds": NotRequired[List[str]],
    },
)

DeregisterEcsClusterRequestRequestTypeDef = TypedDict(
    "DeregisterEcsClusterRequestRequestTypeDef",
    {
        "EcsClusterArn": str,
    },
)

DeregisterElasticIpRequestRequestTypeDef = TypedDict(
    "DeregisterElasticIpRequestRequestTypeDef",
    {
        "ElasticIp": str,
    },
)

DeregisterInstanceRequestRequestTypeDef = TypedDict(
    "DeregisterInstanceRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)

DeregisterRdsDbInstanceRequestRequestTypeDef = TypedDict(
    "DeregisterRdsDbInstanceRequestRequestTypeDef",
    {
        "RdsDbInstanceArn": str,
    },
)

DeregisterVolumeRequestRequestTypeDef = TypedDict(
    "DeregisterVolumeRequestRequestTypeDef",
    {
        "VolumeId": str,
    },
)

DescribeAgentVersionsRequestRequestTypeDef = TypedDict(
    "DescribeAgentVersionsRequestRequestTypeDef",
    {
        "StackId": NotRequired[str],
        "ConfigurationManager": NotRequired["StackConfigurationManagerTypeDef"],
    },
)

DescribeAgentVersionsResultTypeDef = TypedDict(
    "DescribeAgentVersionsResultTypeDef",
    {
        "AgentVersions": List["AgentVersionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAppsRequestAppExistsWaitTypeDef = TypedDict(
    "DescribeAppsRequestAppExistsWaitTypeDef",
    {
        "StackId": NotRequired[str],
        "AppIds": NotRequired[Sequence[str]],
        "WaiterConfig": NotRequired["WaiterConfigTypeDef"],
    },
)

DescribeAppsRequestRequestTypeDef = TypedDict(
    "DescribeAppsRequestRequestTypeDef",
    {
        "StackId": NotRequired[str],
        "AppIds": NotRequired[Sequence[str]],
    },
)

DescribeAppsResultTypeDef = TypedDict(
    "DescribeAppsResultTypeDef",
    {
        "Apps": List["AppTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCommandsRequestRequestTypeDef = TypedDict(
    "DescribeCommandsRequestRequestTypeDef",
    {
        "DeploymentId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "CommandIds": NotRequired[Sequence[str]],
    },
)

DescribeCommandsResultTypeDef = TypedDict(
    "DescribeCommandsResultTypeDef",
    {
        "Commands": List["CommandTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDeploymentsRequestDeploymentSuccessfulWaitTypeDef = TypedDict(
    "DescribeDeploymentsRequestDeploymentSuccessfulWaitTypeDef",
    {
        "StackId": NotRequired[str],
        "AppId": NotRequired[str],
        "DeploymentIds": NotRequired[Sequence[str]],
        "WaiterConfig": NotRequired["WaiterConfigTypeDef"],
    },
)

DescribeDeploymentsRequestRequestTypeDef = TypedDict(
    "DescribeDeploymentsRequestRequestTypeDef",
    {
        "StackId": NotRequired[str],
        "AppId": NotRequired[str],
        "DeploymentIds": NotRequired[Sequence[str]],
    },
)

DescribeDeploymentsResultTypeDef = TypedDict(
    "DescribeDeploymentsResultTypeDef",
    {
        "Deployments": List["DeploymentTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEcsClustersRequestDescribeEcsClustersPaginateTypeDef = TypedDict(
    "DescribeEcsClustersRequestDescribeEcsClustersPaginateTypeDef",
    {
        "EcsClusterArns": NotRequired[Sequence[str]],
        "StackId": NotRequired[str],
        "PaginationConfig": NotRequired["PaginatorConfigTypeDef"],
    },
)

DescribeEcsClustersRequestRequestTypeDef = TypedDict(
    "DescribeEcsClustersRequestRequestTypeDef",
    {
        "EcsClusterArns": NotRequired[Sequence[str]],
        "StackId": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeEcsClustersResultTypeDef = TypedDict(
    "DescribeEcsClustersResultTypeDef",
    {
        "EcsClusters": List["EcsClusterTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeElasticIpsRequestRequestTypeDef = TypedDict(
    "DescribeElasticIpsRequestRequestTypeDef",
    {
        "InstanceId": NotRequired[str],
        "StackId": NotRequired[str],
        "Ips": NotRequired[Sequence[str]],
    },
)

DescribeElasticIpsResultTypeDef = TypedDict(
    "DescribeElasticIpsResultTypeDef",
    {
        "ElasticIps": List["ElasticIpTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeElasticLoadBalancersRequestRequestTypeDef = TypedDict(
    "DescribeElasticLoadBalancersRequestRequestTypeDef",
    {
        "StackId": NotRequired[str],
        "LayerIds": NotRequired[Sequence[str]],
    },
)

DescribeElasticLoadBalancersResultTypeDef = TypedDict(
    "DescribeElasticLoadBalancersResultTypeDef",
    {
        "ElasticLoadBalancers": List["ElasticLoadBalancerTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstancesRequestInstanceOnlineWaitTypeDef = TypedDict(
    "DescribeInstancesRequestInstanceOnlineWaitTypeDef",
    {
        "StackId": NotRequired[str],
        "LayerId": NotRequired[str],
        "InstanceIds": NotRequired[Sequence[str]],
        "WaiterConfig": NotRequired["WaiterConfigTypeDef"],
    },
)

DescribeInstancesRequestInstanceRegisteredWaitTypeDef = TypedDict(
    "DescribeInstancesRequestInstanceRegisteredWaitTypeDef",
    {
        "StackId": NotRequired[str],
        "LayerId": NotRequired[str],
        "InstanceIds": NotRequired[Sequence[str]],
        "WaiterConfig": NotRequired["WaiterConfigTypeDef"],
    },
)

DescribeInstancesRequestInstanceStoppedWaitTypeDef = TypedDict(
    "DescribeInstancesRequestInstanceStoppedWaitTypeDef",
    {
        "StackId": NotRequired[str],
        "LayerId": NotRequired[str],
        "InstanceIds": NotRequired[Sequence[str]],
        "WaiterConfig": NotRequired["WaiterConfigTypeDef"],
    },
)

DescribeInstancesRequestInstanceTerminatedWaitTypeDef = TypedDict(
    "DescribeInstancesRequestInstanceTerminatedWaitTypeDef",
    {
        "StackId": NotRequired[str],
        "LayerId": NotRequired[str],
        "InstanceIds": NotRequired[Sequence[str]],
        "WaiterConfig": NotRequired["WaiterConfigTypeDef"],
    },
)

DescribeInstancesRequestRequestTypeDef = TypedDict(
    "DescribeInstancesRequestRequestTypeDef",
    {
        "StackId": NotRequired[str],
        "LayerId": NotRequired[str],
        "InstanceIds": NotRequired[Sequence[str]],
    },
)

DescribeInstancesResultTypeDef = TypedDict(
    "DescribeInstancesResultTypeDef",
    {
        "Instances": List["InstanceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLayersRequestRequestTypeDef = TypedDict(
    "DescribeLayersRequestRequestTypeDef",
    {
        "StackId": NotRequired[str],
        "LayerIds": NotRequired[Sequence[str]],
    },
)

DescribeLayersResultTypeDef = TypedDict(
    "DescribeLayersResultTypeDef",
    {
        "Layers": List["LayerTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLoadBasedAutoScalingRequestRequestTypeDef = TypedDict(
    "DescribeLoadBasedAutoScalingRequestRequestTypeDef",
    {
        "LayerIds": Sequence[str],
    },
)

DescribeLoadBasedAutoScalingResultTypeDef = TypedDict(
    "DescribeLoadBasedAutoScalingResultTypeDef",
    {
        "LoadBasedAutoScalingConfigurations": List["LoadBasedAutoScalingConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMyUserProfileResultTypeDef = TypedDict(
    "DescribeMyUserProfileResultTypeDef",
    {
        "UserProfile": "SelfUserProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOperatingSystemsResponseTypeDef = TypedDict(
    "DescribeOperatingSystemsResponseTypeDef",
    {
        "OperatingSystems": List["OperatingSystemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePermissionsRequestRequestTypeDef = TypedDict(
    "DescribePermissionsRequestRequestTypeDef",
    {
        "IamUserArn": NotRequired[str],
        "StackId": NotRequired[str],
    },
)

DescribePermissionsResultTypeDef = TypedDict(
    "DescribePermissionsResultTypeDef",
    {
        "Permissions": List["PermissionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRaidArraysRequestRequestTypeDef = TypedDict(
    "DescribeRaidArraysRequestRequestTypeDef",
    {
        "InstanceId": NotRequired[str],
        "StackId": NotRequired[str],
        "RaidArrayIds": NotRequired[Sequence[str]],
    },
)

DescribeRaidArraysResultTypeDef = TypedDict(
    "DescribeRaidArraysResultTypeDef",
    {
        "RaidArrays": List["RaidArrayTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRdsDbInstancesRequestRequestTypeDef = TypedDict(
    "DescribeRdsDbInstancesRequestRequestTypeDef",
    {
        "StackId": str,
        "RdsDbInstanceArns": NotRequired[Sequence[str]],
    },
)

DescribeRdsDbInstancesResultTypeDef = TypedDict(
    "DescribeRdsDbInstancesResultTypeDef",
    {
        "RdsDbInstances": List["RdsDbInstanceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeServiceErrorsRequestRequestTypeDef = TypedDict(
    "DescribeServiceErrorsRequestRequestTypeDef",
    {
        "StackId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "ServiceErrorIds": NotRequired[Sequence[str]],
    },
)

DescribeServiceErrorsResultTypeDef = TypedDict(
    "DescribeServiceErrorsResultTypeDef",
    {
        "ServiceErrors": List["ServiceErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStackProvisioningParametersRequestRequestTypeDef = TypedDict(
    "DescribeStackProvisioningParametersRequestRequestTypeDef",
    {
        "StackId": str,
    },
)

DescribeStackProvisioningParametersResultTypeDef = TypedDict(
    "DescribeStackProvisioningParametersResultTypeDef",
    {
        "AgentInstallerUrl": str,
        "Parameters": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStackSummaryRequestRequestTypeDef = TypedDict(
    "DescribeStackSummaryRequestRequestTypeDef",
    {
        "StackId": str,
    },
)

DescribeStackSummaryResultTypeDef = TypedDict(
    "DescribeStackSummaryResultTypeDef",
    {
        "StackSummary": "StackSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStacksRequestRequestTypeDef = TypedDict(
    "DescribeStacksRequestRequestTypeDef",
    {
        "StackIds": NotRequired[Sequence[str]],
    },
)

DescribeStacksResultTypeDef = TypedDict(
    "DescribeStacksResultTypeDef",
    {
        "Stacks": List["StackTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTimeBasedAutoScalingRequestRequestTypeDef = TypedDict(
    "DescribeTimeBasedAutoScalingRequestRequestTypeDef",
    {
        "InstanceIds": Sequence[str],
    },
)

DescribeTimeBasedAutoScalingResultTypeDef = TypedDict(
    "DescribeTimeBasedAutoScalingResultTypeDef",
    {
        "TimeBasedAutoScalingConfigurations": List["TimeBasedAutoScalingConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserProfilesRequestRequestTypeDef = TypedDict(
    "DescribeUserProfilesRequestRequestTypeDef",
    {
        "IamUserArns": NotRequired[Sequence[str]],
    },
)

DescribeUserProfilesResultTypeDef = TypedDict(
    "DescribeUserProfilesResultTypeDef",
    {
        "UserProfiles": List["UserProfileTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVolumesRequestRequestTypeDef = TypedDict(
    "DescribeVolumesRequestRequestTypeDef",
    {
        "InstanceId": NotRequired[str],
        "StackId": NotRequired[str],
        "RaidArrayId": NotRequired[str],
        "VolumeIds": NotRequired[Sequence[str]],
    },
)

DescribeVolumesResultTypeDef = TypedDict(
    "DescribeVolumesResultTypeDef",
    {
        "Volumes": List["VolumeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetachElasticLoadBalancerRequestRequestTypeDef = TypedDict(
    "DetachElasticLoadBalancerRequestRequestTypeDef",
    {
        "ElasticLoadBalancerName": str,
        "LayerId": str,
    },
)

DisassociateElasticIpRequestRequestTypeDef = TypedDict(
    "DisassociateElasticIpRequestRequestTypeDef",
    {
        "ElasticIp": str,
    },
)

EbsBlockDeviceTypeDef = TypedDict(
    "EbsBlockDeviceTypeDef",
    {
        "SnapshotId": NotRequired[str],
        "Iops": NotRequired[int],
        "VolumeSize": NotRequired[int],
        "VolumeType": NotRequired[VolumeTypeType],
        "DeleteOnTermination": NotRequired[bool],
    },
)

EcsClusterTypeDef = TypedDict(
    "EcsClusterTypeDef",
    {
        "EcsClusterArn": NotRequired[str],
        "EcsClusterName": NotRequired[str],
        "StackId": NotRequired[str],
        "RegisteredAt": NotRequired[str],
    },
)

ElasticIpTypeDef = TypedDict(
    "ElasticIpTypeDef",
    {
        "Ip": NotRequired[str],
        "Name": NotRequired[str],
        "Domain": NotRequired[str],
        "Region": NotRequired[str],
        "InstanceId": NotRequired[str],
    },
)

ElasticLoadBalancerTypeDef = TypedDict(
    "ElasticLoadBalancerTypeDef",
    {
        "ElasticLoadBalancerName": NotRequired[str],
        "Region": NotRequired[str],
        "DnsName": NotRequired[str],
        "StackId": NotRequired[str],
        "LayerId": NotRequired[str],
        "VpcId": NotRequired[str],
        "AvailabilityZones": NotRequired[List[str]],
        "SubnetIds": NotRequired[List[str]],
        "Ec2InstanceIds": NotRequired[List[str]],
    },
)

EnvironmentVariableTypeDef = TypedDict(
    "EnvironmentVariableTypeDef",
    {
        "Key": str,
        "Value": str,
        "Secure": NotRequired[bool],
    },
)

GetHostnameSuggestionRequestRequestTypeDef = TypedDict(
    "GetHostnameSuggestionRequestRequestTypeDef",
    {
        "LayerId": str,
    },
)

GetHostnameSuggestionResultTypeDef = TypedDict(
    "GetHostnameSuggestionResultTypeDef",
    {
        "LayerId": str,
        "Hostname": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GrantAccessRequestRequestTypeDef = TypedDict(
    "GrantAccessRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ValidForInMinutes": NotRequired[int],
    },
)

GrantAccessResultTypeDef = TypedDict(
    "GrantAccessResultTypeDef",
    {
        "TemporaryCredential": "TemporaryCredentialTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InstanceIdentityTypeDef = TypedDict(
    "InstanceIdentityTypeDef",
    {
        "Document": NotRequired[str],
        "Signature": NotRequired[str],
    },
)

InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "AgentVersion": NotRequired[str],
        "AmiId": NotRequired[str],
        "Architecture": NotRequired[ArchitectureType],
        "Arn": NotRequired[str],
        "AutoScalingType": NotRequired[AutoScalingTypeType],
        "AvailabilityZone": NotRequired[str],
        "BlockDeviceMappings": NotRequired[List["BlockDeviceMappingTypeDef"]],
        "CreatedAt": NotRequired[str],
        "EbsOptimized": NotRequired[bool],
        "Ec2InstanceId": NotRequired[str],
        "EcsClusterArn": NotRequired[str],
        "EcsContainerInstanceArn": NotRequired[str],
        "ElasticIp": NotRequired[str],
        "Hostname": NotRequired[str],
        "InfrastructureClass": NotRequired[str],
        "InstallUpdatesOnBoot": NotRequired[bool],
        "InstanceId": NotRequired[str],
        "InstanceProfileArn": NotRequired[str],
        "InstanceType": NotRequired[str],
        "LastServiceErrorId": NotRequired[str],
        "LayerIds": NotRequired[List[str]],
        "Os": NotRequired[str],
        "Platform": NotRequired[str],
        "PrivateDns": NotRequired[str],
        "PrivateIp": NotRequired[str],
        "PublicDns": NotRequired[str],
        "PublicIp": NotRequired[str],
        "RegisteredBy": NotRequired[str],
        "ReportedAgentVersion": NotRequired[str],
        "ReportedOs": NotRequired["ReportedOsTypeDef"],
        "RootDeviceType": NotRequired[RootDeviceTypeType],
        "RootDeviceVolumeId": NotRequired[str],
        "SecurityGroupIds": NotRequired[List[str]],
        "SshHostDsaKeyFingerprint": NotRequired[str],
        "SshHostRsaKeyFingerprint": NotRequired[str],
        "SshKeyName": NotRequired[str],
        "StackId": NotRequired[str],
        "Status": NotRequired[str],
        "SubnetId": NotRequired[str],
        "Tenancy": NotRequired[str],
        "VirtualizationType": NotRequired[VirtualizationTypeType],
    },
)

InstancesCountResponseMetadataTypeDef = TypedDict(
    "InstancesCountResponseMetadataTypeDef",
    {
        "Assigning": int,
        "Booting": int,
        "ConnectionLost": int,
        "Deregistering": int,
        "Online": int,
        "Pending": int,
        "Rebooting": int,
        "Registered": int,
        "Registering": int,
        "Requested": int,
        "RunningSetup": int,
        "SetupFailed": int,
        "ShuttingDown": int,
        "StartFailed": int,
        "StopFailed": int,
        "Stopped": int,
        "Stopping": int,
        "Terminated": int,
        "Terminating": int,
        "Unassigning": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InstancesCountTypeDef = TypedDict(
    "InstancesCountTypeDef",
    {
        "Assigning": NotRequired[int],
        "Booting": NotRequired[int],
        "ConnectionLost": NotRequired[int],
        "Deregistering": NotRequired[int],
        "Online": NotRequired[int],
        "Pending": NotRequired[int],
        "Rebooting": NotRequired[int],
        "Registered": NotRequired[int],
        "Registering": NotRequired[int],
        "Requested": NotRequired[int],
        "RunningSetup": NotRequired[int],
        "SetupFailed": NotRequired[int],
        "ShuttingDown": NotRequired[int],
        "StartFailed": NotRequired[int],
        "StopFailed": NotRequired[int],
        "Stopped": NotRequired[int],
        "Stopping": NotRequired[int],
        "Terminated": NotRequired[int],
        "Terminating": NotRequired[int],
        "Unassigning": NotRequired[int],
    },
)

LayerTypeDef = TypedDict(
    "LayerTypeDef",
    {
        "Arn": NotRequired[str],
        "StackId": NotRequired[str],
        "LayerId": NotRequired[str],
        "Type": NotRequired[LayerTypeType],
        "Name": NotRequired[str],
        "Shortname": NotRequired[str],
        "Attributes": NotRequired[Dict[LayerAttributesKeysType, str]],
        "CloudWatchLogsConfiguration": NotRequired["CloudWatchLogsConfigurationTypeDef"],
        "CustomInstanceProfileArn": NotRequired[str],
        "CustomJson": NotRequired[str],
        "CustomSecurityGroupIds": NotRequired[List[str]],
        "DefaultSecurityGroupNames": NotRequired[List[str]],
        "Packages": NotRequired[List[str]],
        "VolumeConfigurations": NotRequired[List["VolumeConfigurationTypeDef"]],
        "EnableAutoHealing": NotRequired[bool],
        "AutoAssignElasticIps": NotRequired[bool],
        "AutoAssignPublicIps": NotRequired[bool],
        "DefaultRecipes": NotRequired["RecipesTypeDef"],
        "CustomRecipes": NotRequired["RecipesTypeDef"],
        "CreatedAt": NotRequired[str],
        "InstallUpdatesOnBoot": NotRequired[bool],
        "UseEbsOptimizedInstances": NotRequired[bool],
        "LifecycleEventConfiguration": NotRequired["LifecycleEventConfigurationTypeDef"],
    },
)

LifecycleEventConfigurationResponseMetadataTypeDef = TypedDict(
    "LifecycleEventConfigurationResponseMetadataTypeDef",
    {
        "Shutdown": "ShutdownEventConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LifecycleEventConfigurationTypeDef = TypedDict(
    "LifecycleEventConfigurationTypeDef",
    {
        "Shutdown": NotRequired["ShutdownEventConfigurationTypeDef"],
    },
)

ListTagsRequestRequestTypeDef = TypedDict(
    "ListTagsRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListTagsResultTypeDef = TypedDict(
    "ListTagsResultTypeDef",
    {
        "Tags": Dict[str, str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoadBasedAutoScalingConfigurationTypeDef = TypedDict(
    "LoadBasedAutoScalingConfigurationTypeDef",
    {
        "LayerId": NotRequired[str],
        "Enable": NotRequired[bool],
        "UpScaling": NotRequired["AutoScalingThresholdsTypeDef"],
        "DownScaling": NotRequired["AutoScalingThresholdsTypeDef"],
    },
)

OperatingSystemConfigurationManagerTypeDef = TypedDict(
    "OperatingSystemConfigurationManagerTypeDef",
    {
        "Name": NotRequired[str],
        "Version": NotRequired[str],
    },
)

OperatingSystemTypeDef = TypedDict(
    "OperatingSystemTypeDef",
    {
        "Name": NotRequired[str],
        "Id": NotRequired[str],
        "Type": NotRequired[str],
        "ConfigurationManagers": NotRequired[List["OperatingSystemConfigurationManagerTypeDef"]],
        "ReportedName": NotRequired[str],
        "ReportedVersion": NotRequired[str],
        "Supported": NotRequired[bool],
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": NotRequired[int],
        "PageSize": NotRequired[int],
        "StartingToken": NotRequired[str],
    },
)

PermissionTypeDef = TypedDict(
    "PermissionTypeDef",
    {
        "StackId": NotRequired[str],
        "IamUserArn": NotRequired[str],
        "AllowSsh": NotRequired[bool],
        "AllowSudo": NotRequired[bool],
        "Level": NotRequired[str],
    },
)

RaidArrayTypeDef = TypedDict(
    "RaidArrayTypeDef",
    {
        "RaidArrayId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "Name": NotRequired[str],
        "RaidLevel": NotRequired[int],
        "NumberOfDisks": NotRequired[int],
        "Size": NotRequired[int],
        "Device": NotRequired[str],
        "MountPoint": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "CreatedAt": NotRequired[str],
        "StackId": NotRequired[str],
        "VolumeType": NotRequired[str],
        "Iops": NotRequired[int],
    },
)

RdsDbInstanceTypeDef = TypedDict(
    "RdsDbInstanceTypeDef",
    {
        "RdsDbInstanceArn": NotRequired[str],
        "DbInstanceIdentifier": NotRequired[str],
        "DbUser": NotRequired[str],
        "DbPassword": NotRequired[str],
        "Region": NotRequired[str],
        "Address": NotRequired[str],
        "Engine": NotRequired[str],
        "StackId": NotRequired[str],
        "MissingOnRds": NotRequired[bool],
    },
)

RebootInstanceRequestRequestTypeDef = TypedDict(
    "RebootInstanceRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)

RecipesResponseMetadataTypeDef = TypedDict(
    "RecipesResponseMetadataTypeDef",
    {
        "Setup": List[str],
        "Configure": List[str],
        "Deploy": List[str],
        "Undeploy": List[str],
        "Shutdown": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RecipesTypeDef = TypedDict(
    "RecipesTypeDef",
    {
        "Setup": NotRequired[Sequence[str]],
        "Configure": NotRequired[Sequence[str]],
        "Deploy": NotRequired[Sequence[str]],
        "Undeploy": NotRequired[Sequence[str]],
        "Shutdown": NotRequired[Sequence[str]],
    },
)

RegisterEcsClusterRequestRequestTypeDef = TypedDict(
    "RegisterEcsClusterRequestRequestTypeDef",
    {
        "EcsClusterArn": str,
        "StackId": str,
    },
)

RegisterEcsClusterResultTypeDef = TypedDict(
    "RegisterEcsClusterResultTypeDef",
    {
        "EcsClusterArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisterElasticIpRequestRequestTypeDef = TypedDict(
    "RegisterElasticIpRequestRequestTypeDef",
    {
        "ElasticIp": str,
        "StackId": str,
    },
)

RegisterElasticIpResultTypeDef = TypedDict(
    "RegisterElasticIpResultTypeDef",
    {
        "ElasticIp": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisterInstanceRequestRequestTypeDef = TypedDict(
    "RegisterInstanceRequestRequestTypeDef",
    {
        "StackId": str,
        "Hostname": NotRequired[str],
        "PublicIp": NotRequired[str],
        "PrivateIp": NotRequired[str],
        "RsaPublicKey": NotRequired[str],
        "RsaPublicKeyFingerprint": NotRequired[str],
        "InstanceIdentity": NotRequired["InstanceIdentityTypeDef"],
    },
)

RegisterInstanceResultTypeDef = TypedDict(
    "RegisterInstanceResultTypeDef",
    {
        "InstanceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisterRdsDbInstanceRequestRequestTypeDef = TypedDict(
    "RegisterRdsDbInstanceRequestRequestTypeDef",
    {
        "StackId": str,
        "RdsDbInstanceArn": str,
        "DbUser": str,
        "DbPassword": str,
    },
)

RegisterVolumeRequestRequestTypeDef = TypedDict(
    "RegisterVolumeRequestRequestTypeDef",
    {
        "StackId": str,
        "Ec2VolumeId": NotRequired[str],
    },
)

RegisterVolumeResultTypeDef = TypedDict(
    "RegisterVolumeResultTypeDef",
    {
        "VolumeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReportedOsTypeDef = TypedDict(
    "ReportedOsTypeDef",
    {
        "Family": NotRequired[str],
        "Name": NotRequired[str],
        "Version": NotRequired[str],
    },
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, str],
        "RetryAttempts": int,
    },
)

SelfUserProfileTypeDef = TypedDict(
    "SelfUserProfileTypeDef",
    {
        "IamUserArn": NotRequired[str],
        "Name": NotRequired[str],
        "SshUsername": NotRequired[str],
        "SshPublicKey": NotRequired[str],
    },
)

ServiceErrorTypeDef = TypedDict(
    "ServiceErrorTypeDef",
    {
        "ServiceErrorId": NotRequired[str],
        "StackId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "Type": NotRequired[str],
        "Message": NotRequired[str],
        "CreatedAt": NotRequired[str],
    },
)

ServiceResourceLayerRequestTypeDef = TypedDict(
    "ServiceResourceLayerRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceStackRequestTypeDef = TypedDict(
    "ServiceResourceStackRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceStackSummaryRequestTypeDef = TypedDict(
    "ServiceResourceStackSummaryRequestTypeDef",
    {
        "stack_id": str,
    },
)

SetLoadBasedAutoScalingRequestRequestTypeDef = TypedDict(
    "SetLoadBasedAutoScalingRequestRequestTypeDef",
    {
        "LayerId": str,
        "Enable": NotRequired[bool],
        "UpScaling": NotRequired["AutoScalingThresholdsTypeDef"],
        "DownScaling": NotRequired["AutoScalingThresholdsTypeDef"],
    },
)

SetPermissionRequestRequestTypeDef = TypedDict(
    "SetPermissionRequestRequestTypeDef",
    {
        "StackId": str,
        "IamUserArn": str,
        "AllowSsh": NotRequired[bool],
        "AllowSudo": NotRequired[bool],
        "Level": NotRequired[str],
    },
)

SetTimeBasedAutoScalingRequestRequestTypeDef = TypedDict(
    "SetTimeBasedAutoScalingRequestRequestTypeDef",
    {
        "InstanceId": str,
        "AutoScalingSchedule": NotRequired["WeeklyAutoScalingScheduleTypeDef"],
    },
)

ShutdownEventConfigurationTypeDef = TypedDict(
    "ShutdownEventConfigurationTypeDef",
    {
        "ExecutionTimeout": NotRequired[int],
        "DelayUntilElbConnectionsDrained": NotRequired[bool],
    },
)

SourceResponseMetadataTypeDef = TypedDict(
    "SourceResponseMetadataTypeDef",
    {
        "Type": SourceTypeType,
        "Url": str,
        "Username": str,
        "Password": str,
        "SshKey": str,
        "Revision": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SourceTypeDef = TypedDict(
    "SourceTypeDef",
    {
        "Type": NotRequired[SourceTypeType],
        "Url": NotRequired[str],
        "Username": NotRequired[str],
        "Password": NotRequired[str],
        "SshKey": NotRequired[str],
        "Revision": NotRequired[str],
    },
)

SslConfigurationTypeDef = TypedDict(
    "SslConfigurationTypeDef",
    {
        "Certificate": str,
        "PrivateKey": str,
        "Chain": NotRequired[str],
    },
)

StackConfigurationManagerResponseMetadataTypeDef = TypedDict(
    "StackConfigurationManagerResponseMetadataTypeDef",
    {
        "Name": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StackConfigurationManagerTypeDef = TypedDict(
    "StackConfigurationManagerTypeDef",
    {
        "Name": NotRequired[str],
        "Version": NotRequired[str],
    },
)

StackSummaryTypeDef = TypedDict(
    "StackSummaryTypeDef",
    {
        "StackId": NotRequired[str],
        "Name": NotRequired[str],
        "Arn": NotRequired[str],
        "LayersCount": NotRequired[int],
        "AppsCount": NotRequired[int],
        "InstancesCount": NotRequired["InstancesCountTypeDef"],
    },
)

StackTypeDef = TypedDict(
    "StackTypeDef",
    {
        "StackId": NotRequired[str],
        "Name": NotRequired[str],
        "Arn": NotRequired[str],
        "Region": NotRequired[str],
        "VpcId": NotRequired[str],
        "Attributes": NotRequired[Dict[Literal["Color"], str]],
        "ServiceRoleArn": NotRequired[str],
        "DefaultInstanceProfileArn": NotRequired[str],
        "DefaultOs": NotRequired[str],
        "HostnameTheme": NotRequired[str],
        "DefaultAvailabilityZone": NotRequired[str],
        "DefaultSubnetId": NotRequired[str],
        "CustomJson": NotRequired[str],
        "ConfigurationManager": NotRequired["StackConfigurationManagerTypeDef"],
        "ChefConfiguration": NotRequired["ChefConfigurationTypeDef"],
        "UseCustomCookbooks": NotRequired[bool],
        "UseOpsworksSecurityGroups": NotRequired[bool],
        "CustomCookbooksSource": NotRequired["SourceTypeDef"],
        "DefaultSshKeyName": NotRequired[str],
        "CreatedAt": NotRequired[str],
        "DefaultRootDeviceType": NotRequired[RootDeviceTypeType],
        "AgentVersion": NotRequired[str],
    },
)

StartInstanceRequestRequestTypeDef = TypedDict(
    "StartInstanceRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)

StartStackRequestRequestTypeDef = TypedDict(
    "StartStackRequestRequestTypeDef",
    {
        "StackId": str,
    },
)

StopInstanceRequestRequestTypeDef = TypedDict(
    "StopInstanceRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Force": NotRequired[bool],
    },
)

StopStackRequestRequestTypeDef = TypedDict(
    "StopStackRequestRequestTypeDef",
    {
        "StackId": str,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)

TemporaryCredentialTypeDef = TypedDict(
    "TemporaryCredentialTypeDef",
    {
        "Username": NotRequired[str],
        "Password": NotRequired[str],
        "ValidForInMinutes": NotRequired[int],
        "InstanceId": NotRequired[str],
    },
)

TimeBasedAutoScalingConfigurationTypeDef = TypedDict(
    "TimeBasedAutoScalingConfigurationTypeDef",
    {
        "InstanceId": NotRequired[str],
        "AutoScalingSchedule": NotRequired["WeeklyAutoScalingScheduleTypeDef"],
    },
)

UnassignInstanceRequestRequestTypeDef = TypedDict(
    "UnassignInstanceRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)

UnassignVolumeRequestRequestTypeDef = TypedDict(
    "UnassignVolumeRequestRequestTypeDef",
    {
        "VolumeId": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateAppRequestRequestTypeDef = TypedDict(
    "UpdateAppRequestRequestTypeDef",
    {
        "AppId": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "DataSources": NotRequired[Sequence["DataSourceTypeDef"]],
        "Type": NotRequired[AppTypeType],
        "AppSource": NotRequired["SourceTypeDef"],
        "Domains": NotRequired[Sequence[str]],
        "EnableSsl": NotRequired[bool],
        "SslConfiguration": NotRequired["SslConfigurationTypeDef"],
        "Attributes": NotRequired[Mapping[AppAttributesKeysType, str]],
        "Environment": NotRequired[Sequence["EnvironmentVariableTypeDef"]],
    },
)

UpdateElasticIpRequestRequestTypeDef = TypedDict(
    "UpdateElasticIpRequestRequestTypeDef",
    {
        "ElasticIp": str,
        "Name": NotRequired[str],
    },
)

UpdateInstanceRequestRequestTypeDef = TypedDict(
    "UpdateInstanceRequestRequestTypeDef",
    {
        "InstanceId": str,
        "LayerIds": NotRequired[Sequence[str]],
        "InstanceType": NotRequired[str],
        "AutoScalingType": NotRequired[AutoScalingTypeType],
        "Hostname": NotRequired[str],
        "Os": NotRequired[str],
        "AmiId": NotRequired[str],
        "SshKeyName": NotRequired[str],
        "Architecture": NotRequired[ArchitectureType],
        "InstallUpdatesOnBoot": NotRequired[bool],
        "EbsOptimized": NotRequired[bool],
        "AgentVersion": NotRequired[str],
    },
)

UpdateLayerRequestRequestTypeDef = TypedDict(
    "UpdateLayerRequestRequestTypeDef",
    {
        "LayerId": str,
        "Name": NotRequired[str],
        "Shortname": NotRequired[str],
        "Attributes": NotRequired[Mapping[LayerAttributesKeysType, str]],
        "CloudWatchLogsConfiguration": NotRequired["CloudWatchLogsConfigurationTypeDef"],
        "CustomInstanceProfileArn": NotRequired[str],
        "CustomJson": NotRequired[str],
        "CustomSecurityGroupIds": NotRequired[Sequence[str]],
        "Packages": NotRequired[Sequence[str]],
        "VolumeConfigurations": NotRequired[Sequence["VolumeConfigurationTypeDef"]],
        "EnableAutoHealing": NotRequired[bool],
        "AutoAssignElasticIps": NotRequired[bool],
        "AutoAssignPublicIps": NotRequired[bool],
        "CustomRecipes": NotRequired["RecipesTypeDef"],
        "InstallUpdatesOnBoot": NotRequired[bool],
        "UseEbsOptimizedInstances": NotRequired[bool],
        "LifecycleEventConfiguration": NotRequired["LifecycleEventConfigurationTypeDef"],
    },
)

UpdateMyUserProfileRequestRequestTypeDef = TypedDict(
    "UpdateMyUserProfileRequestRequestTypeDef",
    {
        "SshPublicKey": NotRequired[str],
    },
)

UpdateRdsDbInstanceRequestRequestTypeDef = TypedDict(
    "UpdateRdsDbInstanceRequestRequestTypeDef",
    {
        "RdsDbInstanceArn": str,
        "DbUser": NotRequired[str],
        "DbPassword": NotRequired[str],
    },
)

UpdateStackRequestRequestTypeDef = TypedDict(
    "UpdateStackRequestRequestTypeDef",
    {
        "StackId": str,
        "Name": NotRequired[str],
        "Attributes": NotRequired[Mapping[Literal["Color"], str]],
        "ServiceRoleArn": NotRequired[str],
        "DefaultInstanceProfileArn": NotRequired[str],
        "DefaultOs": NotRequired[str],
        "HostnameTheme": NotRequired[str],
        "DefaultAvailabilityZone": NotRequired[str],
        "DefaultSubnetId": NotRequired[str],
        "CustomJson": NotRequired[str],
        "ConfigurationManager": NotRequired["StackConfigurationManagerTypeDef"],
        "ChefConfiguration": NotRequired["ChefConfigurationTypeDef"],
        "UseCustomCookbooks": NotRequired[bool],
        "CustomCookbooksSource": NotRequired["SourceTypeDef"],
        "DefaultSshKeyName": NotRequired[str],
        "DefaultRootDeviceType": NotRequired[RootDeviceTypeType],
        "UseOpsworksSecurityGroups": NotRequired[bool],
        "AgentVersion": NotRequired[str],
    },
)

UpdateUserProfileRequestRequestTypeDef = TypedDict(
    "UpdateUserProfileRequestRequestTypeDef",
    {
        "IamUserArn": str,
        "SshUsername": NotRequired[str],
        "SshPublicKey": NotRequired[str],
        "AllowSelfManagement": NotRequired[bool],
    },
)

UpdateVolumeRequestRequestTypeDef = TypedDict(
    "UpdateVolumeRequestRequestTypeDef",
    {
        "VolumeId": str,
        "Name": NotRequired[str],
        "MountPoint": NotRequired[str],
    },
)

UserProfileTypeDef = TypedDict(
    "UserProfileTypeDef",
    {
        "IamUserArn": NotRequired[str],
        "Name": NotRequired[str],
        "SshUsername": NotRequired[str],
        "SshPublicKey": NotRequired[str],
        "AllowSelfManagement": NotRequired[bool],
    },
)

VolumeConfigurationTypeDef = TypedDict(
    "VolumeConfigurationTypeDef",
    {
        "MountPoint": str,
        "NumberOfDisks": int,
        "Size": int,
        "RaidLevel": NotRequired[int],
        "VolumeType": NotRequired[str],
        "Iops": NotRequired[int],
        "Encrypted": NotRequired[bool],
    },
)

VolumeTypeDef = TypedDict(
    "VolumeTypeDef",
    {
        "VolumeId": NotRequired[str],
        "Ec2VolumeId": NotRequired[str],
        "Name": NotRequired[str],
        "RaidArrayId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "Status": NotRequired[str],
        "Size": NotRequired[int],
        "Device": NotRequired[str],
        "MountPoint": NotRequired[str],
        "Region": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "VolumeType": NotRequired[str],
        "Iops": NotRequired[int],
        "Encrypted": NotRequired[bool],
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)

WeeklyAutoScalingScheduleTypeDef = TypedDict(
    "WeeklyAutoScalingScheduleTypeDef",
    {
        "Monday": NotRequired[Dict[str, str]],
        "Tuesday": NotRequired[Dict[str, str]],
        "Wednesday": NotRequired[Dict[str, str]],
        "Thursday": NotRequired[Dict[str, str]],
        "Friday": NotRequired[Dict[str, str]],
        "Saturday": NotRequired[Dict[str, str]],
        "Sunday": NotRequired[Dict[str, str]],
    },
)
