from django.contrib import admin
from .models import RetrievalMethod,Okapi_bm25,Peformance,Jelinek_mercer,Dirichlet_prior,Customized_retrieval


# Register your models here.
admin.site.register(RetrievalMethod)
admin.site.register(Okapi_bm25)
admin.site.register(Peformance)
admin.site.register(Jelinek_mercer)
admin.site.register(Dirichlet_prior)
admin.site.register(Customized_retrieval)

