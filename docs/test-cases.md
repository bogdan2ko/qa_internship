# Manual Test Cases

---

## Login

| ID    | Test Case                    | Steps                                                                                             | Expected Result                                      | Priority |
|-------|------------------------------|---------------------------------------------------------------------------------------------------|------------------------------------------------------|----------|
| TC-01 | Login with valid credentials | 1. Go to login page<br>2. Enter valid username<br>3. Enter valid password<br>4. Click **Login**   | User is logged in and sees the dashboard             | High     |

---

## Registration

| ID    | Test Case                 | Steps                                                                                             | Expected Result                                      | Priority |
|-------|---------------------------|---------------------------------------------------------------------------------------------------|------------------------------------------------------|----------|
| TC-02 | Register with valid data  | 1. Go to registration page<br>2. Fill in all required fields<br>3. Click **Submit**               | Account is created and confirmation email is sent    | High     |

---

## Search Product

| ID    | Test Case                      | Steps                                                                                             | Expected Result                                      | Priority |
|-------|--------------------------------|---------------------------------------------------------------------------------------------------|------------------------------------------------------|----------|
| TC-03 | Search for an existing product | 1. Go to homepage<br>2. Enter “Laptop” in search field<br>3. Click **Search**                     | Results list shows products matching “Laptop”        | Medium   |

---

## Add to Cart

| ID    | Test Case             | Steps                                                                                             | Expected Result                                      | Priority |
|-------|-----------------------|---------------------------------------------------------------------------------------------------|------------------------------------------------------|----------|
| TC-04 | Add a product to cart | 1. Find a product<br>2. Click **Add to cart**<br>3. Open cart view                                  | Cart shows the item and count increments             | Medium   |

---

## Checkout

| ID    | Test Case               | Steps                                                                                             | Expected Result                                      | Priority |
|-------|-------------------------|---------------------------------------------------------------------------------------------------|------------------------------------------------------|----------|
| TC-05 | Complete the checkout   | 1. Open cart<br>2. Click **Checkout**<br>3. Enter shipping & payment details<br>4. Click **Place Order** | Order confirmation page appears with order number    | High     |
