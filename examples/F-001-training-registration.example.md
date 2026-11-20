# Beispiel – F-001 Trainingsanmeldung (nicht für echten Projektstatus verwenden)

- **Vision:** Spieler melden sich vor einem Training an.
- **Scope:** Status „Dabei“/„Nicht dabei“ für bestehendes Training speichern.
- **Out of Scope:** Benachrichtigungen, Mannschaftskasse.
- **Acceptance Criteria:** AC-01 Status wird gespeichert; AC-02 Status lässt sich aktualisieren; AC-03 unberechtigter Zugriff wird verhindert.
- **Integration:** Auth und Datenmodell entscheiden, bevor gebaut wird.
- **Plan Review:** Prüfen, ob rechtliche Basis und Trainerberechtigungen geklärt sind.
- **Build:** Erst nach menschlicher Freigabe implementieren, Tests dokumentieren, What to Test ergänzen.
- **Test:** Fachdurchlauf mit Spieler/Trainer, Negativfall, Regresion.
- **Accepted/Released:** Nicht automatisch durch Agenten gesetzt.
