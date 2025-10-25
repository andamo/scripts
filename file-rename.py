#!/usr/bin/env python3
import os
import sys

def rename_items(path, old_char, new_char, dry_run=False):
    # Walk bottom-up so directories get renamed after their contents
    for root, dirs, files in os.walk(path, topdown=False):
        # Rename files
        for name in files:
            if old_char in name:
                old_path = os.path.join(root, name)
                new_name = name.replace(old_char, new_char)
                new_path = os.path.join(root, new_name)
                if dry_run:
                    print(f"[DRY-RUN] Would rename file: {old_path} -> {new_path}")
                else:
                    os.rename(old_path, new_path)
                    print(f"Renamed file: {old_path} -> {new_path}")

        # Rename directories
        for name in dirs:
            if old_char in name:
                old_path = os.path.join(root, name)
                new_name = name.replace(old_char, new_char)
                new_path = os.path.join(root, new_name)
                if dry_run:
                    print(f"[DRY-RUN] Would rename dir:  {old_path} -> {new_path}")
                else:
                    os.rename(old_path, new_path)
                    print(f"Renamed dir:  {old_path} -> {new_path}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python3 rename_chars.py <path> <old_char> <new_char> [--dry-run]")
        sys.exit(1)

    path = sys.argv[1]
    old_char = sys.argv[2]
    new_char = sys.argv[3]
    dry_run = "--dry-run" in sys.argv

    if not os.path.isdir(path):
        print(f"Error: {path} is not a valid directory.")
        sys.exit(1)

    rename_items(path, old_char, new_char, dry_run=dry_run)
