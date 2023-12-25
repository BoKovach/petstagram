from django.contrib import admin

from petstagram.common.models import Comment
from petstagram.pets.models import Pet, Like


class LikeInLine(admin.TabularInline):
    model = Like


class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'age')
    list_filter = ('type', "age")
    inlines = (
        LikeInLine,
    )


admin.site.register(Pet, PetAdmin)
admin.site.register(Like)
admin.site.register(Comment)
