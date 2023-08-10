import datetime

from django.contrib import admin

from advertisements.settings import STATIC_URL
from .models import Advertisement
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.utils import timezone

tz = timezone.get_default_timezone()
now_date = datetime.datetime.now().astimezone(tz).strftime("%d.%m.%Y")

# Register your models here.


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'get_image', 'price', 'auction', 'get_created_at', 'get_updated_at']
    list_filter = ['auction', 'created_at']
    actions = ['make_auction_as_false','make_auction_as_true']
    fieldsets = (
        ('Общее', {
            'fields': ('title', 'description', 'image'),
        }),
        ('Финансы', {
            'fields': ('price', 'auction'),
            # 'classes': ['collapse']
        })
    )
    readonly_fields = ('created_at', 'updated_at')
    list_per_page = 10

    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)

    def get_image(self, obj):
        default_image = '/'+STATIC_URL+'img/abc.png'
        if obj.image:
            return format_html(f'<img src={obj.image.url} width=50')
        else:
            return format_html(f'<img src={default_image} width=50')

    def get_created_at(self, obj):
        add_date = obj.created_at.astimezone(tz)
        if now_date == add_date.strftime("%d.%m.%Y"):
            return mark_safe(f'<font color="#000080">Сегодня в {add_date.strftime("%H:%M")}</font>')
        else:
            return add_date

    def get_updated_at(self, obj):
        upd_date = obj.updated_at.astimezone(tz)
        if now_date == upd_date.strftime("%d.%m.%Y"):
            return mark_safe(f'<font color="#000080">Сегодня в {upd_date.strftime("%H:%M")}</font>')
        else:
            return upd_date

    # print(dir(obj.updated_at))
    # return mark_safe(f'<font color="#000080">{obj.updated_at.astimezone(tz).strftime("%d.%m.%Y %H:%M")}</font>')

    get_image.short_description = 'Фото'
    get_updated_at.short_description = 'Обновлено'
    get_created_at.short_description = 'Дата создания'


admin.site.register(Advertisement, AdvertisementAdmin)

admin.site.site_title = 'Админ-панель'
admin.site.site_header = 'Админ-панель'