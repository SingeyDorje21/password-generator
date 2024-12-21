# Password Generator

A simple web application to generate secure passwords based on user-selected criteria.

## Features

- Generate passwords of a specified length
- Include lowercase letters
- Include uppercase letters
- Include numbers
- Include special characters
- Copy generated password to clipboard

## Technologies Used

- Python
- Flask
- HTML
- CSS

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/SingeyDorje21/password-generator.git
    cd password-gen
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

5. Run the application:
    ```sh
    flask run
    ```

6. Open your web browser and go to `http://127.0.0.1:5000/` to use the password generator.

## Usage

1. Enter the desired password length.
2. Select the criteria for the password (lowercase, uppercase, numbers, special characters).
3. Click the "Generate Password" button.
4. The generated password will be displayed below the form.
5. Click the "Copy" button to copy the generated password to your clipboard.

## Project Structure
