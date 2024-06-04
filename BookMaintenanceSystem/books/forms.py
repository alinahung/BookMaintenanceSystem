from django import forms
from accounts.models import Student
from django.contrib.auth.models import User
from .models import BookData, BookCategory, BookCode, BookLendRecord
from django.forms import ModelForm, DateInput, TextInput, Select, Textarea

class BookForm(ModelForm):
    class Meta:
        model = BookData
        fields = ['name', 'category', 'author', 'publisher', 'publish_date', 'summary', 'keeper_id', 'status']
        widgets = {
            'name': TextInput(attrs={"class": "form-control"}),
            'category': Select(attrs={"class": "form-control"}),
            'author': TextInput(attrs={"class": "form-control"}),
            'publisher': TextInput(attrs={"class": "form-control"}),
            'publish_date': DateInput(format='%Y-%m-%d', attrs={"class": "form-control", "type": "date"}),
            'summary': Textarea(attrs={"class": "form-control"}),
            'keeper_id': Select(attrs={"class": "form-control"}),
            'status': Select(attrs={"class": "form-control"}),
        }
        labels = {
            'name': '書名*',
            'category': '書籍類別*',
            'author': '作者',
            'publisher': '出版社',
            'summary': '內容簡介',
            'keeper_id': '借閱人',
            'status': '借閱狀態*',
        }
    
    def clean_publish_date(self):
        publish_date = self.cleaned_data.get('publish_date')
        # Validation logic can be included here
        return publish_date
    
    def __init__(self, *args, **kwargs):
        # 從參數中移除readonly並設定預設值
        readonly = kwargs.pop('readonly', False)
        super().__init__(*args, **kwargs)
        
        # 將字段設為唯讀或禁用狀態，根據readonly參數
        for field_name in ['name', 'author', 'publisher', 'summary']:
            self.fields[field_name].widget.attrs['readonly'] = readonly
        
        for disabled_field in ['category', 'keeper_id', 'status', 'publish_date']:
            self.fields[disabled_field].widget.attrs['disabled'] = readonly
        
        # 從模型中動態獲取選項並設定給對應的字段
        self.setup_field_choices()

    def setup_field_choices(self):
        # 設定書籍類別選項
        self.fields['category'].choices = self.get_book_category_choices()
        # 設定管理者選項
        self.fields['keeper_id'].choices = self.get_keeper_choices()
        # 設定書籍狀態選項
        self.fields['status'].choices = self.get_status_choices()

    @staticmethod
    def get_book_category_choices():
        return [(category.category_id, category.category_name) for category in BookCategory.objects.all()]

    @staticmethod
    def get_keeper_choices():
        return [(student.studentId, student.username) for student in Student.objects.all()]

    @staticmethod
    def get_status_choices():
        return [(code.code_id, code.code_name) for code in BookCode.objects.all()]


class SearchForm(ModelForm):
    class Meta:
        model = BookData
        fields = ['name', 'category', 'keeper_id', 'status']
        widgets = {
            'name': TextInput(attrs={"class": "form-control"}),
            'category': Select(attrs={"class": "form-control"}),
            'keeper_id': Select(attrs={"class": "form-control"}),
            'status': Select(attrs={"class": "form-control"}),
        }
        labels = {
            'name': '書名',
            'category': '書籍類別',
            'keeper_id': '借閱人',
            'status': '借閱狀態',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['category'].required = False
        self.fields['status'].required = False
        self.fields['category'].null = True
        self.fields['name'].null = True
        self.fields['status'].null = True
        self.fields['category'].choices = [('', '請選擇')] + [(category.category_id, category.category_name) for category in BookCategory.objects.all()]
        self.fields['keeper_id'].choices = [('', '請選擇')] + [(student.studentId, student.username) for student in Student.objects.all()]
        self.fields['status'].choices = [('', '請選擇')] + [(code.code_id, code.code_name) for code in BookCode.objects.all()]
        




