from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for product in context['products']:
            product.active_version = product.get_active_version()
        return context


class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:product_list')

class VersionUpdateView(UpdateView):
    model = Version
    form_class = VersionForm
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


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')
