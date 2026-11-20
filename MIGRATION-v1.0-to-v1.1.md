# Upgrade WDF v1.0 → v1.1

> Für bereits bestehende GitHub-Repositories. **Nicht blind alle Dateien ersetzen.** Ein Git-Branch und Diff sind Pflicht; nutze zunächst eine lokale Kopie.

## 1. Sichern und Upgrade-Branch

```bash
cd ~/Projects/DEIN-WDF-REPO
git status
git switch -c chore/wdf-upgrade-v1.1
```

Falls `git status` nicht sauber ist: Änderungen vorher bewusst committen oder separat sichern, nicht überschreiben.

## 2. Aus dem v1.1-ZIP übernehmen

**Neu ergänzen (sofern nicht vorhanden):**
- `templates/feature-plan.md`, `templates/plan-review.md`, `templates/build-review.md`
- `templates/feature-lifecycle.md`, `templates/roles-and-authority.md`
- `scripts/new_feature.py`, `tests/test_wdf.py`
- `prompts/10-feature-define.md` bis `prompts/14-status-triage.md`
- `CHANGELOG.md`
- Verzeichnisse `plans/`, `reviews/` entstehen bei Verwendung, Beispiele liegen in `examples/`.

**Sorgfältig zusammenführen, nicht blind überschreiben:**
- `AGENTS.md` (neue Rollen, Status, Reviews, Sicherheit)
- `README.md`, `SETUP-GUIDE.md`, `templates/gates.md`
- `prompts/04-feature-implementation.md`, `prompts/06-test-acceptance.md`
- `.github/ISSUE_TEMPLATE/feature.yml`, `.github/pull_request_template.md`
- `.github/workflows/` (v1.0-Workflow ggf. entfernen/ersetzen, Dopplungen vermeiden)
- `scripts/check_wdf.py` (v1.1 auf neue Dateien ausgelegt)

**Bewahren:** vorhandene `docs/*.md`, echte Features, Commits, Branches, Issues, Projektboards und Geheimnisse außerhalb von Git.

## 3. Feature-Plan erzeugen

```bash
python3 scripts/new_feature.py F-001 erstes-feature
```

Für bestehende Features die IDs aus `docs/02-requirements.md` übernehmen. Niemals blind Status Accepted/Released übernehmen: vorhandene Nachweise und Freigaben prüfen.

## 4. Upgrade überprüfen

```bash
python3 scripts/check_wdf.py
python3 -m unittest discover -s tests -p 'test_*.py' -v
git diff --check
git diff --stat
```

### 5. Pull Request
1. Änderungen committen und Branch nach ausdrücklicher Entscheidung pushen.
2. PR eröffnen; AGENTS.md, Feature-Modell und GitHub Action besonders prüfen.
3. Erst nach Review mergen.

**Nicht automatisch:** Bestehende Projekte erhalten v1.1 nicht, nur weil das Master-Template aktualisiert wurde.
