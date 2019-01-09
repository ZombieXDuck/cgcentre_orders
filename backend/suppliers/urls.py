from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from suppliers import views

app_name = 'suppliers'
urlpatterns = [
    path('', views.SuppliersView.as_view()),
    path('<int:supplierId>', views.SupplierView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
