from modeltranslation.translator import register,TranslationOptions
from .models import *

@register(Catigorya)
class Catigorya(TranslationOptions):
    fields=('name',)

@register(Product)
class Product(TranslationOptions):
    fields=('name','text',)

@register(Checkout)
class Checkout(TranslationOptions):
    fields=('first_name','last_name','adres','sity','country','zip_code',)


@register(Tek)
class Tek(TranslationOptions):
    fields=('text','ism',)

