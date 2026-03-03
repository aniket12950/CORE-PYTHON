"""
Project: Slug Generator
Description: Converts a title into a URL-friendly slug
"""

import re

def generate_slug(title):
    title = title.lower().strip()
    title = re.sub(r'[^a-z0-9\s]', '', title)
    slug = re.sub(r'\s+', '-', title)
    
    return slug


def main():
    title = input("Enter title: ")
    slug = generate_slug(title)
    print("Generated Slug:", slug)


if __name__ == "__main__":
    main()