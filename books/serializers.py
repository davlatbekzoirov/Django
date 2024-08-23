from rest_framework import serializers
from .models import Book
from rest_framework.exceptions import ValidationError

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'title', 'content', 'subtitle', 'author', 'isbn', 'price')

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)

        if not title.isalpha():
            raise ValidationError(
                {
                    "status": False,
                    "message": "Kitobni sarlavhasi harflardan tashkil topgan bo'lishi kerak"  
                }
            )
        
        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {
                    "status": False,
                    "message": "Kitobni sarlavhasi va muallifi bir xil bo'lgan kitobni yuklay olmaysiz"  
                }
            )
        return data
    
    def validate_price(self, price):
        if price < 0 or price > 999999999999:
            raise ValidationError(
                {
                    "status": False,
                    "message": "Narx Noto'gri kiritilgan"  
                }
            )


# class CashSerializer(serializers.Serializer):
#     input = serializers.CharField(max_length = 200)
#     output = serializers.CharField(max_length = 150)
#     subtitle = serializers.CharField()