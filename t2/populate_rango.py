import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 't2.settings')

import django
django.setup()

from r2.models import Category, Page

def add_cat(name,likes,views):
        c= Category.objects.get_or_create(name=name)[0] # the [0] sets the default return value to the first value the category object which is name
        c.likes=likes                                   #from then on c by itself means c.name 
        c.views=views
        c.save()
        print "========> %s %s %s" %(c,c.likes,c.views)
        return c

    
def add_page(cat, title, url, views=0):
        p= Page.objects.get_or_create(category=cat, title=title)[0]
        p.url=url
        p.views=views
        p.save()
        return p

def populate():
    python_cat = add_cat('Python',128,64)
    
    add_page(cat=python_cat,
            title="Official Python Tutorial",
            url="http://docs.python.org/2/tutorial/")
    add_page(cat=python_cat,
            title="How to Think Like a Computer Scientist",
            url="http://www.greenteapress.com/thinkpython/")
    add_page(cat=python_cat,
        title="Learn Python in 10 Minutes",
        url="http://www.korokithakis.net/tutorials/python/")
    
    
    django_cat = add_cat("Django",64,32)
    add_page(cat=django_cat,
        title="Official Django Tutorial",
        url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/")

    add_page(cat=django_cat,
        title="Django Rocks",
        url="http://www.djangorocks.com/")

    add_page(cat=django_cat,
        title="How to Tango with Django",
        url="http://www.tangowithdjango.com/")

    frame_cat = add_cat("Other Frameworks",32,16)

    add_page(cat=frame_cat,
        title="Bottle",
        url="http://bottlepy.org/docs/dev/")

    add_page(cat=frame_cat,
        title="Flask",
        url="http://flask.pocoo.org")
    
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print "-{0} - {1}".format(str(c),str(p))
    
       
      
if __name__ == '__main__':
    print "\n \n \n******Starting Rango Population Script**********\n \n \n \n"
    populate()
    
    
    