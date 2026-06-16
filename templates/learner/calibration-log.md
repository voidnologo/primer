# Calibration Log

Append-only record of where the Primer mis-estimated the learner, and the adjustment. Mined by `recalibrate` (`primer/feedback-protocol.md`): repeated miss-types get promoted to stable traits or anti-preferences.

Miss-types: `too-basic` · `too-advanced` · `vocab-gap` · `dead-analogy` · `pacing` · `struggle-mismatch` · `retention-miss` (failed cold retrieval in `/primer review` — the external anchor; lowers the domain's confidence)

Format: `<date> | <domain> | <miss-type> | <what happened> | <adjustment>`

---
