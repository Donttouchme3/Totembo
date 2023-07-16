from modeltranslation.translator import translator, TranslationOptions
from .models import Product

class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

translator.register(Product, ProductTranslationOptions)