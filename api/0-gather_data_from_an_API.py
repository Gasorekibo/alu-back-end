
#!/usr/bin/python3
# getting data from API using python
import requests
import sys


if __name__ == "__main__":
    """code to get information from the specified API"""

    Id = int(sys.argv[1])

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(Id)

    request_user = requests.get(user_url)

    data = request_user.json()

    user_todo_url = "https://jsonplaceholder.typicode.com/todos/"

    task = 0
    new = []

    todo_request = requests.get(user_todo_url)

    data2 = todo_request.json()
    for i in data2:
        if i["userId"] == Id:
            task += 1

            if i['completed']:
                new.append(i['title'])

    statement = "Employee {} is done with tasks ({}/{}):".format(data["name"]
                                                                 ,len(new), task)
    print(statement)
    for j in new:
        print('\t {}'.format(j))
