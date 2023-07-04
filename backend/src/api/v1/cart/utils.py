from rest_framework.response import Response
from rest_framework import status


def create_error_404(error_message='Not found'):
    error_data = {'error': error_message}
    return Response(error_data, status=status.HTTP_404_NOT_FOUND)
