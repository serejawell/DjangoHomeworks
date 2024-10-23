from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from catalog.forms import ProductForm, VersionForm, ProductModeratorForm
from catalog.models import Product, Version
from catalog.services import get_products_from_cache


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for product in context['products']:
            product.active_version = product.get_active_version()
        return context

    def get_queryset(self):
        return get_products_from_cache()


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.add_product'
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user  # Привязываем текущего пользователя к продукту
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')


    def get_form_class(self):
        user = self.request.user

        # Здесь выводим все права пользователя в консоль
        print(user.get_all_permissions())  # Это выведет все права пользователя в терминал

        if user == self.object.owner:
            return ProductForm
        if user.has_perm("catalog.can_edit_description") and user.has_perm(
                "catalog.can_edit_category") and user.has_perm("catalog.set_published"):
            print("Модераторская форма выбрана")  # Добавь этот вывод для проверки
            return ProductModeratorForm
        raise PermissionDenied

        print("Модераторская форма выбрана")  # Добавь этот вывод для проверки


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:product_list')


class VersionListView(ListView):
    model = Version
    context_object_name = 'versions'


class VersionDetailView(DetailView):
    model = Version


class VersionDeleteView(DeleteView):
    model = Version
    success_url = reverse_lazy('catalog:product_list')


class VersionUpdateView(UpdateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:product_list')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')

# class ProductCreateView(CreateView):
#     model = Product
#     fields = ('name', 'description', 'image', 'category', 'price')
#     success_url = reverse_lazy('catalog:product_list')
#


# class ProductUpdateView(UpdateView):
#     model = Product
#     fields = ('name', 'description', 'image', 'category', 'price')
#
#     def get_success_url(self):
#         return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])
#
#     def form_valid(self, form):
#         if form.is_valid:
#             new_post = form.save()
#             new_post.slug = slugify(new_post.name)
#             new_post.save()
#
#         return super().form_valid(form)
