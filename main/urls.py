from django.urls import path

from .views import HomePageView, redirect_view, LogoutPageView, LatestPageView, ActionablePageView, TrendingPageView, \
    TopicAreaPageView, InsightUploadPageView, CustomerUploadPageView

urlpatterns = [
    path('', redirect_view, name='login'),
    path('logout', LogoutPageView.as_view(), name='logout'),
    path('insights/latest', LatestPageView.as_view(), name='latest'),
    path('insights/actionable', ActionablePageView.as_view(), name='actionable'),
    path('insights/trending', TrendingPageView.as_view(), name='trending'),
    path('insights/topic/', TopicAreaPageView.as_view(), name='topic'),
    path('insights/upload/', InsightUploadPageView.as_view(), name='insight_upload'),
    path('customers/upload/', CustomerUploadPageView.as_view(), name='customer_upload'),
    path('dashboard/', HomePageView.as_view(), name='home'),
]