from django.shortcuts import redirect, render

# Create your views here.
from django.http import HttpResponse

from .forms import ContatoForm, ProdutoForm

def index(request):
    return render(request,'index.html')

def sobre(request):
    return render(request,'sobre.html')

def contato(request):
    form = ContatoForm()
    contexto = {
        'form': form,
    }
    return render(request, 'contato.html', contexto)

def exibir_item(request, id):
    return render(request, "exibir_item.html", {'id':id})

def perfil(request, usuario):
    return render(request, "perfil.html",{'usuario':usuario})

def diadasemana(request, dia):
    dias = {
        1: "Domingo",
        2: "Segunda-feira",
        3: "Terça-feira",
        4: "Quarta-feira",
        5: "Quinta-feira",
        6: "Sexta-feira",
        7: "Sábado"
    }
    if dia in dias:
        return HttpResponse(f"O dia correspondente é: {dias[dia]}")
    else:
        return HttpResponse("Dia inválido")
    
produtos_lista = [
    {'id': 1, 'nome': 'Notebook', 'preco': '2.500,00'},
    {'id': 2, 'nome': 'Monitor', 'preco': '500,00'},
    {'id': 3, 'nome': 'Teclado', 'preco': '80,00'},
]

def produtos(request):
    contexto = {
        'lista': produtos_lista,
    }
    return render(request, 'produto/lista.html', contexto)

def form_produto(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            # Pegando os dados do formulário
            nome = form.cleaned_data['nome']
            preco = form.cleaned_data['preco']
            
            # Gerando um ID automático
            novo_id = len(produtos_lista) + 1
            
            # Adicionando o produto à lista
            produtos_lista.append({'id': novo_id, 'nome': nome, 'preco': preco})
            
            # Redirecionando para a página de listagem
            return redirect('produtos')
    else:
        form = ProdutoForm()
    
    contexto = {'form': form}
    return render(request, 'produto/form_produto.html', contexto)