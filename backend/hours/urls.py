"""hours URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from main import views
from expenses import views as expense_views
from access import views as access_views
from dollars import views as dollar_views
from django.views.static import serve

# router.register(r'tasks', views.getTasksView(), basename='tasks')

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('tasks/', views.getTasksView),
    path('gdocs/', views.getGdocsStructure),
    path('updatesheet/', views.writeGdocs),
    path('expenses/', expense_views.getExpenses),
    path('expenses/<int:expense_id>/', expense_views.operateExpense),
    path('expensesoptions/', expense_views.Expensesoptions.as_view()),
    path('payments/', expense_views.Payments.as_view()),
    path('payments/<int:payment_id>/', expense_views.Payments.as_view()),
    path('access/', access_views.Access.as_view()),
    path('access/<int:access_id>/', access_views.Access.as_view()),
    path('dollars/', dollar_views.Dollars.as_view()),
    path('dollars/<int:movement_id>/', dollar_views.Dollars.as_view()),
    path('source/', dollar_views.Source.as_view()),
    path('source/<int:source_id>/', dollar_views.Source.as_view()),
    path('movementDetails/', dollar_views.MovementDetails.as_view()),
    path('movementDetails/<int:movement_detail_id>/', dollar_views.MovementDetails.as_view())
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)