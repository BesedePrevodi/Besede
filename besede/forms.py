from django import forms

class NivoForm(forms.Form):
    nID    = forms.IntegerField(label='nID')
    nivo   = forms.CharField(label='Nivo',   max_length=100)
    akcija = forms.CharField(label='Akcija', max_length=100)

class SklopForm(forms.Form):
    nID    = forms.IntegerField(label='nID')
    sID    = forms.IntegerField(label='sID')
    sklop  = forms.CharField(label='Sklop',  max_length=100)
    akcija = forms.CharField(label='Akcija', max_length=100)

class BesedaForm(forms.Form):
    sID    = forms.IntegerField(label='sID')
    bID    = forms.IntegerField(label='bID')
    beseda = forms.CharField(label='Beseda',  max_length=100)
    prevod = forms.CharField(label='Prevod',  max_length=100)
    opis   = forms.CharField(label='Opis',    max_length=100)
    akcija = forms.CharField(label='Akcija',  max_length=100)
