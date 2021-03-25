from import_export export resources
from .models import Program
class ProgramResource(resources.ModelResource):
    class Meta:
        model = Program