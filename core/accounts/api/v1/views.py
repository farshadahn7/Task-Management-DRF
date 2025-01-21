from rest_framework.response import Response
from rest_framework.generics import CreateAPIView


from .serializers import RegistrationSerializers

class RegistrationView(CreateAPIView):
    serializer_class = RegistrationSerializers
    def post(self, request, *args, **kwargs):
        serialized_data = self.serializer_class(data=request.data)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()
        return Response("You registered successfully.")