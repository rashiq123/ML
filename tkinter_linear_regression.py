from tkinter import *
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the datasets
boston_dataset = datasets.load_boston()
diabetes_dataset = datasets.load_diabetes()
wine_dataset = datasets.load_wine()

# Define a function to calculate and display the mean squared error for the selected dataset
def calculate_mse():
    # Get the test size value from the entry widget
    test_size = float(test_size_entry.get())

    # Get the selected dataset from the combobox
    selected_dataset = dataset_combobox.get()

    # Load the selected dataset
    if selected_dataset == "Boston":
        dataset = boston_dataset
    elif selected_dataset == "Diabetes":
        dataset = diabetes_dataset
    elif selected_dataset == "Wine":
        dataset = wine_dataset

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(dataset.data, dataset.target, test_size=test_size, random_state=0)

    # Create a linear regression model
    model = LinearRegression()

    # Train the model using the training set
    model.fit(X_train, y_train)

    # Make predictions on the testing set
    y_pred = model.predict(X_test)

    # Calculate the mean squared error of the model
    mse = mean_squared_error(y_test, y_pred)

    # Update the label widget with the mean squared error value
    mse_label.config(text="Mean Squared Error for %s dataset: %.2f" % (selected_dataset, mse))

# Create the Tkinter GUI
root = Tk()
root.title("Linear Regression Model")

# Create the combobox widget for the dataset selection
dataset_combobox = ttk.Combobox(root, values=["Boston", "Diabetes", "Wine"])
dataset_combobox.current(0)
dataset_combobox.grid(row=0, column=0)

# Create the entry widget for the test size value
test_size_entry = Entry(root)
test_size_entry.insert(0, "0.2")
test_size_entry.grid(row=0, column=1)

# Create the button widget to calculate the mean squared error
mse_button = Button(root, text="Calculate Mean Squared Error", command=calculate_mse)
mse_button.grid(row=0, column=2)

# Create the label widget to display the mean squared error value
mse_label = Label(root, text="")
mse_label.grid(row=1, column=0, columnspan=3)

# Run the Tkinter event loop
root.mainloop()
