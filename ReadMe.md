# SQL Query Generator

An intuitive web application that generates SQL queries from plain language descriptions. It allows users to input their data requirements in natural language, and the application generates the corresponding SQL query along with an explanation and the expected output format. Built with Python, Streamlit, and Gemini API for NLP tasks.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Backend Details](#backend-details)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

The **SQL Query Generator** is a tool designed to simplify the process of generating SQL queries. It uses natural language processing (NLP) to convert plain language inputs into SQL queries, making it easier for individuals with limited SQL knowledge to interact with databases.

## Features

- **Natural Language Input**: Users can describe their data needs in plain language.
- **SQL Query Generation**: The app generates accurate SQL queries based on the input.
- **Query Explanation**: Provides an explanation of the generated query.
- **Output Format**: Displays the expected output format for the query.
- **Interactive Interface**: Built using Streamlit, allowing for easy interaction and visualization.

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/YourGitHubUsername/SQLQueryGenerator.git
    cd SQLQueryGenerator
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the application:
    ```sh
    streamlit run app.py
    ```

## Usage

1. Open your browser and navigate to `http://localhost:8501`.
2. Enter your data requirements in the text box using natural language.
3. Click on the "Generate Query" button to see the SQL query, explanation, and expected output format.

## How It Works

The app uses natural language processing to convert plain text into SQL queries:

1. **Input Parsing**: The user inputs their query requirements in natural language.
2. **NLP Processing**: The Gemini API processes the input and converts it into an SQL query.
3. **SQL Query Generation**: Based on the NLP model's output, the corresponding SQL query is generated.
4. **Explanation**: The system explains the generated query and provides the expected output format.

## Backend Details

The backend consists of NLP models and query generation logic:

- `gemini_api.py`: Integrates with the Gemini API for natural language processing tasks.
- `sql_query_generator.py`: Handles the logic for generating SQL queries.
- `app.py`: The main Streamlit app code for the user interface.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit changes (`git commit -am 'Add your feature'`).
4. Push the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Vipin Rawat - [GitHub](https://github.com/YourGitHubUsername)

Feel free to reach out for questions or suggestions!