from django.shortcuts import render, get_object_or_404,redirect,HttpResponseRedirect,reverse

from .models import BookCategory,BookCode,BookData,BookLendRecord  # 修改引用的模型
from django.db.models import Q
from .forms import SearchForm, BookForm
from accounts.models import Student

def book_search(request):
    """書籍搜尋的視圖，根據表單條件過濾書籍列表。"""
    try:
        if request.method == "POST":
            form = SearchForm(request.POST)
            condition = Q()
            if name := request.POST.get('name'):
                condition &= Q(name__icontains=name)
            if category := request.POST.get('category'):
                condition &= Q(category_id=category)
            if keeper_name := request.POST.get('keeper_name'):
                condition &= Q(keeper_id=keeper_name)
            if status := request.POST.get('status'):
                condition &= Q(status_id=status)
            books = BookData.objects.filter(condition).order_by("id")
        else:
            form = SearchForm()
            books = BookData.objects.all().order_by("id")
        
        for book in books:
            book.category_name = BookCategory.objects.get(category_id=book.category_id).category_name
            book.status_name = BookCode.objects.get(code_id=book.status_id).code_name
            book.keeper_name = Student.objects.get(id=book.keeper_id).username if book.keeper_id else "-"
    except Exception as e:
        errormessage = "讀取錯誤：" + str(e)
        
    return render(request, "books/book_search.html", locals())

def book_detail(request, pk):
    """顯示書籍的詳細信息，僅用於展示，不處理表單提交。"""
    book = get_object_or_404(BookData, pk=pk)  # 確保書籍存在
    if request.method == 'POST':
        # 如果有資料提交，更新書籍信息
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect(reverse('edit_book', kwargs={'pk': pk}))
    else:
        # 非POST請求，顯示書籍詳情
        form = BookForm(instance=book)

    return render(request, 'books/book_detail.html', {'edit': 1, 'form': form, 'pk': pk})



# 創建書籍
def create_book(request):
   
    if request.method == 'POST':
        
        form = BookForm(request.POST)
        if form.is_valid():
            
            new_book = form.save(commit=True)
            return redirect(reverse('Book'))
        
        else:
            
            return render(request, "books/book_detail.html", {'form': form, 'edit': 2})
    else:
        
        form = BookForm()
        return render(request, "books/book_detail.html", {'form': form, 'edit': 2})

def edit_book(request, pk):
    #處理書籍的編輯或更新操作
    book = get_object_or_404(BookData, pk=pk)  # 確保書籍存在，否則返回404錯誤
    # 如果書籍有借閱人信息，則從學生模型中獲取借閱人的名稱
    book.keeper_name = Student.objects.get(id=book.keeper_id).username if book.keeper_id else "-"

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)  # 使用POST數據填充表單
        if form.is_valid():  # 驗證表單數據
            form.save()  # 保存表單更改
            return redirect(reverse('book_detail', kwargs={'pk': pk}))  # 重定向到書籍詳情頁面
    else:
        form = BookForm(instance=book)  # 非POST請求，創建一個未綁定數據的表單

    # 渲染書籍編輯頁面，傳遞表單和書籍信息
    return render(request, "books/book_detail.html", {
        'edit': 3,
        'form': form,
        'pk': pk,
        'book': book
    })    
    


# 刪除書籍
def delete_book(request, pk=None):
   
    book = get_object_or_404(BookData, pk=pk)
    book.delete()
    return redirect(reverse('book_search'))  


# 書籍借閱記錄
def lend_record(request, pk):
    records = BookLendRecord.objects.filter(book=pk).order_by("-borrow_date")
    for record in records:
        record.borrower_id = Student.objects.get(username=record.borrower).id
    context = {'records': records}
    return render(request, "books/lend_record.html", context)





