from Entity.Suggestion import Suggestion as Suggestion
import Dao.db_operate as executor


class Suggestion_Dao:
    def __init__(self):

        self.table_name = "suggestion"
        self.executor = executor.DB_Operate()

    def save_entity(self, suggestion):
        self.executor.save_entity(suggestion)

    def save_entities(self, suggestions):
        for suggestion in suggestions:
            self.executor.save_entity(suggestion)

    def get_entity_rewrite(self, suggestion_id):
        suggestion = Suggestion()
        suggestion_container = self.executor.get_entity(suggestion_id, suggestion)
        return suggestion_container

    def get_count(self):
        count = self.executor.get_count(self.table_name)
        return count

    def rand_get(self):
        suggestion = Suggestion()
        suggestion_container = self.executor.rand_get(suggestion, 7)
        return suggestion_container

    def get_all(self):
        suggestion = Suggestion()
        suggestion_container = self.executor.get_all(suggestion)
        return suggestion_container

    def get_by_key(self, key, key_value):
        suggestion = Suggestion()
        suggestion_container = self.executor.get_by_key(entity=suggestion, key=key, key_value=key_value)
        return suggestion_container

    def delete_by_id(self, id):
        suggestion = Suggestion()
        return self.executor.delete_by_id(suggestion, id)
