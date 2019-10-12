from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Photographer,Location,Image,Category
import datetime as dt

# import pyperclip
# # ...............

#     def test_copy_email(self):
#         '''
#         Test to confirm that we are copying the email address from a found contact
#         '''

#         self.new_contact.save_contact()
#         Contact.copy_email("0712345678")

#         self.assertEqual(self.new_contact.email,pyperclip.paste())
    # def test_copy(self):
    #     '''
    #     Methode to copy the credential and save them
    #     '''

    #     self.new_credential.save_credential()
    #     twitter =Credential("jeanne","Twitter","dukunde","dukunde")
    #     twitter.save_credential()
    #     find_credential=None
    #     for credential in Credential.user_credential_list:

    #         find_credential=Credential.find_site(credential.site_name)
    #         return pyperclip.copy(find_credential.password)

    #     Credential.copy_credential(self.new_credential.site_name)
    #     self.assertEqual('dukunde',pyperclip.paste())
    #     print(pyperclip.paste())
# Create your tests here.
# class PhotographerTestClass(TestCase):

#     # Set up method
#     def setUp(self):
#         self.hannah= Photographer(first_name = 'Hannah', last_name ='Njeri')
#     # Testing  instance
#     def test_instance(self):
#         self.assertTrue(isinstance(self.hannah,Photographer))   
#     # Testing Save Method
#     def test_save_method(self):
#         self.hannah.save_photographer()
#         photographers = Photographer.objects.all()
#         self.assertTrue(len(photographers) > 0) 
#     def test_delete_method(self):
#         self.hannah.save_photographer()
#         self.hannah.delete_photographer()
#         photographers = Photographer.objects.all()
#         self.assertTrue(len(photographers) == 0) 
#     def test_display_method(self):
#         self.hannah.save_photographer()
#         self.hannah.display_photographers()
#         photographers = Photographer.objects.all()
#         self.assertTrue(len(photographers) > 0) 
#     def test_update_method(self):
#         self.hannah.save_photographer()
#         new_photographer = Photographer.objects.filter(first_name="Hannah").update(first_name="mercy")
#         photographers=Photographer.objects.get(first_name="mercy")
#         self.assertTrue(photographers.first_name,"mercy")           

# class LocationTestClass(TestCase):
#     def setUp(self):
#         self.nairobi = Location(photo_location='Kenya')
#         self.nairobi.save_location()

#     def test_instance(self):
#         self.assertTrue(isinstance(self.nairobi,Location))
    
#     def test_updating_location(self):
#         location = Location.get_location_id(self.nairobi.id)
#         location.update_location('Italy')
#         location = Location.get_location_id(self.nairobi.id)
#         self.assertTrue(location.photo_location == 'Italy')
    
#     def tearDown(self):
#         self.nairobi.delete_location() 
# class CategoryTestClass(TestCase):
#     def setUp(self):
#         self.ladieswear = Category(photo_category='Menswear')
#         self.ladieswear.save_category()

#     def test_instance(self):
#         self.assertTrue(isinstance(self.ladieswear,Category))
    
#     def tearDown(self):
#         self.ladieswear.delete_category()
#   =================================
class ImageTestClass(TestCase):
    '''
    image test
    '''
    def setUp(self):
        self.tree=Category(photo_category='Tree')
        self.tree.save_category()

        self.kigali=Location(photo_category='Kigali')  
        self.kigali.save_location()

        self.image=Image(title='Nature',description='tree',location=self.kigali,category=self.tree)
        self.image.save_image()

        def test_instance(self):
            self.assertTrue(isinstance(self.image,Image))
        def test_save_method(self):
            '''
            test image and saved
            '''
            self.image.save_image()
            images=Image.objects.all()
            self.assertTrue(len(images)>0)
        
        def test_delete_method(self):
            '''
            test of delete image
            '''
            self.image.save_image()
            self.image.delete_image

        def test_update(self):
            '''
            test to update image's
            '''
            self.image.save_image()
            this_img=self.image.get_image_by_id(self.image.id)
            image=Image.objects.get(id=self.image.id)
            self.assertTrue(this_img,image)
        
        def test_filter_by_location(self):
            '''
            test of filter image by location
            '''
            self.image.save_image()
            this_img=self.image.filter_by_location(self.image.location_id)
            image=Image.objects.filter(location=self.image.location_id)
            self.assertTrue(this_img,image)

        def test_filter_by_category(self):
            '''
            test image by category
            '''
            self.image.save_image()
            images=Image.search_image('this')
            self.assertTrue(len(images)>0)


class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.kigali= Location(photo_location = 'Kigali')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.kigali,Location))
    #Testing to update
    def test_update(self):
        '''
        test to update image
        '''
        self.kigali.save_location()
        this_img=self.kigali.get_location_id(self.kigali.id)
        location=Location.objects.get(id=self.kigali.id)
        self.assertTrue(this_img,location)

    #test delete
    def tearDown(self):

        Location.objects.all().delete()
        Image.objects.all().delete()

    # Testing Save Method
    def test_save_method(self):
        self.kigali.save_location()
        locations= Location.objects.all()
        self.assertTrue(len(locations) > 0)



# class ArticleTestClass(TestCase):

#     def setUp(self):
#         # Creating a new editor and saving it
#         self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
#         self.james.save_editor()

#         # Creating a new tag and saving it
#         self.new_tag = tags(name = 'testing')
#         self.new_tag.save()

#         self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.james)
#         self.new_article.save()

#         self.new_article.tags.add(self.new_tag)

#     def tearDown(self):
#         Editor.objects.all().delete()
#         tags.objects.all().delete()
#         Article.objects.all().delete()

#     def test_get_news_today(self):
#         today_news = Article.todays_news()
#         self.assertTrue(len(today_news)>0)

#     def test_get_news_by_date(self):
#         test_date = '2017-03-17'
#         date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
#         news_by_date = Article.days_news(date)
#         self.assertTrue(len(news_by_date) == 0)