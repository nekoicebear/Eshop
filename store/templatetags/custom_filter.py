from django import template

register = template.Library()

@register.filter(name='currency')
def currency(number):
    return str(number)+"원"

@register.filter(name='multiply')
def multiply(number , number1):
    return number * number1

#여기는 상품 보여지는 원 부분이다.