#!/bin/bash
# Simple script to start the development server

echo "Building site..."
python3 build.py

echo "Starting server at http://localhost:8000"
echo "Press Ctrl+C to stop the server"
cd dist
python3 -m http.server 8000
