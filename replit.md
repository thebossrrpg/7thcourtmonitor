# 7th Court Roleplay Bot

## Overview
This is a Telegram bot that monitors a Notion page for changes and sends notifications to a Telegram chat group. It includes a Flask health check endpoint for monitoring uptime.

## Purpose
- Monitor a Notion page for edits
- Send automated notifications to a Telegram chat when changes are detected
- Allow manual notifications via the `/re` command in Telegram
- Automatically delete notifications after 24 hours
- Provide health check endpoints for monitoring

## Current State
The application is fully functional and running on Replit with:
- Python 3.11 environment
- All dependencies installed (pyTelegramBotAPI, requests, flask)
- Flask server running on port 5000
- Environment variables configured for sensitive credentials

## Project Architecture

### Components
1. **Telegram Bot** - Main process that handles the `/re` command
2. **Notion Monitor** - Background thread that polls Notion API for changes
3. **Flask Health Check** - Background thread with simple web server for uptime monitoring

### Key Features
- 3-minute cooldown between notifications to prevent spam
- Automatic message deletion after 24 hours
- Continuous polling with error recovery
- Multi-threaded architecture for concurrent operations

## Configuration

### Environment Variables
The application can be configured using the following environment variables (all have fallback defaults):

- `NOTION_TOKEN` - Notion API integration token
- `PAGE_ID` - Notion page ID to monitor
- `TELEGRAM_TOKEN` - Telegram bot token
- `CHAT_ID` - Telegram chat ID for notifications
- `MENSAGEM` - Custom notification message (default: "Uma nova resposta foi enviada em 7th Court Roleplay.")

### Ports
- Port 5000: Flask health check server (webview)

## Endpoints
- `GET /` - Returns "7th Court Monitor - Online"
- `GET /health` - Returns "7th Court vivo! ❤️"

## Telegram Commands
- `/re` - Manually trigger a notification (respects 3-minute cooldown)

## Recent Changes (Dec 7, 2025)
- Migrated to Replit environment
- Updated port from 8080 to 5000 for Replit compatibility
- Added environment variable support for all sensitive credentials
- Configured workflow for automatic startup
- Added Python .gitignore

## Running the Application
The application runs automatically via the configured workflow. It will:
1. Start the Notion monitor in the background
2. Start the Flask health check server on port 5000
3. Start the Telegram bot as the main process with infinity polling
