# WDF Starter Kit v1.2.1 – Collaboration Edition

**Web Development Framework · 8 PDCA-Phasen · GitHub + Codex · Menschen-gesteuerte Freigaben**

Das WDF ist ein **projekt- und technologieunabhängiges** Starter Kit für kleine Softwareprojekte. Es begleitet Vision, Requirements, Architektur, Entwicklung, Tests, Release, Monitoring und Verbesserungen. Eine Astro- oder Next.js-App entsteht erst nach der Architekturentscheidung G1.

**Patch 1.2.1:** konsolidiertes Setup, korrigierte Migration und eindeutige Versionsführung. Konfigurationsschema bleibt 1.2.

## In 5 Schritten starten

1. [`SETUP-GUIDE.md`](SETUP-GUIDE.md) lesen und GitHub-Template-Repository anlegen.
2. Neues Projekt über **Use this template** erzeugen und lokal klonen.
3. Modus in `.wdf/config.json` prüfen (`solo` ist Standard), bei Team/Factory Kapitel 5–7 des Setup-Guides umsetzen. Codex im Projektordner starten; [`prompts/01-onboarding.md`](prompts/01-onboarding.md) verwenden.
4. `docs/01-vision.md`, `docs/02-requirements.md`, `docs/03-architecture.md` prüfen und G1 **persönlich freigeben**.
5. Feature-Plan über `python3 scripts/new_feature.py F-001 training-anmeldung` anlegen; [`prompts/10-feature-define.md`](prompts/10-feature-define.md) ausführen. Plan reviewen, implementieren, testen und erst mit G3 freigeben.

## WDF-Lifecycle

| PDCA | Phase | Projektartefakte |
|---|---|---|
| PLAN | 01 Vision & Scope | `docs/01-vision.md` |
| PLAN | 02 Features & Requirements | `docs/02-requirements.md`, `plans/F-*.md` |
| PLAN | 03 Architecture & Design | `docs/03-architecture.md`, G1 |
| DO | 04 Implementation | Feature-Plan, Code, Tests, Commits |
| DO | 05 Integration & Release Preparation | Build, Staging, G2, Release Notes |
| CHECK | 06 Verification & Validation | `docs/06-test-results.md`, Abnahme, G3 |
| CHECK | 07 Monitoring & Evaluation | `docs/07-monitoring.md` |
| ACT | 08 Improvement & Planning | `docs/08-improvements.md`, G4 |

## Feature-Workflow (seit v1.1)

- Ein **durchgängiger Feature-Plan** (`plans/F-001-*.md`) statt losem Prompt-Handoff.
- **Plan Review** und **Build Review** als separate, nachvollziehbare Schritte.
- **Rollenmodell** mit Human-Driver und Agent-Driver sowie klarer Eskalation.
- **Feature-Status** von `Defined` bis `Released`, mit dokumentierten Übergangsbedingungen.
- **Migration**, `new_feature.py`, strukturelle Validierung, Tests und GitHub Action.

Wichtig: **Review Findings sind Empfehlungen**, kein Beweis für Korrektheit. Ein erfolgreiches CI-Resultat ist keine menschliche Freigabe. `tests/` überprüft die Starter-Kit-Werkzeuge, nicht spätere Apps.

## Wo finde ich was?

| Pfad | Zweck |
|---|---|
| [`AGENTS.md`](AGENTS.md) | Prozess- und Sicherheitsanweisungen für Agenten |
| [`docs/`](docs/) | Projektweite, dauerhafte Dokumente |
| [`plans/`](plans/) | Feature-spezifische Übergabeartefakte |
| [`templates/`](templates/) | Vorlagen, Rollen und Quality Gates |
| [`prompts/`](prompts/) | Onboarding, Reviews, Build, Test, Monitoring |
| [`scripts/`](scripts/) | Feature-Plan erzeugen und Struktur prüfen |
| [`MIGRATION-v1.0-to-v1.1.md`](MIGRATION-v1.0-to-v1.1.md) | Upgrade ohne Verlust bestehender Dateien |
| [`MIGRATION-v1.2-to-v1.2.1.md`](MIGRATION-v1.2-to-v1.2.1.md) | Documentation Patch sicher übernehmen |
| [`VERSION`](VERSION) | Paketversion (Schema separat in `.wdf/config.json`) |
| [`.github/`](.github/) | Issues, PRs, strukturelle CI |

**Abgrenzung:** Keine vollautomatische Software Factory, keine produktiven Deployments, keine Agenten-Orchestrierung, keine generische Sicherheitsfreigabe und keine Abhängigkeit von der Software Factory. Ideen wurden eigenständig für das WDF umgesetzt. Lizenz siehe `LICENSE`.

## Zusammenarbeit (seit v1.2)

Das Kit unterstützt drei **Betriebsmodi**. Standard: **Solo**. Die Modi steuern Prozessregeln, nicht automatisch GitHub-Berechtigungen:

| Modus | Für wen | Kernelement |
|---|---|---|
| Solo | Ein Entwickler mit KI | Schlanker Feature-Workflow und menschliche G1/G3-Freigabe |
| Team | 2–8 Entwickler | Ein Human Owner/Feature, Branch+PR, separater menschlicher Review, gemeinsame Qualitätssicherung |
| Factory | Parallele Agenten/Teams | Team-Regeln plus isolierte Workspaces; keine eingebaute autonome Orchestrierung |

**Erste Schritte:** `python3 scripts/configure_mode.py team` und [`docs/collaboration.md`](docs/collaboration.md) sowie [`CONTRIBUTING.md`](CONTRIBUTING.md) lesen. Rollen in [`docs/team-roles.md`](docs/team-roles.md) besetzen, im GitHub-Webinterface Schutzregeln manuell aktivieren. [`MIGRATION-v1.1-to-v1.2.md`](MIGRATION-v1.1-to-v1.2.md) erklärt den sicheren Upgrade-Pfad.

**Achtung:** `.github/CODEOWNERS` enthält absichtlich nur auskommentierte Beispiele. Vor Team-Einsatz müssen gültige Reviewer eingetragen und die dazugehörigen GitHub-Einstellungen überprüft werden. Der mitgelieferte Actions-Workflow prüft das Starter Kit, **nicht** eine spätere Web-App.
