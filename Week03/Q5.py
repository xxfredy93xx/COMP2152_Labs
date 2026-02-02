contacts = {
    "Alice": "234-2343",
    "Bob" : "234-5555",
    "Charlie" : "222-3456"
}
print(f"Alice's number: {contacts ["Alice"]}")
contacts["Diana"] = "555-9999"
print(f"Contacts after adding Diana: {contacts}")
contacts["Bob"] = "555-1111"
print(f"Contacts after updating Bob: {contacts}")
del contacts["Charlie"]
print(f"Contacts after Deleting Charlie: {contacts}")
print(f"all numbers: {contacts.keys}")
print(f"all numbers: {contacts.values}")
print(f"Total contacts: {len(contacts)}")