
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/',include('product.urls')),
    path('group/',include('group.urls')),
    path('orm/',include('orm.urls')),
    path('Employee/',include('Employee.urls')),
    path('cbv/',include('cbv.urls')),
    path('Task/',include('Task.urls')),
    path('ticket/',include('ticket.urls')),
    path('exam/',include('exam.urls')),
    path('serviceprovider/',include('serviceprovider.urls')),
    
]
