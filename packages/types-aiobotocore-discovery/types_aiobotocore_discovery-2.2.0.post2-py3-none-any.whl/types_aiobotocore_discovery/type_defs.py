"""
Type annotations for discovery service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_discovery/type_defs/)

Usage::

    ```python
    from types_aiobotocore_discovery.type_defs import AgentConfigurationStatusTypeDef

    data: AgentConfigurationStatusTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    AgentStatusType,
    BatchDeleteImportDataErrorCodeType,
    ConfigurationItemTypeType,
    ContinuousExportStatusType,
    ExportDataFormatType,
    ExportStatusType,
    ImportStatusType,
    ImportTaskFilterNameType,
    orderStringType,
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
    "AgentConfigurationStatusTypeDef",
    "AgentInfoTypeDef",
    "AgentNetworkInfoTypeDef",
    "AssociateConfigurationItemsToApplicationRequestRequestTypeDef",
    "BatchDeleteImportDataErrorTypeDef",
    "BatchDeleteImportDataRequestRequestTypeDef",
    "BatchDeleteImportDataResponseTypeDef",
    "ConfigurationTagTypeDef",
    "ContinuousExportDescriptionTypeDef",
    "CreateApplicationRequestRequestTypeDef",
    "CreateApplicationResponseTypeDef",
    "CreateTagsRequestRequestTypeDef",
    "CustomerAgentInfoTypeDef",
    "CustomerConnectorInfoTypeDef",
    "DeleteApplicationsRequestRequestTypeDef",
    "DeleteTagsRequestRequestTypeDef",
    "DescribeAgentsRequestDescribeAgentsPaginateTypeDef",
    "DescribeAgentsRequestRequestTypeDef",
    "DescribeAgentsResponseTypeDef",
    "DescribeConfigurationsRequestRequestTypeDef",
    "DescribeConfigurationsResponseTypeDef",
    "DescribeContinuousExportsRequestDescribeContinuousExportsPaginateTypeDef",
    "DescribeContinuousExportsRequestRequestTypeDef",
    "DescribeContinuousExportsResponseTypeDef",
    "DescribeExportConfigurationsRequestDescribeExportConfigurationsPaginateTypeDef",
    "DescribeExportConfigurationsRequestRequestTypeDef",
    "DescribeExportConfigurationsResponseTypeDef",
    "DescribeExportTasksRequestDescribeExportTasksPaginateTypeDef",
    "DescribeExportTasksRequestRequestTypeDef",
    "DescribeExportTasksResponseTypeDef",
    "DescribeImportTasksRequestRequestTypeDef",
    "DescribeImportTasksResponseTypeDef",
    "DescribeTagsRequestDescribeTagsPaginateTypeDef",
    "DescribeTagsRequestRequestTypeDef",
    "DescribeTagsResponseTypeDef",
    "DisassociateConfigurationItemsFromApplicationRequestRequestTypeDef",
    "ExportConfigurationsResponseTypeDef",
    "ExportFilterTypeDef",
    "ExportInfoTypeDef",
    "FilterTypeDef",
    "GetDiscoverySummaryResponseTypeDef",
    "ImportTaskFilterTypeDef",
    "ImportTaskTypeDef",
    "ListConfigurationsRequestListConfigurationsPaginateTypeDef",
    "ListConfigurationsRequestRequestTypeDef",
    "ListConfigurationsResponseTypeDef",
    "ListServerNeighborsRequestRequestTypeDef",
    "ListServerNeighborsResponseTypeDef",
    "NeighborConnectionDetailTypeDef",
    "OrderByElementTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "StartContinuousExportResponseTypeDef",
    "StartDataCollectionByAgentIdsRequestRequestTypeDef",
    "StartDataCollectionByAgentIdsResponseTypeDef",
    "StartExportTaskRequestRequestTypeDef",
    "StartExportTaskResponseTypeDef",
    "StartImportTaskRequestRequestTypeDef",
    "StartImportTaskResponseTypeDef",
    "StopContinuousExportRequestRequestTypeDef",
    "StopContinuousExportResponseTypeDef",
    "StopDataCollectionByAgentIdsRequestRequestTypeDef",
    "StopDataCollectionByAgentIdsResponseTypeDef",
    "TagFilterTypeDef",
    "TagTypeDef",
    "UpdateApplicationRequestRequestTypeDef",
)

AgentConfigurationStatusTypeDef = TypedDict(
    "AgentConfigurationStatusTypeDef",
    {
        "agentId": NotRequired[str],
        "operationSucceeded": NotRequired[bool],
        "description": NotRequired[str],
    },
)

AgentInfoTypeDef = TypedDict(
    "AgentInfoTypeDef",
    {
        "agentId": NotRequired[str],
        "hostName": NotRequired[str],
        "agentNetworkInfoList": NotRequired[List["AgentNetworkInfoTypeDef"]],
        "connectorId": NotRequired[str],
        "version": NotRequired[str],
        "health": NotRequired[AgentStatusType],
        "lastHealthPingTime": NotRequired[str],
        "collectionStatus": NotRequired[str],
        "agentType": NotRequired[str],
        "registeredTime": NotRequired[str],
    },
)

AgentNetworkInfoTypeDef = TypedDict(
    "AgentNetworkInfoTypeDef",
    {
        "ipAddress": NotRequired[str],
        "macAddress": NotRequired[str],
    },
)

AssociateConfigurationItemsToApplicationRequestRequestTypeDef = TypedDict(
    "AssociateConfigurationItemsToApplicationRequestRequestTypeDef",
    {
        "applicationConfigurationId": str,
        "configurationIds": Sequence[str],
    },
)

BatchDeleteImportDataErrorTypeDef = TypedDict(
    "BatchDeleteImportDataErrorTypeDef",
    {
        "importTaskId": NotRequired[str],
        "errorCode": NotRequired[BatchDeleteImportDataErrorCodeType],
        "errorDescription": NotRequired[str],
    },
)

BatchDeleteImportDataRequestRequestTypeDef = TypedDict(
    "BatchDeleteImportDataRequestRequestTypeDef",
    {
        "importTaskIds": Sequence[str],
    },
)

BatchDeleteImportDataResponseTypeDef = TypedDict(
    "BatchDeleteImportDataResponseTypeDef",
    {
        "errors": List["BatchDeleteImportDataErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConfigurationTagTypeDef = TypedDict(
    "ConfigurationTagTypeDef",
    {
        "configurationType": NotRequired[ConfigurationItemTypeType],
        "configurationId": NotRequired[str],
        "key": NotRequired[str],
        "value": NotRequired[str],
        "timeOfCreation": NotRequired[datetime],
    },
)

ContinuousExportDescriptionTypeDef = TypedDict(
    "ContinuousExportDescriptionTypeDef",
    {
        "exportId": NotRequired[str],
        "status": NotRequired[ContinuousExportStatusType],
        "statusDetail": NotRequired[str],
        "s3Bucket": NotRequired[str],
        "startTime": NotRequired[datetime],
        "stopTime": NotRequired[datetime],
        "dataSource": NotRequired[Literal["AGENT"]],
        "schemaStorageConfig": NotRequired[Dict[str, str]],
    },
)

CreateApplicationRequestRequestTypeDef = TypedDict(
    "CreateApplicationRequestRequestTypeDef",
    {
        "name": str,
        "description": NotRequired[str],
    },
)

CreateApplicationResponseTypeDef = TypedDict(
    "CreateApplicationResponseTypeDef",
    {
        "configurationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTagsRequestRequestTypeDef = TypedDict(
    "CreateTagsRequestRequestTypeDef",
    {
        "configurationIds": Sequence[str],
        "tags": Sequence["TagTypeDef"],
    },
)

CustomerAgentInfoTypeDef = TypedDict(
    "CustomerAgentInfoTypeDef",
    {
        "activeAgents": int,
        "healthyAgents": int,
        "blackListedAgents": int,
        "shutdownAgents": int,
        "unhealthyAgents": int,
        "totalAgents": int,
        "unknownAgents": int,
    },
)

CustomerConnectorInfoTypeDef = TypedDict(
    "CustomerConnectorInfoTypeDef",
    {
        "activeConnectors": int,
        "healthyConnectors": int,
        "blackListedConnectors": int,
        "shutdownConnectors": int,
        "unhealthyConnectors": int,
        "totalConnectors": int,
        "unknownConnectors": int,
    },
)

DeleteApplicationsRequestRequestTypeDef = TypedDict(
    "DeleteApplicationsRequestRequestTypeDef",
    {
        "configurationIds": Sequence[str],
    },
)

DeleteTagsRequestRequestTypeDef = TypedDict(
    "DeleteTagsRequestRequestTypeDef",
    {
        "configurationIds": Sequence[str],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

DescribeAgentsRequestDescribeAgentsPaginateTypeDef = TypedDict(
    "DescribeAgentsRequestDescribeAgentsPaginateTypeDef",
    {
        "agentIds": NotRequired[Sequence[str]],
        "filters": NotRequired[Sequence["FilterTypeDef"]],
        "PaginationConfig": NotRequired["PaginatorConfigTypeDef"],
    },
)

DescribeAgentsRequestRequestTypeDef = TypedDict(
    "DescribeAgentsRequestRequestTypeDef",
    {
        "agentIds": NotRequired[Sequence[str]],
        "filters": NotRequired[Sequence["FilterTypeDef"]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

DescribeAgentsResponseTypeDef = TypedDict(
    "DescribeAgentsResponseTypeDef",
    {
        "agentsInfo": List["AgentInfoTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConfigurationsRequestRequestTypeDef = TypedDict(
    "DescribeConfigurationsRequestRequestTypeDef",
    {
        "configurationIds": Sequence[str],
    },
)

DescribeConfigurationsResponseTypeDef = TypedDict(
    "DescribeConfigurationsResponseTypeDef",
    {
        "configurations": List[Dict[str, str]],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeContinuousExportsRequestDescribeContinuousExportsPaginateTypeDef = TypedDict(
    "DescribeContinuousExportsRequestDescribeContinuousExportsPaginateTypeDef",
    {
        "exportIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired["PaginatorConfigTypeDef"],
    },
)

DescribeContinuousExportsRequestRequestTypeDef = TypedDict(
    "DescribeContinuousExportsRequestRequestTypeDef",
    {
        "exportIds": NotRequired[Sequence[str]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

DescribeContinuousExportsResponseTypeDef = TypedDict(
    "DescribeContinuousExportsResponseTypeDef",
    {
        "descriptions": List["ContinuousExportDescriptionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeExportConfigurationsRequestDescribeExportConfigurationsPaginateTypeDef = TypedDict(
    "DescribeExportConfigurationsRequestDescribeExportConfigurationsPaginateTypeDef",
    {
        "exportIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired["PaginatorConfigTypeDef"],
    },
)

DescribeExportConfigurationsRequestRequestTypeDef = TypedDict(
    "DescribeExportConfigurationsRequestRequestTypeDef",
    {
        "exportIds": NotRequired[Sequence[str]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

DescribeExportConfigurationsResponseTypeDef = TypedDict(
    "DescribeExportConfigurationsResponseTypeDef",
    {
        "exportsInfo": List["ExportInfoTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeExportTasksRequestDescribeExportTasksPaginateTypeDef = TypedDict(
    "DescribeExportTasksRequestDescribeExportTasksPaginateTypeDef",
    {
        "exportIds": NotRequired[Sequence[str]],
        "filters": NotRequired[Sequence["ExportFilterTypeDef"]],
        "PaginationConfig": NotRequired["PaginatorConfigTypeDef"],
    },
)

DescribeExportTasksRequestRequestTypeDef = TypedDict(
    "DescribeExportTasksRequestRequestTypeDef",
    {
        "exportIds": NotRequired[Sequence[str]],
        "filters": NotRequired[Sequence["ExportFilterTypeDef"]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

DescribeExportTasksResponseTypeDef = TypedDict(
    "DescribeExportTasksResponseTypeDef",
    {
        "exportsInfo": List["ExportInfoTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeImportTasksRequestRequestTypeDef = TypedDict(
    "DescribeImportTasksRequestRequestTypeDef",
    {
        "filters": NotRequired[Sequence["ImportTaskFilterTypeDef"]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

DescribeImportTasksResponseTypeDef = TypedDict(
    "DescribeImportTasksResponseTypeDef",
    {
        "nextToken": str,
        "tasks": List["ImportTaskTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTagsRequestDescribeTagsPaginateTypeDef = TypedDict(
    "DescribeTagsRequestDescribeTagsPaginateTypeDef",
    {
        "filters": NotRequired[Sequence["TagFilterTypeDef"]],
        "PaginationConfig": NotRequired["PaginatorConfigTypeDef"],
    },
)

DescribeTagsRequestRequestTypeDef = TypedDict(
    "DescribeTagsRequestRequestTypeDef",
    {
        "filters": NotRequired[Sequence["TagFilterTypeDef"]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

DescribeTagsResponseTypeDef = TypedDict(
    "DescribeTagsResponseTypeDef",
    {
        "tags": List["ConfigurationTagTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateConfigurationItemsFromApplicationRequestRequestTypeDef = TypedDict(
    "DisassociateConfigurationItemsFromApplicationRequestRequestTypeDef",
    {
        "applicationConfigurationId": str,
        "configurationIds": Sequence[str],
    },
)

ExportConfigurationsResponseTypeDef = TypedDict(
    "ExportConfigurationsResponseTypeDef",
    {
        "exportId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExportFilterTypeDef = TypedDict(
    "ExportFilterTypeDef",
    {
        "name": str,
        "values": Sequence[str],
        "condition": str,
    },
)

ExportInfoTypeDef = TypedDict(
    "ExportInfoTypeDef",
    {
        "exportId": str,
        "exportStatus": ExportStatusType,
        "statusMessage": str,
        "exportRequestTime": datetime,
        "configurationsDownloadUrl": NotRequired[str],
        "isTruncated": NotRequired[bool],
        "requestedStartTime": NotRequired[datetime],
        "requestedEndTime": NotRequired[datetime],
    },
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "name": str,
        "values": Sequence[str],
        "condition": str,
    },
)

GetDiscoverySummaryResponseTypeDef = TypedDict(
    "GetDiscoverySummaryResponseTypeDef",
    {
        "servers": int,
        "applications": int,
        "serversMappedToApplications": int,
        "serversMappedtoTags": int,
        "agentSummary": "CustomerAgentInfoTypeDef",
        "connectorSummary": "CustomerConnectorInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportTaskFilterTypeDef = TypedDict(
    "ImportTaskFilterTypeDef",
    {
        "name": NotRequired[ImportTaskFilterNameType],
        "values": NotRequired[Sequence[str]],
    },
)

ImportTaskTypeDef = TypedDict(
    "ImportTaskTypeDef",
    {
        "importTaskId": NotRequired[str],
        "clientRequestToken": NotRequired[str],
        "name": NotRequired[str],
        "importUrl": NotRequired[str],
        "status": NotRequired[ImportStatusType],
        "importRequestTime": NotRequired[datetime],
        "importCompletionTime": NotRequired[datetime],
        "importDeletedTime": NotRequired[datetime],
        "serverImportSuccess": NotRequired[int],
        "serverImportFailure": NotRequired[int],
        "applicationImportSuccess": NotRequired[int],
        "applicationImportFailure": NotRequired[int],
        "errorsAndFailedEntriesZip": NotRequired[str],
    },
)

ListConfigurationsRequestListConfigurationsPaginateTypeDef = TypedDict(
    "ListConfigurationsRequestListConfigurationsPaginateTypeDef",
    {
        "configurationType": ConfigurationItemTypeType,
        "filters": NotRequired[Sequence["FilterTypeDef"]],
        "orderBy": NotRequired[Sequence["OrderByElementTypeDef"]],
        "PaginationConfig": NotRequired["PaginatorConfigTypeDef"],
    },
)

ListConfigurationsRequestRequestTypeDef = TypedDict(
    "ListConfigurationsRequestRequestTypeDef",
    {
        "configurationType": ConfigurationItemTypeType,
        "filters": NotRequired[Sequence["FilterTypeDef"]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "orderBy": NotRequired[Sequence["OrderByElementTypeDef"]],
    },
)

ListConfigurationsResponseTypeDef = TypedDict(
    "ListConfigurationsResponseTypeDef",
    {
        "configurations": List[Dict[str, str]],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServerNeighborsRequestRequestTypeDef = TypedDict(
    "ListServerNeighborsRequestRequestTypeDef",
    {
        "configurationId": str,
        "portInformationNeeded": NotRequired[bool],
        "neighborConfigurationIds": NotRequired[Sequence[str]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListServerNeighborsResponseTypeDef = TypedDict(
    "ListServerNeighborsResponseTypeDef",
    {
        "neighbors": List["NeighborConnectionDetailTypeDef"],
        "nextToken": str,
        "knownDependencyCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NeighborConnectionDetailTypeDef = TypedDict(
    "NeighborConnectionDetailTypeDef",
    {
        "sourceServerId": str,
        "destinationServerId": str,
        "connectionsCount": int,
        "destinationPort": NotRequired[int],
        "transportProtocol": NotRequired[str],
    },
)

OrderByElementTypeDef = TypedDict(
    "OrderByElementTypeDef",
    {
        "fieldName": str,
        "sortOrder": NotRequired[orderStringType],
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

StartContinuousExportResponseTypeDef = TypedDict(
    "StartContinuousExportResponseTypeDef",
    {
        "exportId": str,
        "s3Bucket": str,
        "startTime": datetime,
        "dataSource": Literal["AGENT"],
        "schemaStorageConfig": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartDataCollectionByAgentIdsRequestRequestTypeDef = TypedDict(
    "StartDataCollectionByAgentIdsRequestRequestTypeDef",
    {
        "agentIds": Sequence[str],
    },
)

StartDataCollectionByAgentIdsResponseTypeDef = TypedDict(
    "StartDataCollectionByAgentIdsResponseTypeDef",
    {
        "agentsConfigurationStatus": List["AgentConfigurationStatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartExportTaskRequestRequestTypeDef = TypedDict(
    "StartExportTaskRequestRequestTypeDef",
    {
        "exportDataFormat": NotRequired[Sequence[ExportDataFormatType]],
        "filters": NotRequired[Sequence["ExportFilterTypeDef"]],
        "startTime": NotRequired[Union[datetime, str]],
        "endTime": NotRequired[Union[datetime, str]],
    },
)

StartExportTaskResponseTypeDef = TypedDict(
    "StartExportTaskResponseTypeDef",
    {
        "exportId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartImportTaskRequestRequestTypeDef = TypedDict(
    "StartImportTaskRequestRequestTypeDef",
    {
        "name": str,
        "importUrl": str,
        "clientRequestToken": NotRequired[str],
    },
)

StartImportTaskResponseTypeDef = TypedDict(
    "StartImportTaskResponseTypeDef",
    {
        "task": "ImportTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopContinuousExportRequestRequestTypeDef = TypedDict(
    "StopContinuousExportRequestRequestTypeDef",
    {
        "exportId": str,
    },
)

StopContinuousExportResponseTypeDef = TypedDict(
    "StopContinuousExportResponseTypeDef",
    {
        "startTime": datetime,
        "stopTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopDataCollectionByAgentIdsRequestRequestTypeDef = TypedDict(
    "StopDataCollectionByAgentIdsRequestRequestTypeDef",
    {
        "agentIds": Sequence[str],
    },
)

StopDataCollectionByAgentIdsResponseTypeDef = TypedDict(
    "StopDataCollectionByAgentIdsResponseTypeDef",
    {
        "agentsConfigurationStatus": List["AgentConfigurationStatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagFilterTypeDef = TypedDict(
    "TagFilterTypeDef",
    {
        "name": str,
        "values": Sequence[str],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)

UpdateApplicationRequestRequestTypeDef = TypedDict(
    "UpdateApplicationRequestRequestTypeDef",
    {
        "configurationId": str,
        "name": NotRequired[str],
        "description": NotRequired[str],
    },
)
