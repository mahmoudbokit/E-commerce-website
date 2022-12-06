from django.contrib import admin
from .models import Category, Product, Command, Comment

# Register your models here.
admin.site.site_header = "E-commerce"
admin.site.site_title = "Online Shop"
admin.site.index_title = "Administration"


class AdminCategory(admin.ModelAdmin):
    list_display = ('name', 'date_added')
    search_fields = ('name', )


class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'date_added')
    list_filter = ('price', 'category', 'date_added')
    search_fields = ('title', )
    list_editable = ('price', 'category')


class AdminCommand(admin.ModelAdmin):
    list_display = ('items', 'name', 'email', 'address', 'State', 'city', 'zipcode',
                    'totalQuantity', 'totalPrice', 'date_command')
    list_filter = ('items', 'email', 'address', 'State', 'city', 'zipcode',
                   'totalQuantity', 'totalPrice', 'date_command')
    search_fields = ('name', )


class AdminComment(admin.ModelAdmin):
    list_display = ('name', 'comment', 'date_comment')


admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Command, AdminCommand)
admin.site.register(Comment, AdminComment)