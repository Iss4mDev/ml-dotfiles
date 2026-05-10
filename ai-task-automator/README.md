# AI Task Automator

This is a collection of Python tools I put together to handle the repetitive parts of my day. It's got a file organizer to keep my workspace from becoming a mess and a quick sentiment checker to gauge the "vibe" of any text I throw at it.

## What it Does
- **Smart File Organizer:** It looks at your files and automatically moves them into folders like `Docs`, `Pics`, or `DevStuff` based on their extensions.
- **Vibe Checker:** A simple rule-based sentiment analyzer that tells you if a piece of text feels positive, negative, or just neutral.

## Built With
- **Python 3**
- `os` & `shutil` for moving files around.
- `re` for cleaning up text during analysis.
- `pathlib` for modern, reliable path handling.

## How to Use It

### 1. Get the Code
```bash
git clone https://github.com/Iss4mDev/issam-soubra-portfolio.git
cd issam-soubra-portfolio/ai-task-automator
```

### 2. Run the Script
```bash
python3 ai_task_automator.py
```

## Code Snippet
Here's how you can use the `MyHelper` class in your own scripts:

```python
from ai_task_automator import MyHelper

# Initialize the helper for the current directory
me = MyHelper('.')

# Check the sentiment of some text
text = "This project is coming along great!"
print(f"Vibe: {me.check_the_vibe(text)}")

# Uncomment to actually organize your files
# me.clean_my_folder()
```

---
**Author:** Issam Soubra
