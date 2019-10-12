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
        self.nature=Category(photo_category='Nature')
        self.nature.save_category()

        self.james=Photographer(first_name='James',last_name="Anne")
        self.james.save_photographer()

        self.usa=Location(photo_location='USA')  
        self.usa.save_location()

        self.image=Image(title='leaves',description='beautiful',photographer=self.james,location=self.usa,category=self.nature)
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
        Location.objects.all().delete()
        Image.objects.all().delete()

    def test_update(self):
        '''
        test to update image's
        '''
        self.image.save_image()
        img=self.image.get_image_by_id(self.image.id)
        image=Image.objects.get(id=self.image.id)
        self.assertTrue(img,image)
    
    def test_filter_by_location(self):
        '''
        test of filter image by location
        '''
        self.image.save_image()
        img=self.image.filter_by_location(self.image.location_id)
        image=Image.objects.filter(location=self.image.location_id)
        self.assertTrue(img,image)

    def test_filter_by_category(self):
        '''
        test image by category
        '''
        self.image.save_image()
        images=Image.search_by_category('this')
        self.assertFalse(len(images)>0)


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
        img=self.kigali.get_location_id(self.kigali.id)
        location=Location.objects.get(id=self.kigali.id)
        self.assertTrue(img,location)

    #test delete
    def tearDown(self):

        Location.objects.all().delete()
        Image.objects.all().delete()

    # Testing Save Method
    def test_save_method(self):
        self.kigali.save_location()
        locations= Location.objects.all()
        self.assertTrue(len(locations) > 0)

class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.nature= Category(photo_category = 'Nature')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.nature,Category))
    #Testing to update
    def test_update(self):
        '''
        test to update image
        '''
        self.nature.save_category()
        img=self.nature.get_category_id(self.nature.id)
        category=Category.objects.get(id=self.nature.id)
        self.assertTrue(img,category)

    #test delete
    def tearDown(self):

        Category.objects.all().delete()
        Image.objects.all().delete()

    # Testing Save Method
    def test_save_method(self):
        self.nature.save_category()
        categories= Category.objects.all()
        self.assertTrue(len(categories) > 0)
