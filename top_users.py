import json

with open('data_file.json', 'r') as read_file:
    todos = json.load(read_file)

#  Searching for top users
todos_by_user = {}
for todo in todos:
    if todo['completed']:
        try:
            todos_by_user[todo['userId']] += 1
        except KeyError:
            todos_by_user[todo['userId']] = 1

todos_by_user = sorted(todos_by_user.items(), key=lambda item: item[1], reverse=True)
max_complete = todos_by_user[0][1]

top_users = []
for user, tasks_completed in todos_by_user:
    if max_complete != tasks_completed:
        break
    top_users.append(str(user))

print('Users ' + ', '.join(top_users) + f' has completed max tasks ({max_complete})')


#  Writing completed tasks of top users in filtered_data_file.json
def keep(todo):
    is_complete = todo['completed']
    is_top_user = str(todo['userId']) in top_users
    return is_complete and is_top_user


with open('filtered_data_file.json', 'w') as write_file:
    filtered_todos = list(filter(keep, todos))
    json.dump(filtered_todos, write_file, indent=3)
