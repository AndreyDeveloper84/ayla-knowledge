from __future__ import annotations

import unittest

from scripts.validate_contract_schemas import registered_json_schemas, validate_all


class ContractSchemaTests(unittest.TestCase):
    """Машиночитаемые схемы этапа C (DRF-2261, DRF-2262): мета-схема, $id, версии, фикстуры."""

    def test_registered_schemas_and_fixtures_are_valid(self) -> None:
        self.assertEqual(validate_all(), [])

    def test_registry_is_not_empty(self) -> None:
        # Пустой реестр сделал бы проверку выше пустой по построению.
        self.assertGreater(len(registered_json_schemas()), 0)


if __name__ == "__main__":
    unittest.main()
