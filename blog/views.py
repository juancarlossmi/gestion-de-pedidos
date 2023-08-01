from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Post, Categoria
from django.db.models import Max
from .forms import Post_Form
from django.contrib.auth.decorators import login_required
from .models import Post

# Create your views here.


def blog(request):
    categorias = Categoria.objects.all()
    # Subconsulta para obtener el último post de cada categoría
    subquery = Post.objects.values('categorias').annotate(max_created=Max('created'))
    # Filtrar los posts para obtener las últimas publicaciones de cada categoría y ordenarlos por ultimo creado
    posts = Post.objects.filter(
        categorias__in=subquery.values('categorias'),
        created__in=subquery.values('max_created')
    ).order_by('-created')
    return render(request, 'blog/blog.html', {'posts': posts, 'categorias': categorias})



def categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    posts = categoria.post_set.all()
    context = {'categoria': categoria, 'posts': posts}
    return render(request, 'blog/categoria.html', context)



@login_required(login_url="/autenticacion/logear")
def create_post(request):
    if request.method == 'GET':
        # Creamos un formulario que contenga como opcion de autor al usuario que actualmente sea logeado
        form = Post_Form(user=request.user)
        return render(request, 'blog/create_post.html', {'form': form})
    else:
        form = Post_Form(request.POST, request.FILES, user=request.user)
        # si el formulario es valido entonces obtenemos la informacion de la imagen para conocer su tamaño
        if form.is_valid():
            imagen = form.cleaned_data.get('imagen')
            # una vez conocido las dimensiones de la imagen validamos si es que el tamaño es mayor de 1024bytes si es mayor muestra un error y si no entonces agregala a la publicacion
            if imagen and imagen.size > 1024 * 1024:  # 1024 KB en bytes (1 MB)
                return render(request, 'blog/create_post.html', {
                    'form': form,
                    'error': 'El tamaño máximo de la imagen debe ser de 1024 KB (1 MB).'
                })
            else:
                # Guardamos la publicacion
                new_post = form.save()
                new_post.user = request.user
                new_post.save()
                return redirect('blog')
        else:
            # si el usuario no ingresa correctamente la informacion en algun input mostrados el siguiente error
            return render(request, 'blog/create_post.html', {
                'form': form,
                'error': 'Por favor ingresa información válida en todos los campos.'
            })



@login_required(login_url="/autenticacion/logear")
def delete_post(request, post_id):
    # obtenemos la publicacion creada por el usuario activo actualmente
    post = get_object_or_404(Post, id = post_id, autor = request.user)
    if request.method == 'POST':
        # borramos el post
        post.delete()
        return redirect('blog')



@login_required(login_url="/autenticacion/logear")
def edit_post(request, post_id):
    # obtenemos la publicacion agregando la excepcion 404 si es que la publicacion no existe
    post = get_object_or_404(Post, id=post_id, autor=request.user)
    if request.method == "POST":        
        form = Post_Form(request.POST, request.FILES, user=request.user, instance=post)
        # si el formulario es valido verificamos las dimensiones de la imagen seleccionada para poder agregala a la publicacion nueva si es que no pasa de 1024 bytes
        if form.is_valid():
            imagen = form.cleaned_data.get('imagen')
            if imagen and imagen.size > 1024 * 1024:
                form.add_error('imagen', "La imagen no puede ser mayor a 1 megabyte.")
                return render(request, "blog/edit_post.html", {'post': post, 'form': form})
            form.save()
            return redirect('blog')
        else:
            # En caso de agregar una imagen incorrecta mostradmos nuevamente los inputs con la info de la instancia creada para evitar al usuario agregar nuevamente informacion a los inputs con el uso de "instance"
            form = Post_Form(user=request.user, instance=post, initial={'titulo': post.titulo, 'contenido': post.contenido})
        # obtenemos la informacion original del post para no tener que rellenar nuevamente los campos al crear una instacia nueva
        form = Post_Form(user=request.user, instance=post)
    return render(request, "blog/edit_post.html", {'post': post, 'form': form})


