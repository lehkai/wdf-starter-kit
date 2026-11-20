# Security & Access – Team-Grundregeln

## Geheimnisse und Daten
- Nur minimale Rollen/Rechte für GitHub, Hosting, Datenbank und CI; separate Produktions- und Testkonten.
- `.env` und Tokens niemals committen, in KI-Chats posten oder in Testlogs ausgeben; `.env.example` nur Platzhalter.
- Produktionsdaten nicht unkontrolliert als Testfixtures übernehmen; synthetische Daten bevorzugen.
- Personenbezogene/vertrauliche Daten sowie Datenübertragung an externe KI-Anbieter vor Nutzung prüfen.

## Agenten und CI
- Agenten erhalten nur benötigte Repo- und Terminalrechte, keine pauschalen Admin-Rechte oder Umgehung der Sandbox.
- Agenten führen ohne ausdrücklichen Auftrag weder Push/Merge noch Production Deploy, echte Zahlungen/E-Mails oder destruktive DB-Migrationen aus.
- CI bei fremden Pull Requests nach Least-Privilege; keine produktiven Secrets im PR-Testkontext.
- Dependencies/Actions-Versionen und Sicherheitsupdates prüfen; Supply-Chain-Risiken beachten.

## Ownership
- GitHub Admin: [OFFEN]
- Secrets/Deployment Owner: [OFFEN]
- Incident Kontakt: [OFFEN]
- G3 Freigabepersonen: [OFFEN]
- Notfall-/Rollback-Anleitung: [LINK / OFFEN]

**Achtung:** Dokumentationsvorlagen und einzelne GitHub Actions ersetzen keine Sicherheitsprüfung eines echten Softwareprodukts.
