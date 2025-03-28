from django.shortcuts import render
import hashlib
from .models import UploadedFile
from .forms import FileUploadForm

# Create your views here.

def home(request):
    return render(request, 'home.html')  # Uses global template folder

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save()
            return render(request, 'upload_success.html', {'file': file})  # Make sure the template path is correct
    else:
        form = FileUploadForm()

    # This line ensures a response is returned for GET requests and invalid forms
    return render(request, 'upload.html', {'form': form})  # Make sure the template path is correct
        
def verify_file(request):
    if request.method == 'POST' and 'file' in request.FILES:
        uploaded_file = request.FILES['file']
        hasher = hashlib.sha256()
        for chunk in uploaded_file.chunks():
            hasher.update(chunk)
        file_hash = hasher.hexdigest()

        # Check if hash exists in database
        try:
            original_file = UploadedFile.objects.get(sha256_hash=file_hash)
            message = "File is intact and unchanged."
        except UploadedFile.DoesNotExist:
            message = "Warning: File integrity compromised or not found."

        return render(request, 'verify_result.html', {'message': message})

    return render(request, 'verify.html')
