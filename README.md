# Hacker News Web Crawler

This repository contains a web crawler built to extract entries from Hacker News, providing filtering and sorting capabilities through a REST API. The front-end displays the filtered news data using a React user interface.

## Features

- **Crawler**: Extracts the latest news posts from Hacker News.
- **API**: Exposes the data with filtering and sorting capabilities.
- **Front-End**: React-based user interface for exploring news data.
- **Automated Tests**: Backend tests with `pytest`, front-end tests with `jest`.
- **GitHub Actions**: Continuous integration setup for running automated tests.

## Getting Started

### Prerequisites

- [Node.js LTS](https://nodejs.org/en)
- [Python (v3.12+)](https://www.python.org/downloads/)
- [Poetry (for Python dependency management)](https://python-poetry.org/docs/main/#installation)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/aPonce2001/hacker-news-crawler.git
   cd hacker-news-crawler
   ```

### Running the Project

#### Automatic Execution (Recommended)

For ease of use, you can execute both the back-end and front-end services automatically using the provided script. This option handles everything for you, including the port setup:

```bash
python run.py --port {PORT}
```

Replace `{PORT}` with the desired port number. The script will start both the FastAPI server and the React front-end, making the project accessible from a single entry point. By default, the script will run on port `8000`.

```bash
🚀 Starting server on port 8000...
🌐 Server running at http://localhost:8000/app
🟢 Server started. Press Ctrl+C to exit.
```

Here's a reorganized version of the `README.md` based on the inclusion of the automatic execution option:

# Hacker News Web Crawler

This repository contains a web crawler built to extract entries from Hacker News, providing filtering and sorting capabilities through a REST API. The front-end displays the filtered news data using a React user interface.

## Features

- **Crawler**: Extracts the latest news posts from Hacker News.
- **API**: Exposes the data with filtering and sorting capabilities.
- **Front-End**: React-based user interface for exploring news data.
- **Automated Tests**: Backend tests with `pytest`, front-end tests with `jest`.
- **GitHub Actions**: Continuous integration setup for running automated tests.

## Getting Started

### Prerequisites

- [Node.js LTS](https://nodejs.org/en)
- [Python (v3.12+)](https://www.python.org/downloads/)
- [Poetry (for Python dependency management)](https://python-poetry.org/docs/main/#installation)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/aPonce2001/hacker-news-crawler.git
   cd hacker-news-crawler
   ```

### Running the Project

#### Automatic Execution (Recommended)

For ease of use, you can execute both the back-end and front-end services automatically using the provided script. This option handles everything for you, including the port setup:

```bash
python run.py --port {PORT}
```

Replace `{PORT}` with the desired port number. The script will start both the FastAPI server and the React front-end, making the project accessible from a single entry point.

#### Manual Execution

If you'd prefer to run the services manually, follow these steps:

##### Front-End build (React App)

1. Navigate to the front-end folder:
   ```bash
   cd front-end
   ```

2. Install the Node.js dependencies:
   ```bash
   npm install
   ```

3. Build the React app:
   ```bash
   npm run build
   ```

4. The application will be built in the `dist` folder.

##### Back-End (API)

1. Navigate to the back-end folder:
   ```bash
   cd back-end
   ```
   
2. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

3. Start the FastAPI server:
   ```bash
   poetry run python -m uvicorn src.api.main:app --port {PORT}
   ```
   
4. The API will be available at: `http://127.0.0.1:{PORT}`

5. The front-end will be running at: `http://127.0.0.1:{PORT}/app`

### Testing

#### Back-End Tests
1. Run the Python tests with `pytest`:
   ```bash
   cd back-end
   poetry run python -m pytest /test
   ```

#### Front-End Tests
1. Run the front-end tests with `jest`:
   ```bash
   cd front-end
   npm run test
   ```

### GitHub Actions

The project includes GitHub Actions workflows that automatically run tests when code is pushed. The workflow files are located in the `.github/workflows` directory and include:

- **Back-End Tests**: Runs `pytest` on the FastAPI codebase.
- **Front-End Tests**: Runs `jest` on the React application.