# std
import sys
import os

# first add directory to path so pygments will resolve correctly
for p in sys.path:
    if p.endswith('addons21'):
        sys.path.append(os.path.join(p, __name__))
        break

# anki — modern hook system
from aqt import gui_hooks
from anki.hooks import wrap
from aqt.fields import FieldDialog
from aqt.editor import Editor

# local
from . import config
from . import fields
from .editor import EditorController


def main():
    # ── Fields dialog: inject markdown checkbox ──
    if config.shouldShowEditFieldCheckbox():
        # Instead of overriding FieldDialog.__init__, we hook into the
        # init process to inject our checkbox safely
        def _on_field_dialog_init(dialog, *args, **kwargs):
            """Wrap FieldDialog.__init__ to inject our checkbox after setup."""
            fields._inject_markdown_checkbox(dialog)

        # Use wrap() in "after" mode to inject checkbox after __init__ completes
        FieldDialog.__init__ = wrap(FieldDialog.__init__, _on_field_dialog_init)

        # Wrap saveField and loadField to sync checkbox state
        FieldDialog.saveField = wrap(FieldDialog.saveField, fields.fieldDialogSaveField)
        FieldDialog.loadField = wrap(FieldDialog.loadField, fields.fieldDialogLoadField)

    # ── Editor: set up hooks using modern gui_hooks API ──
    controller = EditorController()

    # Always register the load-note hook to save the editor reference
    gui_hooks.editor_did_load_note.append(controller.onEditorDidLoadNote)

    # Always register the buttons hook to save the editor reference
    gui_hooks.editor_did_init_buttons.append(controller.onEditorDidInitButtons)

    # Optionally add the markdown toggle button
    if config.shouldShowFieldMarkdownButton():
        gui_hooks.editor_did_init_buttons.append(controller.setupEditorButtonsFilter)

    # Focus gained/lost hooks for auto-conversion
    gui_hooks.editor_did_focus_field.append(controller.editFocusGainedHook)
    gui_hooks.editor_did_unfocus_field.append(controller.editFocusLostFilter)


main()
