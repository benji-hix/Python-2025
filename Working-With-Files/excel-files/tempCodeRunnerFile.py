import os
from pathlib import Path

# pathlip represents file paths as objects rather than str

print('\n')

current_dir = Path().resolve()
target_dir = current_dir.parent
new_dir = target_dir / 'path-manipulation'

print(f'| Current dir: \n| {current_dir.absolute()}')
print(f'| Target dir: \n| {target_dir.absolute()}')
print(f'| New directory path: \n| {new_dir.absolute()}')

new_dir.mkdir(exist_ok=False)

print('\n')