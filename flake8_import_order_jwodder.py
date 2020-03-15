from flake8_import_order.styles import AppNexus, Google

class JWodder(AppNexus):
    @staticmethod
    def sorted_names(names):
        return sorted(names)

    @staticmethod
    def import_key(import_):
        modules = [Google.name_key(module) for module in import_.modules]
        return (import_.type, import_.level, modules, import_.names)
