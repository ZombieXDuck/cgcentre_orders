from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from suppliers import views

app_name = 'suppliers'
urlpatterns = [
    path('', views.SupplierList.as_view()),
    path('<int:supplierId>', views.SupplierItemList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
