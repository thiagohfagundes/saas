from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def perfil(request):
    usuario = request.user
    cliente = usuario.customer
    #assinaturas = usuario.usersubscription

    print(usuario)
    print(cliente)
    #print(assinaturas)
    contexto = {
        'usuario': usuario
    }
    return render(request, 'account/profile_page.html', contexto)

