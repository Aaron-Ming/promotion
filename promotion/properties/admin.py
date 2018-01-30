# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from promotion.properties.models import Category, Assets, AssetsImg, Comment

# Register your models here.

class AssetsImgline(admin.TabularInline):
    model = AssetsImg

class AssetsAdmin(admin.ModelAdmin):
    list_display = ('title', 'bond_institution', 'contacts', 'guarantee', 'pub_time', 'debt_type')
    search_fields = ('title', 'debt_type', 'contacts')
    inlines = [AssetsImgline]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'id')
    search_fields = ('category_name',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'assets', 'content', 'c_time')
    search_fields = ('assets', 'author', 'c_time')


admin.site.register(Assets, AssetsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)