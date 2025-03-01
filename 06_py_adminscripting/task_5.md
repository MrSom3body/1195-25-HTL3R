# Python Adminscripting

## Aufgabe 5

- Welche Dateien werden erzeugt?
  - `~/.ssh/id_ed25519`
  - `~/.ssh/id_ed25519.pub`
- Welche Informationen werden angezeigt?
  - Speicherort
  - Key Fingerprint
  - Randomart image
- Welche Daten werden kopiert (Quelle – Ziel)?
  Public Key von Quelle wird dem Ziel unter `~/.ssh/authorized_keys` hinzugefügt
- Was passiert jetzt beim Verbinden mit ssh user@IP-Adresse? Wird nach einem Passwort gefragt?
  Man wird einfach angemeldet
- Warum gilt die Authentifizierung mittels Schlüsselpaar als sicherer als ein Login mittels herkömmlicher Passwörter?
  Weil der private Schlüssel nie übertragen wird, schwerer zu erraten ist als Passwörter und Phishing-Angriffe verhindert
