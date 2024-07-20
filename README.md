# Flask-graphrag-UI

This project provides a basic Flask web interface for interacting with the GraphRAG query engine. The application allows users to run specific Python command-line queries through a simple web form.



## Features

- Execute Global and Local search queries from the GraphRAG repository.
- Asynchronous handling of long-running queries.
- Real-time status updates and result display.

## Setup

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/flask-graphrag-wrapper.git
   cd flask-graphrag-wrapper
   ```

2. **Create a virtual environment:**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```sh
   pip install -r requirements.txt
   ```

### Configuration

- By default, the app uses `./ragtest` as the root directory and `global` as the search method. These can be customized through the web interface.

### Running the Flask Application

1. **Start the Flask app:**

   ```sh
   python app.py
   ```

2. **Open your browser and navigate to:**

   ```
   http://127.0.0.1:5000
   ```

## Usage

1. **Enter the root directory (optional):** The root directory for the GraphRAG repository. Default is `./ragtest`.

2. **Enter the search method (optional):** The search method to use (`global` or `local`). Default is `global`.

3. **Enter your question:** The query you want to run.

4. **Click "Run":** The query will be executed, and the result will be displayed on the same page.

## Directory Structure

```
flask_app/
├── app.py
├── templates/
│   ├── index.html
│   └── result.html
├── static/
│   ├── css/
│   │   └── styles.css  # Optional: for custom CSS styles
│   ├── js/
│   │   └── scripts.js  # Optional: for custom JavaScript
├── requirements.txt
├── config.py  # Optional: for configuration settings
├── instance/
│   └── config.py  # Optional: for instance-specific configuration
├── __init__.py
└── README.md
```

## Explanation of Files

- **`app.py`**: The main Flask application file. Contains the routes and logic for handling the queries.
- **`templates/`**: Directory for HTML templates. Includes `index.html` for the main page and `result.html` (optional).
- **`static/`**: Directory for static files like CSS and JavaScript.
- **`requirements.txt`**: Lists the Python dependencies required for the project.
- **`config.py`**: Optional configuration file for general settings.
- **`instance/config.py`**: Optional configuration file for instance-specific settings.
- **`__init__.py`**: Indicates that this directory should be treated as a package.
- **`README.md`**: Documentation for setting up and running the application.

## Future Enhancements

- Add user authentication for secured access.
- Improve error handling and logging.
- Enhance the UI with more interactive features.

## Contributions

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or find any bugs.

## License

This project is licensed under the MIT License.
