"""
plugins/spotify_control.py — Universal Spotify and Media Playback Control for JARVIS.

Controls music and media playback across Spotify, browser streams (YouTube Music, Soundcloud),
Apple Music, and media players using Windows virtual media keys and Spotify URI hooks.
"""
from __future__ import annotations

import os
import platform
import subprocess
import sys
import time
import urllib.parse

_OS = platform.system()

# Windows Virtual Key Codes for Media and Volume control
_VK_MEDIA_NEXT_TRACK  = 0xB0
_VK_MEDIA_PREV_TRACK  = 0xB1
_VK_MEDIA_STOP        = 0xB2
_VK_MEDIA_PLAY_PAUSE  = 0xB3
_VK_VOLUME_MUTE       = 0xAD
_VK_VOLUME_DOWN       = 0xAE
_VK_VOLUME_UP         = 0xAF

PLUGIN = {
    "name": "spotify_control",
    "label": "Spotify & Media",
    "level": "basic",
    "summary": "Controls Spotify and system media playback: play, pause, next, previous, search, and volume.",
    "setup": [
        "Works out of the box with Spotify, YouTube Music, and any active media player.",
        "Say: 'Jarvis, play music', 'pause the song', 'next track', 'play Daft Punk on Spotify'.",
    ],
    "description": (
        "Controls music and media playback on the computer (Spotify, Apple Music, YouTube Music, web audio). "
        "Use this tool whenever the user asks to play, pause, stop, resume, skip, go to previous track, "
        "search on Spotify, or adjust media playback. "
        "Actions: 'play_pause' (toggle), 'play' (resume/start), 'pause' (stop playback), 'next' (skip song), "
        "'previous' (replay or previous song), 'search_play' (search an artist, album, or song on Spotify), "
        "'open_spotify' (launch the Spotify application), 'volume_up', 'volume_down', 'mute'."
    ),
    "brief": "Control Spotify and background music playback (play, pause, skip, search, volume).",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "action": {
                "type": "STRING",
                "enum": [
                    "play_pause", "play", "pause", "next", "previous",
                    "search_play", "open_spotify", "volume_up", "volume_down", "mute",
                    "status"
                ],
                "description": "The media playback action to perform."
            },
            "query": {
                "type": "STRING",
                "description": "For 'search_play': the artist, track, album, or playlist name to search on Spotify."
            }
        },
        "required": ["action"]
    }
}

PLUGIN_SETTINGS = {
    "namespace": "spotify_control",
    "title": "🎵  SPOTIFY & MEDIA CONTROL",
    "fields": [
        {
            "key": "prefer_desktop_app",
            "label": "Prefer Spotify Desktop application when searching",
            "type": "toggle",
            "default": True
        }
    ]
}


def _send_win_media_key(vk_code: int) -> bool:
    """Send a virtual media key event on Windows using ctypes."""
    try:
        import ctypes
        user32 = ctypes.windll.user32
        # KEYEVENTF_KEYUP = 2
        user32.keybd_event(vk_code, 0, 0, 0)
        time.sleep(0.04)
        user32.keybd_event(vk_code, 0, 2, 0)
        return True
    except Exception:
        return False


def _send_media_fallback(action: str) -> bool:
    """Fallback media key dispatch using pyautogui or os commands."""
    try:
        import pyautogui
        key_map = {
            "play_pause": "playpause",
            "play": "playpause",
            "pause": "playpause",
            "next": "nexttrack",
            "previous": "prevtrack",
            "volume_up": "volumeup",
            "volume_down": "volumedown",
            "mute": "volumemute"
        }
        if action in key_map:
            pyautogui.press(key_map[action])
            return True
    except Exception:
        pass

    if _OS == "Darwin":
        cmd_map = {
            "play_pause": "tell application \"Spotify\" to playpause",
            "next": "tell application \"Spotify\" to next track",
            "previous": "tell application \"Spotify\" to previous track",
            "pause": "tell application \"Spotify\" to pause",
            "play": "tell application \"Spotify\" to play"
        }
        if action in cmd_map:
            try:
                subprocess.run(["osascript", "-e", cmd_map[action]], check=False, timeout=3)
                return True
            except Exception:
                pass

    return False


