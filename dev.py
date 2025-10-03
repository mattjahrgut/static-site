#!/usr/bin/env python3
"""
Development script that rebuilds and serves the site.
"""

import subprocess
import sys
import os

def main():
    print("🔨 Building site...")
    result = subprocess.run([sys.executable, "build.py"], capture_output=True, text=True)
    
    if result.returncode != 0:
        print("❌ Build failed:")
        print(result.stderr)
        return
    
    print("✅ Build successful!")
    print("🌐 Starting server at http://localhost:8000")
    print("📝 Edit files in src/content/ then run this script again to see changes")
    print("🛑 Press Ctrl+C to stop")
    
    os.chdir("dist")
    subprocess.run([sys.executable, "-m", "http.server", "8000"])

if __name__ == "__main__":
    main()
