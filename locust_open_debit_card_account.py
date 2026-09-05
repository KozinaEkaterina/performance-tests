from locust import HttpUser, between, task

from tools.fakers import fake


class OpenDebitCardAccountScenarioUser(HttpUser):
    wait_time = between(1, 3)

    user_id: str

    def on_start(self) -> None:
        """
        Метод on_start вызывается один раз при запуске каждой сессии виртуального пользователя.
        Здесь мы создаем нового пользователя, отправляя POST-запрос к /api/v1/users.
        """
        request = {
            "email": fake.email(),
            "lastName": fake.last_name(),
            "firstName": fake.first_name(),
            "middleName": fake.middle_name(),
            "phoneNumber": fake.phone_number()
        }
        response = self.client.post("/api/v1/users", json=request)
        self.user_id = response.json()['user']['id']

    @task
    def open_debit_card_account_(self):
        """
        Основная нагрузочная задача: получение информации о пользователе.
        Здесь мы выполняем POST-запрос к /api/v1/accounts/open-debit-card-account.
        """
        self.client.post("/api/v1/accounts/open-debit-card-account", json={"userId": self.user_id})