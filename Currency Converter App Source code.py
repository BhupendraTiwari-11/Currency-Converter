import tkinter as tk
from tkinter import ttk, messagebox
import sv_ttk  # For modern theme

class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.root.geometry("400x600")  # Adjusted for mobile-like aspect ratio

        # Apply modern theme
        sv_ttk.set_theme("light")

        # Create main frame with gradient background
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill="both", expand=True)

        # Create canvas for gradient background
        self.canvas = tk.Canvas(self.main_frame, width=400, height=600, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Create gradient (light blue to white)
        for i in range(600):
            r = int(200 + (255-200) * (i/600))
            g = int(220 + (255-220) * (i/600))
            b = int(240 + (255-240) * (i/600))
            color = f'#{r:02x}{g:02x}{b:02x}'
            self.canvas.create_line(0, i, 400, i, fill=color)

        # Create container frame for widgets
        self.container = tk.Frame(self.canvas, bg="#ffffff", bd=10, relief="flat")
        self.container.place(relx=0.5, rely=0.5, anchor="center")

        # Static exchange rates (relative to USD)
        self.exchange_rates = {
            "USD": 1.0,
            "EUR": 0.85,
            "GBP": 0.73,
            "INR": 83.5,
            "JPY": 145.2,
        }

        # GUI Elements - Added Name field
        self.label_name = tk.Label(self.container, text="Your Name:", bg="#ffffff", font=("Arial", 12))
        self.label_name.pack(pady=10)

        self.entry_name = tk.Entry(self.container, font=("Arial", 12), bd=2, relief="groove")
        self.entry_name.pack(pady=10, padx=20, fill="x")

        self.label_amount = tk.Label(self.container, text="Amount:", bg="#ffffff", font=("Arial", 12))
        self.label_amount.pack(pady=10)

        self.entry_amount = tk.Entry(self.container, font=("Arial", 12), bd=2, relief="groove")
        self.entry_amount.pack(pady=10, padx=20, fill="x")

        self.label_from = tk.Label(self.container, text="From Currency:", bg="#ffffff", font=("Arial", 12))
        self.label_from.pack(pady=10)

        self.from_currency = ttk.Combobox(self.container, values=list(self.exchange_rates.keys()), state="readonly", font=("Arial", 12))
        self.from_currency.pack(pady=10, padx=20, fill="x")
        self.from_currency.set("USD")

        self.label_to = tk.Label(self.container, text="To Currency:", bg="#ffffff", font=("Arial", 12))
        self.label_to.pack(pady=10)

        self.to_currency = ttk.Combobox(self.container, values=list(self.exchange_rates.keys()), state="readonly", font=("Arial", 12))
        self.to_currency.pack(pady=10, padx=20, fill="x")
        self.to_currency.set("EUR")

        self.convert_button = tk.Button(self.container, text="Convert", command=self.convert_currency, 
                                      bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), 
                                      bd=0, relief="flat", padx=20, pady=10)
        self.convert_button.pack(pady=20)

        self.result_label = tk.Label(self.container, text="Converted Amount: ", bg="#ffffff", 
                                    font=("Arial", 12), wraplength=300)
        self.result_label.pack(pady=10)

        # Add rounded corners effect to container
        self.container.config(highlightbackground="#cccccc", highlightthickness=2)
        self.canvas.create_window(200, 300, window=self.container)

    def convert_currency(self):
        try:
            # Get user inputs
            name = self.entry_name.get()
            amount = float(self.entry_amount.get())
            from_curr = self.from_currency.get()
            to_curr = self.to_currency.get()

            if not name:
                messagebox.showerror("Error", "Please enter your name")
                return

            if amount <= 0:
                messagebox.showerror("Error", "Amount must be greater than 0")
                return

            # Convert the amount to USD first, then to the target currency
            amount_in_usd = amount / self.exchange_rates[from_curr]
            converted_amount = amount_in_usd * self.exchange_rates[to_curr]

            # Update result label with name
            self.result_label.config(text=f"{name}, Converted Amount: {converted_amount:.2f} {to_curr}")

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount")
        except KeyError:
            messagebox.showerror("Error", "Invalid currency selected")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()
