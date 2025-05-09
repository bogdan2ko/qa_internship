# Functional test cases – AutomationTestStore

| ID  | Title              | Pre‑conditions                                   | Steps (❶…❹)                                                                                                   | Expected result                                             | Priority |
|-----|--------------------|--------------------------------------------------|---------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|----------|
| TC‑001 | **Login – valid creds** | Пользователь зарегистрирован (bogdan2ko1) | 1. Открыть /account/login <br>2. Ввести *Username* = bogdan2ko1 <br>3. Ввести *Password* = ***** <br>4. Нажать **Login** | Переход на Dashboard; в хедере отображается **Logout** | P1 |
| TC‑002 | **Login – wrong password** | – | 1. /account/login <br>2. Username = bogdan2ko1 <br>3. Password = wrong_pass <br>4. **Login** | Появляется alert “Incorrect login or password” | P1 |
| TC‑003 | **Registration – mandatory only** | Email ещё не зарегистрирован | 1. /account/create <br>2. Заполнить поля (*) <br>3. Submit | Пользователь создан; автоматический логин | P2 |
| TC‑004 | **Product search (full match)** | – | 1. В хедере ввести “Skinsheen” <br>2. Нажать **Search** | Отображается каталог, 1 позиция “Skinsheen...” | P2 |
| TC‑005 | **Add‑to‑cart & checkout** | Авторизован | 1. Открыть товар *Seaweed Conditioner* <br>2. **Add to cart** <br>3. Перейти в Cart <br>4. **Checkout** до шага Payment | Order summary показывает выбранный товар и цену | P1 |
