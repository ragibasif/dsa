#!/usr/bin/env python3

import os
import sys
import shutil

TEMPLATE_FILE = "template.cpp"
README_FILE = "README.md"

def update_readme():
    categories = {}
    total_problems = 0
    
    # Scan directories, ignoring hidden ones and the script itself
    dirs = [d for d in os.listdir('.') if os.path.isdir(d) and not d.startswith('.')]
    
    for cat in sorted(dirs):
        files = [f for f in os.listdir(cat) if f.endswith('.cpp')]
        if files:
            categories[cat] = sorted(files)
            total_problems += len(files)

    with open(README_FILE, "w") as f:
        f.write("# CSES Problem Set Solutions\n\n")
        f.write(f"**Total Problems Solved: {total_problems}**\n\n")
        
        for cat, files in categories.items():
            f.write(f"### {cat.replace('_', ' ')}\n")
            f.write("| Problem | Solution Link |\n")
            f.write("| :--- | :--- |\n")
            for file in files:
                prob_name = file.replace('.cpp', '').replace('_', ' ')
                f.write(f"| {prob_name} | [Solution](./{cat}/{file}) |\n")
            f.write("\n")
    print("README.md updated!")

def create_problem(category, name):
    cat_folder = category.replace(" ", "_")
    formatted_name = name.replace(" ", "_")
    
    if not os.path.exists(cat_folder):
        os.makedirs(cat_folder)

    file_path = os.path.join(cat_folder, f"{formatted_name}.cpp")

    if not os.path.exists(file_path):
        shutil.copy(TEMPLATE_FILE, file_path)
        print(f"Created: {file_path}")
        update_readme() # Only update README when a new file is created
    else:
        print(f"File {file_path} already exists.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 solve.py <Category> <ProblemName>")
    else:
        create_problem(sys.argv[1], sys.argv[2])
