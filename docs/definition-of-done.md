# Definition of Done (DoD)

Diese Kriterien gelten für ein **Feature**. Ein Feature kann `Accepted` sein, ohne bereits `Released` zu sein.

- [ ] Feature-ID, Issue, Owner und Plan referenziert; Scope unverändert oder bewusst neu freigegeben.
- [ ] Akzeptanzkriterien implementiert und einzeln mit Test/Beobachtung belegt.
- [ ] Relevante automatisierte Prüfungen (z. B. Lint/Typecheck/Unit/Integration/Build) sind erfolgreich; nicht vorhandene Checks transparent beschrieben.
- [ ] Relevante Negative-/Berechtigungsfälle getestet; Security/Datenschutz-Risiken bewertet.
- [ ] Implementation Notes / What to Test und ggf. Datenbankmigrationen aktualisiert.
- [ ] Plan-Review-/Build-Review-Findings adressiert oder ausdrücklich nachvollziehbar bewertet.
- [ ] Bei Team/Factory unabhängiger menschlicher PR-Review; bei Solo Review nach Risiko.
- [ ] Branch nach vereinbartem GitHub-Workflow integriert; keine ungeklärten kritischen Findings.
- [ ] Fachliche Abnahme von befugtem Menschen dokumentiert; relevante Risiken akzeptiert.

## Nicht automatisch enthalten
Produktivdeployment, Betriebsbereitschaft oder `Released`: Diese erfordern zusätzlich **Gate G3**, Deployment-/Rollback-Plan und – falls produktiv – Monitoring/Backups nach Risiko. Erfolgreiche CI ist keine fachliche Freigabe.