def _is_spotify_running() -> bool:
    """Check if Spotify process is currently active."""
    try:
        import psutil
        for p in psutil.process_iter(["name"]):
            name = (p.info.get("name") or "").lower()
            if "spotify" in name:
                return True
    except Exception:
        pass
    return False


def _open_spotify_uri(uri: str = "spotify:") -> bool:
    """Open Spotify URI protocol on Windows / macOS / Linux."""
    try:
        if _OS == "Windows":
            os.startfile(uri)  # type: ignore
            return True
        elif _OS == "Darwin":
            subprocess.Popen(["open", uri])
            return True
        else:
            subprocess.Popen(["xdg-open", uri])
            return True
    except Exception:
        return False


def run(parameters: dict, player=None, session_memory=None) -> str:
    p = parameters or {}
    action = str(p.get("action") or "play_pause").strip().lower()
    query = str(p.get("query") or "").strip()

    try:
        if action in ("open_spotify",):
            _open_spotify_uri("spotify:")
            return "Opened Spotify for you, sir."

        if action == "search_play":
            if not query:
                _open_spotify_uri("spotify:")
                return "Opened Spotify, sir."
            encoded = urllib.parse.quote(query)
            # spotify:search:<encoded> will open Spotify and navigate to search
            ok = _open_spotify_uri(f"spotify:search:{encoded}")
            if ok:
                # brief pause then press play/enter if needed
                time.sleep(1.0)
                if _OS == "Windows":
                    _send_win_media_key(_VK_MEDIA_PLAY_PAUSE)
                return f"Searching and playing '{query}' on Spotify, sir."
            return f"I opened Spotify search for '{query}'."

        if action in ("play_pause", "play", "pause"):
            spotify_active = _is_spotify_running()
            if not spotify_active and action in ("play", "play_pause"):
                # If Spotify is not open, launch it
                _open_spotify_uri("spotify:")
                time.sleep(1.2)
                if _OS == "Windows":
                    _send_win_media_key(_VK_MEDIA_PLAY_PAUSE)
                return "Started Spotify and initiated playback, sir."

            if _OS == "Windows":
                _send_win_media_key(_VK_MEDIA_PLAY_PAUSE)
            else:
                _send_media_fallback("play_pause")

            if action == "pause":
                return "Media playback paused, sir."
            elif action == "play":
                return "Resumed media playback, sir."
            return "Toggled media playback, sir."

        if action == "next":
            if _OS == "Windows":
                _send_win_media_key(_VK_MEDIA_NEXT_TRACK)
            else:
                _send_media_fallback("next")
            return "Skipped to the next track, sir."

        if action == "previous":
            if _OS == "Windows":
                _send_win_media_key(_VK_MEDIA_PREV_TRACK)
            else:
                _send_media_fallback("previous")
            return "Returned to the previous track, sir."

        if action == "volume_up":
            if _OS == "Windows":
                for _ in range(3):
                    _send_win_media_key(_VK_VOLUME_UP)
            else:
                _send_media_fallback("volume_up")
            return "Turned the volume up, sir."

        if action == "volume_down":
            if _OS == "Windows":
                for _ in range(3):
                    _send_win_media_key(_VK_VOLUME_DOWN)
            else:
                _send_media_fallback("volume_down")
            return "Turned the volume down, sir."

        if action == "mute":
            if _OS == "Windows":
                _send_win_media_key(_VK_VOLUME_MUTE)
            else:
                _send_media_fallback("mute")
            return "Muted or unmuted system audio, sir."

        if action in ("status", "now_playing"):
            running = _is_spotify_running()
            if running:
                return "Spotify is currently running on your system, sir."
            return "Spotify is not running at the moment, sir."

        return f"Unknown media action '{action}'."

    except Exception as e:
        return f"Media control encountered an error: {e}"
