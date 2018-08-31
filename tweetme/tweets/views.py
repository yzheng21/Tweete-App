from .mixins import FormUserNeededMixin, UserOwnerMixin
from django.shortcuts import render,get_object_or_404
from .models import Tweet
from django.views.generic import DetailView, ListView, CreateView, UpdateView,DeleteView
from .forms import TweetModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q
# Create your views here.
'''
create
retrieve
update
delete
'''
#function based views
#retrieve
# def tweet_detail_view(request,pk = None):
#     obj = Tweet.objects.get(pk = pk)  #get from databases
#     context = {
#         'object': obj
#     }
#     return render(request, 'tweets/detail_view.html',context)
#
# def tweet_list_view(request):
#     queryset = Tweet.objects.all()
#     for obj in queryset:
#         print(obj.content)
#     context ={
#         'object_list':queryset
#     }
#     return render(request, 'tweets/list_view.html',context)

# def tweet_create_view(request):
#     form = TweetModelForm(request.POST or None)
#     if form.is_valid():
#         instane = form.save(commit=False)
#         instane.user = request.user
#         instane.save()
#     context = {
#         'form': form
#     }
#     return render(request,'tweets/create_view.html', context)


#based on class views
class TweetCreateView(LoginRequiredMixin,FormUserNeededMixin,CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    login_url = '/admin/login/'

class TweetUpdateView(LoginRequiredMixin,UserOwnerMixin,UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/update_view.html'
    #success_url = '/tweet/'
    login_url = '/admin/login/'

class TweetDetailView(DetailView):
    #template_name = 'tweets/detail_view.html'
    queryset = Tweet.objects.all()
    # def get_object(self):
    #     pk = self.kwargs.get('pk')
    #     obj = get_object_or_404(Tweet, pk=pk)
    #     return obj

class TweetListView(ListView):
    #template_name = 'tweets/list_view.html'
    def get_queryset(self,*args,**kwargs):
        qs = Tweet.objects.all()
        query = self.request.GET.get('q',None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
            )
        return qs

    def get_context_data(self, **kwargs):
        context = super(TweetListView,self).get_context_data(**kwargs)
        # context['another_list'] = Tweet.objects.all()
        # print(context)
        context['create_form'] = TweetModelForm()
        context['create_url'] = reverse_lazy('tweet:create')
        return context

class TweetDeleteView(LoginRequiredMixin,DeleteView):
    model = Tweet
    template_name = 'tweets/delete_confirm.html'
    success_url = reverse_lazy('tweet:list')  #/tweet/list







