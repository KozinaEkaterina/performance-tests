from enum import StrEnum

from pydantic import BaseModel, Field, ConfigDict

class OperationType(StrEnum):
    FEE = "FEE"
    TOP_UP = "TOP_UP"
    PURCHASE = "PURCHASE"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"


class OperationStatus(StrEnum):
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    UNSPECIFIED = "UNSPECIFIED"


class OperationSchema(BaseModel):
    """
    Описание структуры операции.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    type: OperationType
    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    category: str = Field(alias="category")
    created_at: str = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")


class OperationReceiptSchema(BaseModel):
    """
    Описание структуры чека по операции.
    """
    url: str
    document: str


class OperationsSummarySchema(BaseModel):
    """
    Описание структуры статистики по операциям.
    """
    model_config = ConfigDict(populate_by_name=True)

    spent_amount : float = Field(alias="spentAmount")
    received_amount : float = Field(alias="receivedAmount")
    cashback_amount : float = Field(alias="cashbackAmount")


class GetOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа получения операции.
    """
    operation: OperationSchema

class GetOperationReceiptResponseSchema(BaseModel):
    """
    Описание структуры чека по операции.
    """
    receipt: OperationReceiptSchema

class GetOperationsQuerySchema(BaseModel):
    """
    Структура данных для получения списка операций для определенного счета.
    """
    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias="accountId")

class GetOperationsResponseSchema(BaseModel):
    """
    Описание структуры ответа на получение списка операций для определенного счета.
    """
    operations: list[OperationSchema]

class GetOperationsSummaryQuerySchema(BaseModel):
    """
    Структура query параметров запроса для получения статистики по операциям счёта.
    """
    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias="accountId")

class GetOperationsSummaryResponseSchema(BaseModel):
    """
    Описание структуры ответа на получение статистики по операциям для определенного счета.
    """
    summary: GetOperationsSummaryQuerySchema


class MakeFeeOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции комиссии.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeFeeOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа на создание операции комиссии.
    """
    operation: OperationSchema


class MakeTopUpOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции пополнения.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeTopUpOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа на создание операции пополнения.
    """
    operation: OperationSchema


class MakeCashbackOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции кэшбэка.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeCashbackOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа на создание операции кешбэка.
    """
    operation: OperationSchema


class MakeTransferOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции перевода.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeTransferOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа на создание операции перевода.
    """
    operation: OperationSchema


class MakePurchaseOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции покупки.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus
    amount: int
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")
    category: str


class MakePurchaseOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа на создание операции покупки.
    """
    operation: OperationSchema


class MakeBillPaymentOperationRequestSchema(BaseModel):
    """
    Структура запроса для создания операции оплаты по счёту.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeBillPaymentOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа на создание операции оплаты по счёту.
    """
    operation: OperationSchema


class MakeCashWithdrawalOperationRequestSchema(BaseModel):
    """
    Структура запроса для создания операции снятия наличных.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeCashWithdrawalOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа на создание операции снятия наличных.
    """
    operation: OperationSchema
