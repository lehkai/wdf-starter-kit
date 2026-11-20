#!/usr/bin/env python3
"""Validate repository structure only, not human gates or feature content."""
from pathlib import Path
import re
import json
ROOT=Path(__file__).resolve().parents[1]
REQUIRED=[
 'README.md','AGENTS.md','SETUP-GUIDE.md','CHANGELOG.md',
 'docs/01-vision.md','docs/02-requirements.md','docs/03-architecture.md',
 'docs/06-test-results.md','docs/07-monitoring.md','docs/08-improvements.md',
 'templates/feature-plan.md','templates/plan-review.md','templates/build-review.md',
 'templates/roles-and-authority.md','templates/feature-lifecycle.md','templates/gates.md',
 'prompts/01-onboarding.md','prompts/10-feature-define.md','prompts/11-plan-review.md',
 'prompts/12-build-review.md','scripts/new_feature.py',
 'CONTRIBUTING.md','docs/collaboration.md','docs/team-roles.md',
 'docs/definition-of-done.md','docs/security-and-access.md',
 '.wdf/config.json','.github/CODEOWNERS',
 'scripts/configure_mode.py','MIGRATION-v1.1-to-v1.2.md',
]
def validate(root=ROOT):
 errors=[]
 for path in REQUIRED:
  p=root/path
  if not p.is_file() or not p.read_text(encoding='utf-8').strip():
   errors.append(f'Fehlend oder leer: {path}')
 cfg_path=root/'.wdf/config.json'
 if cfg_path.is_file():
  try:
   config=json.loads(cfg_path.read_text(encoding='utf-8'))
   if config.get('schema_version')!='1.2': errors.append('WDF config schema_version muss 1.2 sein')
   if config.get('mode') not in ('solo','team','factory'): errors.append('Ungültiger WDF Mode')
   if config.get('human_release_approval') is not True: errors.append('human_release_approval muss true bleiben')
  except (json.JSONDecodeError,UnicodeDecodeError) as exc:
   errors.append(f'Ungültige .wdf/config.json: {exc}')
 ids={}
 for p in sorted((root/'plans').glob('F-*.md')):
  if not re.fullmatch(r'F-[0-9]{3,6}-[a-z0-9]+(?:-[a-z0-9]+)*\.md',p.name):
   errors.append(f'Ungültiger Plan-Dateiname: {p.name}')
   continue
  id=p.name.split('-')[0]+'-'+p.name.split('-')[1]
  if id in ids: errors.append(f'Doppelte Feature-ID: {id} ({ids[id]} und {p.name})')
  ids[id]=p.name
  content=p.read_text(encoding='utf-8')
  if f'feature_id: "{id}"' not in content:errors.append(f'ID im Frontmatter stimmt nicht: {p.name}')
  for heading in ['## 4. Acceptance Criteria','## 8. Implementation Notes','## 9. What to Test','## 11. QA & Human Acceptance','## Status History']:
   if heading not in content:errors.append(f'Überschrift fehlt in {p.name}: {heading}')
 return errors
if __name__=='__main__':
 issues=validate()
 if issues:
  print('\n'.join('FEHLER: '+x for x in issues));raise SystemExit(1)
 print('OK – WDF-Struktur (Schema 1.2) geprüft. Keine Prüfung inhaltlicher Qualität oder menschlicher Freigaben.')
