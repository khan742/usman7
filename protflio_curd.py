import json
import os

DATA_FILE = 'portfolio.json'


# Load portfolio data from file
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []


# Save portfolio data to file
def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)


# Create a new portfolio item
def create_item():
    data = load_data()
    item = {
        "id": len(data) + 1,
        "title": input("Enter project title: "),
        "description": input("Enter project description: "),
        "link": input("Enter project link: ")
    }
    data.append(item)
    save_data(data)
    print("✅ Portfolio item created successfully!")


# Read (display) all items
def read_items():
    data = load_data()
    if not data:
        print("⚠️ No portfolio items found.")
        return

    for item in data:
        print(f"\nID: {item['id']}")
        print(f"Title: {item['title']}")
        print(f"Description: {item['description']}")
        print(f"Link: {item['link']}")
        print("-" * 30)


# Update an item by ID
def update_item():
    data = load_data()
    item_id = int(input("Enter the ID of the item to update: "))
    for item in data:
        if item["id"] == item_id:
            item["title"] = input("Enter new title: ")
            item["description"] = input("Enter new description: ")
            item["link"] = input("Enter new link: ")
            save_data(data)
            print("✅ Portfolio item updated.")
            return
    print("❌ Item not found.")


# Delete an item by ID
def delete_item():
    data = load_data()
    item_id = int(input("Enter the ID of the item to delete: "))
    new_data = [item for item in data if item["id"] != item_id]
    if len(data) == len(new_data):
        print("❌ Item not found.")
    else:
        # Reassign IDs
        for i, item in enumerate(new_data, 1):
            item["id"] = i
        save_data(new_data)
        print("🗑️ Portfolio item deleted.")


# Main menu
def main():
    while True:
        print("\n--- Portfolio CRUD System ---")
        print("1. Create Portfolio Item")
        print("2. View Portfolio Items")
        print("3. Update Portfolio Item")
        print("4. Delete Portfolio Item")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            create_item()
        elif choice == '2':
            read_items()
        elif choice == '3':
            update_item()
        elif choice == '4':
            delete_item()
        elif choice == '5':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
