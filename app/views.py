from django.shortcuts import render, redirect
from .models import Apps, Comment, Applications
from django.views.generic import DetailView
from .forms import AppsForm, CommentForm


def delete_comment(request):
    comment = Comment.objects.get(id=request.GET.get('comment'))
    if request.session['name'] == comment.name:
        comment.delete()

    return redirect('/app/profile')



def delete_applications(request):
    applications = Applications.objects.get(id=request.GET.get('app'))
    if request.session['name'] == applications.author:
        applications.delete()

    return redirect('/app/profile')


def delete_app(request):
    app = Apps.objects.get(id=request.GET.get('app'))
    if request.session['name'] == app.author:
        app.delete()

    return redirect('/app/profile')


def update_comment(request):
    comment = Comment.objects.get(id=request.GET.get('comment'))
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            if request.session['name'] == comment.name:

                comment.body = form.cleaned_data['body']
                comment.save()
            return redirect('/app/profile')
    else:
        form = CommentForm(initial={
            'body': comment.body,

                                 })
    return render(request, 'app/add.html', {'form': form, 'user': request.session['name']})





def update_applications(request):
    app = Applications.objects.get(id=request.GET.get('app'))
    if request.method == 'POST':
        form = AppsForm(request.POST, request.FILES)
        if form.is_valid():
            if request.session['name'] == app.author:

                app.name = form.cleaned_data['name']
                app.text = form.cleaned_data['text']
                app.file = form.cleaned_data['file']
                app.img = form.cleaned_data['img']
                app.video = form.cleaned_data['video']
                app.save()
            return redirect('/app/profile')
    else:
        form = AppsForm(initial={
            'name': app.name,
            'text': app.text,
            'file': app.file,
            'img': app.img,
            'video': app.video,
                                 })
    return render(request, 'app/add.html', {'form': form, 'user': request.session['name']})



def update_app(request):
    app = Apps.objects.get(id=request.GET.get('app'))
    if request.method == 'POST':
        form = AppsForm(request.POST, request.FILES)
        if form.is_valid():
            if request.session['name'] == app.author:

                app.name = form.cleaned_data['name']
                app.text = form.cleaned_data['text']
                app.file = form.cleaned_data['file']
                app.img = form.cleaned_data['img']
                app.video = form.cleaned_data['video']
                app.save()
            return redirect('/app/profile')
    else:
        form = AppsForm(initial={
            'name': app.name,
            'text': app.text,
            'file': app.file,
            'img': app.img,
            'video': app.video,
                                 })
    return render(request, 'app/add.html', {'form': form, 'user': request.session['name']})


def app(request):
    if request.method == "POST":
        return redirect("/app/search?app=" + request.POST.get("text"))

    apps = Apps.objects.order_by('-date')
    data = {"apps": apps}
    return render(request, 'app/apps.html', data)


class AppsDetailView(DetailView):
    model = Apps
    template_name = 'app/details_view.html'
    context_object_name = 'apps'


def comments_creade(request):
    if request.method == "POST":
        print(88)
        comments = Comment()
        comments.app = Apps(id=request.POST.get("id"))
        comments.name = request.session['name']
        comments.body = request.POST.get("text")
        comments.save()
        return redirect('/app/' + request.POST.get("id"))

    return redirect('/')


def profile(request):
    data = {'username': request.session['name'],
            'comments': Comment.objects.filter(name=request.session['name']),
            'applications': Applications.objects.filter(author=request.session['name']),
            'apps': Apps.objects.filter(author=request.session['name']),}
    return render(request, 'main/profile.html', data)


def search(request):
    apps = Apps.objects.filter(text__contains=request.GET.get('app'))
    data = {"apps": apps}
    return render(request, 'app/apps.html', data)


def add(request):
    if request.method == 'POST':
        form = AppsForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.session['name'])
            apps = Applications()
            apps.name = form.cleaned_data['name']
            apps.author = request.session['name']
            apps.text = form.cleaned_data['text']
            apps.file = form.cleaned_data['file']
            apps.img = form.cleaned_data['img']
            apps.video = form.cleaned_data['video']
            apps.save()
            return redirect('/')
    else:
        form = AppsForm()
    return render(request, 'app/add.html', {'form': form, 'user': request.session['name']})
