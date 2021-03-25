from django.shortcuts import render, redirect
from django.http import HttpResponse
from admindashboard.resources import ProgramResource

def file_upload (request):
    if request.method == 'POST':
        program_resource = ProgramResource()
        dataset = program_resource.export()
        new_programs = request.FILES['myFile']
        imported_data = dataset.load(new_programs.read())
        result = program_resource.import_data(imported_data, dry_run = True)
        
        if not result.has_errors():
            program_resource.import_data(imported_data, dry_run = False)


# Create your views here.
