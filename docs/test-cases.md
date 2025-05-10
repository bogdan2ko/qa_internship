# Manual Test Cases

Below are manual check-lists for key user scenarios.

---

### Login

| ID     | Test Case                      | Steps                                                                                   | Expected Result                                           | Priority |
|--------|--------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------|----------|
| TC-01  | Login with valid credentials   | 1. Navigate to the login page  
2. Enter a valid username  
3. Enter a valid password  
4. Click **Login**                      | User is successfully logged in and redirected to dashboard | High     |

---

### Registration

| ID     | Test Case                           | Steps                                                                                     | Expected Result                                                       | Priority |
|--------|-------------------------------------|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|----------|
| TC-02  | Register with valid data            | 1. Navigate to the registration page  
2. Fill in all required fields with valid information  
3. Click **Submit**                        | Account is created and a confirmation email is sent to the user              | High     |

---

### Search Product

| ID     | Test Case                           | Steps                                                                                     | Expected Result                                               | Priority |
|--------|-------------------------------------|-------------------------------------------------------------------------------------------|---------------------------------------------------------------|----------|
| TC-03  | Search for an existing product      | 1. Navigate to the homepage  
2. Enter a product name (e.g., “Laptop”) in the search field  
3. Click **Search**                       | Search results display products matching the query “Laptop”                     | Medium   |

---

### Add to Cart

| ID     | Test Case                           | Steps                                                                                     | Expected Result                                               | Priority |
|--------|-------------------------------------|-------------------------------------------------------------------------------------------|---------------------------------------------------------------|----------|
| TC-04  | Add a product to the shopping cart  | 1. Locate a product via search or category  
2. On the product page, click **Add to cart**  
3. Open the shopping cart                   | Product appears in the cart and the cart icon item count increments by one     | Medium   |

---

### Checkout

| ID     | Test Case                           | Steps                                                                                     | Expected Result                                               | Priority |
|--------|-------------------------------------|-------------------------------------------------------------------------------------------|---------------------------------------------------------------|----------|
| TC-05  | Complete the checkout process       | 1. Go to the shopping cart  
2. Click **Checkout**  
3. Enter shipping and payment details  
4. Click **Place Order**                   | Order confirmation page is displayed with the order number                     | High     |
