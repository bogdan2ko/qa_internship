# Manual Test Cases

---

### Login

| ID    | Test Case                    | Steps                                                                                  | Expected Result                                             | Priority |
|-------|------------------------------|----------------------------------------------------------------------------------------|-------------------------------------------------------------|----------|
| TC-01 | Login with valid credentials | 1. Go to login page  | User is logged in and sees the dashboard                                   | High     |
2. Enter valid username  
3. Enter valid password  
4. Click **Login**               | User is logged in and sees the dashboard                                   | High     |

---

### Registration

| ID    | Test Case                   | Steps                                                                                  | Expected Result                                             | Priority |
|-------|-----------------------------|----------------------------------------------------------------------------------------|-------------------------------------------------------------|----------|
| TC-02 | Register with valid data    | 1. Go to registration page  
2. Fill in all required fields  
3. Click **Submit**             | Account is created and confirmation email is sent                            | High     |

---

### Search Product

| ID    | Test Case                      | Steps                                                                                  | Expected Result                                             | Priority |
|-------|--------------------------------|----------------------------------------------------------------------------------------|-------------------------------------------------------------|----------|
| TC-03 | Search for an existing product | 1. Go to homepage  
2. Enter “Laptop” in search field  
3. Click **Search**             | Results list shows products matching “Laptop”                                 | Medium   |

---

### Add to Cart

| ID    | Test Case                  | Steps                                                                                  | Expected Result                                             | Priority |
|-------|----------------------------|----------------------------------------------------------------------------------------|-------------------------------------------------------------|----------|
| TC-04 | Add a product to cart      | 1. Find a product  
2. Click **Add to cart**  
3. Open cart view             | Cart shows the item and count increments                                   | Medium   |

---

### Checkout

| ID    | Test Case                  | Steps                                                                                  | Expected Result                                             | Priority |
|-------|----------------------------|----------------------------------------------------------------------------------------|-------------------------------------------------------------|----------|
| TC-05 | Complete the checkout flow | 1. Open cart  
2. Click **Checkout**  
3. Enter shipping & payment  
4. Click **Place Order**     | Order confirmation page appears with order number                            | High     |
