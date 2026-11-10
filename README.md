# Music Assistant Mobile app

*Please note: that this project is still under (heavy) development and not yet in a production state or published to any of the app stores. Development work is in progress to allow this project to become the official mobile app for the Music Assistant project.*

The (official) Music Assistant Mobile app is a cross-platform client application designed for Android and iOS. Developed using Kotlin Multiplatform (KMP) and Compose Multiplatform frameworks, this project aims to provide a unified codebase for seamless music management across mobile platforms.

## iOS 16 experimental: Simplified Chinese and synced lock-screen lyrics

- This feature branch targets iOS 16; upstream platform requirements below remain unchanged.
- Simplified Chinese covers every default Compose resource (including options, accessibility labels and errors). Song names, artist names, server-generated options and provider content remain as supplied by the server. Run `python3 scripts/check-zh-resources.py` to validate keys, plural quantities, printf arguments and escaped whitespace.
- Settings → Misc → **Lock screen synced lyrics** (设置 → 其他选项 → 锁屏同步歌词) is enabled by default and can be disabled. Only the local player's timestamped LRC is used. The current nonblank line replaces the system media title, and the subtitle shows the original song title and artist. Unsynced/plain lyrics, introductions before the first timestamp and blank LRC lines retain the original metadata.
- **The same system Now Playing title is used by the lock screen, Control Center and CarPlay**; iOS does not expose a separate public lock-screen lyric field. Disable the option to keep original titles on every surface. This is line-level title substitution, not Apple Music's full-screen/word-level lyrics UI.
- Lyrics follow `PlayerPositionTracker` (including pause/seek); state is identity-stamped before crossing the KMP bridge, and only `NowPlayingInfoStore` publishes the assembled dictionary. Missing embedded lyrics trigger one repository lookup per cached track, including negative results; the bounded 64-track cache is cleared on connection reset. There is no network polling.
- The unsigned build deliberately does not request Siri authorization during app initialization; it does not claim a Siri entitlement or bypass permission checks.
- Physical-device lock-screen/background timing, CarPlay appearance and Siri behavior require device validation; source-level tests do not establish those runtime outcomes.

## Features

*Disclaimer: This app is not intended to provide offline playback*

- All platforms:
  - managing MA players queues and playback;
  - managing dynamic and static groups (no static group creation);
  - local playback on device from MA library (Sendspin streaming protocol over WebRTC or WebSocket);
  - comprehensive Settings screen with section-based UI for server connection, authentication (builtin/OAuth), and local player configuration.
- Android-specific:
  - requires Android 9 or later; 
  - media service (background playback) and media notification in system area for quick access to players controls;
  - Android Auto support for the built-in player, plus voice playback ("Hey Google, play *X* on Music Assistant") via Google Assistant and Gemini App Actions — works in the car *and* on the phone, single symmetric code path. Full phrase reference, architecture notes and testing in [ANDROID-AUTO.md](docs/ANDROID-AUTO.md).
- iOS-specific:
  - requires iOS 18.5 or later; 
  - native audio playback via AudioQueue (CoreAudio) with support for FLAC, Opus, and PCM;
  - Lock Screen and Control Center integration (Now Playing info, play/pause/next/prev remote commands);
  - background audio playback with automatic resume after phone call or Siri interruptions;
  - WebRTC data channel transport for low-latency Sendspin streaming;
  - Apple CarPlay support for built-in player (very early state, a lot of bugs are expected);
  - *known issue:* artwork may be missing in certain setups, for example peer-to-peer mesh VPN setups such as Tailscale. We're aware of this and looking into it, but we don't have an ETA on a fix yet.
    - Why: iOS App Transport Security (ATS) blocks image requests to insecure hosts, with an exception for local networks. On your LAN, artwork loads fine, but over Tailscale and similar VPNs the server appears to the phone as a remote host, so ATS kicks in and blocks the requests.

### Server compatibility

Releases of the Music Assistant Mobile App are intended to support the latest [Music Assistant Server](https://github.com/music-assistant/server) stable versions.

### Design goals

The goal of this app is to provide an iOS and Android native feeling experience for playing and controlling audio via Music Assistant on both Android/iOS phones and tablets. This means that as well as making it easy to navigate the MA library and sources, this shouldn't come at the expense of being able to quickly control players. Specifically, these actions should be available as quickly as possible when opening the app in pretty much any state:

- See what's playing on the app's current player
- Change the current player
- Play/pause current player
- Transfer playback to another player
- Group current player with another player
- Navigate to "global" (across all sources) search
- Return to home screen
- Skip to next track
- Start browsing library
- Open settings

The app's built-in Local player is designed to be a private player for a personal music experience. It plays music on your device, for you, while you're using it. This is different from the many other players Music Assistant supports, like speakers, that stay on and available all the time. The app's Local player isn't meant to be one of those, and by default you can't find it or control it from other apps.

Compatibility with Apple CarPlay and Android Auto is a core focus, ensuring you can enjoy your music easily and safely through your car’s infotainment system. These in-car experiences are dedicated exclusively to the local player; managing external players is out of scope.

In addition, there's some general design directions that are being observed:

- Optimize for searching/filtering/drilling-down to smaller lists of items over large list navigation
- Keep customization settings as close to the place they affect over maintaining a "centralized" or "global" set of customization settings

## Want to try it?

Android users can download the APK [for the latest release](https://github.com/music-assistant/mobile-app/releases).

iOS users can join [TestFlight](https://testflight.apple.com/join/AkvSDf2z).

### Configuring and using the app

For information on configuring and using the Music Assistant Mobile app, see the [App Documentation](docs/app-documentation/index.md).

## Android Auto & Google Assistant

See [ANDROID-AUTO](docs/ANDROID-AUTO.md) for:

- enabling Android Auto with sideloaded debug/self-signed builds (Unknown sources flow);
- the library browsing layout on the head unit;
- the full list of supported Google Assistant voice phrases (works in the car *and* on the phone);
- shell-based testing of `MEDIA_PLAY_FROM_SEARCH` intents;
- known limitations.

---

[![A project from the Open Home Foundation](https://www.openhomefoundation.org/badges/ohf-project.png)](https://www.openhomefoundation.org/)
