import vk_api
import json
import os

# Используем сервисный ключ
service_key = '42379ae742379ae742379ae779412b162a4423742379ae724fda935a35252e921c2bc54'

# Авторизация в VK API
vk_session = vk_api.VkApi(token=service_key)
vk = vk_session.get_api()

# ID группы
group_id = '201437354'

# Путь к файлу, где будет храниться предыдущий список подписчиков
members_file = 'members.json'

# Получаем текущий список подписчиков группы с дополнительным полем 'domain'
current_members = vk.groups.getMembers(group_id=group_id, fields='first_name,last_name,domain')['items']

# Загружаем предыдущий список подписчиков из файла, если он существует
if os.path.exists(members_file):
    with open(members_file, 'r') as f:
        previous_members = json.load(f)
else:
    previous_members = []

# Определяем новых подписчиков
new_members = [member for member in current_members if member not in previous_members]

# Если есть новые подписчики, выводим их имена и username
if new_members:
    print("Новые подписчики:")
    for member in new_members:
        full_name = f"{member['first_name']} {member['last_name']}"
        username = f"https://vk.com/{member['domain']}"
        print(f"Имя: {full_name}, Username: {username}")
else:
    print("Новых подписчиков нет.")

# Сохраняем текущий список подписчиков в файл для следующей проверки
with open(members_file, 'w') as f:
    json.dump(current_members, f)
