import random
from base.models import Company, Service

def custom_context(request):
    company = Company.objects.first()
    services = list(Service.objects.values('name', 'slug').order_by('-created_at', '-updated_at'))

    icons = [
        'icofont-money',
        'icofont-coins',
        'icofont-bank-alt',
        'icofont-chart-growth',
        'icofont-chart-line-alt',
        'icofont-rocket-alt-1',
        'icofont-building-alt',
        'icofont-briefcase-2',
        'icofont-calculator-alt-1',
        'icofont-investment',
        'icofont-hand-power',
        'icofont-business-man',
        'icofont-dollar-true',
        'icofont-credit-card',
        'icofont-dashboard-web'
    ]
    random_icon = random.choice(icons)
    
    return {
        "company": company,
        "services": services,
        "random_icon": random_icon
    }