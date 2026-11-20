# Rollen und Entscheidungsrechte

| Workflow | Driver | Support | Mensch muss bestätigen |
|---|---|---|---|
| Vision & Scope | Mensch | Interview-Agent | Ziele, MVP, Risiken |
| Requirements / Define | Mensch | Interview-Agent | Feature-Plan und Akzeptanzkriterien |
| Plan Review | Mensch | Reviewer-Agent | Findings-Triage und Plan-Freigabe |
| Build | Agent innerhalb bestätigten Scopes | Mensch bei Entscheidungen | Scope-Änderung, externe Aktionen |
| Build Review | Mensch | Reviewer-Agent | Umgang mit Findings |
| Technical Testing | Agent kann ausführen | Mensch prüft Nachweise | Testlücken / signifikante Risiken |
| Acceptance | Mensch | QA-Agent | Accepted, G3 |
| Merge / Release | Mensch | Agent | Merge, Push, Release, Rollback |
| Monitoring & Act | Mensch | Agent | Prioritäten und nächste Iteration |

**Kernprinzip:** Mensch setzt Absicht und Risikoakzeptanz. Agent kann innerhalb eines *explizit* vereinbarten Umfangs die Umsetzung führen. Mehr Agentenautonomie bedeutet nie implizite Freigabe für externe Systeme oder destruktive Änderungen.

**Review-Unabhängigkeit:** Ein zweites Modell oder ein anderer Agent kann andere Fehler entdecken, ist aber nicht garantiert unabhängig. Dokumentiere Reviewer, Methode und Prüfumfang.
