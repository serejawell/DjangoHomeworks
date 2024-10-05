from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    VersionCreateView, VersionUpdateView, VersionDeleteView, VersionDetailView, VersionListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('products/version/create', VersionCreateView.as_view(), name='version_create'),
    path('products/version/update/<int:pk>', VersionUpdateView.as_view(), name='version_update'),
    path('products/version/<int:pk>/delete', VersionDeleteView.as_view(), name='version_delete'),
    path('products/version/<int:pk>/detail', VersionDetailView.as_view(), name='version_detail'),
    path('products/verion/list', VersionListView.as_view(), name='version_list'),
]
