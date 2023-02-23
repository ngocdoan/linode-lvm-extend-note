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
			"profile_image": "profile-picture.png",
			"username": row["username"],
			"email": row["email"],
			"auth_service": row["auth_service"],
			"auth_data": row["auth_data"],
			"password": row["password"],
			"nickname": row["nickname"],
			"first_name": row["first_name"],
			"last_name": row["last_name"],
			"position": row["position"],
			"roles": row["roles"],
			"locale": row["locale"],
			"teams": [
				{
					"name": row["team-name"],
					"theme": "{
						\"awayIndicator\":\"#DBBD4E\",
						\"buttonBg\":\"#23A1FF\",
						\"buttonColor\":\"#FFFFFF\",
						\"centerChannelBg\":\"#ffffff\",
						\"centerChannelColor\":\"#333333\",
						\"codeTheme\":\"github\",
						\"linkColor\":\"#2389d7\",
						\"mentionBg\":\"#2389d7\",
						\"mentionColor\":\"#ffffff\",
						\"mentionHighlightBg\":\"#fff2bb\",
						\"mentionHighlightLink\":\"#2f81b7\",
						\"newMessageSeparator\":\"#FF8800\",
						\"onlineIndicator\":\"#7DBE00\",
						\"sidebarBg\":\"#fafafa\",
						\"sidebarHeaderBg\":\"#3481B9\",
						\"sidebarHeaderTextColor\":\"#ffffff\",
						\"sidebarText\":\"#333333\",
						\"sidebarTextActiveBorder\":\"#378FD2\",
						\"sidebarTextActiveColor\":\"#111111\",
						\"sidebarTextHoverBg\":\"#e6f2fa\",
						\"sidebarUnreadText\":\"#333333\",
					}",
					"roles": row["team_roles"],
					"channels": [
					  {
						"name": row["channel-name"],
						"roles": row["channel_role]",
						"notify_props": {
						  "desktop": row["notify_desktop"],
						  "mark_unread": row["mark_unread"]
						}
					  }
					]
				}
			]
		}
        users.append(user)

# Tạo đường dẫn tới file JSON đầu ra
json_file_path = input("Nhập đường dẫn tới file JSON đầu ra: ")

# Ghi dữ liệu vào file JSON đầu ra
with open(json_file_path, 'w') as json_file:
    json.dump(users, json_file, indent=4)
