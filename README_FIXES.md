# Leak-main — infrastructure-fixed copy

## What was fixed
- `bot-final-fixed-4.py` and `database.py` now have matching database imports.
- Added the four missing database compatibility functions:
  `save_card_to_db`, `get_total_cards_count`, `get_charged_count`, `get_approved_count`.
- Card persistence stores only a masked card number; full card numbers/CVV are not persisted.
- MongoDB startup now performs an explicit `ping` and fails early if the database is unavailable.
- Global-site insertion is idempotent.
- Telegram secrets were removed from source code and moved to environment variables.
- Added `.env.example`.

## Required
1. Run MongoDB.
2. Set the environment variables from `.env.example`.
3. Install `requirements.txt`.
4. Run `python bot-final-fixed-4.py`.

## Important
This copy does not add or improve any payment-card verification/checking capability. The external checking routines already present in the original project should only be used with authorized test data and systems.
