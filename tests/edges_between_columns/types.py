import sys
from docs import ontoweaver


class sample_to_patient(ontoweaver.Edge):
    @staticmethod
    def source_type():
        return docs.ontoweaver.types.sample

    @staticmethod
    def target_type():
        return docs.ontoweaver.types.patient

    @staticmethod
    def fields():
        return []


all = ontoweaver.All(sys.modules[__name__])
