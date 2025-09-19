from django.shortcuts import redirect
from django.views.decorators.http import require_GET

@require_GET
def github_redirect(request):
    # Redirect to external site
    return redirect("https://github.com/ds2600/", permanent=False)
