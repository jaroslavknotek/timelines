import json

import shared_code.note_model as nm
from azure.data.tables import TableClient, UpdateMode


def _load_connection_string():
    with open("local.settings.json", "r") as f:
        config = json.load(f)
        return config["StorageAccountConnectionString"]


class NotesClient:
    def __init__(self, connection_string, table_name="showmenotes"):
        self.connection_string = connection_string
        self.table_name = table_name

    def _get_client(self):
        return TableClient.from_connection_string(
            conn_str=self.connection_string, table_name=self.table_name
        )

    def remove_all(self):
        entities = self._read_all_entities()
        with self._get_client() as table_client:
            for entity in entities:
                table_client.delete_entity(
                    row_key=entity["RowKey"], partition_key=entity["PartitionKey"]
                )

    def _read_all_entities(self) -> list[dict]:
        with self._get_client() as table_client:
            return list(table_client.list_entities())

    def read_all(self) -> list[nm.Note]:
        entities = self._read_all_entities()
        return [nm.from_entity(e) for e in entities]

    def upsert_notes(self, notes: list[nm.Note]):
        entities = (nm.to_entity(note) for note in notes)
        with self._get_client() as table_client:
            [
                table_client.upsert_entity(mode=UpdateMode.REPLACE, entity=e)
                for e in entities
            ]
