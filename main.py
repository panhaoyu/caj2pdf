import os
from pathlib import Path

from cajparser import CAJParser

for base_dir in (
        Path.home() / 'Downloads',
        Path('D:/E-StudyData'),
):
    for root, sub_dirs, sub_files in os.walk(base_dir):
        root = Path(root)
        for file in sub_files:
            file = root / file
            dst = file.parent / f'{file.stem}.pdf'
            if dst.exists():
                continue
            print(f'Processing: {file.stem}')
            try:
                CAJParser(str(file)).convert(str(dst))
                print(f'Processed: {file.stem}')
            except:
                print(f'Failed: {file.stem}')
                # raise
