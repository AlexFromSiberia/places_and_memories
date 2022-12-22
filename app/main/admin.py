from django.contrib import admin
from .models import Memory
from django.utils.safestring import mark_safe
from .forms import MemoryForm


class MemoriesAdmin(admin.ModelAdmin):
    """setting up Memories look in admin panel """
    form = MemoryForm
    save_as = True
    # fields you can see on main screen
    list_display = ('id', 'owner', 'place', 'slug', 'photo',  'get_photo', 'date_added')
    # fields - links
    list_display_links = ('owner', 'place')
    # fields for search
    search_fields = ('id', 'owner', 'place')
    # fields with filter
    list_filter = ('owner', 'place', 'date_added')
    # fields we can see in every entry
    fields = ('id', 'owner', 'place', 'text', 'slug',  'photo', 'get_photo', 'date_added')

    readonly_fields = ('id', 'date_added',  'get_photo')
    # put one more "save" button
    save_on_top = True
    # slug field will be added automatically
    prepopulated_fields = {'slug': ('place',)}

    # add special function:
    def get_photo(self, obj):
        # избежать ошибки если фото не существует
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return '-'

    get_photo.short_description = 'Thumbnail'


admin.site.register(Memory, MemoriesAdmin)

