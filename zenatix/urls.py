from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from inventory.views import BakeryItemListViewSet, BakeryItemDetailViewSet, IngredientViewSet, BakeryItemIngredientView, BakeryItemPopularListViewSet
from order.views import OfferViewSet
from django.views.decorators.csrf import csrf_exempt


router = DefaultRouter()
router.register(r'item/view/popular',
                BakeryItemPopularListViewSet, basename='popular_item_view')
router.register(r'item/view', BakeryItemListViewSet, basename='item_view')
router.register(r'item', BakeryItemDetailViewSet, basename='item_update')
router.register(r'ingredient', IngredientViewSet, basename='ingredient_view')
router.register(r'offer', OfferViewSet, basename='offer_view')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth.urls')),
    path('order/', include('order.urls')),
    path('item/ingredient/', BakeryItemIngredientView.as_view()),
    path('', include(router.urls)),
    # path('item/', BakeryItemDetailViewSet),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
