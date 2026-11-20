# Migration v1.1 → v1.2 (ohne Projektverlust)

> Bestehendes Projekt statt ZIP blind zu überschreiben. **Alle Schritte zuerst in einem Branch durchführen**.

1. `git status` prüfen; uncommittete Änderungen sichern. `git switch -c chore/wdf-v1.2`.
2. Backup bzw. Version der bisherigen `AGENTS.md`, `README.md`, `SETUP-GUIDE.md`, `.github/pull_request_template.md` und `scripts/check_wdf.py` sichern.
3. Neue Dateien übernehmen: `CONTRIBUTING.md`, `.wdf/config.json`, `docs/team-roles.md`, `docs/collaboration.md`, `docs/definition-of-done.md`, `docs/security-and-access.md`, `.github/CODEOWNERS`, `scripts/configure_mode.py`, `tests/test_collaboration.py`, `prompts/15-team-onboarding.md`, `prompts/16-team-feature-handoff.md`, `prompts/17-collaboration-review.md`, `MIGRATION-v1.1-to-v1.2.md`.
4. Bestehende Dateien **zusammenführen**, nicht blind ersetzen: `AGENTS.md`, `README.md`, `SETUP-GUIDE.md`, PR-Template, `templates/feature-plan.md`, `templates/feature-lifecycle.md`, `.github/ISSUE_TEMPLATE/feature.yml`, `scripts/check_wdf.py`, `CHANGELOG.md`.
5. Bestehende Projekt-Dokumente unter `docs/`, Features unter `plans/`, Reviews und Anwendungsquellcode **nicht überschreiben**. Bereits vorhandene Feature-Pläne können ohne Änderung fortgeführt werden; die v1.2-Collaboration-Felder werden bei Bedarf ergänzt.
6. Mode konfigurieren: `python3 scripts/configure_mode.py solo` (Standard), `team` oder `factory`. Änderungen reviewen.
7. Prüfen: `python3 scripts/check_wdf.py` und `python3 -m unittest discover -s tests -p 'test_*.py' -v`.
8. Bei Team/Factory: menschliche Rollen ausfüllen, `.github/CODEOWNERS` mit echten GitHub-Handles versehen und **im GitHub-Webinterface** Branch-Schutz/Ruleset, erforderliche Reviews und Statuschecks konfigurieren. CODEOWNERS-Kommentare schützen nichts.
9. PR erstellen, durch eine zweite Person prüfen lassen (Team/Factory), erst danach mergen.
10. Für bereits aus v1.1 erzeugte Projekt-Repositories erfolgt **keine automatische Aktualisierung**; jedes betroffene Projekt separat migrieren.

## Nicht automatisch übertragen
GitHub-Projects-Boards, Mitgliederrechte, Branch Rulesets, Secrets, Hosting und Vercel/Supabase-Einstellungen. Diese gehören zum jeweiligen GitHub-/Hosting-Projekt.
