from django.shortcuts import render

db = [
    {
        'id': 1,
        'title': '1',
        'contents': '첫번째 게시물 내용',
        'created_at': '2023-10-10 00:00:00',
        'updated_at': '2023-10-10 00:00:00',
        'author': '이수민',
        'category': '일상',
        'tags': '태그1, 태그2',
        'thumbnail': 'https://piscum.photos/200/300',
    },
    {
        'id': 2,
        'title': '2',
        'contents': '첫번째 게시물 내용',
        'created_at': '2023-10-10 00:00:00',
        'updated_at': '2023-10-10 00:00:00',
        'author': '지하은',
        'category': '팁',
        'tags': '태그1, 태그2',
        'thumbnail': 'https://piscum.photos/200/300',
    },
    {
        'id': 3,
        'title': '3',
        'contents': '첫번째 게시물 내용',
        'created_at': '2023-10-10 00:00:00',
        'updated_at': '2023-10-10 00:00:00',
        'author': '허창준',
        'category': '프로젝트',
        'tags': '태그1, 태그2',
        'thumbnail': 'https://piscum.photos/200/300',
    },
]

def blog(request):
    context = {
        'db': db,
    }
    return render(request, 'blog/blog.html', context)

def post(request, pk):
    context = {
        'db': db[pk-1],
    }
    return render(request, 'blog/post.html', context)