"""
AI-Powered Task Automator
Author: Issam Soubra
Description: A versatile Python script that leverages AI concepts to automate common tasks, 
such as intelligent file organization and basic sentiment analysis for text processing.
"""

import os
import shutil
import re

class TaskAutomator:
    def __init__(self, base_directory):
        self.base_directory = base_directory
        self.categories = {
            'Documents': ['.pdf', '.docx', '.txt', '.md'],
            'Images': ['.jpg', '.jpeg', '.png', '.gif'],
            'Code': ['.py', '.java', '.cpp', '.html', '.css'],
            'Data': ['.csv', '.json', '.xlsx']
        }

    def organize_files(self):
        """
        Intelligently organizes files in the base directory into subfolders based on their extensions.
        """
        print(f"Starting file organization in: {self.base_directory}")
        for filename in os.listdir(self.base_directory):
            file_path = os.path.join(self.base_directory, filename)
            if os.path.isfile(file_path):
                extension = os.path.splitext(filename)[1].lower()
                moved = False
                for category, extensions in self.categories.items():
                    if extension in extensions:
                        target_dir = os.path.join(self.base_directory, category)
                        os.makedirs(target_dir, exist_ok=True)
                        shutil.move(file_path, os.path.join(target_dir, filename))
                        print(f"Moved '{filename}' to '{category}'")
                        moved = True
                        break
                if not moved:
                    target_dir = os.path.join(self.base_directory, 'Others')
                    os.makedirs(target_dir, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_dir, filename))
                    print(f"Moved '{filename}' to 'Others'")

    def basic_sentiment_analysis(self, text):
        """
        A simple rule-based sentiment analysis to demonstrate text processing concepts.
        """
        positive_words = ['good', 'great', 'excellent', 'happy', 'positive', 'success']
        negative_words = ['bad', 'poor', 'terrible', 'sad', 'negative', 'failure']

        words = re.findall(r'\w+', text.lower())
        score = 0
        for word in words:
            if word in positive_words:
                score += 1
            elif word in negative_words:
                score -= 1

        if score > 0:
            return "Positive"
        elif score < 0:
            return "Negative"
        else:
            return "Neutral"

if __name__ == "__main__":
    # Example usage
    # automator = TaskAutomator('/path/to/your/directory')
    # automator.organize_files()
    
    automator = TaskAutomator('.') # Using current directory for demonstration
    sample_text = "The new AI model is great and has achieved significant success!"
    sentiment = automator.basic_sentiment_analysis(sample_text)
    print(f"Sentiment of '{sample_text}': {sentiment}")
