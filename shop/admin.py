from django.contrib import admin
from .models import Medicine, Category

# 1. Kategoriyalarni ro'yxatdan o'tkazish
admin.site.register(Category)

# 2. Dorilarni ro'yxatdan o'tkazish (Chiroyli ko'rinishda)
@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    search_fields = ('name',)
    list_filter = ('category',) # Kategoriyalar bo'yicha filter qilish uchun