"""
Type annotations for devops-guru service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_devops_guru.client import DevOpsGuruClient

    session = Session()
    client: DevOpsGuruClient = session.client("devops-guru")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, Mapping, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    InsightTypeType,
    LocaleType,
    ResourceCollectionTypeType,
    UpdateResourceCollectionActionType,
)
from .paginator import (
    DescribeResourceCollectionHealthPaginator,
    GetCostEstimationPaginator,
    GetResourceCollectionPaginator,
    ListAnomaliesForInsightPaginator,
    ListEventsPaginator,
    ListInsightsPaginator,
    ListNotificationChannelsPaginator,
    ListRecommendationsPaginator,
    SearchInsightsPaginator,
)
from .type_defs import (
    AddNotificationChannelResponseTypeDef,
    CostEstimationResourceCollectionFilterTypeDef,
    DescribeAccountHealthResponseTypeDef,
    DescribeAccountOverviewResponseTypeDef,
    DescribeAnomalyResponseTypeDef,
    DescribeFeedbackResponseTypeDef,
    DescribeInsightResponseTypeDef,
    DescribeResourceCollectionHealthResponseTypeDef,
    DescribeServiceIntegrationResponseTypeDef,
    GetCostEstimationResponseTypeDef,
    GetResourceCollectionResponseTypeDef,
    InsightFeedbackTypeDef,
    ListAnomaliesForInsightResponseTypeDef,
    ListEventsFiltersTypeDef,
    ListEventsResponseTypeDef,
    ListInsightsResponseTypeDef,
    ListInsightsStatusFilterTypeDef,
    ListNotificationChannelsResponseTypeDef,
    ListRecommendationsResponseTypeDef,
    NotificationChannelConfigTypeDef,
    SearchInsightsFiltersTypeDef,
    SearchInsightsResponseTypeDef,
    StartTimeRangeTypeDef,
    UpdateResourceCollectionFilterTypeDef,
    UpdateServiceIntegrationConfigTypeDef,
)

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("DevOpsGuruClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class DevOpsGuruClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevOpsGuru.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        DevOpsGuruClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevOpsGuru.Client.exceptions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#exceptions)
        """
    def add_notification_channel(
        self, *, Config: "NotificationChannelConfigTypeDef"
    ) -> AddNotificationChannelResponseTypeDef:
        """
        Adds a notification channel to DevOps Guru.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevOpsGuru.Client.add_notification_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#add_notification_channel)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevOpsGuru.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#can_paginate)
        """
    def describe_account_health(self) -> DescribeAccountHealthResponseTypeDef:
        """
        Returns the number of open reactive insights, the number of open proactive
        insights, and the number of metrics analyzed in your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevOpsGuru.Client.describe_account_health)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#describe_account_health)
        """
    def describe_account_overview(
        self, *, FromTime: Union[datetime, str], ToTime: Union[datetime, str] = ...
    ) -> DescribeAccountOverviewResponseTypeDef:
        """
        For the time range passed in, returns the number of open reactive insight that
        were created, the number of open proactive insights that were created, and the
        Mean Time to Recover (MTTR) for all closed reactive insights.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevOpsGuru.Client.describe_account_overview)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#describe_account_overview)
        """
    def describe_anomaly(self, *, Id: str) -> DescribeAnomalyResponseTypeDef:
        """
        Returns details about an anomaly that you specify using its ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevOpsGuru.Client.describe_anomaly)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#describe_anomaly)
        """
    def describe_feedback(self, *, InsightId: str = ...) -> DescribeFeedbackResponseTypeDef:
        """
        Returns the most recent feedback submitted in the current AWS account and
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevOpsGuru.Client.describe_feedback)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#describe_feedback)
        """
    def describe_insight(self, *, Id: str) -> DescribeInsightResponseTypeDef:
        """
        Returns details about an insight that you specify using its ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevOpsGuru.Client.describe_insight)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#describe_insight)
        """
    def describe_resource_collection_health(
        self, *, ResourceCollectionType: ResourceCollectionTypeType, NextToken: str = ...
    ) -> DescribeResourceCollectionHealthResponseTypeDef:
        """
        Returns the number of open proactive insights, open reactive insights, and the
        Mean Time to Recover (MTTR) for all closed insights in resource collections in
        your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevOpsGuru.Client.describe_resource_collection_health)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#describe_resource_collection_health)
        """
    def describe_service_integration(self) -> DescribeServiceIntegrationResponseTypeDef:
        """
        Returns the integration status of services that are integrated with DevOps Guru.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevOpsGuru.Client.describe_service_integration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#describe_service_integration)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevOpsGuru.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#generate_presigned_url)
        """
    def get_cost_estimation(self, *, NextToken: str = ...) -> GetCostEstimationResponseTypeDef:
        """
        Returns an estimate of the monthly cost for DevOps Guru to analyze your AWS
        resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevOpsGuru.Client.get_cost_estimation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#get_cost_estimation)
        """
    def get_resource_collection(
        self, *, ResourceCollectionType: ResourceCollectionTypeType, NextToken: str = ...
    ) -> GetResourceCollectionResponseTypeDef:
        """
        Returns lists AWS resources that are of the specified resource collection type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevOpsGuru.Client.get_resource_collection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#get_resource_collection)
        """
    def list_anomalies_for_insight(
        self,
        *,
        InsightId: str,
        StartTimeRange: "StartTimeRangeTypeDef" = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> ListAnomaliesForInsightResponseTypeDef:
        """
        Returns a list of the anomalies that belong to an insight that you specify using
        its ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevOpsGuru.Client.list_anomalies_for_insight)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#list_anomalies_for_insight)
        """
    def list_events(
        self, *, Filters: "ListEventsFiltersTypeDef", MaxResults: int = ..., NextToken: str = ...
    ) -> ListEventsResponseTypeDef:
        """
        Returns a list of the events emitted by the resources that are evaluated by
        DevOps Guru.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevOpsGuru.Client.list_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#list_events)
        """
    def list_insights(
        self,
        *,
        StatusFilter: "ListInsightsStatusFilterTypeDef",
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> ListInsightsResponseTypeDef:
        """
        Returns a list of insights in your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevOpsGuru.Client.list_insights)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#list_insights)
        """
    def list_notification_channels(
        self, *, NextToken: str = ...
    ) -> ListNotificationChannelsResponseTypeDef:
        """
        Returns a list of notification channels configured for DevOps Guru.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevOpsGuru.Client.list_notification_channels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#list_notification_channels)
        """
    def list_recommendations(
        self, *, InsightId: str, NextToken: str = ..., Locale: LocaleType = ...
    ) -> ListRecommendationsResponseTypeDef:
        """
        Returns a list of a specified insight's recommendations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevOpsGuru.Client.list_recommendations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#list_recommendations)
        """
    def put_feedback(self, *, InsightFeedback: "InsightFeedbackTypeDef" = ...) -> Dict[str, Any]:
        """
        Collects customer feedback about the specified insight.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevOpsGuru.Client.put_feedback)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#put_feedback)
        """
    def remove_notification_channel(self, *, Id: str) -> Dict[str, Any]:
        """
        Removes a notification channel from DevOps Guru.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevOpsGuru.Client.remove_notification_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#remove_notification_channel)
        """
    def search_insights(
        self,
        *,
        StartTimeRange: "StartTimeRangeTypeDef",
        Type: InsightTypeType,
        Filters: "SearchInsightsFiltersTypeDef" = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> SearchInsightsResponseTypeDef:
        """
        Returns a list of insights in your AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevOpsGuru.Client.search_insights)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#search_insights)
        """
    def start_cost_estimation(
        self,
        *,
        ResourceCollection: "CostEstimationResourceCollectionFilterTypeDef",
        ClientToken: str = ...
    ) -> Dict[str, Any]:
        """
        Starts the creation of an estimate of the monthly cost to analyze your AWS
        resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevOpsGuru.Client.start_cost_estimation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#start_cost_estimation)
        """
    def update_resource_collection(
        self,
        *,
        Action: UpdateResourceCollectionActionType,
        ResourceCollection: "UpdateResourceCollectionFilterTypeDef"
    ) -> Dict[str, Any]:
        """
        Updates the collection of resources that DevOps Guru analyzes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevOpsGuru.Client.update_resource_collection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#update_resource_collection)
        """
    def update_service_integration(
        self, *, ServiceIntegration: "UpdateServiceIntegrationConfigTypeDef"
    ) -> Dict[str, Any]:
        """
        Enables or disables integration with a service that can be integrated with
        DevOps Guru.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevOpsGuru.Client.update_service_integration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#update_service_integration)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_resource_collection_health"]
    ) -> DescribeResourceCollectionHealthPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevOpsGuru.Client.get_paginator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#get_paginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_cost_estimation"]
    ) -> GetCostEstimationPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevOpsGuru.Client.get_paginator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#get_paginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_resource_collection"]
    ) -> GetResourceCollectionPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevOpsGuru.Client.get_paginator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#get_paginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_anomalies_for_insight"]
    ) -> ListAnomaliesForInsightPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevOpsGuru.Client.get_paginator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#get_paginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_events"]) -> ListEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevOpsGuru.Client.get_paginator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#get_paginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_insights"]) -> ListInsightsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevOpsGuru.Client.get_paginator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#get_paginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_notification_channels"]
    ) -> ListNotificationChannelsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevOpsGuru.Client.get_paginator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#get_paginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_recommendations"]
    ) -> ListRecommendationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevOpsGuru.Client.get_paginator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#get_paginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["search_insights"]) -> SearchInsightsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevOpsGuru.Client.get_paginator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#get_paginator)
        """
