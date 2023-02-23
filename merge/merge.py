import csv
import json

# Đường dẫn tới file CSV đầu vào
csv_file_path = input("Nhập đường dẫn tới file CSV đầu vào: ")

# Mở file CSV và đọc dữ liệu
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    # Bỏ qua dòng đầu tiên vì nó chứa tên các trường
    next(csv_reader)
    # Tạo list chứa các dictionary từ các dòng trong file CSV
    users = []
    for row in csv_reader:
        user = {
            "type": "user",
            "user": {
                "profile_image": "profile-picture.png",
                "username": row[0],
                "email": row[1],
                "auth_service": row[2],
                "auth_data": row[3],
                "password": row[4],
                "nickname": row[5],
                "first_name": row[6],
                "last_name": row[7],
                "position": row[8],
                "roles": row[9],
                "locale": row[10],
                "teams": [
                    {
                        "name": row[11],
                        "roles": row[12],
                        "channels": [
                            {
                                "name": row[13],
                                "roles": row[14],
                                "notify_props": {
                                    "desktop": row[15],
                                    "mark_unread": row[16]
                                }
                            }
                        ]
                    }
                ]
            }
        }
        users.append(user)

# Tạo đường dẫn tới file JSON đầu ra
json_file_path = input("Nhập đường dẫn tới file JSON đầu ra: ")

# Ghi dữ liệu vào file JSON đầu ra
with open(json_file_path, 'w') as json_file:
    json.dump(users, json_file, indent=4)
