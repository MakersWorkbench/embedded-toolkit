#!/usr/bin/env python3
"""Copy the tool from the repository root into the Drupal module's assets folder.

Run from anywhere:  python scripts/sync_drupal_module.py
"""
import shutil
from pathlib import Path

root = Path(__file__).resolve().parent.parent
assets = root / 'drupal' / 'tmwb_embedded_toolkit' / 'assets'
(assets / 'js').mkdir(parents=True, exist_ok=True)
(assets / 'images').mkdir(parents=True, exist_ok=True)

copied = []
shutil.copy2(root / 'emb.css', assets / 'emb.css'); copied.append('emb.css')
for js in sorted((root / 'js').glob('*.js')):
    shutil.copy2(js, assets / 'js' / js.name); copied.append('js/' + js.name)
for name in ('LICENSE', 'NOTICE'):
    shutil.copy2(root / name, assets / name); copied.append(name)
shot = root / 'images' / 'toolkit-overview.png'
if shot.exists():
    shutil.copy2(shot, assets / 'images' / 'toolkit-overview.png'); copied.append('images/toolkit-overview.png')
print('Synced %d files into %s' % (len(copied), assets.relative_to(root)))
for c in copied:
    print('  ', c)
