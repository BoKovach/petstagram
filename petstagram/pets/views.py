from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from petstagram.common.forms import CommentForm
from petstagram.common.models import Comment
from petstagram.pets.forms import PetForm, EditPetForm
from petstagram.pets.models import Pet, Like


@login_required()
def pet_all(request):
    all_pets = Pet.objects.all()
    context = {
        'pets': all_pets
    }
    return render(request, 'pet_list.html', context)


def pet_detail(request, pk):
    pet = Pet.objects.get(pk=pk)
    pet.likes_count = pet.like_set.count()

    is_liked_by_user = pet.like_set.filter(user_id=request.user.id).exists()

    is_owner = pet.user == request.user

    context = {
        'pet': pet,
        'comment_form': CommentForm(
            initial={
                'pet_pk': pk,
            }
        ),
        'comments': pet.comment_set.all(),
        'is_owner': is_owner,
        'is_liked': is_liked_by_user,
    }

    return render(request, 'pet_detail.html', context)


# def comment_pet(request, pk):
#     pet = Pet.objects.get(pk=pk)
#     form = CommentForm(request.POST)
#     if form.is_valid():
#         comment = Comment(
#             comment=form.cleaned_data['text'],
#             pet=pet,
#         )
#         comment.save()
#
#     return redirect('pet details', pet.id)


@login_required()
def comment_pet(request, pk):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.save()

    return redirect('pet details', pk)


@login_required()
def like_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    is_liked_by_user = pet.like_set.filter(user_id=request.user.id).first()

    if is_liked_by_user:
        is_liked_by_user.delete()
    else:
        like = Like(
            pet=pet,
            user=request.user,
        )
        like.save()

    return redirect('pet details', pet.id)


@login_required
def create_pet(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.save()
            return redirect('list pets')

    else:
        form = PetForm()

        context = {
            'form': form
        }
        return render(request, 'create_pet.html', context)


@login_required()
def edit_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditPetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('list pets')

    form = EditPetForm(instance=pet)

    context = {
        'form': form,
        'pet': pet,
    }

    return render(request, 'edit_pet.html', context)


@login_required()
def delete_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'POST':
        pet.delete()
        return redirect('list pets')
    else:
        context = {
            'pet': pet,
        }
        return render(request, 'delete_pet.html', context)
