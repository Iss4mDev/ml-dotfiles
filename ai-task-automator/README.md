# AI Task Automator

## Project Description

This project features a versatile Python script designed to automate common tasks by leveraging AI concepts. It includes functionalities for intelligent file organization and basic sentiment analysis for text processing.

## Features

*   **Intelligent File Organization:** Automatically sorts files into categorized subfolders based on their extensions (e.g., Documents, Images, Code, Data, Others).
*   **Basic Sentiment Analysis:** Performs rule-based sentiment analysis on text inputs, classifying them as Positive, Negative, or Neutral.

## Technologies Used

*   Python
*   `os` module for file system operations
*   `shutil` module for high-level file operations
*   `re` module for regular expressions (used in sentiment analysis)

## How to Use

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Iss4mDev/ml-dotfiles.git
    cd ml-dotfiles
    ```

2.  **Run the script:**

    ```bash
    python3 ai_task_automator.py
    ```

    *Note: The example usage in the `if __name__ == "__main__":` block demonstrates both file organization (commented out) and sentiment analysis.*

## Example

```python
if __name__ == "__main__":
    # Example usage
    # To organize files in a directory:
    # automator = TaskAutomator("/path/to/your/directory")
    # automator.organize_files()
    
    # To perform sentiment analysis:
    automator = TaskAutomator(".") # Using current directory for demonstration
    sample_text = "The new AI model is great and has achieved significant success!"
    sentiment = automator.basic_sentiment_analysis(sample_text)
    print(f"Sentiment of \'{sample_text}\': {sentiment}")
```

## Author

Issam Soubra
