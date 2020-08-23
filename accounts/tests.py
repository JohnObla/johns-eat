from django.contrib.auth import get_user_model
from django.test import TestCase

from .admin import CustomUserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()

        user = User.objects.create_user(
            username='john',
            email='john@email.com',
            password='testpass123'
        )

        self.assertEqual(user.username, 'john')
        self.assertEqual(user.email, 'john@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()

        admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@email.com',
            password='testpass123'
        )

        self.assertEqual(admin_user.username, 'admin')
        self.assertEqual(admin_user.email, 'admin@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class CustomUserFormTests(TestCase):

    def setUp(self):
        self.model = get_user_model()
        self.fields = ('email', 'username',)

    def test_create_user(self):
        form = CustomUserCreationForm

        self.assertEqual(form.Meta.model, self.model)
        self.assertEqual(form.Meta.fields, self.fields)

    def test_change_user(self):
        form = CustomUserChangeForm

        self.assertEqual(form.Meta.model, self.model)
        self.assertEqual(form.Meta.fields, self.fields)


class CustomUserAdminTests(TestCase):

    def test_custom_user_admin(self):
        add_form = CustomUserCreationForm
        form = CustomUserChangeForm
        model = get_user_model()
        list_display = ['email', 'username', ]

        user_admin = CustomUserAdmin

        self.assertEqual(user_admin.add_form, add_form)
        self.assertEqual(user_admin.form, form)
        self.assertEqual(user_admin.model, model)
        self.assertEqual(user_admin.list_display, list_display)
