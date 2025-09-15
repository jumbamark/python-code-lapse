# for statements
accounts = {"Mark": "active", "Mariah": "active", "Lynne":"inactive", "Mercy":"inactive"}
for key in accounts:
    print(key, len(key))
print("\n")

# print(accounts.copy())

# code that modifies a collection while iterating over the same collection is tricky to get right
# it's more straight forward to loop over a copy of the collection or create a new collection instead

# iterating over a copy
for user, status in accounts.copy().items():
    if status == "inactive":
        del accounts[user]
        print(accounts)

print("\n")

# create a new collection
active_users = {}
for user, status in accounts.items():
    if status == "active":
        active_users[user] = status
        print(active_users)