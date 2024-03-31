import tkinter as tk
from tkinter import ttk
import tkinter.messagebox

class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")

        self.expenses = {}
        self.total_expenses = 0

        # Create labels and entry fields
        self.label_desc = ttk.Label(root, text="Description:")
        self.label_desc.grid(row=0, column=0, padx=5, pady=5)
        self.entry_desc = ttk.Entry(root)
        self.entry_desc.grid(row=0, column=1, padx=5, pady=5)

        self.label_amount = ttk.Label(root, text="Amount:")
        self.label_amount.grid(row=1, column=0, padx=5, pady=5)
        self.entry_amount = ttk.Entry(root)
        self.entry_amount.grid(row=1, column=1, padx=5, pady=5)

        self.label_category = ttk.Label(root, text="Category:")
        self.label_category.grid(row=2, column=0, padx=5, pady=5)
        self.entry_category = ttk.Entry(root)
        self.entry_category.grid(row=2, column=1, padx=5, pady=5)

        self.label_month = ttk.Label(root, text="Month (MM/YYYY):")
        self.label_month.grid(row=3, column=0, padx=5, pady=5)
        self.entry_month = ttk.Entry(root)
        self.entry_month.grid(row=3, column=1, padx=5, pady=5)

        # Create buttons
        self.add_button = ttk.Button(root, text="Add Expense", command=self.add_expense)
        self.add_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.show_button = ttk.Button(root, text="Show Expenses", command=self.show_expenses)
        self.show_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        # Create filter entry and button
        self.label_filter = ttk.Label(root, text="Filter by:")
        self.label_filter.grid(row=6, column=0, padx=5, pady=5)
        self.entry_filter = ttk.Entry(root)
        self.entry_filter.grid(row=6, column=1, padx=5, pady=5)
        self.filter_button = ttk.Button(root, text="Apply Filter", command=self.apply_filter)
        self.filter_button.grid(row=6, column=2, padx=5, pady=5)

        # Create expense listbox
        self.expense_list = tk.Listbox(root, height=10, width=50)
        self.expense_list.grid(row=7, column=0, columnspan=3, padx=5, pady=5)

        # Create total label
        self.label_total = ttk.Label(root, text="Total Expenses: $0.00")
        self.label_total.grid(row=8, column=0, columnspan=3, padx=5, pady=5)

    def add_expense(self):
        desc = self.entry_desc.get()
        amount = self.entry_amount.get()
        category = self.entry_category.get()
        month = self.entry_month.get()

        if not desc or not amount or not category or not month:
            tk.messagebox.showerror("Error", "All fields are required.")
            return

        try:
            amount = float(amount)
        except ValueError:
            tk.messagebox.showerror("Error", "Invalid input for amount. Please enter a valid number.")
            return

        if month not in self.expenses:
            self.expenses[month] = []
        
        self.expenses[month].append((desc, amount, category))
        self.total_expenses += amount

        self.entry_desc.delete(0, tk.END)
        self.entry_amount.delete(0, tk.END)
        self.entry_category.delete(0, tk.END)
        self.entry_month.delete(0, tk.END)

        self.update_total_label()

    def update_total_label(self):
        self.label_total.config(text="Total Expenses: ${:.2f}".format(self.total_expenses))

    def show_expenses(self, month=None):
        self.expense_list.delete(0, tk.END)
        if month is None:
            for month, expenses in self.expenses.items():
                self.expense_list.insert(tk.END, f"Month: {month}")
                for expense in expenses:
                    self.expense_list.insert(tk.END, "    {} | ${:.2f} | {}".format(expense[0], expense[1], expense[2]))
        else:
            if month in self.expenses:
                self.expense_list.insert(tk.END, f"Month: {month}")
                for expense in self.expenses[month]:
                    self.expense_list.insert(tk.END, "    {} | ${:.2f} | {}".format(expense[0], expense[1], expense[2]))

    def apply_filter(self):
        filter_text = self.entry_filter.get().lower()
        self.expense_list.delete(0, tk.END)
        for month, expenses in self.expenses.items():
            if filter_text in month.lower():  # Check if filter_text matches month
                self.expense_list.insert(tk.END, f"Month: {month}")
                for expense in expenses:
                    self.expense_list.insert(tk.END, "    {} | ${:.2f} | {}".format(expense[0], expense[1], expense[2]))
            else:
                for expense in expenses:
                    if filter_text in expense[2].lower():  # Check if filter_text matches category
                        self.expense_list.insert(tk.END, "    {} | ${:.2f} | {}".format(expense[0], expense[1], expense[2]))

# Main function
def main():
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()

if __name__ == "__main__":
    main()
