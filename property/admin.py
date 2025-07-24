from django.contrib import admin

from .models import Flat, Complaint, Owner


class SearchAdmin(admin.ModelAdmin):
    search_fields = ('owner', 'town', 'address')
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building',
                    'construction_year', 'town']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ['liked_by']


class ComplaintAboutFlat(admin.ModelAdmin):
    raw_id_fields = ['flat']


class ApartmentsOwned(admin.ModelAdmin):
    # list_display = ['owner']
    raw_id_fields = ['apartments_owned']


admin.site.register(Flat, SearchAdmin)
admin.site.register(Complaint, ComplaintAboutFlat)
admin.site.register(Owner, ApartmentsOwned)
