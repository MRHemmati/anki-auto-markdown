from aqt import mw
from aqt.utils import showInfo
from aqt.qt import *
import aqt

# local
from . import config


def _inject_markdown_checkbox(dialog):
    """Safely inject the auto-markdown checkbox into the FieldDialog.
    
    This avoids overriding __init__ entirely. Instead, we patch in the
    checkbox after the dialog's form is set up.
    """
    try:
        dialog.markdownCheckbox = QCheckBox("Convert to/from markdown automatically")
        
        # Try to find the form layout and add our checkbox
        # The form layout is stored as dialog.form._2 in older versions,
        # but we search more robustly for a QFormLayout or QGridLayout
        form_layout = None
        
        if hasattr(dialog, 'form') and hasattr(dialog.form, '_2'):
            form_layout = dialog.form._2
        
        if form_layout is not None:
            row = form_layout.rowCount()
            form_layout.addWidget(dialog.markdownCheckbox, row, 0, 1, 2)
        else:
            # Fallback: try to find any layout in the dialog and append
            layout = dialog.layout()
            if layout:
                layout.addWidget(dialog.markdownCheckbox)
    except Exception as e:
        # If injection fails, log but don't crash
        print(f"[Auto Markdown] Warning: could not inject checkbox: {e}")


def _get_note_type(obj):
    """Get note type, compatible with old and new API."""
    if hasattr(obj, 'note_type'):
        return obj.note_type()
    if hasattr(obj, 'model'):
        return obj.model()
    return None


# Called after FieldDialog.loadField
def fieldDialogLoadField(self, idx):
    """Load the auto-markdown state for the current field into the checkbox."""
    if not hasattr(self, 'markdownCheckbox'):
        return
    if self.currentIdx is None:
        return
    
    try:
        fld = self.model['flds'][self.currentIdx]
        checked = fld.get('perform-auto-markdown', False)
        self.markdownCheckbox.setChecked(checked)
    except (IndexError, KeyError, TypeError):
        self.markdownCheckbox.setChecked(False)


# Called after FieldDialog.saveField
def fieldDialogSaveField(self):
    """Save the auto-markdown checkbox state to the current field."""
    if not hasattr(self, 'markdownCheckbox'):
        return
    if self.currentIdx is None:
        return
    
    try:
        idx = self.currentIdx
        fld = self.model['flds'][idx]
        fld['perform-auto-markdown'] = self.markdownCheckbox.isChecked()
    except (IndexError, KeyError, TypeError):
        pass
