# CustomCSharp.py
from pygments.lexers.dotnet import CSharpLexer
from pygments.token import Keyword, Name

class CustomCSharpLexer(CSharpLexer):
    name = 'CustomCSharp'
    aliases = ['customcsharp']
    filenames = ['*.cs']

    # List of Unity-specific keywords you want to highlight.
    extra_keywords = {
        'SerializeField', 'HideInInspector', 'Range', 'Header', 'Tooltip',
        'ContextMenu', 'RequireComponent', 'ExecuteInEditMode',
        'DisallowMultipleComponent', 'AddComponentMenu',
        'Awake', 'Start', 'Update', 'FixedUpdate', 'LateUpdate'
    }

    def get_tokens_unprocessed(self, text):
        # Get the original tokens from the base CSharpLexer.
        for index, token, value in super().get_tokens_unprocessed(text):
            # Check if the token is a Name (identifier) and if its value is one of the Unity keywords.
            if token is Name and value in self.extra_keywords:
                yield index, Keyword, value
            else:
                yield index, token, value