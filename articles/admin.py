from django.contrib import admin
from .models import Article, Tag, Scope
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main_true = []
        for form in self.forms:
            if form.cleaned_data.get('is_main') == True:
                is_main_true.append(True)
        if len(is_main_true) > 1:
            raise ValidationError('Основным может быть только один раздел')
        elif len(is_main_true) < 1:
            raise ValidationError('Укажите основной раздел')                
        return super().clean()

class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 1
    formset = ScopeInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']
    list_filter = ['published_at']
    inlines = [ScopeInline,]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']