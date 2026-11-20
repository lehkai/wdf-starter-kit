# WDF Collaboration Policy v1.2

## Mode wählen
Konfigurationsquelle: `.wdf/config.json` → `mode` = `solo`, `team` oder `factory`. Standard ist **solo**; kein öffentliches Starter-Repository darf automatisch Teamfreigaben behaupten. Ändern mit `python3 scripts/configure_mode.py team` oder `factory` und anschließend im PR prüfen.

| Regel | Solo | Team | Factory |
|---|---|---|---|
| Git-Feature-Branch | empfohlen | verpflichtend | verpflichtend und isolierter Workspace |
| Pull Request | empfohlen | verpflichtend | verpflichtend |
| Menschlicher Feature-Owner | dieselbe Person möglich | verpflichtend | verpflichtend |
| Unabhängiger menschlicher Review | nach Risiko | **mindestens 1** | **mindestens 1** plus Agentenreview möglich |
| App-CI (Lint/Type/Test/Build) | nach Stack | verpflichtend für relevante Checks | verpflichtend |
| Plan- und Build-Review | gemäß v1.1 | verpflichtend für nichttriviale Features | verpflichtend |
| Gemeinsame Schnittstellen vorher abstimmen | empfohlen | verpflichtend | verpflichtend |
| Automatisierter Merge | nein | nein (menschliche Freigabe) | nur mit vorher definierter, kontrollierter Policy |
| G3-Produktion | ausdrücklich menschlich | fachlich + technisch menschlich | fachlich + technisch menschlich |

## Ablauf je Feature
1. **Assign:** Issue, human owner, Reviewer und Feature-Plan verlinken. Scope, Abhängigkeiten, gemeinsame Dateien prüfen.
2. **Define / Review:** Plan ausarbeiten; plan-review; fachliche Freigabe. Ohne klare Kriterien keine Agentenimplementierung.
3. **Branch:** `feature/F-001-slug` von `main`. In `factory` oder bei mehreren Agenten auf einem Rechner einen separaten Git-Worktree/Clone verwenden.
4. **Build:** Agent oder Developer bearbeitet nur das vereinbarte Feature, aktualisiert `Implementation Notes` und `What to Test`, führt Tests aus.
5. **PR:** Draft-PR möglich; finaler PR mit Testnachweisen, Risiken, Review-Links und Freigabestatus.
6. **Review / QA:** menschlicher anderer Reviewer; Findings behandeln. G2 erlaubt Staging-Tests; G3 ist eine menschliche Releaseentscheidung.
7. **Merge / Release:** Nach Review und CI in `main` mergen. Deployment nur nach gesondertem Gate G3. Monitoring und Verbesserungen folgen.

## Konflikte und parallele Änderungen
- Vorhersehbare Konflikte früh im Board/Issue markieren und betroffene Owner informieren.
- Gemeinsame DB-Migrationen, Auth-Regeln und API-Verträge nicht unabhängig auseinanderentwickeln.
- Priorität: Security/Datenschutz und kompatible Schnittstellen vor Geschwindigkeit.
- Konflikte nicht mechanisch als 'gelöst' deklarieren: Integrationstests nach Merge wiederholen.
- Feature-Plan/PR und Issue müssen eindeutig verlinkt sein, aber doppelte Freigabeprotokolle vermeiden.

## Status-Quellen (kein doppeltes Statussystem)
- GitHub Issue / Project = Arbeitsstatus, Zuständige, Priorität.
- `plans/F-XXX-*.md` = fachlicher Feature-Zustand und Übergaben aus v1.1.
- PR + CI = Codeänderungen und objektive Prüfnachweise.
- `docs/06-test-results.md` = Tests und dokumentierte G3-Entscheidung.
- Markdown-Statusfelder sind **nicht automatisch** mit GitHub synchronisiert; manuelle Pflege ist erforderlich.

## GitHub-Schutzregeln (einmalig pro Projekt einstellen)
1. Repository Settings → Rules / Rulesets oder Branch protection: `main` schützen.
2. In **Team/Factory**: PR vor Merge, mindestens ein menschlicher Approver, Approval nach neuer Änderung ggf. erneut verlangen, keine Force-Pushes/Löschungen.
3. Require status checks: `starter` (vor App-Setup); nach Initialisierung **zusätzlich projektspezifische Build/Test-/Security-Jobs**, mit stabilem Namen.
4. CODEOWNERS aktivieren: Datei `.github/CODEOWNERS` enthält zunächst **nur Kommentare**. Ersetze Muster durch **gültige GitHub-Nutzer oder Teams**, prüfe Berechtigungen, aktiviere Codeowner-Review (soweit verfügbar).
5. Wer Regeln bypass-en darf, so klein wie möglich halten. Einstellung und Plattform-/Tarifgrenzen wirklich prüfen.
6. Zugriff: Admins nur nach Bedarf, Entwickler Write, Reviewer je nach Prozess geeignete Rechte; produktive Secrets nur Berechtigten.
7. Einstellungen sind **kein Bestandteil eines GitHub Repository Template-Clones** und werden nicht durch die Dateien automatisch erzwungen.

## Kommunikationsregeln
- Issue-Kommentare für Feature-Absprachen, PR-Kommentare für Code-Review, ADR für dauerhafte Architekturentscheidungen.
- Keine sensiblen Daten in Prompts, Issues, Screenshots, Testlogs oder Pull Requests.
- Kurze Abstimmung bei API-/DB-/Auth-Änderungen; danach Entscheidung im Repository dokumentieren.
- Reproduzierbare Übergaben statt Wissen nur in privaten Chats.

## Notfälle
Ein Hotfix folgt dem vereinfachten Ablauf `fix/B-...` → Test → möglichst zweiter Review → explizite G3-Freigabe → Deployment → nachträglicher Root-Cause- und Testnachweis. Gründe für Ausnahmen dokumentieren.
