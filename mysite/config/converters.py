class FilenameExtensionConverter:
    regex = r"(.json|.yaml)"

    def to_python(self, value):
        return value

    def to_url(self, value):
        return value
