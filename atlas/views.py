from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .serializers import RupeeToPaisaSerializer
from rest_framework.views import APIView
from atlas.models import Convertion, Counter

# Create your views here.

class RupeeConvertionView(APIView):

    def get(self, request, format=None):
        convert_obj = Convertion.objects.all()
        serializer = RupeeToPaisaSerializer(convert_obj, many=True)
        return Response(serializer.data)
   

    def post(self, request):
        try:
            serializer = RupeeToPaisaSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            data = serializer.validated_data
            # get paisa from requested data      
            paisa = data.get('paisa')
            # check whether it exists in database, if exists than show the lastest one.
            paisa_obj = Convertion.objects.filter(paisa=paisa).last()
            # to filter the first one.
            count_object = Counter.objects.filter(paisa=paisa_obj).first()
            if count_object:
                count_object.count = count_object.count + 1
                count_object.save()
                

            
            if paisa_obj:
                print('returning from db')
                rupee_val = paisa_obj.rupee
                rupee_bool = True
                notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
                notesCount = {}
                
                for note in notes:
                    if paisa >= note:
                        notesCount[note] = paisa//note
                        paisa = paisa % note
                        print(paisa)
                        
                print ("Currency Count ->")
                print(notesCount)
            else:
                notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
                notesCount = {}
                
                for note in notes:
                    if paisa >= note:
                        notesCount[note] = paisa//note
                        paisa = paisa % note
                        print(paisa)
                        
                print ("Currency Count ->")
                print(notesCount)
                covert_paisa = data.get('paisa')/100
                rupee_obj = Convertion.objects.create(paisa=data.get('paisa'), rupee=covert_paisa)
                print('calculated again')     
                rupee_val = rupee_obj.rupee
                rupee_bool = False

            return Response({"Rupee" : rupee_val, "Paisa" : data.get('paisa'), "From_DB" : rupee_bool, "Denomination": notesCount}, status=status.HTTP_200_OK)  
                        
        except Exception as e:
            return Response(e.__str__(), status=status.HTTP_400_BAD_REQUEST)