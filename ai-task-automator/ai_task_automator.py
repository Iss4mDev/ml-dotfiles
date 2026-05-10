"""
Automating the Boring Stuff: A Personal Task Assistant
Created by Issam Soubra

This script is a collection of tools I built to handle repetitive tasks. 
It includes a file organizer to keep my workspace clean and a quick 
sentiment checker for processing text snippets.
"""

import os
import shutil
import re
from pathlib import Path

class TaskAssistant:
    """
    A handy class to manage local file organization and text analysis.
    """
    def __init__(self, target_dir):
        self.target_dir = Path(target_dir)
        # Grouping files by their common types
        self.file_groups = {
            'Documents': ['.pdf', '.docx', '.txt', '.md', '.pptx'],
            'Images': ['.jpg', '.jpeg', '.png', '.gif', '.svg'],
            'Development': ['.py', '.java', '.cpp', '.html', '.css', '.js', '.json'],
            'Spreadsheets': ['.csv', '.xlsx', '.tsv']
        }

    def tidy_up_directory(self):
        """
        Scans the directory and moves files into categorized folders.
        It's a simple way to keep things from getting cluttered.
        """
        if not self.target_dir.exists():
            print(f"Oops! The directory '{self.target_dir}' doesn't seem to exist.")
            return

        print(f"Cleaning up: {self.target_dir.absolute()}")
        
        for item in self.target_dir.iterdir():
            if item.is_file():
                # Skip the script itself if it's in the same folder
                if item.name == os.path.basename(__file__):
                    continue
                    
                extension = item.suffix.lower()
                destination_folder = 'Miscellaneous'
                
                for folder_name, extensions in self.file_groups.items():
                    if extension in extensions:
                        destination_folder = folder_name
                        break
                
                dest_path = self.target_dir / destination_folder
                dest_path.mkdir(exist_ok=True)
                
                try:
                    shutil.move(str(item), str(dest_path / item.name))
                    print(f"Moved: {item.name} -> {destination_folder}/")
                except Exception as e:
                    print(f"Could not move {item.name}: {e}")

    def quick_sentiment_check(self, text):
        """
        A straightforward way to gauge the 'vibe' of a piece of text.
        It looks for specific keywords to decide if the tone is positive or negative.
        """
        # Just a basic list of words to look for
        pos_vibes = {'good', 'great', 'excellent', 'happy', 'positive', 'success', 'awesome', 'love'}
        neg_vibes = {'bad', 'poor', 'terrible', 'sad', 'negative', 'failure', 'hate', 'awful'}

        # Clean up the text and split into words
        words = re.findall(r'\w+', text.lower())
        
        score = 0
        for word in words:
            if word in pos_vibes:
                score += 1
            elif word in neg_vibes:
                score -= 1

        if score > 0:
            return "Positive"
        elif score < 0:
            return "Negative"
        return "Neutral"

if __name__ == "__main__":
    # Quick test run
    assistant = TaskAssistant('.') 
    
    test_phrase = "I'm really impressed with how this project is coming along!"
    result = assistant.quick_sentiment_check(test_phrase)
    
    print(f"Checking text: \"{test_phrase}\"")
    print(f"Result: {result}")
    
    # Uncomment the line below to actually organize your files
    # assistant.tidy_up_directory()
