# 🎬 Movie Lookup Project

This is my mMovie Lookup project, a Python terminal-based app that lets you search for movies using the [OMDb API](http://www.omdbapi.com/). Just type the name of a movie and get the **top 5 matching results** along with their title, release year, and media type.

---

## Features

- 🔍 **Search by Title**: Enter any movie or show name and get matching results.
- 🧾 **Quick Summary**: Displays the top 5 search results instantly.
- 🎨 **Colorized Output**: Uses `colorama` for a clean and readable terminal UI.
- 🔐 **Secure API Key Handling**: Uses `dotenv` for secure and flexible API key storage.

---

## Demo & Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/movie-lookup-cli.git
cd movie-lookup-cli

# Set up your environment
cp .env.example .env
# Then open .env and add:
# OMDbkey=your_actual_omdb_api_key

# Install required packages
pip install requests python-dotenv colorama

# Run the program
python lookup.py

# Demo
Welcome to my movie lookup project - Just look up a movie name and it will find matching results

What movie are you looking for?: Batman

Now searching results for Batman...

-----Here are the top 5 results for Batman-----
Batman Begins | 2005 | movie

The Batman | 2022 | movie

Batman v Superman: Dawn of Justice | 2016 | movie

Batman | 1989 | movie

Batman Returns | 1992 | movie

