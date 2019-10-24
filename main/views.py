from django.views.generic import TemplateView
from django.shortcuts import redirect, render


class HomePageView(TemplateView):
        template_name = 'home.html'


class LogoutPageView(TemplateView):
    template_name = 'logout.html'


class LatestPageView(TemplateView):
    template_name = 'insights/latest.html'


class ActionablePageView(TemplateView):
    template_name = 'insights/actionable.html'


class TrendingPageView(TemplateView):
    template_name = 'insights/trending.html'


class TopicAreaPageView(TemplateView):
    template_name = 'insights/topic.html'


class InsightUploadPageView(TemplateView):
    template_name = 'insights/upload.html'


class CustomerUploadPageView(TemplateView):
    template_name = 'customers/upload.html'


def redirect_view(request):
    if request.user.is_authenticated:
        response = render(request, 'home.html')
    else:
        response = redirect('accounts/login')
    return response
