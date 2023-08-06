"""
Type annotations for braket service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/type_defs/)

Usage::

    ```python
    from mypy_boto3_braket.type_defs import CancelQuantumTaskRequestRequestTypeDef

    data: CancelQuantumTaskRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    CancellationStatusType,
    DeviceStatusType,
    DeviceTypeType,
    QuantumTaskStatusType,
    SearchQuantumTasksFilterOperatorType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CancelQuantumTaskRequestRequestTypeDef",
    "CancelQuantumTaskResponseTypeDef",
    "CreateQuantumTaskRequestRequestTypeDef",
    "CreateQuantumTaskResponseTypeDef",
    "DeviceSummaryTypeDef",
    "GetDeviceRequestRequestTypeDef",
    "GetDeviceResponseTypeDef",
    "GetQuantumTaskRequestRequestTypeDef",
    "GetQuantumTaskResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "QuantumTaskSummaryTypeDef",
    "ResponseMetadataTypeDef",
    "SearchDevicesFilterTypeDef",
    "SearchDevicesRequestRequestTypeDef",
    "SearchDevicesRequestSearchDevicesPaginateTypeDef",
    "SearchDevicesResponseTypeDef",
    "SearchQuantumTasksFilterTypeDef",
    "SearchQuantumTasksRequestRequestTypeDef",
    "SearchQuantumTasksRequestSearchQuantumTasksPaginateTypeDef",
    "SearchQuantumTasksResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
)

CancelQuantumTaskRequestRequestTypeDef = TypedDict(
    "CancelQuantumTaskRequestRequestTypeDef",
    {
        "clientToken": str,
        "quantumTaskArn": str,
    },
)

CancelQuantumTaskResponseTypeDef = TypedDict(
    "CancelQuantumTaskResponseTypeDef",
    {
        "cancellationStatus": CancellationStatusType,
        "quantumTaskArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateQuantumTaskRequestRequestTypeDef = TypedDict(
    "_RequiredCreateQuantumTaskRequestRequestTypeDef",
    {
        "action": str,
        "clientToken": str,
        "deviceArn": str,
        "outputS3Bucket": str,
        "outputS3KeyPrefix": str,
        "shots": int,
    },
)
_OptionalCreateQuantumTaskRequestRequestTypeDef = TypedDict(
    "_OptionalCreateQuantumTaskRequestRequestTypeDef",
    {
        "deviceParameters": str,
        "tags": Mapping[str, str],
    },
    total=False,
)


class CreateQuantumTaskRequestRequestTypeDef(
    _RequiredCreateQuantumTaskRequestRequestTypeDef, _OptionalCreateQuantumTaskRequestRequestTypeDef
):
    pass


CreateQuantumTaskResponseTypeDef = TypedDict(
    "CreateQuantumTaskResponseTypeDef",
    {
        "quantumTaskArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeviceSummaryTypeDef = TypedDict(
    "DeviceSummaryTypeDef",
    {
        "deviceArn": str,
        "deviceName": str,
        "deviceStatus": DeviceStatusType,
        "deviceType": DeviceTypeType,
        "providerName": str,
    },
)

GetDeviceRequestRequestTypeDef = TypedDict(
    "GetDeviceRequestRequestTypeDef",
    {
        "deviceArn": str,
    },
)

GetDeviceResponseTypeDef = TypedDict(
    "GetDeviceResponseTypeDef",
    {
        "deviceArn": str,
        "deviceCapabilities": str,
        "deviceName": str,
        "deviceStatus": DeviceStatusType,
        "deviceType": DeviceTypeType,
        "providerName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetQuantumTaskRequestRequestTypeDef = TypedDict(
    "GetQuantumTaskRequestRequestTypeDef",
    {
        "quantumTaskArn": str,
    },
)

GetQuantumTaskResponseTypeDef = TypedDict(
    "GetQuantumTaskResponseTypeDef",
    {
        "createdAt": datetime,
        "deviceArn": str,
        "deviceParameters": str,
        "endedAt": datetime,
        "failureReason": str,
        "outputS3Bucket": str,
        "outputS3Directory": str,
        "quantumTaskArn": str,
        "shots": int,
        "status": QuantumTaskStatusType,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

_RequiredQuantumTaskSummaryTypeDef = TypedDict(
    "_RequiredQuantumTaskSummaryTypeDef",
    {
        "createdAt": datetime,
        "deviceArn": str,
        "outputS3Bucket": str,
        "outputS3Directory": str,
        "quantumTaskArn": str,
        "shots": int,
        "status": QuantumTaskStatusType,
    },
)
_OptionalQuantumTaskSummaryTypeDef = TypedDict(
    "_OptionalQuantumTaskSummaryTypeDef",
    {
        "endedAt": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)


class QuantumTaskSummaryTypeDef(
    _RequiredQuantumTaskSummaryTypeDef, _OptionalQuantumTaskSummaryTypeDef
):
    pass


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

SearchDevicesFilterTypeDef = TypedDict(
    "SearchDevicesFilterTypeDef",
    {
        "name": str,
        "values": Sequence[str],
    },
)

_RequiredSearchDevicesRequestRequestTypeDef = TypedDict(
    "_RequiredSearchDevicesRequestRequestTypeDef",
    {
        "filters": Sequence["SearchDevicesFilterTypeDef"],
    },
)
_OptionalSearchDevicesRequestRequestTypeDef = TypedDict(
    "_OptionalSearchDevicesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class SearchDevicesRequestRequestTypeDef(
    _RequiredSearchDevicesRequestRequestTypeDef, _OptionalSearchDevicesRequestRequestTypeDef
):
    pass


_RequiredSearchDevicesRequestSearchDevicesPaginateTypeDef = TypedDict(
    "_RequiredSearchDevicesRequestSearchDevicesPaginateTypeDef",
    {
        "filters": Sequence["SearchDevicesFilterTypeDef"],
    },
)
_OptionalSearchDevicesRequestSearchDevicesPaginateTypeDef = TypedDict(
    "_OptionalSearchDevicesRequestSearchDevicesPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class SearchDevicesRequestSearchDevicesPaginateTypeDef(
    _RequiredSearchDevicesRequestSearchDevicesPaginateTypeDef,
    _OptionalSearchDevicesRequestSearchDevicesPaginateTypeDef,
):
    pass


SearchDevicesResponseTypeDef = TypedDict(
    "SearchDevicesResponseTypeDef",
    {
        "devices": List["DeviceSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchQuantumTasksFilterTypeDef = TypedDict(
    "SearchQuantumTasksFilterTypeDef",
    {
        "name": str,
        "operator": SearchQuantumTasksFilterOperatorType,
        "values": Sequence[str],
    },
)

_RequiredSearchQuantumTasksRequestRequestTypeDef = TypedDict(
    "_RequiredSearchQuantumTasksRequestRequestTypeDef",
    {
        "filters": Sequence["SearchQuantumTasksFilterTypeDef"],
    },
)
_OptionalSearchQuantumTasksRequestRequestTypeDef = TypedDict(
    "_OptionalSearchQuantumTasksRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)


class SearchQuantumTasksRequestRequestTypeDef(
    _RequiredSearchQuantumTasksRequestRequestTypeDef,
    _OptionalSearchQuantumTasksRequestRequestTypeDef,
):
    pass


_RequiredSearchQuantumTasksRequestSearchQuantumTasksPaginateTypeDef = TypedDict(
    "_RequiredSearchQuantumTasksRequestSearchQuantumTasksPaginateTypeDef",
    {
        "filters": Sequence["SearchQuantumTasksFilterTypeDef"],
    },
)
_OptionalSearchQuantumTasksRequestSearchQuantumTasksPaginateTypeDef = TypedDict(
    "_OptionalSearchQuantumTasksRequestSearchQuantumTasksPaginateTypeDef",
    {
        "PaginationConfig": "PaginatorConfigTypeDef",
    },
    total=False,
)


class SearchQuantumTasksRequestSearchQuantumTasksPaginateTypeDef(
    _RequiredSearchQuantumTasksRequestSearchQuantumTasksPaginateTypeDef,
    _OptionalSearchQuantumTasksRequestSearchQuantumTasksPaginateTypeDef,
):
    pass


SearchQuantumTasksResponseTypeDef = TypedDict(
    "SearchQuantumTasksResponseTypeDef",
    {
        "nextToken": str,
        "quantumTasks": List["QuantumTaskSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
