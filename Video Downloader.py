import yt_dlp

def show_progress(d):
    """Function to show download progress percentage."""
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', 'N/A')
        downloaded = d.get('_downloaded_bytes', 0)
        total = d.get('_total_bytes', 0)

        if total > 0:
            print(f"Downloading: {percent} ({downloaded}/{total} bytes)")

def download_video(url, output_path='.'):
    """
    Download a video from a given URL in 1080p quality and display the progress.
    
    Parameters:
        url (str): The URL of the video to download.
        output_path (str): The directory where the video will be saved (default is current directory).
    """
    try:
        # Set up options for yt-dlp
        ydl_opts = {
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Save video as <title>.<extension> in the output directory
            'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',  # Ensure 1080p video quality
            'quiet': False,  # Show detailed output
            'progress_hooks': [show_progress],  # Show progress during download
        }

        # Initialize yt-dlp with the options
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Download the video
            ydl.download([url])
            print(f"Video downloaded successfully to {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
url = input("Enter the video URL: ")
download_video(url)
