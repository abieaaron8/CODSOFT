import json
import os

FILE_NAME = "contacts.json"


def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_contacts():
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


contacts = load_contacts()


def view_contacts():
    if not contacts:
        print("\nNo contacts available.")
        return

    print("\n========== CONTACT LIST ==========")

    for index, contact in enumerate(contacts, start=1):
        print(
            f"{index}. {contact['name']} | "
            f"{contact['phone']}"
        )

    print("\nTotal Contacts:", len(contacts))


def add_contact():
    name = input("\nName: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    address = input("Address: ").strip()

    for contact in contacts:
        if contact["phone"] == phone:
            print("\nA contact with this phone number already exists.")
            return

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })

    save_contacts()

    print("\nContact added successfully.")


def search_contact():
    keyword = input(
        "\nEnter name or phone to search: "
    ).lower()

    found = False

    for contact in contacts:

        if (
            keyword in contact["name"].lower()
            or
            keyword in contact["phone"]
        ):

            print("\n---------- CONTACT FOUND ----------")
            print("Name    :", contact["name"])
            print("Phone   :", contact["phone"])
            print("Email   :", contact["email"])
            print("Address :", contact["address"])

            found = True

    if not found:
        print("\nNo matching contact found.")


def update_contact():
    view_contacts()

    if not contacts:
        return

    try:
        index = int(
            input("\nEnter contact number to update: ")
        ) - 1

        if 0 <= index < len(contacts):

            print("\nLeave blank to keep current value.")

            name = input(
                f"Name ({contacts[index]['name']}): "
            )

            phone = input(
                f"Phone ({contacts[index]['phone']}): "
            )

            email = input(
                f"Email ({contacts[index]['email']}): "
            )

            address = input(
                f"Address ({contacts[index]['address']}): "
            )

            if name:
                contacts[index]["name"] = name

            if phone:
                contacts[index]["phone"] = phone

            if email:
                contacts[index]["email"] = email

            if address:
                contacts[index]["address"] = address

            save_contacts()

            print("\nContact updated successfully.")

        else:
            print("\nInvalid contact number.")

    except ValueError:
        print("\nPlease enter a valid number.")


def delete_contact():
    view_contacts()

    if not contacts:
        return

    try:
        index = int(
            input("\nEnter contact number to delete: ")
        ) - 1

        if 0 <= index < len(contacts):

            removed = contacts.pop(index)

            save_contacts()

            print(
                f"\nDeleted contact: {removed['name']}"
            )

        else:
            print("\nInvalid contact number.")

    except ValueError:
        print("\nPlease enter a valid number.")


def contact_statistics():
    print("\n========== STATISTICS ==========")
    print("Total Contacts:", len(contacts))


while True:

    print("\n" + "=" * 40)
    print("         CONTACT BOOK")
    print("=" * 40)

    print("1. View Contacts")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Contact Statistics")
    print("7. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        view_contacts()

    elif choice == "2":
        add_contact()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        contact_statistics()

    elif choice == "7":
        print("\nThank you for using Contact Book.")
        break

    else:
        print("\nInvalid choice.")
