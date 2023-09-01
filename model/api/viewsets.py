from model.api.serializers import ModelSerializer, CSVFileSerializer
from rest_framework.parsers import FileUploadParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import pandas as pd
import pickle

# Carregando modelo:
path = r'model/models/model.pkl'
with open(path, 'rb') as file:
    model = pickle.load(file)


@api_view(http_method_names=['get'])
def model_api(request):
    return Response({"A previsão de seguro médico na área da saúde."})


@api_view(http_method_names=['post'])
def prediction(request):
    serializer = ModelSerializer(request.data)

    # Como acesso as variáveis?
    bmi = serializer.data['bmi']
    age = serializer.data['age']
    bmi = serializer.data['bmi']
    children = serializer.data['children']
    smoker = serializer.data['smoker']

    # Como transformo as variáveis em um dataframe?
    df_input = pd.DataFrame([
        dict(age=age, bmi=bmi, children=children, smoker=smoker)
    ])

    # Como faço a predição?
    output = model.predict(df_input)[0]

    return Response({'predict': output})


@api_view(http_method_names=['post'])
def multiple_predictions(request):
    df_input = pd.DataFrame(request.data['data'])
    output = model.predict(df_input).tolist()

    return Response({'predicts': output})


class CSVPredictionView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        file_serializer = CSVFileSerializer(data=request.data)

        if file_serializer.is_valid():
            uploaded_file = file_serializer.validated_data['file']

            try:
                df_input = pd.read_csv(uploaded_file)

            except Exception:
                return Response(
                    {'error': 'Erro ao processar o arquivo CSV.'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Faça as previsões com base no DataFrame
            output = model.predict(df_input).tolist()

            return Response({'predicts': output})

        else:
            return Response(
                file_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
