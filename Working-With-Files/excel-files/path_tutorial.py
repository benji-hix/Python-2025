import os
from pathlib import Path
from pydoc import doc

# pathlip represents file paths as objects rather than str
# for p in Path().iterdir():
#     print(p)

documents = Path.home() / 'code'

print('\n')

print(documents)
for p in documents.rglob("*2025*", case_sensitive=False):
    print(p)

print('\n')