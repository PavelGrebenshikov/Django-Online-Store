from django import template
from main.models import Category, Slider, VariousDetails


register = template.Library()

@register.inclusion_tag('main/list_category.html')
def show_category():
    category = Category.objects.all()
    return {"Category": category}

@register.inclusion_tag('main/list_slider_pictures.html')
def show_sliders():
    picture_slider = Slider.objects.all()
    return {'Sliders': picture_slider}


@register.inclusion_tag('main/various_details.html')
def show_various_details():
    return {'VariousDetails': VariousDetails.objects.all()}
