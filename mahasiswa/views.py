from django.shortcuts import render, redirect, get_object_or_404
from .models import Mahasiswa
from django.contrib.auth.decorators import login_required


def index(request):
    context = {
        'judul': 'Halo Mahasiswa',
        'deskripsi': 'Contoh halaman index menggunakan Django templates dan static files.'
    }
    return render(request, 'mahasiswa/index.html', context)


@login_required(login_url='/accounts/login/')
def daftar_mahasiswa(request):
    mahasiswas = Mahasiswa.objects.all()
    return render(request, 'mahasiswa/daftar.html', {'mahasiswas': mahasiswas})


@login_required(login_url='/accounts/login/')
def tambah_mahasiswa(request):

    if request.method == 'POST':
        Mahasiswa.objects.create(
            nim=request.POST['nim'],
            nama=request.POST['nama'],
            programstudi=request.POST['programstudi'],
            angkatan=request.POST['angkatan']
        )

        return redirect('daftar_mahasiswa')

    return render(request, 'mahasiswa/form.html')


@login_required(login_url='/accounts/login/')
def edit_mahasiswa(request, id):

    mahasiswa = get_object_or_404(Mahasiswa, id=id)

    if request.method == 'POST':
        mahasiswa.nim = request.POST['nim']
        mahasiswa.nama = request.POST['nama']
        mahasiswa.programstudi = request.POST['programstudi']
        mahasiswa.angkatan = request.POST['angkatan']
        mahasiswa.save()

        return redirect('daftar_mahasiswa')

    return render(
        request,
        'mahasiswa/form.html',
        {'mahasiswa': mahasiswa}
    )


@login_required(login_url='/accounts/login/')
def hapus_mahasiswa(request, id):

    mahasiswa = get_object_or_404(Mahasiswa, id=id)
    mahasiswa.delete()

    return redirect('daftar_mahasiswa')