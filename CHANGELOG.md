# Changelog

## 1.2.1 – 2026-11-18

### Fixed / Documentation
- Setup-Guide vollständig konsolidiert: 14 Kapitel, Betriebsmodi, GitHub-Setup, Onboarding, Gates, Feature-Workflow, CI und Troubleshooting.
- Versionsüberschriften in README, AGENTS und Feature-Lifecycle aktualisiert; Paketversion in `VERSION`, Konfigurationsschema bleibt 1.2.
- Migration v1.1 → v1.2 um Feature-Lifecycle und Feature-Issue-Formular ergänzt.
- Neue sichere Patch-Migration v1.2 → v1.2.1; bestehende Projekteinstellungen bleiben erhalten.
- G3 vor produktiv auslösendem Merge/Deployment ausdrücklich klargestellt.
- Veraltete Prompt-Bezeichnungen und Ausgabe des Strukturprüfers bereinigt.

### Unchanged
- Acht Phasen, Feature-Status, Gates, Modi, Konfigurationsschema, Generator und GitHub-Workflow bleiben funktional unverändert. Keine neue Abhängigkeit oder Agenten-Orchestrierung.

## 1.2.0 – 2026-11-17

### Added
- Modus-Konfiguration `solo` / `team` / `factory`, mit lokalem `scripts/configure_mode.py`.
- Teamregeln: `CONTRIBUTING.md`, Collaboration Policy, Rollen/RACI, DoD und Zugriffssicherheit.
- CODEOWNERS-Beispiel (bewusst nicht aktiv, bis Handles konfiguriert wurden).
- Drei Team-Codex-Prompts, PR- und Issue-Ergänzungen, Feature-Plan-Übergabe.
- Migrationsanleitung v1.1 → v1.2 und automatisierte Collaboration-Checks.

### Retained
- Acht PDCA-Phasen, G1–G4, S1–S4, Feature-Plan und Reviews aus v1.1.
- Menschliche Freigaben; keine automatische Produktivsetzung.

### Limitations
- Branch-/Ruleset-Schutz, Review-Anforderungen, Teams und GitHub-Projects-Boards werden **manuell** eingerichtet.
- Factory-Modus konfiguriert Prozessregeln, nicht eine automatische Agenten-Fabrik.
- WDF-CI prüft Starter-Struktur/Skripte, nicht den Code einer nachträglich erzeugten Anwendung.

## 1.1.0 – 2026-11-17

### Added
- Feature-Pläne mit DEFINE → BUILD → TEST; zwei Reviews; Rollen- und Statusmodell.
- Feature-Generator, Starter-Validator, Python-Unittests; Upgrade von v1.0.
