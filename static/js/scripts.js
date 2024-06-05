
function submitForm() {
    // 提交表單
    $('form').submit();
}

function clearForm() {
    // 清除表單
    $('form')[0].reset();
}

function navigateToCreate() {
    // 導航至新增書籍的頁面
    window.location.href = '/create_book/';
}

function handleDelete(bookId) {
    // 處理刪除操作的確認
    if (confirm('確認刪除？')) {
        window.location.href = '/delete_book/' + bookId;
    } else {
        alert('取消');
    }
}


