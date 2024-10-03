import requests

# №1
print("№1. Продукты дешевле 20:")
response = requests.get("https://fakestoreapi.com/products")
products = response.json()
for product in products:
    if product['price'] < 20:
        print(product)

# №2
print("\n№2. Все категории:")
response = requests.get("https://fakestoreapi.com/products/categories")
categories = response.json()
print(categories)

# №3
print("\n№3. Все продукты с категорией jewelery:")
response = requests.get("https://fakestoreapi.com/products/category/jewelery")
jewelery_products = response.json()
for product in jewelery_products:
    print(product)

# №4
print("\n№4. Все пользователи:")
response = requests.get("https://fakestoreapi.com/users")
users = response.json()
for user in users:
    print(user)

# №5
print("\n№5. Добавляем пользователя со своим именем:")
user_data = {
    "address": {
        "city": "Екатеринбург",
        "street": "Пушкина",
        "number": "Колотушкина"
    },
    "email": "fariz@example.ru",
    "username": "fariz_nasibov",
    "name": {
        "firstname": "fariz",
        "lastname": "nasibov"
    },
    "phone": "1-234-567-890"
}
response = requests.post("https://fakestoreapi.com/users", json=user_data)
print(response.json())
