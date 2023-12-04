from pymongo import MongoClient

# Подключение к MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']

# Заполнение базы данных
def insert_user(username, email):
    users = db['users']
    user_data = {
        'username': username,
        'email': email
    }
    result = users.insert_one(user_data)
    print(f'Inserted user with ID {result.inserted_id}')

def insert_order(user_id, product, quantity):
    orders = db['orders']
    order_data = {
        'user_id': user_id,
        'product': product,
        'quantity': quantity
    }
    result = orders.insert_one(order_data)
    print(f'Inserted order with ID {result.inserted_id}')

# Пример использования
insert_user('user1', 'user1@example.com')
insert_user('user2', 'user2@example.com')
insert_order('1', 'Product A', 2)
insert_order('2', 'Product C', 3)