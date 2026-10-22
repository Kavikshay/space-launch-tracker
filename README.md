🚀 Space Launch Tracker

A Python project that fetches upcoming space launch information from a public API. It allows users to explore launch schedules, search for launches, view details, and manage their favourite launches using JSON.

✨ Features

- Fetch upcoming space launches from an API.
- Display launch information.
- Search for launches.
- Filter launches by date.
- View launch details, including mission information and video links when available.
- Save favourite launches to a JSON file.
- Load previously saved favourites.
- Handle API and data-loading errors.

🛠️ Technologies Used

- Python — main programming language
- Requests — to send HTTP requests to the API
- JSON — to store and load favourite launches
- Launch Library 2 API — space launch data source

📦 Requirements

Install the required Python library:

pip install requests

▶️ How to Run

1. Download or clone this repository.
2. Make sure Python is installed.
3. Install the required library.
4. Run the Python file:

python space_launch_data.py

🌐 API Used

Launch Library 2 API:

https://ll.thespacedevs.com/2.3.0/launch/upcoming/

The API provides information about upcoming space launches. Available data may change depending on the API response and its limits.

📁 Project Structure

space-launch-tracker/
├── space_launch_data.py
├── favourites.json
└── README.md

Note: "favourites.json" may be created automatically by the program when you save favourites. You do not need to upload it if the program generates it.

🎯 Learning Goals

This project helped me practise:

- Working with REST APIs
- Sending HTTP requests
- Processing JSON responses
- Using functions and loops
- Searching and filtering data
- Reading and writing JSON files
- Handling errors and missing data

👨‍💻 Author

Created as a Python learning project to practise working with APIs and JSON.

📄 License

This project is available under the MIT License if an MIT "LICENSE" file is included in the repository.
