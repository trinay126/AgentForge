# utils/registr.py
# Global registry for tools and agents.

class Registry:
    """
    Global registry for tools and agents.
    Supports duck typing - anything with .name works.
    """

    def __init__(self, registry_type="generic"):
        self.registry_type  = registry_type
        self._items = {}

    def register(self, item):
        """Register any item that has a .name attribute."""
        if not hasattr(item, "name"):
            raise ValueError("Item must have a 'name' attribute")
        name = item.name if not callable(item.name) else item.name
        self._items[name] = item
        return item

    def get(self, name, default=None):
        return self._items.get(name, default)

    def all_names(self):
        return list(self._items.keys())

    def all_items(self):
        return list(self._items.values())

    def remove(self, name):
        if name in self._items:
            del self._items[name]
            