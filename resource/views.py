from django.shortcuts import render, redirect, get_object_or_404
from django.http import FileResponse
from .forms import PDFFileForm
from .models import PDFFile

def resource(request):
    pdf_files = PDFFile.objects.all()  # Отримуємо всі PDF-файли з бази даних
    if request.method == 'POST':
        form = PDFFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = PDFFileForm()

    return render(request, 'main/resources.html', {'form': form, 'pdf_files': pdf_files})


def download_pdf(request, pk):
    pdf_file = get_object_or_404(PDFFile, pk=pk)
    response = FileResponse(pdf_file.file, as_attachment=True)
    return response

