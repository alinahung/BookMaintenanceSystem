
function submitForm() {
    // 提交表單
    document.querySelector('form').submit();
}
function clearForm() {
    // 清除表單
    document.querySelector('form').reset();
}
function navigateToCreate() {
    // 導航至新增書籍的頁面
    window.location.href = '/create_book/';
}
function handleDelete(url) {
    // 處理刪除操作的確認
    if(confirm('確認刪除？')) {
        window.location.href = url;
    } else {
        alert('取消');
    }
}
