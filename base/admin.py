from django.contrib import admin

from base.models import Blog, BlogVisit, Company, Faq, Service

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic Details', {
            'fields': ('name', 'logo', 'phone', 'email', 'address','location'),
        }),
        ('Mission', {
            'fields': ('mission',),
        }),
        ('Vision', {
            'fields': ('vision',),
        }),
        ('Social Media', {
            'fields': ('facebook', 'twitter', 'linkedin', 'instagram'),
        }),
    )
    list_display = ('name', 'phone', 'email', 'updated_at')
    search_fields = ('name', 'phone', 'email')

admin.site.register(Company, CompanyAdmin)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']
    search_fields = ['name']
    list_filter = ['created_at', 'updated_at']
    prepopulated_fields = {'slug': ('name',)}

class BlogVisitInline(admin.TabularInline):
    model = BlogVisit
    extra = 1

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'category', 'created_at', 'updated_at')
    search_fields = ['name', 'author__username']
    list_filter = ['created_at', 'updated_at']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [BlogVisitInline]

# Register BlogVisit if you want it to be accessible as a standalone model as well
# @admin.register(BlogVisit)
class BlogVisitAdmin(admin.ModelAdmin):
    list_display = ['blog', 'ip_address', 'user_agent', 'timestamp']
    search_fields = ['ip_address', 'user_agent']
    list_filter = ['timestamp']


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ['question','category']
    search_fields = ['question','category']
    list_filter = ['created_at', 'updated_at']