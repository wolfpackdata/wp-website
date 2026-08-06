It’s up!

SetMaster 3.0.4 is officially live, installation is now drag-and-drop for both platforms.

Explore, compare, and prep your music library without ever writing to Traktor’s `collection.nml`. It's your set prep copilot. Less scrolling, more mixing.

A few of my favorite features:

→ **Track–playlist matrix:** compound filters across BPM, key, release year, and playlist membership together, which Traktor® itself does not offer.

→ **Playlist comparison:** uncover shared tracks, overlaps, and connections between different set ideas.

→ **Treasure hunting:** rediscover great music buried inside years of playlists.

→ **Turbocharged set prep:** filter and search your library by key, BPM, release date, and more... ALL AT ONCE to find mashups and perfect transitions.

→ **Local-first architecture:** your Traktor collection stays on your machine.

The track–playlist matrix alone saves me an absurd amount of preparation time. Digging through my own collection is a new level of fun—which is how “I’ll prepare a quick set” becomes a three-hour archaeological expedition through music -- all in tune.

I wanted to build an application that wasn’t fintech or business-focused—to learn new skills, get outside my comfort zone, and produce a product I really needed at the same time.

A bonus aspect is hours of user testing means hours of DJing.

One of the biggest engineering challenges was packaging a local Python application so it felt like an actual desktop product—not a Python project asking the user to install six dependencies and believe in themselves.

The Mac release now ships as a proper drag-and-drop DMG with its own bundled Python runtime. It is signed with Wolfpack's Apple Developer ID, so macOS Gatekeeper can verify it during installation.

Underneath the installer is a local Python application with a browser-based interface, deliberately read-only Traktor integration, and an automated test suite covering the core workflows.

Claude and Codex were both heavily involved throughout the development process: architecture, implementation, debugging, testing, packaging, documentation, and crushing through issues.

SetMaster 3 grew out of my love for Traktor, software development, and the satisfaction of building exactly the tool I wanted to use while tuning my AI architecture toolset.

The full technical write-up is on the Wolfpack website. You can also download the application and browse the open-source repository on the Wolfpack GitHub, linked from the site.

I've done a ton of testing on Windows, but less Mac testing so let me know your bugs and enhancement ideas.

Happy SetMastering.