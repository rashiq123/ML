# ML
# Linear Regression Model

This is a simple graphical user interface (GUI) application implemented in Python using the Tkinter library. It allows users to calculate the mean squared error (MSE) for different datasets using a linear regression model.

## Features

The Linear Regression Model application provides the following features:

- **Dataset Selection**: Users can choose from three available datasets: Boston, Diabetes, and Wine. These datasets are included in the scikit-learn library.

- **Test Size**: Users can enter a test size value to specify the proportion of the dataset that will be used for testing the model. The default value is 0.2.

- **Calculate Mean Squared Error**: Users can click the "Calculate Mean Squared Error" button to calculate and display the mean squared error for the selected dataset and test size.

## Getting Started

To run the Linear Regression Model application, follow these steps:

1. Clone the repository or download the source code files.

2. Ensure you have Python 3.x installed on your machine.

3. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

4. Open a terminal or command prompt and navigate to the directory where the source code files are located.

5. Run the following command to start the application:
   ```
   python linear_regression_model.py
   ```

6. The application window will open, displaying the dataset selection combobox, test size entry field, and the "Calculate Mean Squared Error" button.

7. Choose the desired dataset, enter the test size value, and click the button to calculate the mean squared error.

## Usage

1. **Dataset Selection**:
   - Choose the dataset from the combobox by clicking on the dropdown arrow.
   - The available options are "Boston", "Diabetes", and "Wine".
   - The "Boston" dataset contains housing-related features, "Diabetes" contains medical data, and "Wine" contains information about wines.

2. **Test Size**:
   - Enter a test size value in the entry field.
   - The test size represents the proportion of the dataset that will be used for testing the linear regression model.
   - The default value is 0.2, which corresponds to a 20% test size.

3. **Calculate Mean Squared Error**:
   - Click the "Calculate Mean Squared Error" button to perform the linear regression, make predictions, and calculate the mean squared error.
   - The application will display the calculated mean squared error value below the button.

## Contributing

Contributions to this Linear Regression Model application are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

When contributing, please ensure to follow the existing code style and provide a clear description of the changes made.

## License

This Linear Regression Model application is licensed under the [MIT License](LICENSE). You are free to modify, distribute, and use it for personal or commercial purposes.
