# Bank-Mangment-System

This code is a Python script that defines functions for interacting with a MySQL database. The functions defined in this script include all_fuc, endscreen, menu, create, deposit, withdraw, and display.

The **all_fuc** function takes four arguments: no, name, amount, and Id. It appears to be a general function for interacting with the MySQL database, as it has three different branches for inserting a new record, selecting all records, and updating an existing record in the database.

The **endscreen** function prints a menu with two options: 'A' to return to the main menu, and 'B' to exit the program.

The **menu** function is the main menu of the program and presents the user with four options: create a new account, deposit money in an account, withdraw money from an account, and see details and balance of an account.

The **create** function allows the user to create a new account in the database. It prompts the user for their name and initial balance, and then adds a new record to the database with this information.

The **deposit** and withdraw functions allow the user to deposit or withdraw money from an existing account, respectively. They prompt the user to select an account from a list of available accounts, and then update the balance of the selected account in the database.

The **display** function allows the user to see the details and balance of an existing account. It prompts the user to select an account from a list of available accounts, and then displays the name and balance of the selected account.

The **script** also contains several calls to the time.sleep function, which cause the program to pause for a specified number of seconds. This can be used to pause the program and give the user time to read messages on the screen.

1. The script begins by importing the time, datetime, and mysql.connector modules.

2. It defines the all_fuc function, which takes four arguments: no, name, amount, and Id.

3. The all_fuc function has three branches, each corresponding to a different action to be taken with the MySQL database:

4. If the no argument is 'A', 'a', or 1, the function inserts a new record into the database with the name and amount arguments as the values for the name and balance    columns, respectively.

5. If the no argument is 'B', 'b', or 2, the function selects all records from the database and returns the result.

6. If the no argument is 'C', 'c', or 3, the function updates the balance column of the record with the Id argument as the value for the id column.

7. The script defines the endscreen function, which prints a menu with two options: 'A' to return to the main menu, and 'B' to exit the program.

8. The script defines the menu function, which is the main menu of the program. It presents the user with four options:

9. 'A' or 'a' to create a new account in the database.

10. 'B' or 'b' to deposit money in an existing account.

11. 'C' or 'c' to withdraw money from an existing account.

12. 'D' or 'd' to see the details and balance of an existing account.

13. The create function allows the user to create a new account in the database. It prompts the user for their name and initial balance, and then adds a new record to     the database with this information.

14. The deposit function allows the user to deposit money into an existing account. It prompts the user to select an account from a list of available accounts, and         then updates the balance of the selected account in the database with the deposited amount.

15. The withdraw function allows the user to withdraw money from an existing account. It prompts the user to select an account from a list of available accounts, and       then updates the balance of the selected account in the database by subtracting the withdrawn amount.

16. The display function allows the user to see the details and balance of an existing account. It prompts the user to select an account from a list of available           accounts, and then displays the name and balance of the selected account.

17. The script contains several calls to the time.sleep function, which cause the program to pause for a specified number of seconds. This can be used to pause the         program and give the user time to read messages on the screen.


