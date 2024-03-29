from django.contrib import admin
from django.urls import path, include  # include fonksiyonunu eklemeyi unutmayın
from myapp.views import hello_world  # Direkt hello_world görünümünü import edin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include('myapp.urls')),  # myapp uygulaması için
    path('', hello_world, name='hello_world'),  # Kök URL için
]
