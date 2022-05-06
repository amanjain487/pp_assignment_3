from crud_api.viewsets import AuthorViewset, BookViewset, GenreViewset, RentedBooksViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('books', BookViewset)
router.register('authors', AuthorViewset)
router.register('genre', GenreViewset)
router.register('rent', RentedBooksViewset)
