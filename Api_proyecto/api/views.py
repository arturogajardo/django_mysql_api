from django.http.response import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from .models import User
from rest_framework.decorators import api_view

# Create your views here.

class UserView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id>0):
            users=list(User.objects.filter(id=id).values())
            if len(users)>0:
                users=users[0]
                datos={'message':"Success",'users':users}
            else:
                datos={'message':"Users not found..."}
            return JsonResponse(datos)
        else:
            users=list(User.objects.values())
            if len(users)>0:
                datos={'message':"Success",'users':users}
            else:
                datos={'message':"Users not found..."}
            return JsonResponse(datos)

    def post(self, request):
        jd=json.loads(request.body)
        User.objects.create(usuario=jd['usuario'], email=jd['email'], password=jd['password'])
        datos={'message':"Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        users = list(User.objects.filter(id=id).values())
        if len(users) > 0:
            users = User.objects.get(id=id)
            users.usuario = jd['usuario']
            users.email = jd['email']
            users.password = jd['password']
            users.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "User not found..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        users = list(User.objects.filter(id=id).values())
        if len(users) > 0:
            User.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "User not found..."}
        return JsonResponse(datos)


class LoginView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):

        return super().dispatch(request, *args, **kwargs)
    
    def login(self, request):
        jd=json.loads(request.body)
        users = User.objects.get(email=jd.data.get("email"),password=jd.data.get("password"))
        users=list(User.objects.filter(email=request.data.get("email")).values())
        print(users)
        if len(users)>0:
            datos={'message':"Success", "email":users.email, "password":users.password}
        else:
            datos={'message':"User not found..."}

        return JsonResponse(datos)
