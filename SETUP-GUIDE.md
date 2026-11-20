# WDF Starter Kit v1.2.1 – Setup & Onboarding Guide

**Web Development Framework · Collaboration Edition · Documentation Patch**

Diese Anleitung begleitet dich vom leeren GitHub-Repository bis zum ersten freigegebenen Feature. Du brauchst keine Erfahrung mit professioneller Softwareentwicklung. Beginne mit einem kleinen Projekt und synthetischen Testdaten. Das Starter Kit enthält Methoden, Vorlagen und lokale Hilfsprogramme, aber noch keine fertige Web-App.

## Inhaltsverzeichnis

1. [Einführung und Betriebsmodus](#01--einführung-und-betriebsmodus)
2. [Voraussetzungen](#02--voraussetzungen)
3. [Master-Template einmalig einrichten](#03--master-template-einmalig-einrichten)
4. [Neues Projekt initialisieren](#04--neues-projekt-initialisieren)
5. [Projekt konfigurieren](#05--projekt-konfigurieren)
6. [GitHub konfigurieren](#06--github-konfigurieren)
7. [KI-Onboarding](#07--ki-onboarding)
8. [Projekt-Lifecycle und Gates](#08--projekt-lifecycle-und-gates)
9. [Feature-Entwicklung](#09--feature-entwicklung)
10. [Zusammenarbeit und Factory](#10--zusammenarbeit-und-factory)
11. [Tests und Verifikation](#11--tests-und-verifikation)
12. [Migration und Wartung](#12--migration-und-wartung)
13. [Troubleshooting](#13--troubleshooting)
14. [Quick Reference](#14--quick-reference)

---

## 01 – Einführung und Betriebsmodus

WDF kombiniert einen projektweiten PDCA-Zyklus mit einem wiederholbaren Feature-Prozess. Der Mensch entscheidet über Produktziele, Scope und Freigaben; KI kann Planung, Umsetzung, Reviews und Tests unterstützen.

| Modus | Geeignet für | Zusätzliche Pflichten |
|---|---|---|
| `solo` | Eine Person mit KI | Plan und Reviews nach WDF, menschliche Freigaben; PR empfohlen |
| `team` | Mehrere Entwickler | Feature-Owner, eigener Branch, PR, unabhängiger menschlicher Review und App-CI |
| `factory` | Parallele Agenten / Teams | Team-Regeln plus isolierte Arbeitsverzeichnisse pro Agent; kontrollierte Integration |

**Standard: Solo.** Factory ist eine Prozesskonfiguration, keine installierte Agenten-Orchestrierung. Du kannst später den Modus wechseln, ohne den Tech Stack zu wechseln.

| Profil | Anwendung | Empfohlener Ausgangspunkt |
|---|---|---|
| S1 | Statische Website | Astro, TypeScript, Tailwind CSS; statisches Hosting |
| S2 | Interaktive Website mit Daten | Next.js, React, Tailwind/shadcn, Supabase nach Bedarf |
| S3 | Dynamische Website mit Fachlogik | Next.js, serverseitige Services, Supabase PostgreSQL |
| S4 | Umfangreiche Web-App | Next.js, modularer Backend-Aufbau, PostgreSQL/Auth, separate Dienste nur bei Bedarf |

Betriebsmodus und Architekturprofil sind unabhängig: Eine S1-Website kann von einem Team entwickelt werden; eine S4-Demo kann ein Solo-Projekt sein. Hosting, technische Prüfungen und Datenschutz werden für das konkrete Projekt entschieden.

## 02 – Voraussetzungen

| Voraussetzung | Wofür? | Prüfung |
|---|---|---|
| GitHub-Konto | Repository, Issues, PRs, Actions | Anmeldung auf github.com |
| Git | Lokale Versionsverwaltung | `git --version` |
| Python 3 (3.10+ empfohlen) | WDF-Hilfsskripte und Tests | `python3 --version` |
| Editor, z. B. VS Code | Dateien bearbeiten | Projektordner öffnen |
| Codex oder kompatibler Coding-Agent | KI-Unterstützung | Zugang und Projektkontext prüfen |
| GitHub CLI (optional) | Terminal-Alternative | `gh --version` |
| Node.js / Paketmanager (später) | Astro/Next.js-Anwendung | Erst nach G1 passend zum Stack installieren |

macOS/Linux: Die Beispiele verwenden ein Bash-kompatibles Terminal. Unter Windows vorzugsweise Git Bash oder WSL verwenden; gegebenenfalls `python3` durch `python` ersetzen. Python-Skripte im Kit verwenden nur die Standardbibliothek.

GitHub-Anmeldung für HTTPS-Push: unterstützte Authentifizierung (z. B. Git Credential Manager oder `gh auth login`), alternativ SSH. Ein normales GitHub-Kontopasswort genügt nicht. Niemals Tokens in Dateien, Befehlsverlauf oder Remote-URLs hinterlegen.

Optional lokale Git-Identität setzen (für diesen Repository-Ordner, nachdem er existiert):

```bash
git config user.name "DEIN NAME"
git config user.email "DEINE COMMIT-EMAIL"
```

## 03 – Master-Template einmalig einrichten

**Nur für einen neuen Master.** Falls du bereits v1.2 hast, gehe zu Kapitel 12 und verwende die [Migrationsanleitung](MIGRATION-v1.2-to-v1.2.1.md) statt erneut `git init` auszuführen.

1. Vollständiges v1.2.1-ZIP entpacken; den Ordner `wdf-starter-kit-v1.2.1` in deiner IDE öffnen.
2. Auf GitHub unter <https://github.com/new> ein leeres Repository `wdf-starter-kit` erstellen. Keine zusätzliche README, License oder `.gitignore` generieren. Public nur für zur Veröffentlichung bestimmte Inhalte, ansonsten Private.
3. Terminal im entpackten Kit-Ordner öffnen und die folgenden Befehle ausführen. Platzhalter ersetzen.

```bash
git init
git add .
git diff --cached --stat
git commit -m "Initial WDF starter kit v1.2.1"
git branch -M main
git remote add origin https://github.com/DEIN-NAME/wdf-starter-kit.git
git push -u origin main
```

4. Auf GitHub im Repository unter Settings → General die Option **Template repository** aktivieren. Issues und Actions müssen verfügbar sein. Die tatsächliche Oberfläche kann sich ändern.
5. Unter Actions den ersten Lauf von **WDF Starter Checks** prüfen. Falls erforderlich, Actions im Repository erlauben.
6. Prüfen, ob `Use this template` angezeigt wird. Für Freunde den Master-Link teilen, nicht den Zugang zu deinen privaten Projekten.

Der Master bleibt eine leere Vorlage: keine echten Produktdaten, keine produktiven Secrets, keine persönlichen Rollenbesetzungen. Standardmodus `solo` beibehalten. Änderungen am Master werden nicht automatisch in bereits erstellte Projekte übertragen.

## 04 – Neues Projekt initialisieren

1. Im Master: **Use this template → Create a new repository**. Eigentümer, Projektname und Sichtbarkeit festlegen; für nicht öffentliche Arbeit Private wählen.
2. Das **neue Projekt**, nicht den Master, lokal klonen. Beispiel:

```bash
mkdir -p ~/Projects
cd ~/Projects
git clone https://github.com/DEIN-NAME/MEIN-PROJEKT.git
cd MEIN-PROJEKT
git remote -v
git status
python3 scripts/check_wdf.py
```

3. Den Projektwurzelordner in IDE und Codex öffnen. Optional beim VS-Code-Terminal `code .` verwenden, wenn der CLI-Befehl installiert ist.
4. Für Teamprojekte Aufgaben und Rollen besetzen. Konfiguration in Kapitel 5, GitHub-Schutz in Kapitel 6.
5. Erst nach Briefing und G1 App-Code initialisieren. Das Framework bleibt im bestehenden Repo; keine zweite verschachtelte Git-Historie erzeugen. Bei einem Framework-Generator, der ein leeres Verzeichnis verlangt, ein temporäres Verzeichnis nutzen, Änderungen prüfen und nur benötigte App-Dateien ins Projekt übernehmen. Bestehende `README.md`, `AGENTS.md`, `.gitignore`, `.github/`, `docs/`, `tests/` und WDF-Skripte nicht überschreiben.

**Beispiel lokale Struktur** (vor App-Initialisierung):

```text
~/Projects/
├── wdf-starter-kit/             # Master, optional lokal
└── mein-projekt/                # Unabhängiges Projekt-Repository
    ├── AGENTS.md
    ├── README.md
    ├── SETUP-GUIDE.md
    ├── CONTRIBUTING.md
    ├── .wdf/config.json
    ├── .github/
    ├── docs/
    ├── plans/
    ├── reviews/
    ├── templates/
    ├── prompts/
    ├── scripts/
    └── tests/
```

Quellcode, Projekt-Konfiguration und App-Tests werden entsprechend S1–S4 ergänzt. Persönliche Notizen können außerhalb des Projekt-Repositories bleiben.

## 05 – Projekt konfigurieren

Im **Projekt** ausführen (genau einen Modus wählen):

```bash
python3 scripts/configure_mode.py solo
# oder:
python3 scripts/configure_mode.py team
# oder:
python3 scripts/configure_mode.py factory
```

Datei `.wdf/config.json` kontrollieren und die Änderung reviewen. `schema_version` bleibt `1.2`; diese Patch-Version ändert das Schema nicht. Die Paketversion steht in `VERSION`. `human_release_approval` muss `true` bleiben. Der Modus aktiviert keine GitHub-Regeln automatisch.

Team/Factory: `docs/team-roles.md` mit tatsächlichen menschlichen Verantwortlichen, Vertretungen und GitHub-Handles füllen. Product Owner verantwortet fachlichen Scope, Tech Lead technische Entscheidungen, Developer die Umsetzung, Reviewer/QA die separate Prüfung. Eine Person kann Rollen kombinieren, darf im Team aber nicht allein den eigenen PR freigeben.

Bei Solo genügt ein benannter menschlicher Projekt- und Feature-Verantwortlicher; auch hier sind G1/G3 menschliche Entscheidungen. Ein späterer Wechsel zu Team erfordert zusätzlich Kapitel 6, 7 und 10. Lies [CONTRIBUTING](CONTRIBUTING.md), [Collaboration](docs/collaboration.md) und [Security](docs/security-and-access.md).

## 06 – GitHub konfigurieren

### A. Issues und Aufgabenboard (alle Modi)

Issues unter Settings → General → Features aktivieren. Unter Issues → New issue werden `Feature`, `Bug` und `Improvement` aus `.github/ISSUE_TEMPLATE/` angeboten. Ein Feature erhält eine eindeutige ID, z. B. `F-001`, ein Issue, einen menschlichen Owner und später einen Link zum Feature-Plan. Issue-Nummer und Feature-ID sind getrennte Kennungen.

Optional ein GitHub Projects Board im Benutzer-/Organisationsbereich anlegen, z. B. `WDF – Mein Projekt`. Status: Backlog, Ready, In Progress, Review, Done. Issues zum Board hinzufügen, Verantwortliche und Prioritäten pflegen. Projects-Boards werden nicht durch das Repository-Template kopiert. Ein optional gespiegeltes Feld für den Feature-Status benötigt manuelle Pflege; keine automatische Synchronisation wird mitgeliefert.

### B. Mitglieder und Berechtigungen (Team/Factory verbindlich)

1. In Settings → Collaborators / Access die benötigten Entwickler bzw. Organisationsteams einladen. Nur notwendige Rechte vergeben; Admin- und produktive Zugangsdaten nicht pauschal teilen.
2. Einladungen bestätigen lassen. Rollen und Vertretungen in `docs/team-roles.md` festhalten.
3. In `.github/CODEOWNERS` die auskommentierten Beispiele durch gültige GitHub-Nutzer/Organisationsteams mit passenden Schreibrechten ersetzen. Beispiel (Platzhalter ersetzen, nur passende Pfade aktivieren):

```text
* @DEIN-REVIEWER
/src/ @DEIN-ORG/maintainers
/supabase/ @DEIN-ORG/database-reviewers
/.github/ @DEIN-ORG/maintainers
/AGENTS.md @DEIN-ORG/maintainers
```

GitHub wertet bei überlappenden Mustern den letzten passenden Eintrag aus. Für mehrere zuständige Personen auf demselben Muster alle benötigten Handles auf einer Zeile angeben. Ein CODEOWNERS-Eintrag allein erzwingt keine Freigabe. Für die erste Aktivierung müssen die Regeln auf dem relevanten Basisbranch vorhanden sein. CODEOWNERS selbst und Sicherheitsregeln besonders schützen.

### C. Branch-Schutz / Rulesets für `main` (Team/Factory verbindlich)

Im Projekt-Repository Settings → Rules → Rulesets (oder Branches / Branch protection) öffnen. Verfügbarkeit hängt von Konto, Sichtbarkeit, Tarif und Rechten ab. Wenn die benötigte technische Durchsetzung nicht verfügbar ist, Teamregeln organisatorisch anwenden, die Lücke dokumentieren und vor produktivem Einsatz geeignete Schutzmechanismen bereitstellen.

1. Ein Branch-Ruleset bzw. eine Schutzregel für `main` erstellen; bei Rulesets Enforcement auf Active setzen.
2. Direkte Änderungen über **Require a pull request before merging** einschränken.
3. Mindestens einen unabhängigen menschlichen Review erfordern; bei vorhandenen gültigen CODEOWNERS zusätzlich deren Review verlangen, wo erforderlich. Veraltete Freigaben bei neuen Änderungen verwerfen bzw. neue prüfpflichtige Änderungen erneut reviewen lassen.
4. **Require status checks to pass** aktivieren. Zuerst einen Actions-Lauf auf relevantem Commit bzw. PR ausführen; anschließend den tatsächlich angezeigten Job `starter` (Workflow **WDF Starter Checks**) auswählen. Den exakten Check-Kontext in GitHub überprüfen, nicht blind einen Namen eingeben.
5. Nach App-Initialisierung zusätzlich die tatsächlich laufenden App-CI-Checks verpflichtend machen. Optional Aktualität gegenüber `main` vor Merge verlangen und festlegen, wer Konflikte löst.
6. Force-Push und Branch-Löschung für `main` unterbinden; Bypass-Rechte minimal und bewusst festlegen. Nicht durch alternative Merge-Wege umgehen.
7. Test-PR mit einer zweiten Person durchführen: ohne Review bzw. mit fehlerhafter CI darf Merge nicht möglich sein. Danach korrigieren, Review einholen und Test-PR mergen. Ergebnisse dokumentieren.

### D. CI und Deployment trennen

`.github/workflows/wdf-check.yml` führt den WDF-Strukturprüfer und Python-Unittests aus. Nach G1 die App-CI ergänzen: reproduzierbare Paketinstallation (Lockfile), Lint, Typprüfung, relevante Tests und Build. Verwende die tatsächlich vorhandenen Skripte der App; keine erfundenen Befehle. Bei einer statischen Website können weniger Checks genügen als bei einer App mit Datenbank.

Für Produktion eine separate Freigabe-/Deployment-Kontrolle einrichten (z. B. manuelles Deployment oder geeignete geschützte Umgebung, sofern verfügbar). Bei Vercel oder anderen Auto-Deploy-Integrationen prüfen, ob Merge nach `main` automatisch Produktion aktualisiert. Falls ja, diesen Automatismus so konfigurieren, dass die G3-Freigabe **vor** dem produktiven Merge/Deployment erfolgt, oder Produktion über einen separaten freigegebenen Release-Weg deployen. Ein PR-Merge darf nicht unbemerkt G3 umgehen.

Keine Produktions-Secrets in untrusted PR-Jobs bereitstellen. Secrets in dafür vorgesehenen Plattform-Einstellungen, nur für benötigte Jobs/Umgebungen. Test- und Produktivdaten trennen; Datenbankmigrationen und Rollback prüfen.

Offizielle Hilfe: [GitHub Templates](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository), [Rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets), [CODEOWNERS](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners), [Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects).

## 07 – KI-Onboarding

Codex im **Projektwurzelverzeichnis** starten. `AGENTS.md` enthält dauerhafte Projektregeln; die Dateien in `prompts/` sind Arbeitsaufträge und werden nicht automatisch ausgeführt. Kopiere den passenden Prompt oder bitte Codex, ihn aus dem lokalen Projekt zu lesen. Das Kit selbst installiert keinen Agenten und erteilt ihm keine zusätzlichen Berechtigungen.

Für einen neuen Projekt-Chat:

```text
Lies AGENTS.md, README.md und .wdf/config.json dieses Repositories.
Meine Projektidee: [2–4 Sätze]. Zielgruppe: [wer].
Nutze prompts/01-onboarding.md und führe mich durch Vision,
MVP, Requirements und Architekturprofil S1–S4.
Noch keinen Anwendungscode erstellen. G1 bleibt offen,
bis ich die Entscheidung ausdrücklich bestätigt habe.
```

Team/Factory zusätzlich vor Entwicklungsbeginn:

```text
Nutze prompts/15-team-onboarding.md. Prüfe Rollen, GitHub-Regeln,
CI, CODEOWNERS, Zugriffsrechte und Vertretungen anhand der
Projektdateien. Nenne fehlende manuelle Einstellungen.
Ändere keine Remote-Einstellungen ohne ausdrückliche Freigabe.
```

Teammitglieder klonen dasselbe Projekt in eigene Ordner, lesen `AGENTS.md`, `CONTRIBUTING.md`, `docs/03-architecture.md`, Rollen und Security-Regeln. Für eine neue Sitzung in einem laufenden Projekt `prompts/09-new-session.md` verwenden; es soll den aktuellen Stand zusammenfassen, noch nicht eigenmächtig implementieren.

## 08 – Projekt-Lifecycle und Gates

| PDCA | Phase | Deliverables / Nachweise |
|---|---|---|
| PLAN | 01 Vision & Scope | `docs/01-vision.md`: Problem, Zielgruppe, MVP, Erfolg |
| PLAN | 02 Features & Requirements | `docs/02-requirements.md`, Feature-IDs, Pläne |
| PLAN | 03 Architecture & Design | `docs/03-architecture.md`: S-Profil, Daten, Schnittstellen, Betrieb; G1 |
| DO | 04 Implementation | Code, Tests, Feature-Plan, Review |
| DO | 05 Integration & Release Preparation | Build, Staging, Release-Vorbereitung, G2 |
| CHECK | 06 Verification & Validation | Testnachweise in `docs/06-test-results.md`, Abnahme, G3 |
| CHECK | 07 Monitoring & Evaluation | `docs/07-monitoring.md`, Logs, Feedback und Nutzen |
| ACT | 08 Improvement & Planning | `docs/08-improvements.md`, nächste Iteration, G4 |

| Gate | Vor dem Übergang | Wer entscheidet in Team/Factory? |
|---|---|---|
| G1 – Ready for Development | Vision, MVP, Requirements, Architektur und Risiken ausreichend klar | PO fachlich, Tech Lead technisch |
| G2 – Ready for Testing | Integrierter, nutzbarer Build und geeignete Testumgebung | Tech Lead/Reviewer gemäß Rollenregel, Developer liefert Nachweise |
| G3 – Ready for Release | Tests, Abnahme, offene Risiken und Rollback bewertet | PO fachlich und Tech Lead technisch/betrieblich |
| G4 – Next Iteration | Feedback ausgewertet, Maßnahmen priorisiert | PO mit Team |

Solo: Mensch als Verantwortlicher dokumentiert Entscheidungen. G2 kann gemäß `templates/gates.md` über einen vorab autorisierten, dokumentierten Prozess geprüft werden; G1, G3 und G4 werden nicht automatisch aus CI abgeleitet. Nutze `templates/gates.md` für die Dokumentation oder verweise eindeutig auf den bestehenden Nachweis. G1 ist projektbezogen; jedes konkrete Feature braucht zusätzlich seine eigene Plan-Freigabe auf Reviewed.

Nach G1 kann das gewählte Astro-/Next.js-Grundgerüst eingerichtet werden. Dokumentiere Abhängigkeiten, Start- und Testbefehle im Projekt-README; behalte den WDF-Einstieg. G3 vor Produktion, G4 führt zurück zur nächsten PLAN-Iteration.

## 09 – Feature-Entwicklung

Ein Feature durchläuft einen kleinen Zyklus innerhalb des WDF-Projekt-Lifecycles.

1. **Assign:** Issue, ID, Owner, Reviewer und Abhängigkeiten festlegen. Für Team/Factory eigenen Branch anlegen, von gepflegtem `main` ausgehen. Beispiel (noch nicht auf Produktion deployen):

```bash
git switch main
git pull --ff-only
git switch -c feature/F-001-trainings-anmeldung
python3 scripts/new_feature.py F-001 trainings-anmeldung
```

   Solo ohne Branch möglich, ein Branch ist dennoch empfohlen. Der Generator erzeugt `plans/F-001-trainings-anmeldung.md` und verweigert eine bereits belegte ID im lokalen Arbeitsstand. In Teams IDs zentral im Issue/Board reservieren, da mehrere Clones nicht gegenseitig geprüft werden.
2. **Define:** `prompts/10-feature-define.md` mit dem konkreten Pfad verwenden. Plan, Scope, Kriterien, Schnittstellen und Owner ausfüllen. Der Generator startet mit `Defined`, das ist noch keine bestätigte Definition.
3. **Plan Review:** `prompts/11-plan-review.md` möglichst in separater Review-Sitzung verwenden. Findings nach `reviews/F-001-plan-review.md`; Mensch entscheidet über Findings und bestätigt Build-Freigabe. Erst dann `Reviewed` im Plan inkl. Status History dokumentieren.
4. **Build:** `prompts/04-feature-implementation.md` verwenden. Agent liest genehmigten Plan, arbeitet begrenzt auf dem Feature, schreibt geeignete Tests vor oder mit dem Code. `Building` und tatsächliche Änderungen, Testausgaben, Implementation Notes und What to Test dokumentieren.
5. **Build Review:** `prompts/12-build-review.md` auf Diff/PR anwenden, Findings in `reviews/F-001-build-review.md` festhalten und behandeln. KI-Review ist kein Ersatz für den unabhängigen menschlichen PR-Review in Team/Factory.
6. **Integration / QA:** `prompts/05-integration-release.md` für integrierten Build/Release-Vorbereitung; `prompts/13-feature-qa-handoff.md` für Testmatrix. G2 dokumentieren, dann Status `Testing` gemäß Lifecycle. `prompts/06-test-acceptance.md` verwenden, Testfälle real ausführen und Ergebnisse dokumentieren. Ggf. nach Integration erneut testen.
7. **Accepted:** Definition of Done prüfen, Akzeptanzkriterien und relevante Tests nachweisen und fachliche Abnahme im Plan festhalten. In Team/Factory unabhängiger menschlicher PR-Review erforderlich. `Accepted` ist noch keine Veröffentlichung.
8. **Release:** G3-Freigabe mit Nachweis dokumentieren; den freigegebenen Stand kontrolliert veröffentlichen. `Released` erst bei tatsächlichem Deployment/Release vermerken. Release-Notizen via `templates/05-release.md`, Monitoring und Verbesserungen mit Prompts 07/08.

PR: Issue und Plan verlinken; `Refs #123` für einen offenen Arbeitsbezug, `Closes #123` nur wenn das Issue nach Merge tatsächlich geschlossen werden soll (beim Merge in den Default-Branch). Ein Closed Issue oder ein Done-Boardstatus ist kein Nachweis von Release. Ggf. Release-Status getrennt im Plan führen. Vor Merge alle erforderlichen Reviews und Checks erneut prüfen.

Bei Abweichungen `Blocked` oder `Retry` mit vorherigem Status, Gründen und Entscheidung dokumentieren. Keine automatischen Statuswechsel aufgrund eines grünen CI-Laufs. Details in [Feature-Lifecycle](templates/feature-lifecycle.md), [Feature-Plan](templates/feature-plan.md), [DoD](docs/definition-of-done.md).

## 10 – Zusammenarbeit und Factory

GitHub Issue/Projects = operativer Status, Priorität und Zuweisung; Feature-Plan = fachlicher Status, Akzeptanzkriterien und Übergabe; PR/CI = Codeänderungen und Prüfnachweise. Einmal dokumentieren, an anderen Stellen verlinken. `docs/06-test-results.md` enthält die Test-/G3-Nachweise.

Für Team/Factory gelten `CONTRIBUTING.md`, `docs/team-roles.md`, `docs/collaboration.md` sowie die Sicherheits- und DoD-Regeln. In jedem PR mindestens ein anderer menschlicher Reviewer; für kritische Änderungen Codeowner nach den festgelegten Regeln. Änderungen an gemeinsamen APIs, DB-Migrationen, Auth oder Architektur mit dem Tech Lead und betroffenen Ownern abstimmen, bevor implementiert wird.

Bei Übergabe an eine andere Person `prompts/16-team-feature-handoff.md` verwenden; für den Kollaborationsreview `prompts/17-collaboration-review.md`. Offene Entscheidungen, letzte Commits, Teststatus und Risiken dokumentieren. Feature-Branches möglichst klein halten, neueste Änderungen aus `main` koordiniert integrieren und erneut testen. Nicht mechanisch Konflikte auflösen, ohne fachliche Folgen zu prüfen.

**Factory / parallele Agenten:** Jeder Agent benötigt einen eigenen Workspace und Feature-Branch. Beispiel mit einem bereits vorhandenen lokalen Repository (Pfad und ID anpassen; Branch darf noch nicht existieren):

```bash
git fetch origin
git worktree add ../mein-projekt-f002 -b feature/F-002-beispiel origin/main
git worktree list
```

Den Agenten in genau diesem neuen Ordner starten, nicht im gemeinsamen Arbeitsverzeichnis. Alternativ einen separaten Clone anlegen. Git-Worktrees teilen Elemente der Git-Historie und sind keine Sicherheits-Sandbox. Umgebungsdateien, Datenbank, Ports und Testdaten bewusst getrennt konfigurieren. Agenten erhalten nur erforderliche Rechte; kein automatischer Zugang zu Produktion. Integrationsentscheidungen, Push, Merge und Produktion bleiben kontrolliert. Factory liefert keine eigenen Worktree-Launcher, automatische Agentenkoordination oder automatische Merge-Pläne.

## 11 – Tests und Verifikation

Im Repository-Root ausführen:

```bash
python3 scripts/check_wdf.py
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

Erwartung: keine Strukturfehler, alle mitgelieferten WDF-Tests bestanden. Der Validator prüft Datei- und ausgewählte Plan-/Konfigurationsstrukturen, nicht die Richtigkeit fachlicher Informationen. Die Python-Tests prüfen ausschließlich das Starter Kit. Sie geben keine Freigabe und ersetzen keine Tests für deine Web-App.

Nach Initialisierung der Anwendung zusätzlich die projektbezogenen Befehle aus dem README ausführen. Beispiele (nur wenn die Skripte tatsächlich vorhanden sind): `pnpm lint`, `pnpm typecheck`, `pnpm test`, `pnpm build`. Relevante Anforderungen mit Testfällen verknüpfen. Negative Fälle, mobile Bedienung, Berechtigungen und Regressionen je Risiko prüfen. Dokumentiere echte Ergebnisse, auch fehlgeschlagene oder nicht ausgeführte Prüfungen.

**Vor dem ersten Team-Praxisbetrieb:** Test-PR mit getrenntem Reviewer, G2-Testumgebung und vorgeschaltetem G3-Releaseprozess durchführen. GitHub-Schutzregeln und Deployment tatsächlich überprüfen; der lokale Konfigurationsmodus bestätigt das nicht.

## 12 – Migration und Wartung

| Ausgangspunkt | Anleitung |
|---|---|
| Neues Projekt | Vollständiges v1.2.1-ZIP, Kapitel 3–11 |
| v1.0 | [v1.0 → v1.1](MIGRATION-v1.0-to-v1.1.md), dann weitere Schritte |
| v1.1 | [v1.1 → v1.2](MIGRATION-v1.1-to-v1.2.md), danach Patch |
| v1.2 | [v1.2 → v1.2.1](MIGRATION-v1.2-to-v1.2.1.md) |

Patch-ZIP enthält nur geänderte/neue Dateien. In einen temporären Ordner entpacken und gezielt auf einem Upgrade-Branch übernehmen. Bei bestehenden Projekten individuelle README/AGENTS-Anweisungen, Rollen, Feature-Pläne, Reviews, App-Code, GitHub-Einstellungen und `.wdf/config.json` nicht pauschal ersetzen. `schema_version: "1.2"` und gewählten Mode beibehalten. Master-Updates werden nicht an abgeleitete Repos vererbt; jedes Projekt separat migrieren. `CHANGELOG.md` beschreibt die Paketänderungen. Optional getaggte GitHub-Releases am Master erstellen.

## 13 – Troubleshooting

| Problem | Prüfung / Lösung |
|---|---|
| `python3: command not found` | Python 3 installieren oder auf Windows `python` verwenden |
| `remote origin already exists` | `git remote -v`; bestehende Ziele nicht blind überschreiben |
| Push verweigert | Anmeldung, Schreibrechte und Ruleset prüfen; keinen Force-Push als Abhilfe |
| `Use this template` fehlt | Master-Einstellung Template repository überprüfen |
| Issue-Form fehlt | `.github/ISSUE_TEMPLATE/` im Default-Branch und aktivierte Issues prüfen |
| Required Check nicht auswählbar | Workflow zuerst ausführen und exakten Check-Kontext aus GitHub auswählen |
| CODEOWNERS greift nicht | Basisbranch, gültige Reviewer mit Zugriff, Musterreihenfolge und Ruleset prüfen |
| Eigener PR kann nicht gemergt werden | Andere Person muss reviewen; offene Checks oder Änderungen erneut prüfen |
| Feature-ID schon belegt | Backlog/Plan prüfen; neue ID reservieren, nicht überschreiben |
| Codex kennt WDF nicht | Projektroot öffnen, `AGENTS.md` prüfen, neue Sitzung; Prompt-Datei ausdrücklich nennen |
| App-Generator überschreibt Dateien | In separatem Verzeichnis initialisieren; Diff prüfen und WDF-Dateien erhalten |
| Factory startet keine Agenten | Erwartet: Mode ist Policy, kein ausführbarer Orchestrator |
| Production deployt bei Merge sofort | Deployment-Integration prüfen; G3 vor produktivem Merge erzwingen oder separaten Release-Weg nutzen |

## 14 – Quick Reference

### Lokale Befehle

| Aufgabe | Befehl |
|---|---|
| Modus setzen | `python3 scripts/configure_mode.py solo` (alternativ `team` oder `factory`) |
| Feature erstellen | `python3 scripts/new_feature.py F-001 trainings-anmeldung` |
| Struktur prüfen | `python3 scripts/check_wdf.py` |
| Kit-Tests | `python3 -m unittest discover -s tests -p 'test_*.py' -v` |
| Lokalen Stand prüfen | `git status` / `git diff` |
| Paketversion anzeigen | `cat VERSION` |

### Prompt-Verzeichnis

| Nr. | Datei | Einsatz |
|---|---|---|
| 01 | [`01-onboarding.md`](prompts/01-onboarding.md) | Projektbriefing/G1 |
| 02 | [`02-requirements-review.md`](prompts/02-requirements-review.md) | Requirements prüfen |
| 03 | [`03-architecture-review.md`](prompts/03-architecture-review.md) | Architektur prüfen |
| 04 | [`04-feature-implementation.md`](prompts/04-feature-implementation.md) | Feature implementieren |
| 05 | [`05-integration-release.md`](prompts/05-integration-release.md) | Integration und Release-Vorbereitung |
| 06 | [`06-test-acceptance.md`](prompts/06-test-acceptance.md) | Verifikation und Abnahme |
| 07 | [`07-monitoring-review.md`](prompts/07-monitoring-review.md) | Monitoring auswerten |
| 08 | [`08-improvement.md`](prompts/08-improvement.md) | Verbesserungen planen |
| 09 | [`09-new-session.md`](prompts/09-new-session.md) | Neue Sitzung starten |
| 10 | [`10-feature-define.md`](prompts/10-feature-define.md) | Feature definieren |
| 11 | [`11-plan-review.md`](prompts/11-plan-review.md) | Plan prüfen |
| 12 | [`12-build-review.md`](prompts/12-build-review.md) | Build prüfen |
| 13 | [`13-feature-qa-handoff.md`](prompts/13-feature-qa-handoff.md) | QA-Übergabe vorbereiten |
| 14 | [`14-status-triage.md`](prompts/14-status-triage.md) | Status und Blocker prüfen |
| 15 | [`15-team-onboarding.md`](prompts/15-team-onboarding.md) | Team einarbeiten |
| 16 | [`16-team-feature-handoff.md`](prompts/16-team-feature-handoff.md) | Feature im Team übergeben |
| 17 | [`17-collaboration-review.md`](prompts/17-collaboration-review.md) | Zusammenarbeit prüfen |

### Checkliste für den ersten produktiven Release

- [ ] Projektbriefing, Scope und Architektur bestätigt; G1 dokumentiert.
- [ ] Betriebsmodus gewählt, Owner und Freigabeverantwortliche festgelegt.
- [ ] Feature-Plan reviewed und Build ausdrücklich genehmigt.
- [ ] Code Review, relevante Tests, G2 und fachliche Abnahme nachvollziehbar.
- [ ] In Team/Factory: unabhängiger menschlicher PR-Review und erforderliche CI-Checks erfolgreich.
- [ ] Zugriffsschutz, Test-/Produktivumgebung, Backup/Rollback nach Risiko geprüft.
- [ ] G3 menschlich dokumentiert, bevor Produktion verändert wird.
- [ ] Tatsächliches Release, Monitoring und Feedback dokumentiert; nächste Iteration (G4) geplant.

**WDF-Prinzip:** So wenig Prozess wie möglich, so viel Struktur und Qualität wie nötig.
