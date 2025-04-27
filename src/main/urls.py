from django.urls import path
from main.views import TolcToCharacterStreamView, chat_page, home, locker_view, wishlist_view, delete_wishlist_item


urlpatterns = [
    path('', home, name = 'home'),
    path('chat/', chat_page, name='chat'),
    path('cosmetics/', locker_view, name = 'cosmetics'),
    path('wishlist/', wishlist_view, name = 'wishlist'),
    path('wishlist/delete/<int:item_id>/', delete_wishlist_item, name='delete-wishlist-item'),
    path('api/tolc_to_character_stream/', TolcToCharacterStreamView.as_view(), name='chat-stream')
]
