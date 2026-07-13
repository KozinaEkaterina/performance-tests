import time
import httpx

# Создание нового пользователя
create_user_payload = {
    "email": f"user.{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}
create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()

# Создание кредитного счета для пользователя
open_credit_card_account_payload = {
    "userId": create_user_response_data["user"]["id"]
}
open_credit_card_account_response = httpx.post(
    "http://localhost:8003/api/v1/accounts/open-credit-card-account",
    json=open_credit_card_account_payload
)
open_credit_card_account_response_data = open_credit_card_account_response.json()

# Выполнение операции покупки
make_purchase_payload = {
  "status": "IN_PROGRESS",
  "amount": 77.99,
  "cardId": open_credit_card_account_response_data["account"]["cards"][0]["id"],
  "accountId": open_credit_card_account_response_data["account"]["id"],
  "category": "taxi"
}
make_purchase_response = httpx.post(
    "http://localhost:8003/api/v1/operations/make-purchase-operation",
    json=make_purchase_payload
)
make_purchase_response_data = make_purchase_response.json()

# Получение чека по операции
receipt_response = httpx.get(
    f"http://localhost:8003/api/v1/operations/operation-receipt/{make_purchase_response_data["operation"]["id"]}"
)
receipt_response_data = receipt_response.json()
print(receipt_response_data)
print("Get operation receipt response:", receipt_response_data)
print("Get operation receipt code:", receipt_response.status_code)