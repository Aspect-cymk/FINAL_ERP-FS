
#======================================================================================= IMPORT STATEMENTS =================================================================================#

import pickle
import random
from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser
from rich.table import Table
from rich.console import Console
import time
import os, sys
root = Tk()

#============================================================================================ MAIN MENU ====================================================================================#


def progress_bar():
  L = [" Processing....{█████████                            } %14 "," Processing....{██████████████                       } %38 ",
       " Processing....{█████████████████                    } %50 "," Processing....{█████████████████████████            } %66 ",
       " Processing....{███████████████████████████████████  } %98 "," Processing....{█████████████████████████████████████} %100" ]
  for i in L:
       print(i, end = "\n\n")
       time.sleep(0.5)

def MAIN_MENU():
    ans = "y"
    while ans == "y":
        print("""   
       _______  ___     ___  ___  ____  __________  ________  _____  ____   
      / __/ _ \/ _ \   / _ \/ _ \/ __ \/_  __/ __ \/_  __/\ \/ / _ \/ __/  
     / _// , _/ ___/  / ___/ , _/ /_/ / / / / /_/ / / /    \  / ___/ _/     
    /___/_/|_/_/     /_/  /_/|_|\____/ /_/  \____/ /_/     /_/_/  /___/     
               __  ______   _____  __    __  ________  ____  __               
              /  |/  / _ | /  _/ |/ /   /  |/  / __/ |/ / / / /               
             / /|_/ / __ |_/ //    /   / /|_/ / _//    / /_/ /                
            /_/  /_/_/ |_/___/_/|_/   /_/  /_/___/_/|_/\____/                 
                                                                             """)
        print("""  AVAILABLE MODULES ( BETA VERSION )
1. EXCHANGE RATES MODULE """)
        print("2. CUSTOMERS MODULE")
        print("3. EMPLOYEES MODULE")
        print("4. ORDER MODULE")
        print("5. MAIL MODULE")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            exc()
        elif choice == '2':
            customers()
        elif choice == '3':
            employee()
        elif choice == '4':
            orders()
        elif choice == '5':
            Mail_Module()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.") 

        ans = input("Do you want to continue? (y/n) ")

#============================================================================================ MODULES ======================================================================================#

