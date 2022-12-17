from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
import csv
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage

from rest_framework.decorators import action

from .models import *
from .serializers import *

fs = FileSystemStorage(location='tmp/')

# class WomenViewSet(viewsets.ModelViewSet):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
# до меня слишком поздно дошло что файл не пользователь будет загружать, поэтому пока так.
    @action(detail=False, methods=['POST'])
    def upload_data(self, request):
        file = request.FILES["file"]

        content = file.read()

        file_content = ContentFile(content)
        file_name = fs.save(
            "tmp.csv", file_content
        )
        tmp_file = fs.path(file_name)

        csv_file = open(tmp_file) #, errors="ignore" это надо?
        reader = csv.reader(csv_file, delimiter=";")
        next(reader)

        product_list = []
        print(enumerate(reader))
        for id_, row in enumerate(reader):
            (
                product_name,
                product_number,
                year,
                factory,
                comment,
            ) = row

            product_list.append(
                Product(
                    product_name=product_name,
                    product_number=product_number,
                    year=year,
                    factory=factory,
                    comment=comment,
                )
            )

        Product.objects.bulk_create(product_list)

        return Response("Успешно загрузили таблицу")


