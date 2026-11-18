# JARVIS Plugins

A collection of modular plugins for the JARVIS desktop assistant. This repository adds capabilities for maps, system monitoring, productivity, media, health, files, Google services, GitHub, and more.

The plugins were tested for compatibility with **Mark 57**. Compatibility with other JARVIS versions depends on the plugin loader and internal APIs available in that build.

> **Important:** A folder containing several Python files is one complete plugin package when those files depend on one another. The helper files are not separate plugins. Copy the entire contents of that folder into JARVIS's plugins directory so the main plugin can import its supporting modules.

## Contents

- [Installation](#installation)
- [Plugin catalogue](#plugin-catalogue)
- [Folder-based plugin packages](#folder-based-plugin-packages)
- [Single-file plugins](#single-file-plugins)
- [Setup and dependencies](#setup-and-dependencies)
- [Privacy and permissions](#privacy-and-permissions)
- [Troubleshooting](#troubleshooting)

---

## Installation

### Step 1: Download the repository

Download this repository using **Code → Download ZIP**, then extract the ZIP file.

Or clone it with Git:

~~~bash
git clone https://github.com/nived938/Jarvis-Plugins.git
~~~

### Step 2: Open your JARVIS plugins directory

Find the existing plugins folder inside the JARVIS project you use.

Example:

~~~text
JARVIS/
└── plugins/
~~~

Use the plugins directory belonging to your actual JARVIS installation. Do not create another nested plugins folder.

### Step 3: Install a plugin from a folder

For a plugin stored inside a named folder, open that folder and:

1. Select **all files inside the folder**.
2. Copy all of them, including files whose names begin with an underscore.
3. Open your JARVIS plugins folder.
4. Paste all the copied files directly into that plugins folder.

**Copy the contents of the folder, not the outer folder itself.**

For example, to install **3D Earth Overview**, open the repository's 3D Earth Overview folder, select every file inside it, copy them, and paste them directly into JARVIS/plugins.

The main file and its helper files must stay together. For example, planet_watch.py uses supporting modules such as _planet_live.py and _planet_view.py. Copying only planet_watch.py will leave the plugin incomplete.

### Step 4: Install a single-file plugin

Some plugins are individual Python files located in the repository root.

For one of these:

1. Find the plugin's .py file in the root of the downloaded repository.
2. Copy that file.
3. Paste it directly into JARVIS/plugins.

For example, copy github_sentinel.py and paste it into JARVIS/plugins.

Do not copy README.md or LICENSE into the JARVIS plugins directory.

### Step 5: Restart JARVIS

Restart JARVIS so its plugin loader can discover the new plugin files. Open JARVIS Plugin Settings and complete any setup required by the plugin, such as a location, API token, Google OAuth credentials, or an Obsidian vault path.

Then try one of the example commands in the catalogue.

### Installing multiple folder-based plugins

You can install more than one folder-based plugin. Repeat the folder installation steps for each package, copying **all files inside each selected folder** into the same JARVIS/plugins directory.

Some packages include the same shared helper file. In this repository, the copies of _live_panels_core.py in Disk Map, Live Panels, and PC Electricity Cost are identical. Only one copy is needed in the destination. Replacing that helper with another copy from this repository is safe because the copies are identical.

---

## Plugin catalogue

There are **26 installable plugin packages/features** in this repository: 6 folder-based packages and 20 single-file plugins.

The folder-based packages are each listed as one package in this catalogue. Their supporting Python files are part of that package and are not separate plugins.

| # | Plugin / package | Type | What it does |
|---:|---|---|---|
| 1 | **3D Earth Overview / Planet Watch** | Folder package | Interactive 3D globe and maps with zoom, places, routes, earthquakes, disasters, weather, aircraft, aurora, ISS location, satellite tracking, and optional hand controls. |
| 2 | **Build Diagram** | Folder package | Uses a photo or camera view to identify components, explain assembly, create connection diagrams, mark possible problems, and compare a new photo with a build plan. |
| 3 | **Disk Map** | Folder package | Scans a drive or folder and displays a clickable treemap showing which files and folders use the most storage. It does not delete or move files. |
| 4 | **Google Workspace** | Folder package | Includes Gmail and Google Calendar controls. Read/search email, create drafts, send email when requested, view calendar events, search the agenda, and create events. Both controls use the shared Google helper module. |
| 5 | **Live Panels** | Folder package | Displays live CPU, RAM, GPU, disk, network, and process information, plus current weather and forecasts for a chosen city. |
| 6 | **PC Electricity Cost** | Folder package | Estimates PC power consumption and electricity costs per hour, day, and month. Includes a live power panel and configurable electricity tariff. |
| 7 | **Aircraft Report** | Single file | Finds aircraft reported near a configured location, provides aircraft details, displays nearby traffic, and can watch for aircraft approaching an alert radius. |
| 8 | **Audio Ripper** | Single file | Extracts audio from a supported video URL and saves an MP3 in the Music folder. Can use a URL copied to the clipboard. |
| 9 | **Auto-Pause When Away** | Single file | Uses webcam-based presence detection to pause media when you leave your desk and resume it when you return. |
| 10 | **Calorie Counter** | Single file | Analyzes food shown to the camera, estimates calories and nutrition, and keeps a daily intake total. |
| 11 | **Chat Takeover** | Single file | Watches the conversation visible on screen and can reply in your style until you stop it. Includes a focus guard to reduce the risk of typing into the wrong window. |
| 12 | **Document Review** | Single file | Organizes an AI-assisted document review into serious points, cautions, and notes to help explain terms and obligations before you act or sign. It is not legal advice. |
| 13 | **Ergonomic Guard** | Single file | Helps with posture checks, 20-20-20 eye breaks, desk stretches, and desk-session tracking. Webcam posture checks are optional. |
| 14 | **Event Countdown** | Single file | Saves birthdays, anniversaries, holidays, bills, and other events, then shows upcoming countdowns and events happening today. |
| 15 | **GitHub Sentinel** | Single file | Looks up GitHub profiles, repositories, repository details, issues, and pull requests. Can also inspect local Git status and pull updates. |
| 16 | **Media Downloader** | Single file | Downloads videos from supported video sites into the Videos folder. Can use a URL copied to the clipboard. |
| 17 | **Notification Reader** | Single file | Reads notifications from the Windows notification center, filters by app, and watches for a matching sender or phrase. |
| 18 | **Obsidian Vault** | Single file | Searches and reads Markdown notes, lists recent notes, creates or appends notes, updates daily notes, finds tasks and backlinks, and opens notes in Obsidian. It has no delete action. |
| 19 | **Pomodoro** | Single file | Runs focus and break sessions in the background, announces phase changes, and tracks daily focus time. |
| 20 | **Push-up Counter** | Single file | Counts push-ups through the webcam and saves workout sessions. MediaPipe can improve pose tracking when installed. |
| 21 | **Quiz** | Single file | Creates an on-screen quiz from a topic or supplied material, lets you answer at your own pace, and returns results to JARVIS for feedback. |
| 22 | **Screen Recorder** | Single file | Starts, stops, pauses, resumes, and checks a real screen recording. Supports optional microphone audio and Windows hotkeys. |
| 23 | **Spaced Repetition / Flashcards** | Single file | Creates and reviews persistent flashcards with an SM-2-style schedule, bringing difficult cards back sooner and easy cards less often. |
| 24 | **Spotify & Media Control** | Single file | Controls Spotify and system media playback, including play/pause, next/previous, search and play, volume, and mute. |
| 25 | **Water Reminder** | Single file | Gives recurring hydration reminders, logs water intake, tracks a daily goal, and reports today's total. |
| 26 | **YouTube Controller** | Single file | Controls an active YouTube tab with keyboard shortcuts for playback, seeking, captions, volume, speed, fullscreen, theater mode, miniplayer, and supported ad skipping. |

---

## Folder-based plugin packages

**Each row below is one complete package.** Copy every file listed in that row from its repository folder and paste all of them directly into JARVIS/plugins. Do not install the helper files as standalone plugins.

| Package folder | Files to copy together |
|---|---|
| **3D Earth Overview** | planet_watch.py, _hands.py, _planet_hands.py, _planet_live.py, _planet_view.py |
| **Build Diagram** | build_guide.py, _build_diagram.py |
| **Disk Map** | disk_map.py, _disk_map_core.py, _live_panels_core.py |
| **Google Workspace** | _google_core.py, calendar_control.py, gmail_control.py |
| **Live Panels** | live_panels.py, _live_panels_core.py |
| **PC Electricity Cost** | pc_electricity_cost.py, _electricity_cost_panel.py, _live_panels_core.py |

For example, **Google Workspace is one folder-based package**. Its Gmail and Calendar controls are two capabilities provided by that package, and both rely on _google_core.py. Copy all three files together.

---

## Single-file plugins

Each of these is an individual plugin file in the repository root. Copy only the plugin file you want into JARVIS/plugins.

| Plugin | File to copy |
|---|---|
| Aircraft Report | aircraft_report.py |
| Audio Ripper | audio_ripper.py |
| Auto-Pause When Away | auto_pause_eyes.py |
| Calorie Counter | calorie_counter.py |
| Chat Takeover | chat_takeover.py |
| Document Review | document_review.py |
| Ergonomic Guard | ergonomic_guard.py |
| Event Countdown | event_countdown.py |
| GitHub Sentinel | github_sentinel.py |
| Media Downloader | media_downloader.py |
| Notification Reader | notification_reader.py |
| Obsidian Vault | obsidian_vault.py |
| Pomodoro | pomodoro.py |
| Push-up Counter | pushup_counter.py |
| Quiz | quiz.py |
| Screen Recorder | screen_recorder.py |
| Spaced Repetition / Flashcards | spaced_repetition.py |
| Spotify & Media Control | spotify_control.py |
| Water Reminder | water_reminder.py |
| YouTube Controller | youtube_control.py |

---

## Setup and dependencies

Not every plugin needs an API key. Many use local Python or operating-system functionality. Install packages into the **same Python environment used to run JARVIS**, not a separate Python installation.

| Plugin / package | Setup and requirements |
|---|---|
| **3D Earth Overview / Planet Watch** | The listed public data sources do not require a personal API key. Install sgp4 for ISS pass predictions: pip install sgp4. Basic ISS location display can still work without it. |
| **Build Diagram** | Uses the AI/vision provider configured in JARVIS and needs a camera frame, photo, screen image, or other supported visual input for image-based tasks. |
| **Google Workspace** | Install google-api-python-client and google-auth-oauthlib. Create your own Google Cloud project, enable the Gmail API and Google Calendar API you intend to use, configure a Desktop OAuth client, enter the Client ID and Client Secret in Plugin Settings, and authorize your Google account. |
| **Disk Map** | Uses the Python standard library for scanning and the JARVIS desktop UI's PyQt6 dependency for rendering the map. No account or API key is required. |
| **Live Panels** | Uses psutil and the JARVIS desktop UI's PyQt6 dependency for system information and panels. GPU telemetry depends on supported NVIDIA driver/NVML availability. Weather data is obtained from a public source and does not require a personal API key. |
| **PC Electricity Cost** | Uses psutil for system information. NVIDIA GPU telemetry is optional and depends on driver/NVML support. Set your local electricity price per kWh in Plugin Settings for more useful cost estimates. |
| **Aircraft Report** | Configure your location in Plugin Settings using coordinates or a place name. Aircraft coverage depends on public volunteer ADS-B receivers, so low-flying aircraft may not appear. |
| **Audio Ripper and Media Downloader** | Install yt-dlp in the JARVIS environment. Audio extraction/conversion may also need FFmpeg installed and available on PATH. Only download content you have the right to save. |
| **Auto-Pause, Calorie Counter, and Push-up Counter** | Require a working webcam. Camera analysis uses OpenCV; install opencv-python if it is missing. Push-up counting can use mediapipe for enhanced pose tracking, while its fallback uses OpenCV. |
| **Chat Takeover** | Requires a configured Gemini Live connection or the supported REST fallback, plus the screen and keyboard automation dependencies used by the plugin. Focus the intended chat input before starting, keep the correct app focused, and stop takeover when you want to reply manually. |
| **Notification Reader** | Windows 10/11 only. Grant JARVIS notification access in Windows Settings under Privacy & security → Notifications. |
| **GitHub Sentinel** | Public GitHub lookups work without a token. Add your own GitHub Personal Access Token in Plugin Settings if you need private repository access. |
| **Obsidian Vault** | Choose your Obsidian vault folder in plugin settings. The plugin works directly with Markdown files in that folder. |
| **YouTube Controller** | Requires pyautogui and pygetwindow. pywinauto is optional for enhanced ad-button detection. It controls an already-open YouTube tab and does not search for or open videos. |
| **Ergonomic Guard** | Basic reminders and stretch guidance need no API key. Webcam-based posture checks need a working camera and the relevant vision dependencies. |
| **Screen Recorder** | Needs the capture dependencies and tools available to the JARVIS environment. Microphone capture is optional. See startup logs if a recorder backend is missing. |

### Google OAuth setup

Google Workspace uses **your own Google account**. This repository does not provide shared OAuth credentials.

1. Create a project in Google Cloud Console.
2. Enable the Gmail API and/or Google Calendar API.
3. Configure the OAuth consent screen. If the application is in testing mode, add your Google account as a test user.
4. Create an OAuth Client ID for a **Desktop app**.
5. Enter the Client ID and Client Secret in the Google Workspace plugin settings.
6. Press **Authorize** and complete Google's consent flow in the browser.

Gmail can create drafts or send messages. Ask for a draft when you want to review the message before sending.

---

## Privacy and permissions

Some plugins can access sensitive parts of your desktop experience. Understand their behavior before enabling them.

- **Camera plugins** use the webcam for the feature you request. Stop the feature when you are finished.
- **Chat Takeover** reads visible chat content and can send messages. Verify the focused application and recipient before starting it.
- **Document Review, Build Diagram, and Calorie Counter** use the AI/vision capabilities configured in JARVIS to analyze the material or image supplied. Do not send confidential material to an AI provider unless you are comfortable with that provider's data handling.
- **Obsidian Vault** reads and writes Markdown files inside the configured vault. It has no delete action and refuses to overwrite an existing note when creating a new one.
- **Disk Map** is read-only. It scans names and sizes but does not move or delete files.
- **Google Workspace and GitHub** use credentials that you provide. Keep tokens, OAuth secrets, and generated credential files private.
- **Notification Reader** reads Windows notification content after you grant the operating-system permission.

Some plugins save settings or progress in JARVIS's memory/data directory so that timers, events, flashcards, and daily totals can persist across restarts.

---

## Troubleshooting

### JARVIS does not detect a plugin

- Confirm that the main .py file is directly inside the correct JARVIS plugins folder.
- For a folder-based package, confirm that **every file in that package** was copied into the same destination folder.
- Make sure you did not paste a folder inside JARVIS/plugins, creating an incorrect nested directory.
- Restart JARVIS and check its startup/plugin logs for an import or dependency error.

### A plugin loads but a feature does not work

- Check the setup notes above and the plugin's settings.
- Install missing packages into the Python environment that launches JARVIS.
- Check whether the feature is Windows-only or needs a camera, internet connection, OAuth authorization, or an active AI provider.

### A plugin stops working after a JARVIS update

The repository was tested against Mark 57. A different JARVIS release may change internal APIs or the plugin loader. Check the error log and compare the affected plugin with the JARVIS version you are running.

### A helper file already exists

Do not rename helper modules. Keep filenames exactly as they are in this repository. The repeated _live_panels_core.py files in Disk Map, Live Panels, and PC Electricity Cost are identical in this repository, so one copy is sufficient.

---

## Credits and license

This repository contains custom JARVIS plugin work and integrations. Some individual plugins retain their original author and license notices in their source files. Preserve those notices when copying or redistributing code.

See [LICENSE](LICENSE) for the repository license and the source headers for plugin-specific attribution.
