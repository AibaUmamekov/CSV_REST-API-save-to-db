from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status, mixins, serializers, generics
from .serializers import FileSerializer, DealSerializer
from .models import Deals, File
import csv, io


class DealsView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    serializer_class = FileSerializer
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        file = request.FILES['file']
        decoded_file = file.read().decode('utf-8')
        io_string = io.StringIO(decoded_file)
        reader = csv.reader(io_string)
        for fields in reader:
            item = {}
            item['customer'] = fields[0]
            item['item'] = fields[1]
            item['total'] = fields[2]
            item['quantity'] = fields[3]
            item['date'] = fields[4]

            DealInstance = Deals(customer=fields[0], item=fields[1],
                                 total=fields[2], quantity=fields[3],
                                 date=fields[4])

            DealInstance.save()
            return Response(status=status.HTTP_200_OK)
        return self.create(request)

    def get(self, request):
        return self.list(request)


class DealsListView(ListAPIView):

    queryset = Deals.objects.all()
    serializer_class = DealSerializer
    # filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['customer', 'item', 'total', 'quantity', 'date']
