orders = []

for i in range(5):
    order = input(f"Enter Order {i +1}: ")
    orders.append(order)

print("Original Orders:", orders)

additional = input("Enter additional order: ")
orders.append(additional)

print("Updated Orders:", orders)

priority = input("Enter priority order: ")
orders.append(priority)

print("Updated Orders:", orders)

search = input("\nSearch for an order: ")

if search in orders:
    print("Number of Occurrences:", orders.count(search))
    print("First Index:", orders.index(search))
else:
    print("Order not found.")

cancel = input("\nEnter order to cancel: ")

if cancel in orders:
    orders.remove(cancel)

    print("Updated Orders:")
    print(orders)
else:
    print("Order not found.")

removed = orders.pop()
print("\nLast Order Removed:", removed)

orders.sort()

print("\n===== FINAL ORDER REPORT =====")
print("Orders:", orders)
print("Total Remaining Orders:", len(orders))