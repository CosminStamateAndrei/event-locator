# Event Locator Discord Bot

A Discord bot that lets users search for nearby events via the Ticketmaster API and interactively browse the results using paginated embeds.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)

---

## Overview

The **Event Locator Discord Bot** allows users to search for events in a specific city by providing a search radius. The bot retrieves event data from Ticketmaster, filters out events whose ticket sales have ended, and displays the results in a neat, paginated embed with interactive navigation buttons. It also includes basic commands such as `!hello`, `!ping`, and `!clear`.

---

## Features

- **Event Search:** Prompt users to enter a city and radius to search for events.
- **Interactive Pagination:** Browse through events in batches of 5 with navigation buttons (previous/next) and numbered buttons for quick access to event links.
- **Command Set:** Simple text and slash commands:
  - `/hello` – Greets the user.
  - `!ping` – Replies with "Pong!".
  - `!clear <amount>` – Clears a specified number of messages (requires proper permissions).
  - `!events` – Starts the event search flow.
- **Sales Filtering:** Only shows events where ticket sales are still active based on the sales end time.

---

## Prerequisites

- **Python 3.11+**
- [discord.py v2.0+](https://github.com/Rapptz/discord.py)
- [Requests](https://pypi.org/project/requests/)

---

## Installation

1. **Clone the Repository:**
   - Open your terminal.
   - Run the following command to clone the repository:
     ```bash
     git clone https://github.com/yourusername/event-locator.git
     ```
   - Navigate into the project directory:
     ```bash
     cd event-locator
     ```

2. **Create a Virtual Environment:**
   - Create a virtual environment by running:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - **On Windows:**
       ```bash
       venv\Scripts\activate
       ```
     - **On macOS/Linux:**
       ```bash
       source venv/bin/activate
       ```

3. **Install Dependencies:**
   - Install all required dependencies using the provided `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```
   - *If `requirements.txt` is not available, install the necessary packages manually:*
     ```bash
     pip install discord.py requests
     ```

---

## Setup

1. **Ticketmaster API Key:**
   - Navigate to the `api_contents/` directory.
   - Create a file named `api_key.txt`.
   - Paste your Ticketmaster API key into this file.
   - Save and close the file.

2. **Discord Bot Token:**
   - In the same `api_contents/` directory, create a file named `token.txt`.
   - Paste your Discord bot token into this file.
   - Save and close the file.

---

## Usage

1. **Start the Bot:**
   - Run the following command in your terminal:
     ```bash
     python main.py
     ```

2. **Interact with the Bot:**

   - **Slash Command: `/hello`**
     - In any Discord channel where the bot is active, type `/hello`.
     - The bot will greet you with a personalized message.

   - **Text Command: `!ping`**
     - Type `!ping` in a text channel.
     - The bot will respond with "Pong!".

   - **Text Command: `!clear <amount>`**
     - Use `!clear` followed by the number of messages you want to delete. For example:
       ```bash
       !clear 10
       ```
     - **Note:** You must have the "Manage Messages" permission to use this command.

   - **Text Command: `!events`**
     - Type `!events` to begin an interactive event search.
     - The bot will prompt you for:
       1. **City Name:** Enter the city where you want to search for events.
       2. **Search Radius:** Enter the radius (in kilometers) for the search.
     - Once provided, the bot will:
       - Retrieve event data from the Ticketmaster API.
       - Filter out events with expired ticket sales.
       - Display the events in a paginated embed with interactive buttons for navigation and to view event details.
