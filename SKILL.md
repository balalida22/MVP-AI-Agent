## Skill: File System Management

- List files: `ls -la <path>`
- Find files by name: `find <path> -name "<pattern>"`
- Find files by content: `grep -r "<text>" <path>`
- Create directories: `mkdir -p <path>`
- Copy files: `cp -r <src> <dst>`
- Move/rename: `mv <src> <dst>`
- Delete safely: `rm -r <path>`
- Check disk usage: `du -sh <path>` or `df -h`
- Check file type: `file <path>`

---

## Skill: Reading & Editing Files

- Print file contents: `cat <file>`
- Print with line numbers: `cat -n <file>`
- View large files page by page: `less <file>`
- Print first/last N lines: `head -n <N> <file>` / `tail -n <N> <file>`
- Search within a file: `grep -n "<pattern>" <file>`
- Replace text in file: `sed -i 's/<old>/<new>/g' <file>`
- Count lines/words: `wc -l <file>` / `wc -w <file>`
- Compare two files: `diff <file1> <file2>`

---

## Skill: Package Management

- Update package list: `sudo apt update`
- Upgrade all packages: `sudo apt upgrade -y`
- Install a package: `sudo apt install -y <package>`
- Remove a package: `sudo apt remove -y <package>`
- Search for a package: `apt search <package>`
- Check if installed: `dpkg -l | grep <package>`
- Install Python packages: `pip install <package>` or `pip3 install <package>`

---

## Skill: Process Management

- List running processes: `ps aux`
- Search for a process: `ps aux | grep <name>`
- Kill a process by name: `pkill <name>`
- Kill a process by PID: `kill -9 <pid>`
- Monitor system resources: `top` or `htop`
- Check CPU/memory usage: `free -h` and `vmstat`
- Run a command in background: `<command> &`
- Check background jobs: `jobs`

---

## Skill: Networking

- Check IP address: `ip addr show`
- Check open ports: `ss -tulnp`
- Test connectivity: `ping -c 4 <host>`
- Download a file: `wget <url>` or `curl -O <url>`
- Fetch URL content: `curl -s <url>`
- Check DNS resolution: `nslookup <domain>`
- Trace network route: `traceroute <host>`
- Check active connections: `netstat -antp`

---

## Skill: Python Development

- Run a script: `python3 <script.py>`
- Create a virtual environment: `python3 -m venv <env>`
- Activate virtual environment: `source <env>/bin/activate`
- Install from requirements: `pip install -r requirements.txt`
- List installed packages: `pip list`
- Check Python version: `python3 --version`
- Run a quick expression: `python3 -c "<expression>"`

---

## Skill: Git

- Clone a repo: `git clone <url>`
- Check status: `git status`
- Stage changes: `git add .`
- Commit: `git commit -m "<message>"`
- Push: `git push`
- Pull latest: `git pull`
- Check log: `git log --oneline -10`
- Create branch: `git checkout -b <branch>`
- Switch branch: `git checkout <branch>`

---

## Skill: Compression & Archives

- Create tar.gz: `tar -czf <archive.tar.gz> <folder>`
- Extract tar.gz: `tar -xzf <archive.tar.gz>`
- Create zip: `zip -r <archive.zip> <folder>`
- Extract zip: `unzip <archive.zip>`
- List archive contents: `tar -tzf <archive.tar.gz>`

---

## Skill: System Information

- OS info: `lsb_release -a`
- Kernel version: `uname -r`
- CPU info: `lscpu`
- Memory info: `free -h`
- Disk info: `lsblk`
- Uptime: `uptime`
- Current user: `whoami`
- Environment variables: `env`
- Check a specific variable: `echo $<VAR>`

---

## Skill: Video Downloading with yt-dlp

- Download a video (best quality): `yt-dlp <url>`
- Download audio only (mp3): `yt-dlp -x --audio-format mp3 <url>`
- Download audio only (best quality): `yt-dlp -x --audio-quality 0 <url>`
- Download to a specific folder: `yt-dlp -o "<path>/%(title)s.%(ext)s" <url>`
- Download specific resolution: `yt-dlp -f "bestvideo[height<=1080]+bestaudio" <url>`
- List available formats: `yt-dlp -F <url>`
- Download a specific format by ID: `yt-dlp -f <format_id> <url>`
- Download a playlist: `yt-dlp -o "%(playlist_index)s-%(title)s.%(ext)s" <playlist_url>`
- Download playlist range: `yt-dlp --playlist-start 1 --playlist-end 5 <playlist_url>`
- Download with subtitles: `yt-dlp --write-subs --sub-lang en <url>`
- Embed subtitles into video: `yt-dlp --embed-subs <url>`
- Download thumbnail: `yt-dlp --write-thumbnail <url>`
- Embed thumbnail into file: `yt-dlp --embed-thumbnail <url>`
- Limit download speed: `yt-dlp --rate-limit 1M <url>`
- Resume interrupted download: `yt-dlp -c <url>`
- Show video metadata without downloading: `yt-dlp --dump-json <url>`
- Update yt-dlp to latest version: `yt-dlp -U`
- Install yt-dlp if not present: `pip install yt-dlp`

