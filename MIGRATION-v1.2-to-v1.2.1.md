# Patch-Migration v1.2 → v1.2.1

Dieser Dokumentationspatch enthält keine neue Konfigurationsstruktur. Dein Modus, die Projekttexte, GitHub-Berechtigungen, Secrets und App-Dateien bleiben unangetastet. Du kannst das Patch-ZIP für bestehende Repos oder das vollständige ZIP für einen neuen Master verwenden.

## 1. Vorbereitungen

- Stelle sicher, dass du v1.2 verwendest. Bei älteren Versionen die jeweiligen Migrationsanleitungen zuerst abarbeiten.
- Entpacke das Patch-ZIP in einen separaten Ordner, nicht direkt über das Projekt. Alternativ die unten genannten Dateien aus dem vollständigen ZIP einzeln übernehmen.
- Sichere uncommittete Arbeit und wechsle auf einen Upgrade-Branch:

```bash
git status
git switch main
git pull --ff-only
git switch -c chore/wdf-v1.2.1
```

Bei Offline-Repositories oder abweichendem Default-Branch die Befehle entsprechend anpassen. Nicht verwendete oder fremde Änderungen nicht verwerfen.

## 2. Dateiliste

| Datei | Vorgehen |
|---|---|
| `VERSION` | Neu anlegen (1.2.1) |
| `SETUP-GUIDE.md` | Neue konsolidierte Anleitung übernehmen, individuelle Hinweise erhalten |
| `README.md` | WDF-Einstieg und Versionsangabe aktualisieren; App-Dokumentation bewahren |
| `AGENTS.md` | Neue WDF-Regeln zusammenführen; lokale Coding-Konventionen bewahren |
| `templates/feature-lifecycle.md` | Versionsangaben/Statusquellen aktualisieren |
| `MIGRATION-v1.1-to-v1.2.md` | Korrigierte Datei übernehmen |
| `MIGRATION-v1.2-to-v1.2.1.md` | Neu übernehmen |
| `CHANGELOG.md` | Patch-Eintrag ergänzen; eigene Einträge erhalten |
| `prompts/01-onboarding.md` | Aktuelle Rollen-/Modusreferenz übernehmen |
| `prompts/04-feature-implementation.md` | Aktualisierte Überschrift übernehmen |
| `scripts/check_wdf.py` | Nur angepasste Statusausgabe übernehmen; eigene Erweiterungen bewahren |

**Nicht ändern:** `.wdf/config.json` (insbesondere `mode` und `schema_version: "1.2"`), `docs/`-Projektinhalte, `plans/`, `reviews/`, `.github/CODEOWNERS`, Anwendungscode und Secrets. Andere Dateien des vollständigen ZIPs sind gegenüber dem originalen v1.2-Paket unverändert. GitHub-Rulesets, Projects und Deployments sind externe Einstellungen, nicht Bestandteil der Migration.

Falls dein v1.2 durch Upgrade von v1.1 entstanden ist: prüfe zusätzlich, ob `templates/feature-lifecycle.md` bereits die Team-Statusübergänge und `.github/ISSUE_TEMPLATE/feature.yml` die aktuellen Collaboration-Felder aus v1.2 enthält. Letztere ist nicht Teil des reinen Patches, weil sie sich gegenüber dem Original-v1.2-ZIP nicht ändert; bei Bedarf aus dem vollständigen v1.2.1-ZIP zusammenführen.

## 3. Verifikation und Merge

```bash
cat VERSION
python3 scripts/check_wdf.py
python3 -m unittest discover -s tests -p 'test_*.py' -v
git status
git diff
```

Prüfe Diff und neue Dateien, insbesondere dass eigene Regeln, Rollen und Konfigurationen erhalten sind. In Team-/Factory-Projekten PR mit unabhängigem menschlichem Review und erforderlicher CI erstellen. Falls `main` automatisch produktiv deployt, vorher prüfen, ob G3 erforderlich ist, und Produktivänderung kontrollieren. Nach bestätigtem Merge kann am Master ein Release-Tag `v1.2.1` gesetzt werden. Bereits aus dem Master erzeugte Projekte müssen separat aktualisiert werden.