#MAIL MODULE
def Mail_Module():

    def write_mail():
        root.title('Mail Module')
        root.geometry("1200x710")


        # Set variable for open file name
        global open_status_name
        open_status_name = False

        global selected
        selected = False

        # Create New File Function
        def new_file():
            # Delete previous text
            my_text.delete("1.0", END)
            # Update status bars
            root.title('New File - Mail')
            status_bar.config(text="New File        ")

            global open_status_name
            open_status_name = False

        # Open Files
        def open_file():
            # Delete previous text
            my_text.delete("1.0", END)

            # Grab Filename
            text_file = filedialog.askopenfilename(initialdir="C:/gui/", title="Open File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
            
            # Check to see if there is a file name
            if text_file:
                # Make filename global so we can access it later
                global open_status_name
                open_status_name = text_file

            # Update Status bars
            name = text_file
            status_bar.config(text=f'{name}        ')
            name = name.replace("C:/gui/", "")
            root.title(f'{name} - Mail')

            # Open the file
            text_file = open(text_file, 'r')
            stuff = text_file.read()
            # Add file to textbox
            my_text.insert(END, stuff)
            # Close the opened file
            text_file.close()

        # Save As File
        def save_as_file():
            text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:/gui/", title="Save File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
            if text_file:
                # Update Status Bars
                name = text_file
                status_bar.config(text=f'Saved: {name}        ')
                name = name.replace("C:/gui/", "")
                root.title(f'{name} - Mail')

                # Save the file
                text_file = open(text_file, 'w')
                text_file.write(my_text.get(1.0, END))
                # Close the file
                text_file.close()

        # Save File
        def save_file():
            global open_status_name
            if open_status_name:
                # Save the file
                text_file = open(open_status_name, 'w')
                text_file.write(my_text.get(1.0, END))
                # Close the file
                text_file.close()
                # Put status update or popup code
                status_bar.config(text=f'Saved: {open_status_name}        ')
                name = open_status_name
                name = name.replace("C:/gui/", "")
                root.title(f'{name} - Mail')
            else:
                save_as_file()

        # Cut Text
        def cut_text(e):
            global selected
            # Check to see if keyboard shortcut used
            if e:
                selected = root.clipboard_get()
            else:
                if my_text.selection_get():
                    # Grab selected text from text box
                    selected = my_text.selection_get()
                    # Delete Selected Text from text box
                    my_text.delete("sel.first", "sel.last")
                    # Clear the clipboard then append
                    root.clipboard_clear()
                    root.clipboard_append(selected)

        # Copy Text
        def copy_text(e):
            global selected
            # check to see if we used keyboard shortcuts
            if e:
                selected = root.clipboard_get()

            if my_text.selection_get():
                # Grab selected text from text box
                selected = my_text.selection_get()
                # Clear the clipboard then append
                root.clipboard_clear()
                root.clipboard_append(selected)

        # Paste Text
        def paste_text(e):
            global selected
            #Check to see if keyboard shortcut used
            if e:
                selected = root.clipboard_get()
            else:
                if selected:
                    position = my_text.index(INSERT)
                    my_text.insert(position, selected)

        # Bold Text
        def bold_it():
            # Create our font
            bold_font = font.Font(my_text, my_text.cget("font"))
            bold_font.configure(weight="bold")

            # Configure a tag
            my_text.tag_configure("bold", font=bold_font)

            # Define Current tags
            current_tags = my_text.tag_names("sel.first")

            # If statment to see if tag has been set
            if "bold" in current_tags:
                my_text.tag_remove("bold", "sel.first", "sel.last")
            else:
                my_text.tag_add("bold", "sel.first", "sel.last")

        # Italics Text
        def italics_it():
            # Create our font
            italics_font = font.Font(my_text, my_text.cget("font"))
            italics_font.configure(slant="italic")

            # Configure a tag
            my_text.tag_configure("italic", font=italics_font)

            # Define Current tags
            current_tags = my_text.tag_names("sel.first")

            # If statment to see if tag has been set
            if "italic" in current_tags:
                my_text.tag_remove("italic", "sel.first", "sel.last")
            else:
                my_text.tag_add("italic", "sel.first", "sel.last")

        # Change Selected Text Color
        def text_color():
            # Pick a color
            my_color = colorchooser.askcolor()[1]
            if my_color:
                # Create our font
                color_font = font.Font(my_text, my_text.cget("font"))

                # Configure a tag
                my_text.tag_configure("colored", font=color_font, foreground=my_color)

                # Define Current tags
                current_tags = my_text.tag_names("sel.first")

                # If statment to see if tag has been set
                if "colored" in current_tags:
                    my_text.tag_remove("colored", "sel.first", "sel.last")
                else:
                    my_text.tag_add("colored", "sel.first", "sel.last")

        # Change bg color
        def bg_color():
            my_color = colorchooser.askcolor()[1]
            if my_color:
                my_text.config(bg=my_color)

        # Change ALL Text Color
        def all_text_color():
            my_color = colorchooser.askcolor()[1]
            if my_color:
                my_text.config(fg=my_color)

        # Print File Function
        def print_file():
            #printer_name = win32print.GetDefaultPrinter()
            #status_bar.config(text=printer_name)
            
            # Grab Filename
            file_to_print = filedialog.askopenfilename(initialdir="C:/gui/", title="Open File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))

            # Check to see if we grabbed a filename
            if file_to_print:
                # Print the file
                win32api.ShellExecute(0, "print", file_to_print, None, ".", 0)

        # Select all Text
        def select_all(e):
            # Add sel tag to select all text
            my_text.tag_add('sel', '1.0', 'end')

        # Clear All Text
        def clear_all():
            my_text.delete(1.0, END)

        # Turn on Night Mode
        def night_on():
            main_color = "#4b6b96"
            second_color = "#f0f3b6"
            text_color = "black"

            root.config(bg=main_color)
            status_bar.config(bg=main_color, fg=text_color)
            my_text.config(bg=second_color)
            toolbar_frame.config(bg=main_color)
            # toolbar buttons
            bold_button.config(bg=second_color)
            italics_button.config(bg=second_color)
            redo_button.config(bg=second_color)
            undo_button.config(bg=second_color)
            color_text_button.config(bg=second_color)
            # file menu colors
            file_menu.config(bg=main_color, fg=text_color)
            edit_menu.config(bg=main_color, fg=text_color)
            color_menu.config(bg=main_color, fg=text_color)
            options_menu.config(bg=main_color, fg=text_color)


        # Turn Off Night Mode:
        def night_off():
            main_color = "SystemButtonFace"
            second_color = "SystemButtonFace"
            text_color = "black"

            root.config(bg=main_color)
            status_bar.config(bg=main_color, fg=text_color)
            my_text.config(bg="white")
            toolbar_frame.config(bg=main_color)
            # toolbar buttons
            bold_button.config(bg=second_color)
            italics_button.config(bg=second_color)
            redo_button.config(bg=second_color)
            undo_button.config(bg=second_color)
            color_text_button.config(bg=second_color)
            # file menu colors
            file_menu.config(bg=main_color, fg=text_color)
            edit_menu.config(bg=main_color, fg=text_color)
            color_menu.config(bg=main_color, fg=text_color)
            options_menu.config(bg=main_color, fg=text_color)



        # Create a toolbar frame
        toolbar_frame = Frame(root)
        toolbar_frame.pack(fill=X)

        # Create Main Frame
        my_frame = Frame(root)
        my_frame.pack(pady=5)

        # Create our Scrollbar For the Text Box
        text_scroll = Scrollbar(my_frame)
        text_scroll.pack(side=RIGHT, fill=Y)

        # Horizontal Scrollbar
        hor_scroll = Scrollbar(my_frame, orient='horizontal')
        hor_scroll.pack(side=BOTTOM, fill=X)

        # Create Text Box
        my_text = Text(my_frame, width=97, height=25, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black", undo=True, yscrollcommand=text_scroll.set, wrap="none", xscrollcommand=hor_scroll.set)
        my_text.pack()

        # Configure our Scrollbar
        text_scroll.config(command=my_text.yview)
        hor_scroll.config(command=my_text.xview)

        # Create Menu
        my_menu = Menu(root)
        root.config(menu=my_menu)

        # Add File Menu
        file_menu = Menu(my_menu, tearoff=False)
        my_menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=new_file)
        file_menu.add_command(label="Open", command=open_file)
        file_menu.add_command(label="Save", command=save_file)
        file_menu.add_command(label="Save As...", command=save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="Print File", command=print_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)

        # Add Edit Menu
        edit_menu = Menu(my_menu, tearoff=False)
        my_menu.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Cut", command=lambda: cut_text(False), accelerator="(Ctrl+x)")
        edit_menu.add_command(label="Copy", command=lambda: copy_text(False), accelerator="(Ctrl+c)")
        edit_menu.add_command(label="Paste             ", command=lambda: paste_text(False), accelerator="(Ctrl+v)")
        edit_menu.add_separator()
        edit_menu.add_command(label="Undo", command=my_text.edit_undo, accelerator="(Ctrl+z)")
        edit_menu.add_command(label="Redo", command=my_text.edit_redo, accelerator="(Ctrl+y)")
        edit_menu.add_separator()
        edit_menu.add_command(label="Select All", command=lambda: select_all(True), accelerator="(Ctrl+a)")
        edit_menu.add_command(label="Clear", command=clear_all)

        # Add Color Menu
        color_menu = Menu(my_menu, tearoff=False)
        my_menu.add_cascade(label="Colors", menu=color_menu)
        color_menu.add_command(label="Selected Text", command=text_color)
        color_menu.add_command(label="All Text", command=all_text_color)
        color_menu.add_command(label="Background", command=bg_color)

        # Add Options Menu
        options_menu = Menu(my_menu, tearoff=False)
        my_menu.add_cascade(label="Options", menu=options_menu)
        options_menu.add_command(label="Night Mode On", command=night_on)
        options_menu.add_command(label="Night Mode Off", command=night_off)


        # Add Status Bar To Bottom Of App
        status_bar = Label(root, text='Ready        ', anchor=E)
        status_bar.pack(fill=X, side=BOTTOM, ipady=15)

        # Edit Bindings
        root.bind('<Control-Key-x>', cut_text)
        root.bind('<Control-Key-c>', copy_text)
        root.bind('<Control-Key-v>', paste_text)
        # Select Binding
        root.bind('<Control-A>', select_all)
        root.bind('<Control-a>', select_all)

        # Create Buttons

        # Bold Button
        bold_button = Button(toolbar_frame, text="Bold", command=bold_it)
        bold_button.grid(row=0, column=0, sticky=W, padx=5, pady=5)
        # Italics Button
        italics_button = Button(toolbar_frame, text="Italics", command=italics_it)
        italics_button.grid(row=0, column=1, padx=5, pady=5)

        # Undo/Redo Buttons
        undo_button = Button(toolbar_frame, text="Undo", command=my_text.edit_undo)
        undo_button.grid(row=0, column=2, padx=5, pady=5)
        redo_button = Button(toolbar_frame, text="Redo", command=my_text.edit_redo)
        redo_button.grid(row=0, column=3, padx=5, pady=5)

        # Text Color
        color_text_button = Button(toolbar_frame, text="Text Color", command=text_color)
        color_text_button.grid(row=0, column=4, padx=5, pady=5)



        root.mainloop()

    def send_mail():

      # list of email_id to send the mail
      g = input(" Enter the gmail you have to send the mail to :")
      li = [g]
      f = input(" Enter the name of the file you want to send as the mail(eg: abc.txt ): ")
      file = open( f, "r")
      re = file.read()
      for dest in li:
          s = smtplib.SMTP('smtp.gmail.com', 587)
          s.starttls()
          s.login("Kaearekae@gmail.com", "xnko iuvd okhc bquu")
          message = re
          s.sendmail("Kaearekae@gmail.com", dest, message)
          print("  Mail has been succesfully sent via GMAIL!")
          s.quit()
      file.close()

      
        
    while True:
        print("\nEmployee Management System:")
        print("1. Write Mail")
        print("2. Send Mail")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            write_mail()
        elif choice == '2':
            send_mail()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")
    






# EXCHANGE RATES MODULE
def exc(): 

    print(""" /n𝕮𝖚𝖗𝖗𝖊𝖓𝖙 𝕰𝖝𝖈𝖍𝖆𝖓𝖌𝖊 𝕽𝖆𝖙𝖊𝖘

                1. 1$(USD) = 82.90 ₹(INR)
                2. 1€ (EURO)= 89.63 ₹(INR)
                3. 1¥(YEN) = 0.55 ₹(INR)
                4. 1$(CAD) = 61.40 ₹(INR)""")

#CUSTOMERS MODULE
    
def customers():
    """Main function for customer management."""
    while True:
        print("\nCustomer Management System:")
        print("1. Add Customer")
        print("2. View Customers")
        print("3. Update Customer")
        print("4. Delete Customer")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_customer()
        elif choice == '2':
            view_customers()
        elif choice == '3':
            update_customer()
        elif choice == '4':
            delete_customer()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
            
def add_customer():
    """Adds a new customer record to the binary file."""
    try:
        with open("customers.dat", "ab") as file:
            customer = {}
            customer["customer_id"] = input("Enter Customer ID: ")
            customer["name"] = input("Enter Customer Name: ")
            customer["email"] = input("Enter Customer Email: ")
            customer["phone"] = input("Enter Customer Phone: ")
            pickle.dump(customer, file)
            progress_bar()
            print("Customer added successfully!" , end = "\n")
    except Exception as e:
        print(f"Error adding customer: {e}")
        
def view_customers():
    """Displays all customer records from the binary file."""
    try:
        with open("customers.dat", "rb") as file:
            table = Table(title="Customer Records")
            table.add_column("Customer ID", style="cyan", no_wrap=True)
            table.add_column("Name", style="magenta")
            table.add_column("Email", style="green")
            table.add_column("Phone", style="yellow")
            while True:
                try:
                    customer = pickle.load(file)
                    table.add_row(
                        customer["customer_id"],
                        customer["name"],
                        customer["email"],
                        customer["phone"],
                    )
                except EOFError:
                    break
            console = Console()
            console.print(table)
    except Exception as e:
        print(f"Error viewing customers: {e}")

def update_customer():
    """Updates an existing customer record in the binary file."""
    try:
        with open("customers.dat", "rb+") as file:
            customer_id_to_update = input("Enter the Customer ID to update: ")
            found = False
            while True:
                try:
                    customer = pickle.load(file)
                    if customer["customer_id"] == customer_id_to_update:
                        print("Customer Found:")
                        print(f"{'Customer ID':<15} {'Name':<20} {'Email':<30} {'Phone':<15}")
                        print(f"{customer['customer_id']:<15} {customer['name']:<20} {customer['email']:<30} {customer['phone']:<15}")
                        print("-" * 50)
                        customer["name"] = input("Enter New Name (or press Enter to keep current): ") or customer["name"]
                        customer["email"] = input("Enter New Email (or press Enter to keep current): ") or customer["email"]
                        customer["phone"] = input("Enter New Phone (or press Enter to keep current): ") or customer["phone"]
                        file.seek(-pickle.dumps(customer).__len__(), 1)
                        pickle.dump(customer, file)
                        found = True
                        print("Customer updated successfully!")
                        break
                except EOFError:
                    break
        if not found:
            print(f"Customer with ID '{customer_id_to_update}' not found.")
    except Exception as e:
        print(f"Error updating customer: {e}")
        
def delete_customer():
    """Deletes a customer record from the binary file."""
    try:
        with open("customers.dat", "rb+") as file:
            customer_id_to_delete = input("Enter the Customer ID to delete: ")
            temp_file = "temp.dat"
            found = False
            while True:
                try:
                    customer = pickle.load(file)
                    if customer["customer_id"] != customer_id_to_delete:
                        with open(temp_file, "ab") as temp:
                            pickle.dump(customer, temp)
                    else:
                        found = True
                except EOFError:
                    break
        if found:
            print("Customer deleted successfully!")
            with open(temp_file, "rb") as temp:
                with open("customers.dat", "wb") as file:
                    while True:
                        try:
                            customer = pickle.load(temp)
                            pickle.dump(customer, file)
                        except EOFError:
                            break
        else:
            print(f"Customer with ID '{customer_id_to_delete}' not found.")
        if found:
            os.remove(temp_file)
    except Exception as e:
        print(f"Error deleting customer: {e}")

#EMPLOYEES MODULE

def employee():
    def add_employee():
        """Adds an employee record to the binary file."""
        try:
            with open("employees.dat", "ab") as file:
                employee = {}
                employee["emp_id"] = input("Enter Employee ID: ")
                employee["name"] = input("Enter Employee Name: ")
                employee["department"] = input("Enter Department: ")
                employee["salary"] = float(input("Enter Salary: "))
                pickle.dump(employee, file)
            progress_bar()
            print("Employee added successfully!", end = "\n")
        except Exception as e:
            print(f"Error adding employee: {e}")


    def view_employees():
        """Displays all employee records from the binary file."""
        try:
            with open("employees.dat", "rb") as file:
                table = Table(title="Employee Records")
                table.add_column("Emp ID", style="cyan", no_wrap=True)
                table.add_column("Name", style="magenta")
                table.add_column("Department", style="green")
                table.add_column("Salary", style="yellow")
                while True:
                    try:
                        employee = pickle.load(file)
                        table.add_row(
                            employee["emp_id"],
                            employee["name"],
                            employee["department"],
                            str(employee["salary"]),
                        )
                    except EOFError:
                        break
                console = Console()
                console.print(table)
        except Exception as e:
            print(f"Error viewing employees: {e}")



    def update_employee():
        """Updates an existing employee record in the binary file."""
        try:
            with open("employees.dat", "rb+") as file:
                emp_id_to_update = input("Enter the Employee ID to update: ")
                found = False
                while True:
                    try:
                        employee = pickle.load(file)
                        if employee["emp_id"] == emp_id_to_update:
                            print("Employee Found:")
                            print(f"{'Emp ID':<10} {'Name':<20} {'Department':<15} {'Salary':<10}")
                            print(f"{employee['emp_id']:<10} {employee['name']:<20} {employee['department']:<15} {employee['salary']:<10}")
                            print("-" * 40)
                            employee["name"] = input("Enter New Name (or press Enter to keep current): ") or employee["name"]
                            employee["department"] = input("Enter New Department (or press Enter to keep current): ") or employee["department"]
                            employee["salary"] = float(input("Enter New Salary (or press Enter to keep current): ")) or employee["salary"]
                            file.seek(-pickle.dumps(employee).__len__(), 1)
                            pickle.dump(employee, file)
                            found = True
                            print("Employee updated successfully!")
                            break
                    except EOFError:
                        break
                if not found:
                    print(f"Employee with ID '{emp_id_to_update}' not found.")
        except Exception as e:
                print(f"Error updating employee: {e}")

                
    def delete_employee():
        """Deletes an employee record from the binary file."""
        try:
            with open("employees.dat", "rb+") as file:
                emp_id_to_delete = input("Enter the Employee ID to delete: ")
                temp_file = "temp.dat"
                found = False
                while True:
                    try:
                        employee = pickle.load(file)
                        if employee["emp_id"] != emp_id_to_delete:
                            with open(temp_file, "ab") as temp:
                                pickle.dump(employee, temp)
                        else:
                            found = True
                    except EOFError:
                        break
                if found:
                    print("Employee deleted successfully!")
                    with open(temp_file, "rb") as temp:
                        with open("employees.dat", "wb") as file:
                            while True:
                                try:
                                    employee = pickle.load(temp)
                                    pickle.dump(employee, file)
                                except EOFError:
                                    break
                else:
                    print(f"Employee with ID '{emp_id_to_delete}' not found.")
                if found:
                    os.remove(temp_file)
        except Exception as e:
            print(f"Error deleting employee: {e}")

        """Main function to drive the menu."""
    while True:
        print("\nEmployee Management System:")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            update_employee()
        elif choice == '4':
            delete_employee()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

#ORDER MODULE
def orders():
    """Main function for order management."""
    while True:
        print("\nOrder Management System:")
        print("1. Create Order")
        print("2. View Orders")
        print("3. Cancel Order")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_order()
        elif choice == '2':
            view_orders()
        elif choice == '3':
            cancel_order()
        elif choice == '4':
            break
        else:
            
            rint("Invalid choice. Please try again.")

def create_order():
    """Creates a new order record in the binary file."""
    try:
        with open("orders.dat", "ab") as file:
            order = {}
            order["order_id"] = input("Enter Order ID: ")
            order["customer_id"] = input("Enter Customer ID: ")
            order["items"] = []
            while True:
                item_name = input("Enter item name (or press Enter to finish adding items): ")
                if not item_name:
                    break
                item_quantity = int(input("Enter item quantity: "))
                order["items"].append({"name": item_name, "quantity": item_quantity})
            order["status"] = "Pending"
            pickle.dump(order, file)
        progress_bar()
        print("Order created successfully!", end = "\n")
    except Exception as e:
        print(f"Error creating order: {e}")

def view_orders():
    """Displays all order records from the binary file."""
    try:
        with open("orders.dat", "rb") as file:
            table = Table(title="Order Records")
            table.add_column("Order ID", style="cyan", no_wrap=True)
            table.add_column("Customer ID", style="magenta")
            table.add_column("Items", style="green")
            table.add_column("Status", style="yellow")
            while True:
                try:
                    order = pickle.load(file)
                    items_str = ", ".join([f"{item['name']} ({item['quantity']})" for item in order["items"]])
                    table.add_row(
                        order["order_id"],
                        order["customer_id"],
                        items_str,
                        order["status"],
                    )
                except EOFError:
                    break
            console = Console()
            console.print(table)
    except Exception as e:
        print(f"Error viewing orders: {e}")

def cancel_order():
    """Cancels an existing order in the binary file."""
    try:
        with open("orders.dat", "rb+") as file:
            order_id_to_cancel = input("Enter the Order ID to cancel: ")
            temp_file = "temp.dat"
            found = False
            while True:
                try:
                    order = pickle.load(file)
                    if order["order_id"] == order_id_to_cancel:
                        order["status"] = "Cancelled"
                        file.seek(-pickle.dumps(order).__len__(), 1)
                        pickle.dump(order, file)
                        found = True
                        print("Order cancelled successfully!")
                        break
                    else:
                        with open(temp_file, "ab") as temp:
                            pickle.dump(order, temp)
                except EOFError:
                    break
            if not found:
                print(f"Order with ID '{order_id_to_cancel}' not found.")
            if found:
                with open(temp_file, "rb") as temp:
                    with open("orders.dat", "wb") as file:
                        while True:
                            try:
                                order = pickle.load(temp)
                                pickle.dump(order, file)
                            except EOFError:
                                break
                os.remove(temp_file)
    except Exception as e:
        print(f"Error cancelling order: {e}")


def sgn(): # SIGN UP MODULE
  stu = {}
  ans = "y"
  file = open("py.dat", "wb")
  while ans == "y":
    
    usr = input (" Enter your username :")
    pss = input (" Enter a password :")
    pss2 = input (" Enter your password again :")
    fcs = random.getrandbits(16)
    stu["username"] = usr
    stu["password"] = pss
    stu["Branch ID"] = fcs
    if pss == pss2:
      progress_bar()
      print(" You have successfully signed up! ", end = "\n")
      print(" Your branch ID is : ", fcs, "NOTE: PLEASE KEEP IT SAFE!", end = "\n")
      pickle.dump(stu, file)
      ans = input("Do you want to enter more records(y/n) :")
    else:
            print("Make sure the password is correct!")
    
    file.close()

def lgn(): # LOGIN MODULE
    file = open("py.dat", "rb")
    login = input(" Enter your username: ")
    password = input(" Enter your password: ")
    try:
        while True:
          stu = pickle.load(file)
          if stu["username"] == login and stu["password"] == password:
            print("Login successful")
            found = True
            while True:
      
              print(" \nBRANCHES OF YOUR COMPANY ")
              print(" 1. HPL(PVT.LTD) BANGALORE, HSR ")
              print(" 2. HPL(PVT.LTD) BANGALORE, ELECRONIC CITY ")
              print(" 3. HPL(PVT.LTD) BANGALORE, HEBAL ")
              print(" 4. HPL(PVT.LTD) BANGALORE, WHITEFIELD ")
              print(" 5. HPL(PVT.LTD) BANGALORE, KORMANGALA ")
              print(" 6. HPL(PVT.LTD) BANGALORE, INDIRANAGAR ")

              I = int(input(" Enter your  Branch ID: "))
              choice = int(input(" Enter your Branch: "))
              
              if I == stu["Branch ID"]:
            
                if choice == 1:
                    print(" You have successfully logged in to HPL(PVT.LTD) BANGALORE, HSR ")
                    MAIN_MENU()
                
                if choice == 2:
                    print(" You have successfully logged in to HPL(PVT.LTD) BANGALORE, ELECRONIC CITY ")
                    MAIN_MENU()


                if choice == 3:
                    print(" You have successfully logged in to HPL(PVT.LTD) BANGALORE, HEBAL ")
                    MAIN_MENU()

                if choice == 4:
                    print(" You have successfully logged in to HPL(PVT.LTD) BANGALORE, WHITEFIELD ")
                    MAIN_MENU()

                if choice == 5:
                    print(" You have successfully logged in to HPL(PVT.LTD) BANGALORE, KORMANGALA ")
                    MAIN_MENU()

                if choice == 6:
                    print(" You have successfully logged in to HPL(PVT.LTD) BANGALORE, INDIRANAGAR ")
                    MAIN_MENU()

                
                
          else:
            print(" Wrong Branch ID entered ")

    except:
        if found == False:
            print("Wrong credentials entered! Try again.")
    file.close()


while True:



    
    print ("""
========================================================================================================================================================================================
========================================================================================================================================================================================
                                    ____     __                   _            ___                                   ___  __               _                                           
                                   / __/__  / /____ _______  ____(_)__ ___    / _ \___ ___ ___  __ _____________    / _ \/ /__ ____  ___  (_)__  ___ _                                 
                                  / _// _ \/ __/ -_) __/ _ \/ __/ (_-</ -_)  / , _/ -_|_-</ _ \/ // / __/ __/ -_)  / ___/ / _ `/ _ \/ _ \/ / _ \/ _ `/                                 
                                 /___/_//_/\__/\__/_/ / .__/_/ /_/___/\__/  /_/|_|\__/___/\___/\_,_/_/  \__/\__/  /_/  /_/\_,_/_//_/_//_/_/_//_/\_, /                           
                                                     /_/                              _______  ___                                             /___/                                   
                                                                                     / __/ _ \/ _ \                                                                                    
                                                                                    / _// , _/ ___/                                                                                    
                                                                                   /___/_/|_/_/                                                                                        
                                                                                                                                                                                       
========================================================================================================================================================================================
========================================================================================================================================================================================



                                                               """)


    
    print ("""                                                                                  1. SIGN UP. """)
    print ("""                                                                                  2. LOGIN. """)
    print("                                                                                  5. EXIT")
    

    choice = int (input ("                                                                               ENTER YOUR CHOICE : "))

    if choice == 1:
        sgn()

    elif choice == 2:
        lgn()
  
    elif choice == 5:
        print ("See you nxt time!")
        break

    else:
        print("Incorrect choice!!!")

