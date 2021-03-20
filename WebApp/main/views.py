from django.views.generic import ListView, DetailView
from .models import Product, Slider, Edit, EditCenterText, VariousDetails, Category
# Create your views here.


class IndexView(ListView):
    model = Product
    template_name = 'main/index.html'
    context_object_name = 'Products'
    ordering = ['id']
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({
            'EditText': Edit.objects.all(),
            'EditHeadText': EditCenterText.objects.all()
        })
        return context

    def get_queryset(self):
        return Product.objects.filter(ToPut=True).select_related('category')


class ProductDetailView(ListView):
    model = Product
    template_name = 'main/product_detail.html'
    context_object_name = 'Products'
    ordering = ['id']
    paginate_by = 6

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs.get('slug')).select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context.update({
            'EditText': Edit.objects.all(),
            'EditHeadText': EditCenterText.objects.all()
        })
        return context


class ProfileDetailView(ListView):
    model = Product
    template_name = 'main/profile_detail.html'
    context_object_name = 'Products'

    def get_queryset(self):
        return Product.objects.filter(id=self.kwargs['pk'])
