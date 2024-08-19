from .models import Book
from .serializers import BookSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# class BookListAPIView(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookListAPIView(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        data = {
            "status": f"Returned {len(books)} books",
            "books": serializer_data
        }
        return Response(data)

# class BookDetalView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
    
class BookDetalView(APIView):

    def get(selF, request, pk):
        try:
            book = Book.objects.get(id = pk)
            serializer_data = BookSerializer(book).data 

            data = {
                'status': 'Successful',
                'book': serializer_data
            }

            return Response(data, status=status.HTTP_200_OK)
        except Exception:
            return Response({"status": "Does not exist",
                             'message': 'Book is not found'}, 
                             status=status.HTTP_404_NOT_FOUND)

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# class BookCreateApiView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookCreateApiView(APIView):

    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = {'status': f"Books are saved to the database",
                    'books': data
                    }
            return Response(data)
        else:
            return Response({'status': False,
                             'message': 'Serialazer is not valid'}, 
                             status=status.HTTP_400_BAD_REQUEST)

class BookListCreateApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
# @api_view(['GET'])
# def book_list_view(request, *args, **kwargs):
#     books = Book.objects.all()
#     serializer = BookSerializer(books, many=True)
#     return Response(serializer.data)