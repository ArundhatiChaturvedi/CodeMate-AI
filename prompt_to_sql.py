def nl_to_sql(prompt):
    if "users" in prompt.lower() and "signed up" in prompt:
        return "SELECT * FROM users WHERE signup_date >= DATE_SUB(CURDATE(), INTERVAL 30 DAY);"
    elif "top 10" in prompt.lower() and "products" in prompt:
        return "SELECT * FROM products ORDER BY sales DESC LIMIT 10;"
    else:
        return "Sorry, I couldn't generate a query for that. Try rephrasing!"
