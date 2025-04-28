from django.shortcuts import get_object_or_404, redirect, render
from django.conf import settings
from django.http import StreamingHttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from config.utils.character_chat_bot import ai_tolc
from config.utils.fort_season_chat_bot import history_tolc


import os
import csv

from main.models import UserLockerItem

from django.shortcuts import render
from .models import UserLockerItem

def home(request):
    return render(request, 'home.html')

def chat_page(request):
    outfits = UserLockerItem.objects.filter(user = request.user, item_type = 'outfit')
    return render(request, 'chat.html', {'outfits': outfits})



def wishlist_view(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        item_image_url = request.POST.get('item_image_url')
        item_video_url = request.POST.get('item_video_url')
        item_type = request.POST.get('item_type')

        UserLockerItem.objects.get_or_create(
            user=request.user,
            name=item_name,
            defaults={
                'image_url': item_image_url,
                'video_url': item_video_url,
                'item_type': item_type,
            }
        )
    
    # Get category filter from URL parameter
    category = request.GET.get('category', 'all')
    
    # Filter items based on category
    if category and category != 'all':
        locker_items = UserLockerItem.objects.filter(user=request.user, item_type=category)
    else:
        locker_items = UserLockerItem.objects.filter(user=request.user)
    
    return render(request, 'wishlist.html', {
        'locker_items': locker_items,
        'category': category
    })

def delete_wishlist_item(request, item_id):
    if request.user.is_authenticated:
        item = get_object_or_404(UserLockerItem, id=item_id, user=request.user)
        item.delete()
    
    category = request.GET.get('category', 'all')
    return redirect(f'/wishlist/?category={category}')

def locker_view(request):
    cards = []
    category = request.GET.get('category', 'outfit')  
    

    csv_files = {
        'outfit': 'outfits.csv',     
        'emote': 'updated_emotes.csv',        
        'pickaxe': 'updated_pickaxes.csv',     
        'backpack': 'backpack.csv',
        'glider': 'gliders.csv'        
    }
    

    csv_filename = csv_files.get(category, csv_files['outfit'])
    csv_path = os.path.join(settings.BASE_DIR, 'static', 'cards_csv', csv_filename)
    

    if not os.path.exists(csv_path):
        csv_path = os.path.join(settings.BASE_DIR, 'static', 'cards_csv', 'fortnite.csv')
    
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:

            img_src = row['item-icon-img src']
            
            img_src = img_src.strip()
            
            fallback_url = 'https://placehold.co/150x150/114a5a/FFF?text=' + row['item-icon-name'].replace(' ', '+')
            
            cards.append({
                'href': row['item-icon href'],
                'img_src': img_src,
                'fallback_src': fallback_url,
                'name': row['item-icon-name'],
                'category': category,  
            })
    
    return render(request, 'cosmetics.html', {
        'cards': cards,
        'current_category': category
    })



class TolcToCharacterStreamView(View):
    def get(self, request):
        character = request.GET.get("character", "Jonesy")
        prompt = request.GET.get("prompt", "Hello")
        stream = ai_tolc(character, prompt)
        response = StreamingHttpResponse(stream, content_type='text/event-stream')
        return response  
    

