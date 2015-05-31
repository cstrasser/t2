from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from r2.models import Category , Page
from r2.forms import CategoryForm, PageForm, UserForm, UserProfileForm
from r2.bing_search import run_query



def index(request):
    
    context = {'bold_message': "Bold message here"}
    category_list = Category.objects.all()
    page_list = Page.objects.order_by('-views') [:6]
    context= {'categories':category_list, 'pages':page_list}
    visits = request.session.get('visits')
    
    if not visits:
        visits = 1
    reset_last_visit_time = False
    last_visit = request.session.get('last_visit')
   
    if last_visit:
        last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")
        print "last visit %r " %last_visit_time
        if (datetime.now() - last_visit_time).seconds > 0:
            visits = visits + 1
            reset_last_visit_time = True
    else:
        reset_last_visit_time = True

    if reset_last_visit_time:
        request.session['last_visit'] = str(datetime.now())
        request.session['visits'] = visits
    
    context['visits'] = visits
    response = render(request,'r2/index.html', context)
    return response

def about(request):
    context = {'message': "R2 Django 1.7, SQLite"}
    return render(request, 'r2/about.html', context)


def category(request, category_name_url = 'none'):
    context = {}
    
    try:
        category =  Category.objects.get(slug=category_name_url)
        context['category_name'] = category.name
        pages = Page.objects.filter(category=category).order_by('-views')#pages = Page.objects.filter(category = category)
        context['pages'] = pages
        context['category'] = category
        context['name_slug'] = category_name_url
    except Category.DoesNotExist:
        pass
  
   
    return render(request,'r2/category.html', context)


def add_category(request):
   
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = CategoryForm()
    
    return render(request, 'r2/add_category.html', {'form': form})

@login_required
def add_page(request, category_name):

    try:
        cat = Category.objects.get(slug=category_name)
        print "slug %s" %cat.slug           
    except Category.DoesNotExist:
                print "no cat"
                cat = None

    if request.method == 'POST':
        form = PageForm(request.POST)
        
        if form.is_valid():
            if cat:
                page = form.save(commit=False)
                page.category = cat
                page.views = 0
                page.save()
                return_cat = cat.slug.encode('utf-8').lower()
                #return_cat = return_cat.lower()
                #lowercase =lambda s: s[:1].lower() + s[1:] if s else ''
                #lowercase =lambda s: s.lower()  if s else ''
                #return_cat = "/r2/category/" + lowercase(return_cat)
                return_cat = "/r2/category/" + return_cat
                print "Return Cat %s" %return_cat
                return redirect(return_cat)
        else:
            print form.errors
    else:
        form = PageForm()

    context = {'form':form, 'category': cat, 'category_name': cat.name}
    
    return render(request, 'r2/add_page.html', context)



def register(request):
    
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
            'r2/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('/r2/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login : {0}, {1}".format(username, password)
            return HttpResponse("Invalid login ")

    else:
        return render(request, 'r2/login.html', {})
    
@login_required
def user_logout(request):
    logout(request)
    return redirect('/r2')

@login_required
def search(request):

    result_list = []

    if request.method == 'POST':
        query = request.POST['query'].strip()

        if query:
            # Run our Bing function to get the results list!
            result_list = run_query(query)

    return render(request, 'r2/search.html', {'result_list': result_list})

def f2(request):
     

    return render(request, 'r2/tabbed_form.html')

def track_url(request):
    page_id = None
    url = '/r2'
    if request.method == 'GET':
        if 'page_id' in request.GET:
            page_id= request.GET['page_id']
            
            try:
                page = Page.objects.get(id=page_id)
                page.views = page.views +1
                page.save()
                url = page.url
               
            except:
                pass
          
    return redirect(url)


    



    