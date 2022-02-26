from pathlib import Path

from cajparser import CAJParser

base_dir = Path.home() / 'Downloads'
for f in base_dir.glob('*.caj'):
    dst = f.parent / f'{f.stem}.pdf'
    if dst.exists():
        continue
    try:
        CAJParser(str(f)).convert(str(dst))
    except:
        print(f'Failed: {f.stem}')
        # raise
