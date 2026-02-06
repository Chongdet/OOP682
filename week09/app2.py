from models.BankAccount import BankAccount

my_acc = BankAccount(1000)
your_acc = BankAccount(200)

our_acc = my_acc + your_acc
our_acc = our_acc - BankAccount(150)
print(our_acc)  