# Beitragen zum WDF-Projekt – v1.2

## Erst lesen
`README.md`, `AGENTS.md`, `.wdf/config.json`, `docs/collaboration.md`, `docs/definition-of-done.md`, `docs/03-architecture.md` und den betreffenden `plans/F-XXX-*.md`.

## Rollen und Aufgaben
- Jeder Feature-Plan hat **einen menschlichen Owner**; weitere Personen können mitarbeiten.
- `Product Owner`: Prioritäten/MVP/fachliche Abnahme. `Tech Lead`: Architektur/Sicherheit/technische Freigabe. `Developer`: Umsetzung und Tests. `Reviewer/QA`: unabhängiger Review. Personen dürfen Rollen kombinieren; im Team darf die Autorin/der Autor nicht allein ihre/seine eigene Änderung freigeben.
- Alle Features haben eine Issue-Referenz und Akzeptanzkriterien; operative Zuweisung in GitHub Issues/Projects, langfristige Entscheidungen in Markdown.

## Git und Pull Requests
1. Vor Arbeit Issue und Feature-Plan lesen; Dependencies/überlappende Dateien mit Team abstimmen.
2. Branch von aktuellem `main`: `feature/F-001-kurzer-name`, `fix/B-001-kurzer-name`, `docs/...`.
3. Eine abgeschlossene Änderung pro PR. Frühes Öffnen als Draft ist ausdrücklich willkommen.
4. PR-Template vollständig ausfüllen, Issue mit `Closes #123` verlinken, Testbefehle und tatsächliche Ergebnisse dokumentieren.
5. Prüfer ist nicht ausschließlich der PR-Autor; Review-Findings werden adressiert oder mit Begründung und Zustimmung verworfen.
6. Relevante CI-Checks müssen erfolgreich sein; ohne App-Gerüst prüft die CI **nur die WDF-Struktur und Starter-Skripte**.
7. Merge in `main` nur mit im gewählten Modus geforderten Reviews/Freigaben; kein Force-Push auf `main`.
8. Deployment ist ein eigenständiger Vorgang mit G3 und schriftlicher Freigabe, **nicht automatisch** die Folge eines PR-Merges.

## Architecture Change Protocol
Änderungen an Auth/Autorisierung, Datenbank-Schema, gemeinsamen APIs, Kernbibliotheken oder Deploymentarchitektur vor Implementierung im Issue ankündigen. Tech Lead prüft Rückwärtskompatibilität, Migration, Datenschutz und betroffene Teams. Entscheidung als ADR oder in `docs/03-architecture.md` dokumentieren.

## Agenten
Agenten dürfen in einem isolierten Feature-Arbeitsverzeichnis editieren und verfügbare Tests durchführen. Keine eigenständige Freigabe, kein eigenmächtiger Push/Merge/Release, keine Secrets auslesen oder veröffentlichen. Externe Dienste nur nach ausdrücklicher Autorisierung.

## Ausnahmen
Notfalländerungen müssen begründet, von einer zweiten Person möglichst vor Deployment geprüft und nachträglich getestet/dokumentiert werden. Eine Ausnahme von CI/Review ersetzt nicht die verantwortliche Freigabe.

Siehe `docs/collaboration.md` für Mode-spezifische Anforderungen.
