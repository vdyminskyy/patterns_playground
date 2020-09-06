import yaml

from factory_method_rp import serializers


class YamlSerializer(serializers.JsonSerializer):
    def to_str(self):
        return yaml.dump(self._current_object)


serializers.factory.register_format('YAML', YamlSerializer)
