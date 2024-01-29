from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def restricted_view(request):
    # Kod widoku, który wymaga zalogowania
    return render(request, 'core/restricted.html')