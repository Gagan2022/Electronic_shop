from django.contrib import admin
from general_links.models import Address, Contact, \
	Product, Provider, Factory, Distributor, \
	Dealership, Retailer, Businessman


class AddressAdmin(admin.ModelAdmin):
	list_display = ("country", "city", "street", "num_house")
	search_fields = ("country", "city")


class ContactAdmin(admin.ModelAdmin):
	list_display = ('email', 'address')
	search_fields = ('email', 'address')


class ProductAdmin(admin.ModelAdmin):
	list_display = ("name", "model", "pubdate")
	search_fields = ("name", "model")


class ProviderAdmin(admin.ModelAdmin):
	list_display = ("name",)
	search_fields = ("name",)


class FactoryAdmin(admin.ModelAdmin):
	list_display = ("name", "contact", "product", "provider", "debt", "published")
	search_fields = ("name", "product", "provider")


class DistributorAdmin(admin.ModelAdmin):
	list_display = ("name", "contact", "product", "provider", "debt", "published")
	search_fields = ("name", "product", "provider")


class DealershipAdmin(admin.ModelAdmin):
	list_display = ("name", "contact", "product", "provider", "debt", "published")
	search_fields = ("name", "product", "provider")


class RetailerAdmin(admin.ModelAdmin):
	list_display = ("name", "contact", "product", "provider", "debt", "published")
	search_fields = ("name", "product", "provider")


class BusinessmanAdmin(admin.ModelAdmin):
	list_display = ("name", "contact", "product", "provider", "debt", "published")
	search_fields = ("name", "product", "provider")


admin.site.register(Address, AddressAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Provider, ProviderAdmin)
admin.site.register(Factory, FactoryAdmin)
admin.site.register(Distributor, DistributorAdmin)
admin.site.register(Dealership, DealershipAdmin)
admin.site.register(Retailer, RetailerAdmin)
admin.site.register(Businessman, BusinessmanAdmin)
