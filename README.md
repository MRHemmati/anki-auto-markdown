# Auto Markdown (Modernized for Anki 23.x - 25.x+)

This is a fully modernized and refactored version of the classic "Auto Markdown" add-on. It has been rewritten from scratch to support modern Anki's editor backend (Svelte + Shadow DOM) and is fully compatible with Anki 23.x, 24.x, and 25.x+.

## Features

- **Automated Markdown Rendering:** Type your notes in markdown. The add-on automatically renders them into styled HTML when the field loses focus.
- **Seamless Editing:** Click back into any rendered field to automatically restore your raw markdown syntax (e.g. `**bold**`, `*italics*`, lists, links).
- **No Monkey Patching:** Rewritten using official `aqt.gui_hooks` APIs to guarantee editor stability and compatibility with future Anki releases.
- **Safe State Storage:** Stores the original markdown draft in a hidden HTML span to ensure it is not stripped by Anki's strict HTML sanitizer.
- **Built-in Syntax Highlighting:** Bundled with Pygments and standard markdown extensions (Fenced Code, Footnotes, Tables, Abbreviation, Definition Lists, nl2br).

## Usage

1. Tag fields in your Note Type settings with **Auto-Markdown**.
2. Type raw markdown in those fields.
3. Switch fields or unfocus to render. Focus again to edit the raw markdown source.
4. Press the markdown toolbar button (or use the shortcut) to manually toggle formatting.
