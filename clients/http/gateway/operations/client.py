from typing import TypedDict

from httpx import Response, QueryParams

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client
from clients.http.gateway.documents.client import DocumentDict


class OperationDict(TypedDict):
    """
    Описание структуры операции.
    """
    id: str
    type: str
    status: str
    amount: float
    cardId: str
    category: str
    createdAt: str
    accountId: str

class OperationReceiptDict(TypedDict):
    """
    Описание структуры чека по операции.
    """
    url: str
    document: str

class OperationsSummaryDict(TypedDict):
    """
    Описание структуры статистики по операциям.
    """
    spentAmount: float
    receivedAmount: float
    cashbackAmount: float

class GetOperationResponseDict(TypedDict):
    """
    Описание структуры ответа получения операции.
    """
    operation: OperationDict

class GetOperationReceiptResponseDict(TypedDict):
    """
    Описание структуры чека по операции.
    """
    receipt: DocumentDict

class GetOperationsQueryDict(TypedDict):
    """
    Структура данных для получения списка операций для определенного счета.
    """
    accountId : str

class GetOperationsResponseDict(TypedDict):
    """
    Описание структуры ответа на получение списка операций для определенного счета.
    """
    operations: list[GetOperationResponseDict]

class GetOperationsSummaryQueryDict(TypedDict):
    """
    Структура данных для получения статистики по операциям для определенного счета.
    """
    accountId : str

class GetOperationsSummaryResponseDict(TypedDict):
    """
    Описание структуры ответа на получение статистики по операциям для определенного счета.
    """
    summary: GetOperationsSummaryQueryDict

class MakeFeeOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции комиссии.
    """
    status: str
    amount: int
    cardId: str
    accountId: str

class MakeFeeOperationResponseDict(TypedDict):
    """
    Описание структуры ответа на создание операции комиссии.
    """
    operation: OperationDict

class MakeTopUpOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции пополнения.
    """
    status: str
    amount: int
    cardId: str
    accountId: str

class MakeTopUpOperationResponseDict(TypedDict):
    """
    Описание структуры ответа на создание операции пополнения.
    """
    operation: OperationDict

class MakeCashbackOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции кэшбэка.
    """
    status: str
    amount: int
    cardId: str
    accountId: str

class MakeCashbackOperationResponseDict(TypedDict):
    """
    Описание структуры ответа на создание операции кэшбэка.
    """
    operation: OperationDict

class MakeTransferOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции перевода.
    """
    status: str
    amount: int
    cardId: str
    accountId: str

class MakeTransferOperationResponseDict(TypedDict):
    """
    Описание структуры ответа на создание операции перевода.
    """
    operation: OperationDict

class MakePurchaseOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции покупки.
    """
    status: str
    amount: int
    cardId: str
    accountId: str
    category: str

class MakePurchaseOperationResponseDict(TypedDict):
    """
    Описание структуры ответа на создание операции покупки.
    """
    operation: OperationDict

class MakeBillPaymentOperationRequestDict(TypedDict):
    """
    Структура запроса для создания операции оплаты по счёту.
    """
    status: str
    amount: int
    cardId: str
    accountId: str

class MakeBillPaymentOperationResponseDict(TypedDict):
    """
    Описание структуры ответа на создание операции оплаты по счёту.
    """
    operation: OperationDict

class MakeCashWithdrawalOperationRequestDict(TypedDict):
    """
    Структура запроса для создания операции снятия наличных.
    """
    status: str
    amount: int
    cardId: str
    accountId: str

class MakeCashWithdrawalOperationResponseDict(TypedDict):
    """
    Описание структуры ответа на создание операции снятия наличных.
    """
    operation: OperationDict

class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Получение информации об операции.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/operations/{operation_id}")

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Получение чека по операции.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Выполняет GET-запрос на получение списка операций для определенного счета.

        :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
        :return: Объект httpx.Response с данными об операциях.
        """
        return self.get("/api/v1/operations", params=QueryParams(**query))

    def get_operations_summary_api(self, query: GetOperationsSummaryQueryDict) -> Response:
        """
        Выполняет GET-запрос на получение статистики по операциям для определенного счета.

        :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
        :return: Объект httpx.Response с данными о статистике.
        """
        return self.get("/api/v1/operations/operations-summary", params=QueryParams(**query))

    def make_fee_operation_api(self, request: MakeFeeOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции комиссии.

        :param request: Словарь с данными для создания операции комиссии.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции пополнения.

        :param request: Словарь с данными для создания операции пополнения.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции кэшбэка.

        :param request: Словарь с данными для создания операции кэшбэка.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции перевода.

        :param request: Словарь с данными для создания операции перевода.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции покупки.

        :param request: Словарь с данными для создания операции покупки.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции оплаты по счету.

        :param request: Словарь с данными для создания операции оплаты по счету.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции снятия наличных денег.

        :param request: Словарь с данными для создания операции снятия наличных денег.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)

    def get_operation(self, operation_id: str) -> GetOperationResponseDict:
        response = self.get_operation_api(operation_id)
        return response.json()

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseDict:
        response = self.get_operation_receipt_api(operation_id)
        return response.json()

    def get_operations(self, query: GetOperationsQueryDict) -> GetOperationsResponseDict:
        response = self.get_operations_api(query)
        return response.json()

    def get_operations_summary(self, query: GetOperationsSummaryQueryDict) -> GetOperationsSummaryResponseDict:
        response = self.get_operations_summary_api(query)
        return response.json()

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseDict:
        request = MakeFeeOperationRequestDict(
            status="COMPLETED",
            amount=666.6,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_fee_operation_api(request)
        return response.json()

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseDict:
        request = MakeTopUpOperationRequestDict(
            status="COMPLETED",
            amount=666.06,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_top_up_operation_api(request)
        return response.json()

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponseDict:
        request = MakeCashbackOperationRequestDict(
            status="COMPLETED",
            amount=666.06,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cashback_operation_api(request)
        return response.json()

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponseDict:
        request = MakeTransferOperationRequestDict(
            status="COMPLETED",
            amount=55.06,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_transfer_operation_api(request)
        return response.json()

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponseDict:
        request = MakePurchaseOperationRequestDict(
            status="COMPLETED",
            amount=11.11,
            cardId=card_id,
            category="taxi",
            accountId=account_id
        )
        response = self.make_purchase_operation_api(request)
        return response.json()

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponseDict:
        request = MakeBillPaymentOperationRequestDict(
            status="COMPLETED",
            amount=156.25,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_bill_payment_operation_api(request)
        return response.json()

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeCashWithdrawalOperationResponseDict:
        request = MakeCashWithdrawalOperationRequestDict(
            status="COMPLETED",
            amount=80.00,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return response.json()


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())