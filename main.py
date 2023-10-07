import os
from pathlib import Path

from caj2pdf.cajparser import CAJParser


def main():
    base_dirs = (
        Path.home() / 'Downloads',
        Path('D:/E-StudyData'),
    )
    files = [Path(r) / f for b in base_dirs for r, _, fs in os.walk(b) for f in fs]
    files = [f for f in files if f.suffix == '.caj']
    for file in files:
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


if __name__ == '__main__':
    main()
