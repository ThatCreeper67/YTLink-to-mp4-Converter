# 🎬 YTLink-to-MP4-Converter

**A simple Python command-line tool to download YouTube videos as MP4 files or extract their audio as MP3 — straight from your terminal.**

Stop juggling separate tools for video and audio. `YTLink-to-MP4-Converter` brings both workflows into one lightweight command-line utility, with configurable output locations for your files.

## ✨ Features

- 🎥 **Video downloads** — Download videos as MP4 at a selected resolution, including 1080p.
- 🎵 **MP3 audio extraction** — Extract audio from a video and save it as an MP3 file.
- 📂 **Separate output directories** — Choose where your video and audio files are saved.
- ⚡ **Simple command-line interface** — Run everything from your terminal or PowerShell.
- 🐍 **Python-powered** — A lightweight tool built around Python and its media-processing dependencies.

## 🚀 Getting Started

### Prerequisites

Before using the converter, make sure you have:

- Python installed and available from your terminal.
- The project dependencies installed.
- Any additional media-processing tools required by your configuration, such as FFmpeg for MP3 extraction.

### Installation

Clone the repository:

```bash
git clone https://github.com/ThatCreeper67/YTLink-to-mp4-Converter.git
```

Navigate into the project directory:

```bash
cd YTLink-to-mp4-Converter
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## 💻 Usage

The converter supports two primary modes: **MP4 video** and **MP3 audio**.

### 1. Download a video as MP4

Use the `pull` command followed by the desired resolution and the video URL.

```bash
python converter.py pull "1080 YOUTUBE_VIDEO_URL"
```

**Example:**

```bash
python converter.py pull "1080 https://www.youtube.com/watch?v=VIDEO_ID"
```

This downloads the video at a maximum target resolution of 1080p, subject to source availability and the converter's format-selection logic, and saves the resulting MP4 to your configured video output directory.

### 2. Extract audio as MP3

Want the audio without the video? Use MP3 mode:

```bash
python converter.py pull MP3 "YOUTUBE_VIDEO_URL"
```

**Example:**

```bash
python converter.py pull MP3 "https://www.youtube.com/watch?v=VIDEO_ID"
```

This extracts the video's audio, converts it to MP3, and saves the resulting audio file to your configured audio output directory.

### 📁 Output Directories

The converter supports separate destinations for video and audio files:

| Mode | Output | Destination |
|---|---|---|
| Video mode | MP4 video | Configured video folder |
| MP3 mode | MP3 audio | Configured audio folder |

Configure the output directories according to the paths supported by your local setup.

## 🛠️ Built With

- **Python** — Command-line application and download workflow.
- **yt-dlp** — Video retrieval and format selection.
- **FFmpeg** — Media conversion and audio extraction, where required.

## ⚠️ Notes and Limitations

- Available video resolutions depend on the source.
- A requested resolution is not guaranteed if the source does not provide a suitable format.
- MP3 extraction may require FFmpeg to be installed and accessible.
- Download behavior can change when the source platform changes its systems.
- Output locations and supported command syntax depend on the current project configuration.

## 🔒 Responsible Use

Use this software only for content you own or are authorized to download and convert. Respect copyright, platform terms, and applicable laws.

## 🤝 Contributions

Contributions, bug reports, and suggestions are welcome!

If you find a bug, please open an issue with:

1. A brief description of the problem.
2. The command you ran.
3. The error message or unexpected behavior.
4. Your operating system and Python version.

Pull requests that improve reliability, documentation, testing, or usability are appreciated.

## 📌 Roadmap

Potential improvements for future versions:

- [ ] Interactive command-line help and usage examples.
- [ ] Improved error messages and input validation.
- [ ] Automatic output-directory configuration.
- [ ] Progress reporting and clearer download status.
- [ ] Automated tests and continuous integration.
- [ ] Packaged releases for easier installation.
