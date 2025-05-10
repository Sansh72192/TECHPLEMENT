from django.shortcuts import render
from django.http import JsonResponse
from .models import Quote
import requests

def index_view(request):
    return render(request, 'quotesapp/index.html')

def get_quote(request):
    author = request.GET.get('author', '').strip().lower()
    quote_data = None

    try:
        if author:
            # Check if quote from this author exists in DB
            stored_quote = Quote.objects.filter(author__icontains=author).first()
            if stored_quote:
                quote_data = {
                    "q": stored_quote.text,
                    "a": stored_quote.author
                }
            else:
                response = requests.get("https://zenquotes.io/api/quotes")
                data = response.json()
                match = next((q for q in data if author in q['a'].lower()), None)
                if match:
                    quote_data = match
        else:
            response = requests.get("https://zenquotes.io/api/random")
            data = response.json()
            quote_data = data[0]

        if quote_data:
            # Save to DB if not already there
            if not Quote.objects.filter(text=quote_data["q"]).exists():
                Quote.objects.create(text=quote_data["q"], author=quote_data["a"])
            return JsonResponse({"quote": quote_data["q"], "author": quote_data["a"]})
        else:
            return JsonResponse({"quote": "No quote found.", "author": ""})
    
    except Exception as e:
        return JsonResponse({"quote": "Could not load quote.", "author": ""})
