from pathlib import Path

from cajparser import CAJParser

base_dir = Path.home() / 'Downloads'
for f in base_dir.glob('*.caj'):
    dst = f.parent / f'{f.stem}.pdf'
    if dst.exists():
        continue
    print(f'Processing: {f.stem}')
    try:
        CAJParser(str(f)).convert(str(dst))
        print(f'Processed: {f.stem}')
    except:
        print(f'Failed: {f.stem}')
        # raise
