# Bug reports – AutomationTestStore (sample)

## BUG‑01  Reset Password → HTTP 500

| Field | Value |
|-------|-------|
| **Summary** | “Forgot Password” form returns 500 |
| **Env** | Prod · Chrome 136 · Win 11 |
| **Steps** | 1. /account/forgotten<br>2. Email = *any registered*<br>3. Submit |
| **Actual result** | Blank page, HTTP 500 in DevTools |
| **Expected result** | Success message “Password reset email sent” |
| **Severity** | Major (S2) |

---

## BUG‑02  Cart quantity not updated after refresh

| Field | Value |
|-------|-------|
| **Summary** | Cart badge stays at “1” after item removal (F5) |
| **Env** | Prod · Firefox 125 · Ubuntu 22.04 |
| **Steps** | 1. Добавить любой товар<br>2. Перейти в Cart<br>3. Remove → Cart empty<br>4. F5 |
| **Actual result** | Значок корзины в хедере всё ещё “1” |
| **Expected result** | Значок = “0”/не отображается |
| **Severity** | Minor (S3) |
