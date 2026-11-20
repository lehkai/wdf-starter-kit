#!/usr/bin/env python3
"""Create a WDF feature plan without overwriting existing files (stdlib only)."""
import argparse
from datetime import date
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

def make_plan(feature_id, slug, *, root=ROOT, today=None):
    if not re.fullmatch(r"F-[0-9]{3,6}", feature_id):
        raise ValueError('Feature-ID muss F-001 (3–6 Ziffern) sein.')
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
        raise ValueError('Slug muss klein und kebab-case sein (z. B. trainings-anmeldung).')
    today = today or date.today().isoformat()
    target = root / 'plans' / f'{feature_id}-{slug}.md'
    existing = list((root/'plans').glob(f'{feature_id}-*.md'))
    if existing:
        raise FileExistsError(f'ID bereits belegt: {existing[0].name}')
    template = (root/'templates'/'feature-plan.md').read_text(encoding='utf-8')
    filled = (template.replace('{{FEATURE_ID}}',feature_id)
                .replace('{{FEATURE_TITLE}}',slug.replace('-',' ').title())
                .replace('{{CREATED}}',today))
    target.parent.mkdir(parents=True,exist_ok=True)
    with target.open('x',encoding='utf-8') as outfile:
        outfile.write(filled)
    return target

if __name__=='__main__':
    p=argparse.ArgumentParser(description='WDF Feature-Plan aus Vorlage erzeugen.')
    p.add_argument('feature_id',help='z. B. F-001')
    p.add_argument('slug',help='z. B. trainings-anmeldung')
    a=p.parse_args()
    try:
        print(f'Erstellt: {make_plan(a.feature_id,a.slug).relative_to(ROOT)}')
    except (ValueError,FileExistsError) as exc:
        p.error(str(exc))
