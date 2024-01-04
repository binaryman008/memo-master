from django_elasticsearch_dsl import Document, Index, fields
from notes.models import NotesModel

notes_index = Index('notes')

@notes_index.doc_type
class NotesDocument(Document):
    author = fields.KeywordField(attr='author.username')
    title = fields.TextField()
    content = fields.TextField()

    class Django:
        model = NotesModel