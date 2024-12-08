Python Video Downloader
A Python script that downloads videos in 1080p HD quality (if available) from various video websites using the yt-dlp library. The script shows the download progress in percentage and allows users to specify the download location.

Features

1. Download in 1080p HD quality (if available).
2. Shows download progress in percentage, total bytes downloaded, and estimated time remaining.
3. Flexible: Can be used to download videos from any website supported by yt-dlp.

Prerequisites
Before running the script, make sure you have the following installed on your system:

Python 3.x: Make sure Python 3 is installed.

yt-dlp: The script uses yt-dlp, a command-line program to download videos from various websites. You can install it using pip.
Install Python 3

You can download and install Python 3 from the official website:
https://www.python.org/downloads/

Install yt-dlp

Install the yt-dlp library using pip. You can do this by running the following command in your terminal:

bash
Copy code
pip install yt-dlp
Usage
Clone or download the Python script to your local machine.

Open a terminal and navigate to the directory where the script is saved.

Run the script using the following command:

bash
Copy code
python download_video.py
Enter the URL of the video you want to download when prompted.

The script will download the video in 1080p HD quality (if available) and show the download progress in real-time.

Example:
bash
Copy code
Enter the video URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Downloading: 0.0% (0/46.33MiB) 357.27KiB/s ETA 02:14
...
Video downloaded successfully to ./Rick_Astley_Never_Gonna_Give_You_Up.mp4
Options
Download directory: You can specify a custom download directory by passing the directory path as an argument to the script (e.g., python download_video.py /path/to/directory).
Video format: The script automatically selects the best available video with a height of 1080p or less. If a 1080p version is not available, it will download the best quality possible.
Troubleshooting
Issue: yt-dlp command not found.

Solution: Make sure yt-dlp is installed correctly. You can check this by running yt-dlp --version in your terminal.
Issue: No 1080p available for the video.

Solution: If 1080p quality is not available, the script will automatically fall back to the best available quality (lower than 1080p).
Issue: No video downloaded.

Solution: Ensure that the URL is valid and the video is not restricted or removed.
License
This project is licensed under the MIT License – see the LICENSE file for details.

Acknowledgements
This script uses yt-dlp, a popular video download tool based on youtube-dl, that supports downloading from many video platforms.
