from django.contrib import admin
from cip.models import bienAmbiente, bienPersonal, bienpat,dependencia,ambiente,personal, bienImag,certiDigital

# Register your models here.

class imagenInline(admin.TabularInline):
    model = bienImag

class bienpatAdmin(admin.ModelAdmin):
    list_display = ('codEti','desBien','serBien','modBien','marBien','situBien','valBien','estBien')
    search_fields = ('codEti',)
    inlines = [imagenInline]

class dependenciaAdmin(admin.ModelAdmin):
    list_display = ('codDep','descDep')
    search_fields = ('codDep',)

class ambienteAdmin(admin.ModelAdmin):
    list_display = ('codAmb','descAmb','dependencia')
    search_fields = ('codAmb',)

class personalAdmin(admin.ModelAdmin):
    list_display = ('dniPer','apePatPer','apeMatPer','nomPer','codPlaPer','fecNacPer','estPer')
    search_fields = ('codPlaPer','dniPer')

class bienPersonalAdmin(admin.ModelAdmin):
    list_display = ('personal','bienpat')

class bienAmbienteAdmin(admin.ModelAdmin):
    list_display = ('ambiente','bienpat')

class certiDigitalAdmin(admin.ModelAdmin):
    list_display = ('personal','fecOtor','fecLimInsta','fecInsta','fecVenci','obsCerti','tipoCerti')
    search_fields = ('obsCerti',)

    
admin.site.register(personal, personalAdmin)
admin.site.register(bienpat, bienpatAdmin)
admin.site.register(dependencia, dependenciaAdmin)
admin.site.register(ambiente, ambienteAdmin)
admin.site.register(bienPersonal, bienPersonalAdmin)
admin.site.register(bienAmbiente, bienAmbienteAdmin)
admin.site.register(certiDigital, certiDigitalAdmin)
