# Standard Library
import glob
import os

# Django Library
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# import subprocess



class RenameImage(FileSystemStorage):
    """Returns a filename that's free on the target storage system, and
    available for new content to be written to.

    Found at http://djangosnippets.org/snippets/976/    """

    def get_available_name(self, name, max_length=None):
        """This file storage solves overwrite on upload problem. Another
        proposed solution was to override the save method on the model
        like so (from https://code.djangoproject.com/ticket/11663):
        """
        # If the filename already exists with any ext, remove it as if it was
        # a true file system
        root, ext = os.path.splitext(name)
        name_to_delete = "{}{}{}{}".format(settings.BASE_DIR, settings.MEDIA_URL, root, '*')
        for filename in glob.glob(name_to_delete):
            os.remove(filename)

        return name
