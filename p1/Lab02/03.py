# input
inc=float(input())
ex=float(input())
# output
print("1234567890" * 3)
print("{0:<12} {1:+8.2f} {2:>5}".format("Total Income",inc,"bahts"))
print("{0:<12} {1:-8.2f} {2:>5}".format("Expense",ex,"bahts"))
print("{0:<12} {1:>08.2f} {2:>5s}".format("Profit",inc+ex,"bahts"))