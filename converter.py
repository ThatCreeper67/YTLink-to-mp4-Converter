import os
import sys
from yt_dlp import YoutubeDL

def download_video_by_command():
    # Capture everything typed after 'python converter.py' as a single unified string
    full_args_string = " ".join(sys.argv[1:]).strip()

    # Split exclusively by the first two spaces to safely isolate:
    # 1. "pull" 
    # 2. "1080" (or other preset)
    # 3. The raw unbroken URL string balance
    split_parts = full_args_string.split(maxsplit=2)

    if len(split_parts) < 3 or split_parts[0].lower() != "pull":
        print("❌ Invalid command structure!")
        print("💡 Type the instruction in one single line exactly like this:")
        print('   python converter.py pull 1080 "https://youtu.be"')
        return

    requested_quality = split_parts[1].lower().replace("p", "")
    video_url = split_parts[2].strip("'\" ")  # Strips off whitespace and any quotes

    VALID_PRESETS = {"144", "360", "480", "720", "1080"}
    if requested_quality not in VALID_PRESETS:
        print(f"❌ '{requested_quality}p' is not a supported preset. Pick: 144, 360, 480, 720, or 1080.")
        return

    # 📁 Updated target directory mapped straight to your exact local machine folder structure
    output_dir = r"C:\Nerd\YT\video assets\mp4s"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f"🚀 Initialising download for {requested_quality}p video profile...")
    print(f"📂 Destination Path: {output_dir}")
    print(f"🔗 Processing Full Target URL: {video_url}\n")

    ydl_opts = {
        'format': f'bestvideo[height<={requested_quality}][ext=mp4]+bestaudio[ext=m4a]/best[height<={requested_quality}][ext=mp4]/best',
        'outtmpl': os.path.join(output_dir, '%(title)s_%(height)sp.%(ext)s'),
        'merge_output_format': 'mp4',
        'quiet': False,
        'no_warnings': True,
        'js_runtimes': {'node': {}},
        'restrictfilenames': True,
        'noplaylist': True,
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print(f"\n🎉 Finished! File successfully saved to your asset directory.")
    except Exception as e:
        print(f"\n❌ Script Error: {e}", file=sys.stderr)

if __name__ == "__main__":
    download_video_by_command()
