from lists.models import Item, List
from django.test import TestCase


class HomePageTest(TestCase):
    """тест домашней страницы"""

    def test_uses_home_template(self):
        """тест: используется домашний шаблон"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html') #сравнивает два шаблона друг с другом


class ListAndItemModelsTest(TestCase):
    """тест модели элемента списка"""

    def test_saving_and_retrieving_items(self):
        """тест сохранения и получения элементов списка"""
        list_ = List()
        list_.save()

        first_item = Item()
        first_item.text = 'Первый (самый) элемент списка'
        first_item.list = list_
        first_item.save()

        second_item = Item()
        second_item.text = 'Элемент второй'
        second_item.list = list_
        second_item.save()

        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'Первый (самый) элемент списка')
        self.assertEqual(first_saved_item.list, list_)
        self.assertEqual(second_saved_item.text, 'Элемент второй')
        self.assertEqual(second_saved_item.list, list_)


class ListViewTest(TestCase):
    """тест представления списка"""

    def test_uses_list_template(self):
        """тест: используется шаблон списка"""
        response = self.client.get('/lists/единственный-список-в-мире/')
        self.assertTemplateUsed(response, 'list.html')

    def test_displays_all_items(self):
        """тест: отображаются все элементы списка"""
        list_ = List.objects.create()
        Item.objects.create(text='itemey 1', list=list_)
        Item.objects.create(text='itemey 2', list=list_)

        response = self.client.get('/lists/единственный-список-в-мире/')

        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')


class NewListTest(TestCase):
    """тест нового списка"""

    def test_can_save_a_POST_request(self):
        """тест: можно сохранить пост запрос"""
        self.client.post('/lists/new', data={'item_text': 'A new list item'})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        """тест: переадресует после пост-запроса"""
        response = self.client.post('/lists/new', data={'item_text': 'A new list item'})
        #self.assertEqual(response.status_code, 302)
        #self.assertEqual(response['location'], '/lists/единственный-список-в-мире/')
        #self.assertRedirects(response, '/lists/единственный-список-в-мире/')
