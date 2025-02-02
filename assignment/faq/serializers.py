from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    translated_question = serializers.SerializerMethodField()
    language = serializers.ChoiceField(choices=['en', 'hi', 'bn'], required=False, default='en')

    class Meta:
        model = FAQ
        fields = ['id', 'question', 'translated_question', 'answer', 'language']

    def get_translated_question(self, obj):
        # Get the language from the query parameter, default to 'en'
        lang = self.context.get('request').query_params.get('lang', 'en')
        return obj.get_translated_question(lang)

    def create(self, validated_data):
        """Override the create method to handle language selection"""
        language = validated_data.pop('language', 'en')  # Default to 'en' if no language is provided
        faq = FAQ.objects.create(**validated_data)
        
        # Translate and save based on the selected language
        faq.save()  # This triggers the translation
        return faq
