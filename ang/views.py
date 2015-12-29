from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.template.defaulttags import register

from besede.models import Nivo

# @login_required
def home(request):
	
	return render_to_response(
        'angindex.html',
        {
          'title'  : "ANGlescina",
        }
        , context_instance=RequestContext(request)
    )