## Skill: Playing Audio/Video with VLC

- Play a file: `cvlc <file>`
- Play without interface (clean output): `cvlc --play-and-exit <file>`
- Play an audio file: `cvlc --play-and-exit ./path/to/file.mp3`
- Play a video file: `cvlc --play-and-exit ./path/to/file.mp4`
- Play a playlist folder: `cvlc ./folder/`
- Play with volume (0-512, default 256): `cvlc --gain 1.5 <file>`
- Loop a file: `cvlc --loop <file>`
- Play a YouTube URL: `cvlc <youtube_url>`

Note: Always use `cvlc` instead of `vlc` when running from a subprocess or terminal agent,
as `vlc` requires a graphical interface and may fail in non-desktop environments.

---

## Skill: Media Manipulation with FFmpeg

### Format Conversion
- Convert video format: `ffmpeg -i <input.mp4> <output.mkv>`
- Convert audio format: `ffmpeg -i <input.mp3> <output.wav>`
- Extract audio from video: `ffmpeg -i <input.mp4> -vn -acodec mp3 <output.mp3>`
- Strip audio from video: `ffmpeg -i <input.mp4> -an <output.mp4>`

### Trimming & Cutting
- Trim by time: `ffmpeg -i <input> -ss 00:01:00 -to 00:02:00 -c copy <output>`
- Trim by duration: `ffmpeg -i <input> -ss 00:01:00 -t 30 -c copy <output>`
- Cut from start: `ffmpeg -i <input> -t 00:01:00 -c copy <output>`

### Merging & Concatenation
- Merge video and audio: `ffmpeg -i <video.mp4> -i <audio.mp3> -c:v copy -c:a aac <output.mp4>`
- Concatenate files (requires a list file): `ffmpeg -f concat -safe 0 -i list.txt -c copy <output.mp4>`
- Create list.txt for concat: `printf "file 'part1.mp4'\nfile 'part2.mp4'" > list.txt`

### Video Manipulation
- Resize video: `ffmpeg -i <input.mp4> -vf scale=1280:720 <output.mp4>`
- Change framerate: `ffmpeg -i <input.mp4> -r 30 <output.mp4>`
- Rotate video 90°: `ffmpeg -i <input.mp4> -vf transpose=1 <output.mp4>`
- Add subtitles: `ffmpeg -i <input.mp4> -vf subtitles=<sub.srt> <output.mp4>`
- Speed up video 2x: `ffmpeg -i <input.mp4> -vf setpts=0.5*PTS <output.mp4>`
- Slow down video 0.5x: `ffmpeg -i <input.mp4> -vf setpts=2.0*PTS <output.mp4>`

### Audio Manipulation
- Adjust volume: `ffmpeg -i <input.mp3> -af volume=1.5 <output.mp3>`
- Normalize audio: `ffmpeg -i <input.mp3> -af loudnorm <output.mp3>`
- Change audio speed: `ffmpeg -i <input.mp3> -af atempo=1.5 <output.mp3>`
- Trim silence: `ffmpeg -i <input.mp3> -af silenceremove=1:0:-50dB <output.mp3>`

### Thumbnails & Frames
- Extract a frame at timestamp: `ffmpeg -i <input.mp4> -ss 00:00:05 -frames:v 1 <output.jpg>`
- Extract frames every second: `ffmpeg -i <input.mp4> -vf fps=1 frame_%04d.jpg`
- Create video from images: `ffmpeg -framerate 24 -i frame_%04d.jpg <output.mp4>`

## Essential Commands the Agent Should Master

### Inspection
- Show file info: `ffprobe -v quiet -print_format json -show_format -show_streams <file>`
- Show duration only: `ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1 <file>`
- Check codec info: `ffprobe -v error -select_streams v:0 -show_entries stream=codec_name <file>`

