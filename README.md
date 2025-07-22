# 🛒 CRUD Store

A simple inventory & shopping program in Python.  
This project allows users to **shop** for items and **manage inventory** depending on their selected role—Buyer or Seller.

---

## 📌 Features

The CRUD Store has two main functionalities:

### 1. 🛍️ Shopping (Buyer Role)
- View available items
- Add items to cart
- Automatic discount of 10% for purchases over 10 units
- Checkout with total calculation and change handling

### 2. 📦 Inventory Management (Seller Role)
- View current inventory
- Add new items to stock (with duplication check)
- Update existing stock quantity and/or price
- Remove items from inventory
- Password-protected access (default password: `admin`)

---

## 🧠 Program Structure

### 🗃️ Inventory
Inventory data is stored in a 2D list with each item having:
- Name
- Quantity in stock
- Price (in IDR)

### 🛠️ Core Components
- `crosscheck()` – Validates if an item already exists in inventory (case-insensitive)
- Menu-based structure, navigated via input prompts

---

## 📋 Menu Overview

### Buyer Menu
```
1. View Items in Store
2. Shop Items
3. $$$ Current Deals $$$
0. Exit Program
```

### Seller Menu *(Password Required: `admin`)*
```
1. View Items in Store
2. Add New Item(s)
3. Update an Item
4. Remove an Item
5. Shop Items
6. $$$ Current Deals $$$
0. Return to Main Menu
```

---

## 💡 Deals & Promotions
Every item has:
- A **10% discount** if more than 10 units are purchased in one transaction.

---

## 🚀 How to Run

1. Make sure Python is installed on your system.
2. Save the script into a `.py` file (e.g., `crud_store.py`)
3. Open a terminal or command prompt
4. Run the script using:
```bash
python crud_store.py
```

---

## 🔐 Access Roles

- Buyer: No password required
- Seller: Requires password (`admin`) to access inventory management features

---

## 🧑‍💻 Author

**Nickholas Adriaansz**  
Student – Purwadhika Job Connector Data Science & Machine Learning  
Email: nkyadriaansz@gmail.com
