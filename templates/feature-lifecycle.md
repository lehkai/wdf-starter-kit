# WDF Feature-Zustände – v1.2.1

| Status | Eintritt / Bedeutung | Übergang durch |
|---|---|---|
| **Defined** | User Story, Scope, Kriterien, Integrationen und offene Punkte dokumentiert | Human bestätigt Definition |
| **Reviewed** | Plan-Review durchgeführt; Findings bewertet; relevante Blocker adressiert; Plan freigegeben | Human gibt Build frei |
| **Building** | Agent implementiert den genehmigten Scope | Build beendet, Tests und Review vorbereitet |
| **Testing** | Build integriert/testbar; Build-Review-Findings bewertet; What to Test vorhanden | Mensch prüft Akzeptanz |
| **Accepted** | Kriterien nachweislich erfüllt, Risiken akzeptiert, menschliche Abnahme dokumentiert | Human genehmigt Release |
| **Released** | Produktiver Release nach G3 nachweislich erfolgt | Nach Deployment vermerkt |
| **Blocked** | Externe Entscheidung/Abhängigkeit verhindert Fortsetzung | Human dokumentiert Freigabe zur Wiederaufnahme |
| **Retry** | Defect oder geänderte Requirements machen Nacharbeit erforderlich | Zurück zu Defined/Reviewed/Building/Testing nach Ursache |

**Übergänge:** `Defined → Reviewed → Building → Testing → Accepted → Released`. Bei `Retry` dokumentiere `previous_status`, Ursache, Reviewbedarf und Folgeaktion. Von `Blocked` zurück zum vorherigen gültigen Status nach Entscheidung. Keine automatische Statusänderung nur aufgrund CI oder GitHub-Labels.

**GitHub Projects:** Board-Status (Backlog/Ready/In Progress/Review/Done) ist die operative Aufgabenansicht; der Feature-Status wird im Feature-Plan geführt und kann optional als Projektfeld gespiegelt werden. Die Feature-Plan-Datei ist die Quelle für den fachlichen Feature-Status.

**Release-Regel:** `Accepted` bedeutet noch nicht `Released`. Gate G3 ist menschliche Freigabe vor Produktion.

## Team-spezifische Statusübergänge (seit v1.2)
- `Defined` → `Reviewed`: Feature Owner/PO hat Scope bestätigt und Plan-Review-Findings entschieden.
- `Building` → `Testing`: Änderungen in Branch/PR, Tests und Implementation Notes nachvollziehbar; Team-Review folgt bzw. ist dokumentiert.
- `Testing` → `Accepted`: technische Prüfergebnisse und **menschliche fachliche Abnahme** dokumentiert; in Team/Factory zusätzlich unabhängiger menschlicher PR-Review.
- `Accepted` → `Released`: G3 und Deployment dokumentiert; PR-Merge genügt nicht.
- Operativer Issue-/Board-Status bleibt in GitHub; keine automatische Synchronisation.