### Date & Time
- `date` — current date and time
- `date +%Y-%m-%d` — formatted date
- `python3 -c "from datetime import date; print((date.today() - date(YEAR,M,D)).days)"` — date arithmetic

### System Info
- `uname -r` — kernel version
- `lsb_release -a` — OS version
- `uptime` — system uptime
- `whoami` — current user
- `echo $HOME` — home directory
- `lscpu | grep -E 'Model|CPU\(s\)|MHz'` — CPU summary
- `free -h` — memory usage
- `df -h` — disk usage
- `top -bn1 | head -20` — CPU/memory snapshot

### File System
- `find . -name "*.py" | wc -l` — count files by type
- `find . -size +10M` — files larger than 10MB
- `ls -lt | head -5` — most recently modified files
- `wc -l <file>` — line count
- `du -sh <folder>` — folder size
- `stat <file>` — file metadata

### Process Management
- `ps aux --sort=-%mem | head -10` — top memory processes
- `ps aux --sort=-%cpu | head -10` — top CPU processes

### Networking
- `curl -s <url>` — fetch URL content
- `ss -tulnp` — open ports
- `ping -c 3 <host>` — connectivity check

### Media
- `ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1 <file>` — media duration
- `ffprobe -v quiet -print_format json -show_format -show_streams <file>` — full media info
- `ffmpeg -i <input> <output>` — convert format
- `cvlc --play-and-exit <file>` — play audio

### Text Processing
- `cat <file>` — print file
- `grep -r "<pattern>" .` — search content
- `wc -w <file>` — word count
- `sed -i 's/old/new/g' <file>` — find and replace
- `awk '{print $1}' <file>` — extract column
- `sort <file> | uniq -c | sort -rn` — frequency count

### Python One-liners (for computation)
- `python3 -c "import math; print(math.sqrt(144))"` — math
- `python3 -c "from datetime import date; print(date.today())"` — today's date
- `python3 -c "print(2026 - 1955)"` — arithmetic

## Skill: Web Interaction

### Fetching Web Content
- Fetch a webpage as text: `curl -s <url>`
- Fetch with headers: `curl -sI <url>`
- Fetch and save to file: `curl -s <url> -o <file>`
- Fetch with redirect following: `curl -sL <url>`
- Fetch JSON from an API: `curl -s <url> | python3 -m json.tool`
- Download a file: `wget -q <url> -O <file>`

### Web Search & Data Extraction
- Extract page title: `curl -sL <url> | grep -o '<title>[^<]*' | head -1`
- Count words on a page: `curl -sL <url> | sed 's/<[^>]*>//g' | wc -w`
- Extract all links from a page: `curl -sL <url> | grep -oP 'href="\K[^"]*'`
- Strip HTML tags and read content: `curl -sL <url> | sed 's/<[^>]*>//g' | tr -s ' \n'`

### APIs & JSON
- Fetch public JSON API: `curl -s <api_url>`
- Pretty print JSON response: `curl -s <api_url> | python3 -m json.tool`
- Get current public IP: `curl -s https://api.ipify.org`
- Get IP geolocation info: `curl -s https://ipinfo.io`
- Get weather (wttr.in): `curl -s wttr.in/<city>?format=3`
- Get a random joke: `curl -s https://icanhazdadjoke.com/ -H "Accept: application/json"`
- Look up a word definition: `curl -s https://api.dictionaryapi.dev/api/v2/entries/en/<word>`

### Checking Connectivity
- Check if a site is reachable: `curl -s --max-time 5 <url> -o /dev/null -w "%{http_code}"`
- Check HTTP response code: `curl -o /dev/null -sw "%{http_code}" <url>`
- Measure page load time: `curl -s -o /dev/null -w "%{time_total}s" <url>`

### Wikipedia & Public Knowledge
- Get a Wikipedia summary: `curl -s "https://en.wikipedia.org/api/rest_v1/page/summary/<topic>" | python3 -m json.tool`
- Extract just the summary text: `curl -s "https://en.wikipedia.org/api/rest_v1/page/summary/<topic>" | python3 -c "import sys,json; print(json.load(sys.stdin)['extract'])"`

### Date & Time via Web
- Get current UTC time: `curl -s "https://worldtimeapi.org/api/timezone/UTC" | python3 -c "import sys,json; print(json.load(sys.stdin)['datetime'])"`
- Get time for a timezone: `curl -s "https://worldtimeapi.org/api/timezone/<region>/<city>" | python3 -c "import sys,json; print(json.load(sys.stdin)['datetime'])"`