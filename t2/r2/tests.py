from django.test import TestCase

from r2.models import Category

class CategoryMethodTests(TestCase):
    
    def test_ensure_views_are_positive(self):
        
        cat = Category(name= 'test',views=-1, likes=0)
        cat.save
        self.assertEqual((cat.views >=0),True)
        
    def test_slug_line_creation(self):
             """
             slug_line_creation checks to make sure that when we add a category an appropriate slug line is created
             i.e. "Random Category String" -> "random-category-string"
             """
             
             cat = cat('Random Category String')
             cat.save()
             self.assertEqual(cat.slug, 'random-category-string')      

