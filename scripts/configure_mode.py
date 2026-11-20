#!/usr/bin/env python3
"""Set WDF collaboration mode in local config only; does not configure GitHub."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODES = {'solo', 'team', 'factory'}

def configure(mode, root=ROOT):
    if mode not in MODES:
        raise ValueError(f'Unknown WDF mode: {mode}')
    target = root / '.wdf' / 'config.json'
    cfg = json.loads(target.read_text(encoding='utf-8'))
    cfg['mode'] = mode
    cfg['schema_version'] = '1.2'
    target.write_text(json.dumps(cfg, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    return target

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description='WDF Solo/Team/Factory Modus lokal setzen.')
    parser.add_argument('mode',choices=sorted(MODES))
    args=parser.parse_args()
    path=configure(args.mode)
    print(f'Mode auf {args.mode} gesetzt: {path.relative_to(ROOT)}')
    if args.mode != 'solo':
        print('WICHTIG: Team-Reviews, CODEOWNERS, Rulesets und CI separat in GitHub einrichten. Diese Einstellung aktiviert keinen Schutz.')
