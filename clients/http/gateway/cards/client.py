from typing import TypedDict

from httpx import Response

from clients.http.client import HTTPClient

class IssueCardRequestDict(TypedDict):
    """
    Структура данных для выпуска карты.
    """
    userId: str
    accountId: str

class CardsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/cards сервиса http-gateway.
    """

    def issue_virtual_card_api(self, request: IssueCardRequestDict) -> Response:
        """
        Выпуск виртуальной карты.

        :param request: Словарь с данными для выпуска виртуальной карты.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/cards/issue-virtual-card", json=request)


    def issue_physical_card_api(self, request: IssueCardRequestDict) -> Response:
        """
        Выпусе физической карты.

        :param request: Словарь с данными для выпуска физической карты.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/cards/issue-physical-card", json=request)