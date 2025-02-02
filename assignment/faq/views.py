from rest_framework import generics
from .models import FAQ
from .serializers import FAQSerializer

class FAQListCreateView(generics.ListCreateAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def get_serializer_context(self):
        """
        Pass the 'lang' query parameter to the serializer context.
        This will allow us to dynamically get the translated question based on the language selected in the request.
        """
        context = super().get_serializer_context()
        context['request'] = self.request  # Pass the request so that we can access query parameters in the serializer
        return context

    def perform_create(self, serializer):
        """
        Perform custom save to handle language when creating a new FAQ.
        """
        language = self.request.data.get('language', 'en')  # Default to 'en' if no language is provided
        faq = serializer.save(language=language)  # Save FAQ instance with the selected language
        faq.save()  # Ensure save method is called again to apply translations if needed
        return faq

class FAQDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    lookup_field = 'id'  # 'id' is fine if you're using it explicitly; otherwise, you can use 'pk'

    def get_serializer_context(self):
        """
        Pass the 'lang' query parameter to the serializer context for the detail view as well.
        This will allow the translation to be applied when retrieving the FAQ.
        """
        context = super().get_serializer_context()
        context['request'] = self.request  # Pass the request so that we can access query parameters in the serializer
        return context
