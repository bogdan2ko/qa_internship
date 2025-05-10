# Bug Reports

## Bug 1: Reset Password Returns 500 Error

**Summary**  
When a user tries to reset their password, the application returns a 500 Internal Server Error.

**Steps to Reproduce**  
1. Go to the **Login** page.  
2. Click **Forgot Password**.  
3. Enter a valid email address (e.g. `user@example.com`).  
4. Click **Submit**.

**Actual Result**  
A “500 Internal Server Error” page is displayed.

**Expected Result**  
A confirmation message “Password reset email sent” appears and no server error occurs.

**Severity**  
Major

**Environment**  
- OS: Windows 10  
- Browser: Chrome 112.0.5615.49  
- Application version: QA Demo v1.0  

---

## Bug 2: Search with Special Characters Shows Blank Page

**Summary**  
Entering only special characters into the product search field leaves the results area blank instead of showing a “no results” message.

**Steps to Reproduce**  
1. Navigate to the **Home** page.  
2. In the search field, type `@#$%^&*`.  
3. Click **Search**.

**Actual Result**  
The page reloads and the product listing area is completely empty (no feedback).

**Expected Result**  
A “No results found” message should be displayed when the query returns zero products.

**Severity**  
Minor

**Environment**  
- OS: Windows 10  
- Browser: Firefox 115.0.1  
- Application version: QA Demo v1.0  
