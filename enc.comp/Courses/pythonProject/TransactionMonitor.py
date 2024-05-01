from plyer import notification
from plyer import battery

# Transaction Monitor
# Code for retrieving pending transaction data from account

# Code for displaying pending transactions and notifying user

transactionsPending = int(input())

if transactionsPending == 1:
    print(transactionsPending, "Transaction pending.")
    notification.notify(
        title="Transaction Monitor",
        message="You have 1 transaction pending",
        timeout=10,
        app_icon="E:\System Icons\pyc.ico"
    )

if transactionsPending > 1:
    print(transactionsPending, "Transactions pending.")
    notification.notify(
        title="Transaction Monitor",
        message="You have multiple transactions pending.",
        timeout=10,
        app_icon="E:\System Icons\pyc.ico"
    )
elif transactionsPending == 0:
    print("No transactions pending")

print("Would you like to view pending transactions?")
viewTransactions = input()

if viewTransactions == 'yes':
    print("Pending transactions:")
    print()
    notification.notify(
        title="Transaction Monitor",
        message=" You are viewing pending transactions",
        timeout=10,
        app_icon="E:\System Icons\pyc.ico"
    )

if viewTransactions == 'no':
    print()