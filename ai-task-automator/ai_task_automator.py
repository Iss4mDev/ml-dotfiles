# ---------------------------------------------------------
# My Personal Task Automator
# Written by: Issam Soubra
# ---------------------------------------------------------
# I got tired of manually moving files around and checking text vibes,
# so I threw this together. It's not perfect, but it works for me.
# ---------------------------------------------------------

import os
import shutil
import re
from pathlib import Path

class MyHelper:
    def __init__(self, folder_to_fix):
        # Setting up where we want to work
        self.work_dir = Path(folder_to_fix)
        
        # Just a map of what goes where
        self.my_groups = {
            'Docs': ['.pdf', '.docx', '.txt', '.md', '.pptx'],
            'Pics': ['.jpg', '.jpeg', '.png', '.gif', '.svg'],
            'DevStuff': ['.py', '.java', '.cpp', '.html', '.css', '.js', '.json'],
            'Sheets': ['.csv', '.xlsx', '.tsv']
        }

    def clean_my_folder(self):
        # Make sure the folder actually exists first lol
        if not self.work_dir.exists():
            print(f"Wait, I can't find '{self.work_dir}'. Check the path again?")
            return

        print(f"Alright, cleaning up: {self.work_dir.resolve()}")
        
        for thing in self.work_dir.iterdir():
            # We only care about files, not other folders
            if thing.is_file():
                # Don't move this script if it's in the same spot
                if thing.name == os.path.basename(__file__):
                    continue
                    
                ext = thing.suffix.lower()
                where_to_put_it = 'Other'
                
                # Figure out which folder it belongs in
                for folder, extensions in self.my_groups.items():
                    if ext in extensions:
                        where_to_put_it = folder
                        break
                
                target_path = self.work_dir / where_to_put_it
                target_path.mkdir(exist_ok=True)
                
                try:
                    shutil.move(str(thing), str(target_path / thing.name))
                    print(f"Moved {thing.name} -> {where_to_put_it}/")
                except Exception as err:
                    print(f"Dang, couldn't move {thing.name}: {err}")

    def check_the_vibe(self, some_text):
        # Just a quick way to see if text is positive or negative
        # I just picked some common words that pop up
        good_words = {'good', 'great', 'excellent', 'happy', 'positive', 'success', 'awesome', 'love', 'nice'}
        bad_words = {'bad', 'poor', 'terrible', 'sad', 'negative', 'failure', 'hate', 'awful', 'sucks'}

        # Strip out the junk and look at the words
        clean_words = re.findall(r'\w+', some_text.lower())
        
        vibe_score = 0
        for w in clean_words:
            if w in good_words:
                vibe_score += 1
            elif w in bad_words:
                vibe_score -= 1

        if vibe_score > 0:
            return "Positive Vibe"
        if vibe_score < 0:
            return "Negative Vibe"
        return "Neutral / Hard to tell"

if __name__ == "__main__":
    # Just testing it out here
    me = MyHelper('.') 
    
    my_text = "Honestly, this new setup is pretty awesome. I love it!"
    vibe = me.check_the_vibe(my_text)
    
    print(f"Testing text: \"{my_text}\"")
    print(f"Vibe check: {vibe}")
    
    # If I want to actually run the cleaner, I'll uncomment this:
    # me.clean_my_folder()
