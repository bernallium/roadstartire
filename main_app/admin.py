from django.contrib import admin
from .models import Cart, Tire, CartDetail

# ────────────────────────────────────────────────────────────────────────────────
# list_display - Fields displayed in the list page
# list_editable - Fields that can be editted directly within the list page
# list_filter - Filters in the right sidebar of the list page
# ────────────────────────────────────────────────────────────────────────────────

class CartDetailAdmin(admin.ModelAdmin):
  list_display = (
    'id',
    'cart',
    'tire',
    'price_each',
    'quantity',
    'get_subtotal',
  )

  list_display_links = (
    'id',
    'cart',
  )
  
  list_editable = ('quantity',)

# ────────────────────────────────────────────────────────────────────────────────

class CartDetailInline(admin.TabularInline):
  model = CartDetail
  can_delete = True
  extra = 1 # Number of extra forms the formset will display in addition to the initial forms

  readonly_fields = (
    'price_each', 
    'get_subtotal',
  )
  
# ────────────────────────────────────────────────────────────────────────────────

class CartAdmin(admin.ModelAdmin):
  list_display = (
    'id',
    'user',
    'get_owner',
    'date_ordered',
    'status',
    'discount_ratio_applied',
    'get_item_count',
    'get_total',
  )

  list_display_links = (
    'id',
    'user',
  )

  list_editable = ('status',)

  list_filter = (
    'date_ordered',
    'status',
  )

  search_fields = (
    'id',
    'user',
  )

  readonly_fields = ('get_item_count', 'get_total',)

  inlines = (CartDetailInline,)

# ────────────────────────────────────────────────────────────────────────────────

class TireAdmin(admin.ModelAdmin):
  list_display = (
    'name',
    'brand',
    'year',
    'width',
    'aspect_ratio',
    'rim_size',
    'price',
    'season',
    'current_quantity',
    'total_quantity',
    'sold',
  )

  list_filter = (
    'brand',
    'year',
    'season',
  )

  search_fields = (
    'name',
    'brand',
    'year',
  )

# ────────────────────────────────────────────────────────────────────────────────

# Register your models here
admin.site.register(CartDetail, CartDetailAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Tire, TireAdmin)