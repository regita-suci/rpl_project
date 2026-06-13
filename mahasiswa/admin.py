from django.contrib import admin
from .models import Mahasiswa

@admin.register(Mahasiswa)
class MahasiswaAdmin(admin.ModelAdmin):
    list_display = ('nim', 'nama', 'programstudi', 'angkatan')
    search_fields = ('nim', 'nama')
    list_filter = ('programstudi', 'angkatan')