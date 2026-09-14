from locust import HttpUser, between, task, User

from clients.http.gateway.accounts.client import build_accounts_gateway_locust_http_client, AccountsGatewayHTTPClient
from clients.http.gateway.users.client import build_users_gateway_locust_http_client, UsersGatewayHTTPClient
from clients.http.gateway.users.schema import CreateUserResponseSchema
from tools.fakers import fake


class OpenDebitCardAccountScenarioUser(User):
    host = "localhost"
    wait_time = between(1, 3)

    users_gateway_client: UsersGatewayHTTPClient
    accounts_gateway_client: AccountsGatewayHTTPClient
    create_user_response: CreateUserResponseSchema
    user_id: str

    def on_start(self) -> None:
        """
        Метод on_start вызывается один раз при запуске каждой сессии виртуального пользователя.
        Здесь мы создаем нового пользователя, отправляя POST-запрос к /api/v1/users.
        """
        self.users_gateway_client = build_users_gateway_locust_http_client(self.environment)
        self.accounts_gateway_client = build_accounts_gateway_locust_http_client(self.environment)
        self.create_user_response = self.users_gateway_client.create_user()
        self.user_id = self.create_user_response.user.id

    @task
    def open_debit_card_account_(self):
        """
        Основная нагрузочная задача: получение информации о пользователе.
        Здесь мы выполняем POST-запрос к /api/v1/accounts/open-debit-card-account.
        """
        self.accounts_gateway_client.open_debit_card_account(self.user_id)