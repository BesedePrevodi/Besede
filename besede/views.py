from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.template.defaulttags import register
from django.shortcuts import render
import random

from besede.models import Nivo
from besede.models import Sklop
from besede.models import Beseda
from besede.forms import NivoForm
from besede.forms import SklopForm
from besede.forms import BesedaForm

def napaka(request, msg):
	return render(request, 'napaka.html', 
    	{
    	  'napaka'    : msg,
        }
    )

# @login_required
def vpisN(request):
	# ce je bila metoda klicana preko forme (nov vpis),
	# nov nivo vpisem v bazo
	if request.method == 'POST':        
		nivo = NivoForm(request.POST)
		try:
   		  if nivo.is_valid():
			nID        = nivo.cleaned_data['nID']
			akcija     = nivo.cleaned_data['akcija']
			imeNivoja  = nivo.cleaned_data['nivo']
			if akcija == "ADD":
				n = Nivo(ime_nivoja = imeNivoja)
				n.save()
			elif akcija == "DEL":
				Nivo.objects.filter(id=nID).delete()
		except:
			return napaka(request, "Napaka pri definiciji nivoja")
        	

	# nato preberem vse nivoje in jih izpisem
	nivoji = list(Nivo.objects.all())

	return render(request, 'vpisN.html', 
    	{
          'nivoji'  : nivoji,
        }
    )

# @login_required
def vpisS(request):
	nID = 0
	if request.method == 'POST':        
		sklop = SklopForm(request.POST)
		if sklop.is_valid():
			nID       = sklop.cleaned_data['nID']
			sID       = sklop.cleaned_data['sID']
			imeSklopa = sklop.cleaned_data['sklop']
			akcija    = sklop.cleaned_data['akcija']
			if akcija == "ADD":
				parentNivo = Nivo.objects.get(id=nID)
				s = Sklop(ime_sklopa=imeSklopa, nivo=parentNivo)
				s.save()
			elif akcija == "DEL":
				Sklop.objects.filter(id=sID).delete()
		else:
			return napaka(request, "Vpisi ime sklopa!")
	else:
		nID = request.GET.get('nID', 0)

	try:
	  parentNivo = Nivo.objects.get(id=nID)
	  sklopi = list(Sklop.objects.filter(nivo=parentNivo))	
	except:
	  return napaka(request, "Neznan sklop!")
	return render(request, 'vpisS.html', 
    	{
    	  'nID'       : nID,
    	  'imeNivoja' : parentNivo.ime_nivoja,
          'sklopi'    : sklopi,
        }
    )

# @login_required
def vpisB(request):
	sID = 0
	if request.method == 'POST':        
		beseda = BesedaForm(request.POST)
		try:
		  if beseda.is_valid():
			sID       = beseda.cleaned_data['sID']
			bID       = beseda.cleaned_data['bID']
			iBeseda   = beseda.cleaned_data['beseda']
			iPrevod   = beseda.cleaned_data['prevod']
			iOpis     = beseda.cleaned_data['opis']
			akcija    = beseda.cleaned_data['akcija']			
			if akcija == "ADD":
				parentSklop = Sklop.objects.get(id=sID)

				b = Beseda(
					  sklop  = parentSklop, beseda = iBeseda,
					  prevod = iPrevod,     opis   = iOpis
					)
				b.save()
			elif akcija == "DEL":
				Beseda.objects.filter(id=bID).delete()
		except:
			return napaka(request, "Narobe definirana beseda")
	else:
		sID = request.GET.get('sID', 0)

	try:
	  parentSklop = Sklop.objects.get(id=sID)
  	  besede = list(Beseda.objects.filter(sklop=parentSklop))
  	  imeSklopa = parentSklop.ime_sklopa
  	  imeNivoja = parentSklop.nivo.ime_nivoja	
	except:
		return napaka(request, "Vpisi besedo in prevod")	    

	return render(request, 'vpisB.html', 
    	{
    	  'sID' : sID,
    	  'nID' : parentSklop.nivo.id,
    	  'imeSklopa' : imeSklopa,
    	  'imeNivoja' : imeNivoja,
    	  'besede'    : besede
        }
    )


# @login_required
def kviz(request):
	nivoji = list(Nivo.objects.all())

	return render(request, 'kvizA.html', 
    	{
           'nivoji'  : nivoji,
        }
    )

# @login_required
def kvizB(request):
	try:
	  nID        = request.GET.get('nID', 0)	
	  parentNivo = Nivo.objects.get(id=nID)
	  sklopi     = list(Sklop.objects.filter(nivo=parentNivo))	
	except:
	  return napaka(request, "Neznan nivo!")

	return render(request, 'kvizB.html', 
    	{
    	   'nivo'    : parentNivo,
    	   'nID'     : nID,
           'sklopi'  : sklopi,
        }
    )

# @login_required
def kvizC(request):
	try:
	  nID        = request.GET.get('nID', 0)	
	  qNo        = request.GET.get('qNo', 0)
	  sklops     = request.GET.get('sklops', 0)

	  if (sklops == "/"):
	  	sklopi = []
	  else:
	  	sklopi     = map(int, sklops.split(":"));

	  besede     = list(Beseda.objects.all())
  	  besede     = [x for x in besede if (x.sklop.id in sklopi)]

  	  qNo = min(int(qNo), len(besede))


  	  selBes = random.sample(besede, qNo)

	except :
	  return napaka(request, "Napaka - " + e)

	return render(request, 'kvizC.html', 
    	{
    	   'nID'     : nID,
           'qNo'     : qNo,
           'sklopi'  : sklopi,
           'besede'  : selBes,
        }
    )
