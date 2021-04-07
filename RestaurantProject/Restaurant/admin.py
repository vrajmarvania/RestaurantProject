from django.contrib import admin
from .models import Admin_Register,User_Register, Restaurant_sales, overall_sales, Food, RestaurantData, Restaurantl, Product, Ordert

admin.site.register(Admin_Register)
admin.site.register(Restaurant_sales)
admin.site.register(overall_sales)
admin.site.register(Food)
admin.site.register(RestaurantData)
admin.site.register(Restaurantl)
admin.site.register(Ordert)
admin.site.register(Product)
admin.site.register(User_Register)



