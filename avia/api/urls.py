# from django.urls import include, path
# from rest_framework.routers import DefaultRouter

# from api import views

# app_name = 'api'
# router_v1 = DefaultRouter()
# router_v1.register('category', CategoryViewSet, 'category')
# router_v1.register('item', ItemViewSet, 'item')
# router_v1.register('name', NameViewSet, 'name')

# urlpatterns = [
#     path('v1/post_items_serial/<name_id>/',
#          PostItemsSerialViews.as_view(), name='post_items_serial'),
#     path('v1/delete_items_serial/',
#          DeleteItemsSerialViews.as_view(), name='delete_items_serial'),
#     path('v1/alt_delete_items_serial/',
#          AltDeleteItemsSerialViews.as_view(), name='alt_delete_items_serial'),
#     path('v1/', include(router_v1.urls)),
# ]
