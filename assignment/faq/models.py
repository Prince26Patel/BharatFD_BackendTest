from django.db import models
from deep_translator import GoogleTranslator

class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()  # You can use RichTextField if you want rich text support
    question_hi = models.TextField(blank=True, null=True)  # Hindi translation
    question_bn = models.TextField(blank=True, null=True)  # Bengali translation
    language = models.CharField(max_length=10, default='en')  # Field to store the language of the question
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_translated_question(self, lang):
        # Return the translation for the specified language
        if lang == 'hi' and self.question_hi:
            return self.question_hi
        elif lang == 'bn' and self.question_bn:
            return self.question_bn
        return self.question  # Default to original question if no translation exists

    def save(self, *args, **kwargs):
        """Translate the question into Hindi and Bengali if not already translated."""
        # Translate question to Hindi if not already present
        if not self.question_hi:
            self.question_hi = GoogleTranslator(source='auto', target='hi').translate(self.question)

        # Translate question to Bengali if not already present
        if not self.question_bn:
            self.question_bn = GoogleTranslator(source='auto', target='bn').translate(self.question)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.question[:50]
