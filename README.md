# GitHub Activity CLI

A simple command-line tool written in Python to fetch and display the recent public activity of any GitHub user using GitHub’s public API.

https://roadmap.sh/projects/github-user-activity

## Features

- Accepts GitHub username as a command-line argument.
- Fetches the latest activities (pushes, issues, stars, etc.) from GitHub API.
- Displays activity summaries in a user-friendly format in the terminal.
- Handles errors gracefully for invalid usernames or network issues.
- No external libraries used — built with Python standard library.

## Usage

```bash
python main.py <github_username>
