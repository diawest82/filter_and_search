from django import template

register = template.Library()

groups = ["Silicates", "Oxides", "Sulfates", "Sulfides", "Carbonates", "Halides",
          "Sulfosalts", "Phosphates", "Borates", "Organic Minerals", "Arsenates",
          "Native Elements", "Other"]


@register.inclusion_tag('minerals/mineral_nav.html')
def nav_mineral_list():
    return {'groups': groups}
